#!/usr/bin/python
"""
Create a training corpus from a list of topics.

Input: A newline seperated list of topics
Output: A 2 column .csv file (TEXT, TOPIC)

NOTE: Need to download 'punkt' nltk resource (sentence tokenizer).

TODO: Remove 2 column input list... Only one column
TODO: Main function, accepts FILE, or ARRAY from input.
TODO: Main function, to accept output file as input.
TODO: Organize into __main__.py (CLI), and CorpusGenerate.py (expose functions).
"""

import csv
import urllib.parse

from googlesearch import search
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from newspaper import Article
import nltk.data


class CorpusGenerate:
    """Parse and retrieve articles from the net, given an input topic."""

    # Input topics (change to stdin  or file input).
    CTOPICS_LIST = ".\\topics_list.txt"

    # Output corpus path. (change to stdout or file output).
    CCORPUS_PATH = ".\\corpus.csv"

    # Main DS to create corpus in.
    VCORPUS = [] 

    def parse_input (self):
        """Read the list of topics to generate the corpus from."""
        vtopics = []
        vlines = []
        with open(CTOPICS_LIST, "r") as vf:
            # Read in lines.
            vlines = vf.read().split("\n")
            vf.close()
        for vline in vlines:
            # Parse each line.
            vtopics.append({
                "name": vline.split("\t")[0],
                "explanation": vline.split("\t")[1]
            })
        return vtopics

    ## Get and parse ###########################################################

    def get_google_results (self, vquery, vnum_articles):
        """Return search result links of a term."""
        vlinks = []
        vresults = search(vquery, tld="com", 
            num=vnum_articles, stop=vnum_articles, pause=2)
        for vlink in vresults:
            vlinks.append(vlink)
        return vlinks

    def get_google_results_old (self, vsearch_term):
        """Return search results of a term. Manual parse using BS4."""
        vurl = ("http://google.com/search?q=%s" % 
            (urllib.parse.quote(vsearch_term)))
        print(vurl)
        vsession = HTMLSession()
        vresp = vsession.get(vurl)
        vresp.html.render()
        vhtml = vresp.html.html
        print("[* corpus-generate] Reuquesting: [%s] [%s]" % 
            (vurl, str(vresp.status_code)))
        vsoup = BeautifulSoup(vhtml, 'html.parser')
        vres = []

        for vdiv in vsoup.find_all("div", attrs={'class':'r'}):
            vlink = vdiv.find_all('a')
            if len(vlink) > 0:
                vres.append(vlink[0].get('href'))

        return vres

    def get_article (self, vstr_url):
        """Use newspaper to get main article from a webpage. Will return an 
        array of paragraphs, each which can be used as a record in the 
        training data."""
        varticle = Article(vstr_url)
        varticle.download()
        varticle.parse()
        vtokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        vtext = varticle.text.replace("\n", " ")
        vpgraphs = self.arr_chunk(vtokenizer.tokenize(vtext), 5)
        return vpgraphs

    ## Write out ###############################################################

    def arr_chunk (self, varr, vsize):
        """Divide an array into chunks of size vsize."""
        return [varr[i * vsize:(i + 1) * vsize] for i in range(
                (len(varr) + vsize - 1) // vsize )]

    def write_corpus( self):
        """Write out the corpus ds into a csv file."""
        with open(CCORPUS_PATH, "w+", newline='') as vcsv:
            vwriter = csv.writer(vcsv, delimiter=',')
            # vwriter.writerows(VCORPUS)
            for vtext in VCORPUS:
                vwriter.writerow(vtext)
                # vcsv.write("%s, %s\n" % (vtext[0], vtext[1]))
            vcsv.close()

    def write_article (self, varticle, vname):
        """Write article data to csv."""
        with open(CCORPUS_PATH, "w+", newline='', encoding='utf-8') as vcsv:
            vwriter = csv.writer(vcsv, delimiter=',')
            for vpg in varticle:
                vwriter.writerow([" ".join(vpg), vname])
            vcsv.close()

    ## Generate ################################################################

    def generate_old (self):
        """Old version of generator, which uses 2 column input..."""
        vtopics = self.parse_input()
        for vtopic in vtopics:
            print("[* corpus-generate] Researching: [%s]" % vtopic)
            vlinks = self.get_google_results(vtopic["explanation"])
            
            # Extract article chunked into paragraphs.
            for vlink in vlinks:
                try:
                    print("[* corpus-generate] Retrieve article for [%s]" 
                        % vlink)
                    varticle = get_article(vlink)

                    # Add to output corpus
                    for vpg in varticle: VCORPUS.append(
                        [" ".join(vpg), vtopic['name']])
                    
                    print("[* corpus-generate] Writing article(?")
                    write_article(varticle, vtopic['name'])
                
                except Exception as e:
                    print("[* corpus-generate] Could not run!: " + str(e))
    
    def write_corpus (self, vcorpus, voutfile):
        """Write corpus data to csv."""
        with open(voutfile, "w+", newline='', encoding='utf-8') as vcsv:
            vwriter = csv.writer(vcsv, delimiter=',')
            for vpair in vcorpus:
                vwriter.writerow([vpair[0], vpair[1]])
            vcsv.close()

    def generate (self, vtopics, vnum_articles, voutfile=None):
        """Generate a corpus of text from a given topic."""
        
        for vtopic in vtopics:
            print("[* corpus-generate] Researching %s...\n" % vtopic)
            vlinks = self.get_google_results(vtopic, vnum_articles)
            
            # Extract article chunked into paragraphs.
            for vlink in vlinks:
                try:
                    print("[* corpus-generate] Retrieve article for [%s]" 
                        % vlink)
                    varticle = self.get_article(vlink)

                    # Add to output corpus
                    for vpara in varticle: 
                        self.VCORPUS.append([" ".join(vpara), vtopic])

                    print()
                except Exception as e:
                    print("[* corpus-generate] Could not run!: " + str(e))

            # Write to stdout, or to disk.
            print("[* corpus-generate] Writing article...")
            if voutfile:
                print("[* corpus-generate] Write to %s" % voutfile)
                self.write_corpus(self.VCORPUS, voutfile)
            else:
                print(self.VCORPUS)