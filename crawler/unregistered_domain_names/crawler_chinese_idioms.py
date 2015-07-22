#!/usr/bin/env python3

# this program is designed to crawler Chinese idioms betwee 3 and 12 charaters
# By SparkandShine,  sparkandshine.net
# July 21th, 2015

from bs4 import BeautifulSoup
import bs4
import requests
import requests.exceptions
import re
#from urlparse import urlparse  python2.x
from urllib.parse import urlparse
from urllib.parse import urljoin

import os

class Crawler_Chinese_Idioms :
    def __init__(self):
        pass

    ### function output ###
    def format_output(self, filename, chinese_idioms):
        fp = open(filename, 'w')


        for item in chinese_idioms :
            s = '\t'.join(item)
            fp.write(s + '\n')
            #print(s)

        fp.close()


    ### function crawler chinese idioms, word counts [3, 12]###
    def crawler_chinese_idioms(self):
        out_dir = 'dataset_chinese_idioms/'
        format_filename = 'chinese_idioms_{word_counts}.dat'

        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        format_url = 'http://chengyu.911cha.com/zishu_{word_counts}.html'


        for word_counts in range(3, 13) :
        #for word_counts in [8] :
            chinese_idioms = set()

            ## Step 1: get all page urls
            urls_set = set()
            url = format_url.format(word_counts=word_counts)
            parsed_uri = urlparse(url)
            base_url = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
            try:
                response = requests.get(url)
            except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                pass

            soup = BeautifulSoup(response.text)
            for anchor in soup.find_all('div', {'class' : 'gclear pp bt center f14'}) : #navigate pages
                for item in anchor.find_all('a') :
                    page_url = urljoin(base_url, item.attrs['href'])
                    urls_set.add(page_url)
                #print(urls_set)

            ## Step 2: crawler chinese idioms
            for url in urls_set :
                idioms = self.crawler_chinese_idiom(url)
                chinese_idioms.update(idioms)

            ## Step 3: write to file
            filename = out_dir + format_filename.format(word_counts=word_counts)
            self.format_output(filename, chinese_idioms)


    ### function, crawler chinese idioms from a given url ###
    def crawler_chinese_idiom(self, url):
        idioms = list()

        parsed_uri = urlparse(url)
        base_url = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        #print('base_url', base_url)

        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            # ignore pages with errors
            return idioms

        soup = BeautifulSoup(response.text)

        ## !!! there might be a bug !!!
        #for result_set in soup.find_all("ul", {"class", re.compile(r"l[45]\s+center")}): #l4 center or l5 center
        #for result_set in soup.find_all("ul", {"class" :  "l4 center"}):
        for result_set in soup.find_all("ul", {"class" :  ['l3', 'l4', 'l5', 'center']}):
        #for result_set in soup.find_all("ul", {"class" :  ["l4 center", "l5 center"]}):
            for idiom in result_set.find_all('li') :
                sub_url = idiom.find_all('a')[0].attrs['href']
                idiom_url = urljoin(base_url, sub_url)

                t = (idiom.get_text(), idiom_url)
                #print(t)
                idioms.append(t)

        return idioms

### END OF CLASS ###

def main():
    crawler = Crawler_Chinese_Idioms()
    crawler.crawler_chinese_idioms()


if __name__ == '__main__':
    main()
