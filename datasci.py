# coding: utf-8
#  -*- Mode: Python; -*-                                              
#
# python examplerosie.py [local | system]
#  AUTHOR Jenna N. Shockley

# TODO:
# - replace magic error code numbers with constants
# coding: utf-8

# TODO:
# - replace magic error code numbers with constants
# python test.py [local | system]
#
from __future__ import unicode_literals, print_function

import sys, os, json
import rosie
import csv

# Notes
#
# (1) We use the librosie.so that is in the directory above this one,
#     i.e. "..", so we supply the librosiedir argument to
#     rosie.engine().  Normally, no argument to rosie.engine() is
#     needed.

if sys.version_info.major < 3:
    str23 = lambda s: str(s)
    bytes23 = lambda s: bytes(s)
else:
    str23 = lambda s: str(s, encoding='UTF-8')
    bytes23 = lambda s: bytes(s, encoding='UTF-8')

# -----------------------------------------------------------------------------
# Tests for Engine class
# -----------------------------------------------------------------------------
def hello():
    
    print(engine)
    match_object = engine.load('year = [0-9]{4}')
    print(match_object)
    match_object = engine.search("year", "The year is 2018")
    print(match_object.group())
    package = engine.import_package('net')
    print(package)
    netmatch = engine.findall("net.email", "this is an email: johndoe@example.com")
    print(netmatch)
# -----------------------------------------------------------------------------
def readFile() :
    librosiedir = './lib'
    rosie.load(librosiedir, quiet=True)
    engine = rosie.engine()
    package = engine.import_package('all')
    allPackages = ['ts', 'date', 'time', 'net', 'num', 'id', 'word']
    arrayOfPatterns = None
    for pack in allPackages:
        engine.import_package(pack)
    with open('pattern.csv', 'r') as csvfile:
        fileRead = csv.reader(csvfile)
        rowOne = next(fileRead)
        cols = len(rowOne)
        arrayOfPatterns = [set() for j in range(0, cols)]
        for row in fileRead:            
            for i in range(0, cols):
                element = row[i]
                stringBuilder = ""
                match = None
                b = None
                if len(arrayOfPatterns[i]) > 0:
                    for each in arrayOfPatterns[i]:
                        if (match != None):
                            break
                        stringBuilder += each + '/'
                        b = engine.compile(each)
                        match = b.fullmatch(element)
                if match == None:
                    stringBuilder = 'all.thing'
                    b = engine.compile('all.thing')
                    match = b.fullmatch(element)
                if match is None:
                    print('NO MATCH', element)
                    continue
                best_match = None
                if stringBuilder == 'all.thing':
                    best_match = rosieSub(match.rosie_match)
                    print(best_match['type'], ',', best_match['data'])
                if best_match != None and best_match['type'] == 'all.thing':
                    continue
                elif best_match != None:
                    arrayOfPatterns[i].add(best_match['type'])
                    print(arrayOfPatterns)
                
            print()
            
    return arrayOfPatterns

def rosieSub(m):
    if ('subs' in m):
        if (len(m['subs']) == 1):
           return rosieSub(m['subs'][0])
        else:
           return m
    return m

if __name__ == '__main__':
    arrayOfPatterns = readFile()
    length = len(arrayOfPatterns)
    f = open("description.txt", "w")
    f.write(len(arrayOfPatterns))
    for each in arrayOfPatterns:
        stringOfPatterns = ""
        for every in each:
            stringOfPatterns += every + "/"
        if stringOfPatterns[len(stringOfPatterns)] == '/':
            stringOfPatterns = stringOfPatterns[0:len(stringOfPatterns) - 1]
        f.write(stringOfPatterns)                
    
# Add a description of the array of patterns and have readFile() return it.
# Write this data to a file.
# Write another program that takes two command line arguments: the name of the description file and the name of the data file.