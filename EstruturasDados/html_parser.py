
from html.parser import HTMLParser

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])

parser = MyParser()
parser.feed(html)


    #     HTMLParser.__init__(self)
    #     self.n_polos = 0

    # def hndle_starttag(self, tag, attrs):
    #     if tag == 'a':
    #         for attr in attrs:
    #             if attr[0] == 'class' and attr[1] == 'item-polos':
    #                 self.n_polos += 1

    # def num_polos(self):
    #     return self.n.polos

