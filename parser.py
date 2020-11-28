_author__ = 'thiagocastroferreira'

"""
Author: Thiago Castro Ferreira
Date: 18/10/2018
Description:
    Parser for the WebNLG corpus
    PYTHON VERSION: 3
"""

import os
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

class Entry():
    def __init__(self, category, eid, size, originaltripleset, modifiedtripleset, entitymap, lexEntries):
        self.category = category
        self.eid = eid
        self.size = size
        self.originaltripleset = originaltripleset
        self.modifiedtripleset = modifiedtripleset
        self.lexEntries = lexEntries
        self.entitymap = entitymap

    def entitymap_to_dict(self):
        return dict(map(lambda tagentity: tagentity.to_tuple(), self.entitymap))

class Triple():
    def __init__(self, subject, predicate, object):
        self.subject = subject
        self.predicate = predicate
        self.object = object

class Lex():
    def __init__(self, comment, lid, text, template, orderedtripleset=[], references=[]):
        self.comment = comment
        self.lid = lid
        self.text = text
        self.template = template
        self.tree = ''
        self.lex_template = ''
        self.orderedtripleset = orderedtripleset
        self.references = references

        # german entry
        self.text_de = ''
        self.template_de = ''
        self.tree_de = ''
        self.orderedtripleset_de = []
        self.references_de = []

class TagEntity():
    def __init__(self, tag, entity):
        self.tag = tag
        self.entity = entity

    def to_tuple(self):
        return (self.tag, self.entity)

class Reference():
    def __init__(self, tag, entity, refex, number, reftype):
        self.tag = tag
        self.entity = entity
        self.refex = refex
        self.number = number
        self.reftype = reftype

def parse(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    entries = root.find('entries')

    dataset = []

    for entry in entries:
        eid = entry.attrib['eid']
        size = entry.attrib['size']
        category = entry.attrib['category']

        originaltripleset = []
        otripleset = entry.find('originaltripleset')
        for otriple in otripleset:
            e1, pred, e2 = otriple.text.split(' | ')
            originaltripleset.append(Triple(subject=e1.replace('\'', ''), predicate=pred, object=e2.replace('\'', '')))

        modifiedtripleset = []
        mtripleset = entry.find('modifiedtripleset')
        for mtriple in mtripleset:
            e1, pred, e2 = mtriple.text.split(' | ')

            modifiedtripleset.append(Triple(subject=e1.replace('\'', ''), predicate=pred, object=e2.replace('\'', '')))

        lexList = []
        lexEntries = entry.findall('lex')
        for lex in lexEntries:
            lid = lex.attrib['lid']
            text = lex.text
            template = ''

            lexList.append(Lex(comment='', lid=lid, text=text, template=template))

        dataset.append(Entry(eid=eid, size=size, category=category, originaltripleset=originaltripleset, modifiedtripleset=modifiedtripleset, entitymap={}, lexEntries=lexList))
    return dataset