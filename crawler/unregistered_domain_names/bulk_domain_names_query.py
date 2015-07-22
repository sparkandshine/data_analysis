#!/usr/bin/env python

# the program is designed to query domain names in bulk
# sparkandshine.net
# July 21st, 2015

import whois  #pip install python-whois
import string
import itertools

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

class Bulk_domain_names_query :
    def __init__(self):
        self.characters = list(string.ascii_lowercase)
        self.domain_suffixes = ['com']
        self.domain_names = list()

        self.unregistered_names = list()
        pass

    def generate_domain_names(self, min_length, max_length):
        self.characters = list(string.ascii_lowercase)
        for r in range(min_length, max_length+1) :
            for name in itertools.combinations(self.characters, r) :
                for suffix in self.domain_suffixes :
                    domain_name = ''.join(name) + '.' + str(suffix)
                    self.domain_names.append(domain_name)



    def format_output(self, filename):
        for domain_name in self.domain_names:
            #print(domain_name)
            pass

        fp = open(filename, 'w')
        for domain_name in self.unregistered_names :
        #for domain_name in self.domain_names:
            fp.write(domain_name + '\n')

        fp.close()

    def find_unregistered_names(self):
        '''
        for url in self.domain_names :
            #url = 'sparkandshine.me'
            self.whois_domain_name(self, url)
        '''

        #Parallelism using map
        pool = ThreadPool(16)  # Sets the pool size
        results = pool.map(self.whois_domain_name, self.domain_names)
        pool.close()  #close the pool and wait for the work to finish
        pool.join()



    def whois_domain_name(self, url):
        try :
            w = whois.whois(url)
        except (whois.parser.PywhoisError):
            self.unregistered_names.append(url)
            print(url)

### END OF CLASS ###

def main():
    query = Bulk_domain_names_query()

    query.generate_domain_names(1, 5)
    query.find_unregistered_names()


    filename = 'unregistered_domain_names.dat'
    query.format_output(filename)


if __name__ == '__main__':
    main()
