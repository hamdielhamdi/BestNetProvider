import requests 
import pandas as pd
import os
import math
import numpy as np

"""

"""

class MinDist:
	'''
    Returns the location of the nearest point from the dataframe .

            Parameters:
                    None
            
            Returns:
                    pandas row (type : serie): the closest point to the given adr
    '''

	def __init__(self, url):
		# used to get the source file from the relaive path
		cur_path = os.path.dirname(__file__)					# get dir path
		self.new_path = cur_path+'\\local_process\\source.csv'  # move to the  relative dir
		self.base_url  = url				 					# url to get the coord
		self.nereastpnt = []
		self.index = 0
	def geocoord(self, adr):
		"""convert the string adress to x,y geo location on the map """

		response = requests.get(self.base_url+adr)

		if response.status_code != 200:
			return False

		r = response.json()['features']  

		if len(r)<1 : 											# this mean that no adress was found
			return False

		properties = r[0]['properties'] # since the list is already sorted by score, we will just take the first element
		return int(properties['x']), int(properties['y'])


	def read_file(self):
		df = pd.read_csv(self.new_path, sep=',')
		df = df.dropna()
		return df

	def square_root(self, x):
		return math.sqrt(x)



	def mindistance(self, df, point) : 
			"""calculate distance between 2 point and return the min"""

			df['x1'], df['y1'] = point[0], point[1] # create new x1, y1 column

			df['vertical_dist'] = df['X'] - df['x1']
			df['horiz_dist'] = df['Y'] - df['y1']

			df['vertical_dist'] = df['vertical_dist'].pow(2)
			df['horiz_dist'] = df['horiz_dist'].pow(2)

			df['distance'] = df['vertical_dist'] + df['horiz_dist']
			df['final_distance'] = df['distance'].apply(lambda x: self.square_root(x)) # Euclidean distance

			result  = df[df['final_distance'] == df['final_distance'].min()] # get teh index from df whre distance is min

			return result



	def three_nearest_point(self, df,point):
		r = self.mindistance(df, point)

		self.nereastpnt.append(r)
		
		df  = df[df['final_distance'] != df['final_distance'].min()]

		if len(self.nereastpnt) != 5: 
			self.three_nearest_point(df,point)

		df_nrst_point = pd.DataFrame()

		for df in self.nereastpnt:
			df_nrst_point = df_nrst_point.append(df)

		df_nrst_point = df_nrst_point[['Operateur','2G','3G','4G']]

		return df_nrst_point

	
	def process_output(self, df):
		output = {}
		for i in range(df.shape[0]):
			item = {df['Operateur'].iloc[i] : {'2G': df['2G'].iloc[i], '3G': df['3G'].iloc[i], '4G': df['4G'].iloc[i]} }	
			output.update(item)
		return output