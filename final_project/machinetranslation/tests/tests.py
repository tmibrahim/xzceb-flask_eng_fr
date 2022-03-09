import unittest
from translator import english_to_french, french_to_english

class testEnglishToFrench(unittest.TestCase):
    def test1_1(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour") #test when english text Hello given as input the output is french text Bonjour.
    def test1_2(self):
        self.assertNotEqual(english_to_french("None"), '') 
        self.assertNotEqual(english_to_french(0), 0) 

class testFrechToEnglish(unittest.TestCase):
    def test2_1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello") #test when french text Bonjour given as input the output is english text Hello.
    def test2_2(self):
        self.assertNotEqual(french_to_english("None"), '') 
        self.assertNotEqual(french_to_english(0), 0) 

unittest.main()