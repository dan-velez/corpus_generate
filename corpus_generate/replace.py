#!/usr/bin/python
"""
Replacing slashes with dashes? Its been a while...
"""

import csv

vnew_csv = []

with open('corpus.csv', encoding='utf-8') as vcsv:
    vcsv_reader = csv.reader(vcsv, delimiter=',')
    for vrow in vcsv_reader:
        vnew_csv.append([vrow[0], vrow[1].replace("/", "-")])

# print(vnew_csv)

with open("corpus_new.csv", "w", newline='', encoding='utf-8') as vcsv:
    vwriter = csv.writer(vcsv, delimiter=',')
    vwriter.writerows(vnew_csv)
    vcsv.close()