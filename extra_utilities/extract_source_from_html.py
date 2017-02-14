#!/usr/bin/env python

from bs4 import BeautifulSoup
from io import open as io_open
from os import listdir

def get_rst_files_listing():
    PATH = '/projects/dojo-website/docs/source/'
    rst_filename_list = []
    for filename in listdir(PATH):
        if filename.endswith('.rst'):
            rst_filename_list.append(filename)
    return rst_filename_list

def get_html_files_listing():
    PATH = '/projects/dojo-website/docs/build/html/'
    rst_filename_list = get_rst_files_listing()
    html_filename_list = []
    for rst_filename in rst_filename_list:
        filename_without_extension = rst_filename[:rst_filename.rfind('.')]
        html_filename = filename_without_extension + '.html'
        html_filename_list.append(PATH + html_filename)
    return html_filename_list

def extract_relevant_text(html_file_content):
    soup = BeautifulSoup(html_file_content, 'html.parser')
    soup = soup.find('div', {'class': 'section'})
    relevant_text = soup.get_text()
    relevant_text = relevant_text.replace('\n', '')
    return relevant_text

def process_file(html_filename, txt_filename):
    PATH = '/projects/dojo-website/docs/build/html/_sources/'
    with open(html_filename) as file_:
        html_file_content = file_.read()
    source_relevant_portion = extract_relevant_text(html_file_content)
    with io_open(PATH + txt_filename, 'w', encoding='utf-8') as file_:
        file_.write(source_relevant_portion)

def copy_source():
    html_filename_list = get_html_files_listing()
    for html_filename in html_filename_list:
        txt_filename = html_filename[html_filename.rfind('/') + 1:html_filename.rfind('.')] + '.txt'
        print 'Writing ' + txt_filename + '...  ',
        process_file(html_filename, txt_filename)
        print 'Done!'
    return 'Success!'

def main():
    copy_source()

if __name__ == '__main__':
    main()
        
