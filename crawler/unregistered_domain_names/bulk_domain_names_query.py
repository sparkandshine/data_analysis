#!/usr/bin/env python

# the program is designed to query domain names in bulk
# sparkandshine.net
# July 21st, 2015

import whois  #pip install python-whois
import string
import itertools
import os

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

class Bulk_domain_names_query :
    def __init__(self):
        pass


    def get_unregistered_domain_names(self, domain_names, out_filename):
        unregistered_domain_names = self.select_unregisteredd_domain_names(domain_names)
        self.format_output(unregistered_domain_names, out_filename)


    def domain_names_generator(self, characters, extensions, min_length, max_length):
        domain_names = list()
        for r in range(min_length, max_length+1) :
            for name in itertools.permutations(characters, r) :
                for extension in extensions :
                    domain_name = ''.join(name) + '.' + str(extension)
                    domain_names.append(domain_name)

        return domain_names


    def select_unregisteredd_domain_names(self, domain_names):
        '''
        for url in self.domain_names :
            #url = 'sparkandshine.me'
            self.whois_domain_name(self, url)
        '''

        #Parallelism using map
        pool = ThreadPool(16)  # Sets the pool size
        results = pool.map(self.whois_domain_name, domain_names)
        pool.close()  #close the pool and wait for the work to finish
        pool.join()

        return results



    def whois_domain_name(self, url):
        try :
            w = whois.whois(url)
        except (whois.parser.PywhoisError):
            print(url)
            return url


    def format_output(self, unregistered_domain_names, filename):
        fp = open(filename, 'w')
        for domain_name in unregistered_domain_names :
            #if domain_name is not None :
                #fp.write(domain_name + '\n')
            try :
                fp.write(domain_name + '\n')
            except :
                pass

            '''
            if domain_name is None : #skip NoneType
                fp.write(domain_name + '\n')
            '''

        fp.close()

### END OF CLASS ###

def main():
    characters = list(string.ascii_lowercase)
    extensions = ['net', 'org', 'me', 'info', 'cn', 'in', 'it']
    min_length = 1
    max_length = 3

    out_dir = 'dataset_unregistered_domain_names/'
    try :
        os.mkdir(out_dir)
    except :
        pass


    ### bulk query
    query = Bulk_domain_names_query()

    ### write to separated files
    for extension in extensions :
        domain_names = query.domain_names_generator(characters, [extension], min_length, max_length)

        format_filename = '_'.join(['len', str(min_length), str(max_length)]) + '_' + extension + '.dat'
        out_filename = out_dir + format_filename

        query.get_unregistered_domain_names(domain_names, out_filename)


    ### write to a single file
    '''
    format_filename = '_'.join(['len', str(min_length), str(max_length)]) + '_' + '_'.join(extensions) + '.dat'
    out_filename = out_dir + format_filename

    domain_names = query.domain_names_generator(characters, extensions, min_length, max_length)
    query.get_unregistered_domain_names(domain_names, out_filename)
    '''

if __name__ == '__main__':
    main()
