#!/usr/bin/env python3

# this program is designed to crawler colleges contact info
# By Sparkandshine
# July 19th, 2015

from bs4 import BeautifulSoup
import bs4
import requests
import requests.exceptions


class Crawler_Contact_Infos :
    def __init__(self):
        self.set_urls = set()
        self.contact_infos = list()
        pass

    
    ### function output ###
    def format_output(self, filename):
        fp = open(filename, 'w')

        
        for record in self.contact_infos :
            s = '\t'.join(record).replace('\n', ' & ')
            fp.write(s + '\n')
            #print(s)    
        
        fp.close()
        
    
    ### function,  ###
    def get_all_contact_urls(self):
        #<h3>Annuaire</h3>
        base_url = 'http://www.irit.fr/Personnel,197?lang=fr'
        try:
            response = requests.get(base_url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            return
        
        soup = BeautifulSoup(response.text)

        ## retrieve links like: http://www.irit.fr/spip.php?page=annuaire&code=8292 
        for anchor in soup.find_all("a") :
            if anchor.has_attr('href') :
                link = anchor['href']
                if 'annuaire&code' in link :
                    self.set_urls.add(link)
                
                #print(anchor['href'], type(anchor['href']))
       
        
    ### function crawler all contact infos ###
    def crawler_contact_infos(self):
        
        self.get_all_contact_urls()
        
        header = ['Name', 'Statut', 'Service/Equipe', 'Contact', 'Localisation', 'Téléphone']
        self.contact_infos.append(header)
        
        for url in self.set_urls :
            #url = 'http://www.irit.fr/spip.php?page=annuaire&code=8955&lang=fr'
            record = self.crawler_contact_info(url)
            self.contact_infos.append(record)

        #print(contact_infos)


    ### function, extract a row, containing name, .... ###
    def crawler_contact_info(self, url):

        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            return list()
            # ignore pages with errors

        '''
        Su Qiankun

        Statut :    Doctorant
        Service/Equipe :     Signal et Communication
        Ingénierie Réseaux et Télécommunications
        Contact :    Qiankun.Su at irit.fr
        Localisation :    ENSEEIHT - F / 405
        Téléphone :    05 34 32 2256
        '''

        record = list()

        soup = BeautifulSoup(response.text)
        tags_name = soup.find_all("p", {"class" : "titre"})  #<p class="titre">  Su Qiankun</p>
        #print('tags_name:\t', tags_name[0].get_text())
        
        #deal with tags_name=[]
        if not tags_name:
            return record
        
        name = tags_name[0].contents[0].strip() #strip() remove whitespace
        record.append(name)


        table = soup.find('table')
        #table_body = table.find('tbody')
        for row in table.find_all('tr') :
            rep = {ord(':'): ''}  #remove ':' at the end of string, such as 'Statut : '
            columns = [col.get_text().translate(rep).replace(' at ', '@').strip() for col in row.find_all('td')]
            #print('columns: \t', columns)
            record.append(columns[1]) #store value
            
        return record


### END OF CLASS ###

def main():
    crawler = Crawler_Contact_Infos()
    crawler.crawler_contact_infos()
    
    filename = 'contacts_info.dat'
    crawler.format_output(filename)
    

if __name__ == '__main__':
    main()