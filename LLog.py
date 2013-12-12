import csv

class LLog:
    '''Class to log progress in learning a new language.'''

    def __init__(self, csv_path = None):
        self.vocabs = {}
        if csv_path != None:
            csv_file = open(csv_path, 'rb')
            reader = csv.reader(csv_file)
            for row in reader:
                self.add_vocab(row[0], row[1], row[2], row[3])
        else:
            self.manual_entry()    
    def __str__(self):
        rep = ""
        for pos in self.vocabs:
            for entry in self.vocabs[ pos ]:
                rep += "%s(%s): (%s.) %s\n" % (entry[0], entry[2], pos, entry[1])
        return rep

    def add_vocab(self, term, pos, definition, kanji):
        if not pos in self.vocabs:
            self.vocabs[ pos ]  = set()
        self.vocabs[pos].add((term, definition, kanji))

    def print_pos(self, pos):
        for entry in self.vocabs[pos]:
            print("%s(%s): (%s.) %s" % (entry[0], entry[2], pos, entry[1]))

    def print_all(self):
        for key in self.vocabs:
            self.print_pos(key)

    def print_html(self):
        rep = "<html><head><title>JAPN 201</title></head><p>"
        for pos in self.vocabs:
            rep+="<h2>%s</h2><ul>" % pos
            for entry in self.vocabs[ pos ]:
                if entry[2] != '':
                    rep+= "<li><b>%s<b> (%s): %s" % (entry[0], entry[2], entry[1])
                else:
                    rep+= "<li><b>%s<b>: %s" % (entry[0], entry[1])

            rep+="</ul>"
        rep += "</p></html>"
        return rep

    def manual_entry(self):
        text = raw_input("Please enter [term] [part of speech] [definition] [kanji], separated by commai\n")
        while not text == 'quit':
            term, pos, definition, kanji = tuple(text.split(","))
            self.add_vocab(term, pos, definition, kanji)
            text = raw_input()
            
            if text == 'quit':
                if raw_input("Are you sure? y/n: ") == 'y':
                    break

if __name__ == "__main__":
    log = LLog('japn201vocab.csv')
    print(str(log))
