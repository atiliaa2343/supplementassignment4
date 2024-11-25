import unittest 
from functions import get_numbers, list_comma, csv_ 
import os 
import csv 

class TestFunctions(unittest.TestCase): 
    def test_get_numbers(self): 
        #positive number 
        self.assertEqual(get_numbers(4), "5,6,7,8,9,10,11,12,13,14") 

        #test with zero 
        self.assertEqual(get_numbers(0), "1,2,3,4,5,6,7,8,9,10") 

        #test with a negative number 
        self.assertEqual(get_numbers(-10), "-9,-8,-7,-6,-5,-4,-3,-2,-1,0") 

    def test_list_comma(self): 
        #test with a list of strings 
        self.assertEqual(list_comma(["car", "bike", "bus"]), "car, bike,bus") 

        #test with empty list 
        self.assertEqual(list_comma([]), "") 

        #test with one element 
        self.assertEqual(list_comma(["car"]), "car") 



    def csv_(self): 
        #test to write to csv file 
        filename = "output/test.csv"  
        headers = ["Header1", "Header2", "Header3"] 
        data = [4,10,30]

        #function to write the csv 
        csv_(filename, headers, data) 

        #check file 
        self.assertTrue(os.path.exists(filename)) 

        #read file 
        with open(filename, 'r') as csvfile: 
            reader = csv.reader(csvfile) 
            rows = list(reader) 
            self.assertEqual(rows[0], headers) 
            self.assertEqual(rows[1], ['4', '10', '30'])  


        #remove file 
        os.remove(filename) 

if __name__ == "__main__": 
    unittest.main()