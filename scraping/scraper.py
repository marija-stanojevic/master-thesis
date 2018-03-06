import xml.etree.ElementTree as ET
import datetime
import time
from urllib.request import urlopen
from urllib.error import HTTPError
import csv as csv

# URLs
OAI = '{http://www.openarchives.org/OAI/2.0/}'
ARXIV = '{http://arxiv.org/OAI/arXiv/}'
BASE = 'http://export.arxiv.org/oai2?verb=ListRecords&'

class Record(object):
    '''
    A class to hold a single record from ArXiv
    Each records contains the following properties:
    object should be of xml.etree.ElementTree.Element.
    '''
    def __init__(self,xml_record):
        self.xml=xml_record
        #print(ET.tostring(self.xml, encoding='utf8', method='xml'))
        self.id = self._get_text(ARXIV, 'id').encode('utf8')
        self.title = self._get_text(ARXIV, 'title').encode('utf8')
        self.abstract = self._get_text(ARXIV, 'abstract').encode('utf8')
        self.cats = self._get_text(ARXIV, 'categories').encode('utf8')
        self.created = self._get_text(ARXIV, 'created').encode('utf8')
        self.updated = self._get_text(ARXIV, 'updated').encode('utf8')
        self.doi = self._get_text(ARXIV, 'doi').encode('utf8')
        self.authors = self._get_authors().encode('utf8')
        self.journal = self._get_text(ARXIV, 'journal-ref').encode('utf8')
        self.submitted = self._get_text(ARXIV, 'submitted').encode('utf8')

    def _get_text(self, namespace, tag):
        'Extracts text from an xml field'
        try:
            return self.xml.find(namespace + tag).text.strip()
        except:
            return ''

    def _get_authors(self):
        # authors
        authors = self.xml.findall(ARXIV+'authors/' + ARXIV + 'author')
        authorsList = ''
        for author in authors:
            if (author.find(ARXIV+'forenames') is not None):
                authorsList = authorsList + author.find(ARXIV+'forenames').text + ' ' +  author.find(ARXIV+'keyname').text
        return authorsList

    def output(self):
        '''d = {'title': self.title,
            'id': self.id,
            'abstract': self.abstract,
            'categories': self.cats,
            'doi': self.doi,
            'created': self.created,
            'updated': self.updated,
            'authors': self.authors}'''
        d = [self.title, self.id, self.abstract, self.cats, self.doi, self.created, self.updated, self.authors]
        return d

class Scraper(object):
    '''
    A class to hold info about attributes of scraping,
    such as date range, categories, and number of returned
    records. If `from` is not provided, the first day of
    the current month will be used. If `until` is not provided,
    the current day will be used.
    '''
    def __init__(self, category, date_from=None, date_until=None, t=30):
        self.cat = str(category)
        self.t = t
        #If from is not provided, use the first day of the current month.
        DateToday = datetime.date.today()
        if date_from is None:
            self.f = str(DateToday.replace(day=1))
        else:
            self.f = date_from
        #If date is not provided, use the current day.
        if date_until is None:
            self.u = str(DateToday)
        else:
            self.u = date_until
        self.url = (BASE + 'from=' + self.f + '&until=' + self.u +
                    '&metadataPrefix=arXiv&set=%s'%self.cat)

    def scrape(self):
        url = self.url
        ds = [] # collect all records in a list
        k=0
        while True:
            k+=1
            print ('fetching up to ', 1000*k, 'records...')
            try:
                response = urlopen(url)
            except HTTPError as e:
                # catch time error
                if e.code == 503:
                    to = int(e.hdrs.get("retry-after", 30))
                    print ("Got 503. Retrying after {0:d} seconds.".format(self.t))
                    time.sleep(to)
                    continue
                else:
                    raise

            xml = response.read()
            root = ET.fromstring(xml)
            records = root.findall(OAI + 'ListRecords/' + OAI + 'record')
            for record in records:
                meta = record.find(OAI+'metadata').find(ARXIV+"arXiv")
                record = Record(meta).output()
                ds.append(record)

            token = root.find(OAI+'ListRecords').find(OAI+"resumptionToken")
            if token is None or token.text is None:
                break
            else:
                url = (BASE + "resumptionToken=%s"%(token.text))

        print ('fetching is complete.')
        return ds

#Code up to this point is taken from: https://github.com/Mahdisadjadi/arxivscraper and updated for this purpose

categories = {'Astrophysics':'astro-ph', 'Condensed Matter':'cond-mat', 'General Relativity and Quantum Cosmology':'gr-qc', 'High Energy Physics - Experiment':'hep-ex',
              'High Energy Physics - Lattice':'hep-lat', 'High Energy Physics - Phenomenology':'hep-ph', 'High Energy Physics - Theory':'hep-th','Mathematical Physics':'math-ph',
              'Nonlinear Sciences':'nlin', 'Nuclear Experiment':'nucl-ex', 'Nuclear Theory':'nucl-th', 'Physics':'physics','Quantum Physics':'quant-ph', 'Mathematics':'math',
              'Computing Research Repository':'CoRR','Quantitative Biology':'q-bio','Quantitative Finance':'q-fin', 'Statistics':'stat'}

start_date = datetime.datetime.strptime('2007-08-01', '%Y-%m-%d')
end_date = datetime.datetime.strptime('2008-07-31', '%Y-%m-%d')

with open('arxivData.csv', 'a', newline="") as csvfile:
    writer = csv.writer(csvfile)
    while start_date <= end_date:
        for c in categories:
            print(start_date.strftime('%Y-%m-%d'))
            date_to = start_date + datetime.timedelta(days=9)
            print(date_to.strftime('%Y-%m-%d'))
            scraper = Scraper(category='physics:cond-mat', date_from=start_date.strftime('%Y-%m-%d'), date_until=date_to.strftime('%Y-%m-%d'), t=30)
            output = scraper.scrape()
            writer.writerows(output)
        start_date = start_date + datetime.timedelta(days=10)