from os import path
import pandas as pd
import requests 
import sys

class ProcessLD:
	'''
    Returns a file with a dict format containt all .

            Parameters:
                    source (str): url of the source file.
            
            Returns:
                    source.json (json_file):fiel containing a new data structure
    '''

	def __init__(self):
		# url to the source file / csv file 
		self.source ="https://www.data.gouv.fr/s/resources/monreseaumobile/20180228-174515/2018_01_Sites_mobiles_2G_3G_4G_France_metropolitaine_L93.csv"


	def check_source_exist(self):
		""" check if source fiel already exist"""
		if path.exists('source.csv'):
			return True
		return False


	def download_source(self):
		""" request source and download it """
		response = requests.get(self.source, stream=True)

		if response.status_code == 200:
			with open('source.csv', 'wb') as csv_file:
				csv_file.write(response.content)
				csv_file.close()
			return 'Done.'
		return 'Error'

	def read_df(self):
		return pd.read_csv('source.csv')

	def save_to_csv(self):
		df = pd.read_csv('source.csv', sep=';')
		df.to_csv(('source.csv'))

	def map_provider(self, df):
		map_ = {20801 : "Orange", 20810 : "SFR", 20815 : "Free", 20820 : "Bouygue"}

		df['Operateur']  =df['Operateur'].map(map_)
		df.to_csv('source.csv')
		return df