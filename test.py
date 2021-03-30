from utils.workflow import workflow
from utils.local_process import offline_process
import pandas as pd
import unittest
import os

class TestCase_(unittest.TestCase):

    def test_workflow(self):
        result = {'SFR': {'2G': 1, '3G': 1, '4G': 1}, 'Orange': {'2G': 1, '3G': 1, '4G': 1}, 'Free': {'2G': 0, '3G': 1, '4G': 1}}
        self.assertEqual(workflow('2 rue paul vaillant couurier'), result)
        self.assertEqual(workflow('**'), False)
        

    def test_localprocess(self):
        offline_process.process_all(update=1)
                        
        new_path =  os.getcwd()+'\\utils\\local_process\\source.csv'
        df = pd.read_csv(new_path)
        self.assertNotEquals(df.shape[0],0) 

if __name__ == '__main__':
    unittest.main()