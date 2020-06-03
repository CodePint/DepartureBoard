from templates import *
from bs4 import BeautifulSoup

class TableGenerator():
    def __init__(self, template, source, elements, output):
        self.template = template
        self.source = source
        self.element = elements
        self.output = output

    def read_file(self):
        file = open(self.source, 'r')
        self.content = file.read()

    def fetch_records(self):
        soup = BeautifulSoup(self.content, 'lxml')
        self.records = soup.find_all(elements['parent'])

    def parse_records(self):
        self.context = {'table': []}

        for record in self.records:
            row = {}
            for key in elements['child']:
                try:
                    row[key] = record.find(key).get_text()
                except AttributeError:
                    print("No value found")
                    row['key'] = " "

            self.context['table'].append(row)

    def render(self):
        self.rendered = get_template("index.html").render(self.context)

    def write(self):
        file = open(output, "w")
        file.write(self.rendered)
        file.close



source = 'departures.xml'
output = 'output/index.html'
template = 'index.html'
parent = 'record'
child = ['flight', 'destination', 'std', 'status']
elements = {'parent': parent, 'child': child }

generator = TableGenerator(template, source, elements, output)

# xml read/parse
generator.read_file()
generator.fetch_records()
generator.parse_records()

# html template parse/write
generator.render()
generator.write()

