import csv
import codecs

from bs4 import BeautifulSoup

# HTML file
file = codecs.open("../Plandeestudios.html", 'r')

file_raw_html = file.read()

# Sintactic analysis
html = BeautifulSoup(file_raw_html, 'html.parser')

column_titles = html.find_all('th')
column_titles = BeautifulSoup(str(column_titles), 'html.parser')

title_list = list()

for title in column_titles:
    title_list.append(title.text)

print('Funca')
print(f'{title_list}')