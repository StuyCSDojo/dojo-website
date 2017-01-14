#!/usr/bin/env python

from sys import argv
from os import sep

def patchCodeblockWhiteSpace(filename):
    with open(filename) as file_:
        fileContent = file_.readlines()
    index = 0
    while index < len(fileContent):
        line = fileContent[index]
        if '<codeblock>' in line:
            fileContent[index] = line.strip('\r\n')
            if '</codeblock>' not in line:
                index += 1
                while index < len(fileContent) - 1 and '</codeblock>' not in fileContent[index]:
                    line = fileContent[index]
                    fileContent[index] = line.lstrip()
                    index += 1
                fileContent[index - 1] = fileContent[index - 1].strip('\r\n')
                fileContent[index] = fileContent[index].lstrip()
        index += 1
    with open('../release/' + filename[filename.rfind(sep) + 1:] + 'c', 'w') as file_:
        file_.writelines(fileContent)
    return

def main():
    for filename in argv[1:]:
        if filename.endswith('.html'):
            print 'Processing ' + filename + '...',
            patchCodeblockWhiteSpace(filename)
            print 'Success!'
        else:
            print filename + ' is not supported!'

if __name__ == '__main__':
    main()

