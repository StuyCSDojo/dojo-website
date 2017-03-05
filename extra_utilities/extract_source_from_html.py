#!/usr/bin/env python

from bs4 import BeautifulSoup
from io import open as io_open
from os import listdir, path
from sys import argv

def get_rst_filenames(RST_FILE_LISTING_PATH):
    rst_filename_list = []
    for filename in listdir(RST_FILE_LISTING_PATH):
        full_path = path.join(RST_FILE_LISTING_PATH, filename)
        if path.isdir(full_path):
            rst_filename_list.extend(get_rst_filenames(full_path))
        elif filename.endswith('.rst'):
            rst_filename_list.append(full_path)
    return rst_filename_list

def get_html_filenames(RST_FILE_LISTING_PATH, HTML_FILE_LISTING_PATH):
    rst_filename_list = get_rst_filenames(RST_FILE_LISTING_PATH)
    html_filename_list = []
    for rst_filename in rst_filename_list:
        filename_without_extension = rst_filename[len(RST_FILE_LISTING_PATH):rst_filename.rfind('.')]
        html_filename = filename_without_extension + '.html'
        full_path = path.join(HTML_FILE_LISTING_PATH, html_filename)
        html_filename_list.append(full_path)
    return html_filename_list

def extract_relevant_text(html_file_content):
    html_file_content = [line for line in html_file_content if 'class="reference internal"' not in line]                                                                                       
    processed_html_file_content = ' '.join(html_file_content)
    soup = BeautifulSoup(processed_html_file_content, 'html.parser')
    soup = soup.find('div', {'class': 'section'})
    if not soup:
        return u''
    relevant_text = soup.get_text()    
    relevant_text = relevant_text.replace('\n\n', '\n')
    relevant_text = relevant_text.replace('\n', ' ')
    relevant_text = relevant_text.replace(u'\xb6', '  ')
    return relevant_text

def process_file(PROCESS_FILE_PATH, html_filename, txt_filename):
    with open(html_filename) as file_:
        html_file_content = file_.readlines()
    source_relevant_portion = extract_relevant_text(html_file_content)
    full_path = path.join(PROCESS_FILE_PATH, txt_filename)
    with io_open(full_path, 'w', encoding='utf-8') as file_:
        file_.write(source_relevant_portion)

def copy_source(RST_FILE_LISTING_PATH, HTML_FILE_LISTING_PATH, PROCESS_FILE_PATH):
    html_filename_list = get_html_filenames(RST_FILE_LISTING_PATH, HTML_FILE_LISTING_PATH)
    for html_filename in html_filename_list:
        txt_filename = html_filename[len(HTML_FILE_LISTING_PATH):-4] + 'txt'
        print 'Writing ' + txt_filename + '...  ',
        process_file(PROCESS_FILE_PATH, html_filename, txt_filename)
        print 'Done!'
    return 'Success!'

def main():
    if '-a' in argv or '--all' in argv:
        argv.append('--resources')
        argv.append('--docs')
    for arg in argv[1:]:
        if arg == '-a' or arg == '--all':
            continue
        elif arg == '--docs':
            RST_FILE_LISTING_PATH = '/projects/dojo-website/docs/source/'
            HTML_FILE_LISTING_PATH = '/projects/dojo-website/docs/build/html/'
            PROCESS_FILE_PATH = '/projects/dojo-website/docs/build/html/_sources/'
            print copy_source(RST_FILE_LISTING_PATH, HTML_FILE_LISTING_PATH, PROCESS_FILE_PATH)
        elif arg == '--resources':
            RST_FILE_LISTING_PATH = '/projects/dojo-website/app/resources/source/'
            HTML_FILE_LISTING_PATH = '/projects/dojo-website/app/resources/build/html/'
            PROCESS_FILE_PATH = '/projects/dojo-website/app/resources/build/html/_sources/'
            print copy_source(RST_FILE_LISTING_PATH, HTML_FILE_LISTING_PATH, PROCESS_FILE_PATH)
        else:
            print 'Unknown argument: ' + str(arg)
            raise SystemExit(0)
        print ''
        
if __name__ == '__main__':
    main()
