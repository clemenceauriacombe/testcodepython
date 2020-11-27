#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest


def fonctionquivatester(word, text):
    textsplit = text.split(' ')
    word = word.lower()
    resultat = 0
    for item in textsplit: 
        if word == item.lower():
            resultat += 1

    return resultat


class TestFonctionQuiVaTester(unittest.TestCase):
    def testfonctionquivatester(self):

        self.assertEqual(1, fonctionquivatester("en", "Je suis en retard"))
        self.assertEqual(1, fonctionquivatester("en", "Je suis EN retard"))
        self.assertEqual(1, fonctionquivatester("EN", "Je suis en retard"))
        self.assertEqual(2, fonctionquivatester("EN", "Je suis en retard, je suis très en retard"))

if __name__ == '__main__':

    unittest.main()
