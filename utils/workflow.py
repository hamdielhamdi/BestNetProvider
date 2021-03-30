import pandas as pd
from utils.geo_structure import MinDist


def workflow(adr):
	"""
	API core method : process input and return json response 
	"""
	url = "https://api-adresse.data.gouv.fr/search/?q="
	# init class
	mindist = MinDist(url)

	# get the geo location as a tuple x,y
	coord =  mindist.geocoord(adr) # convert location to geo coord 

	if not coord : 
		return False

	# read the source data
	source = mindist.read_file()
	
	r  = mindist.three_nearest_point(source, coord) # get the 3 nearest point 
	r = mindist.process_output(r)		# convert df to json records format 

	return  r # out put like {“orange”: {“2G”: True, “3G”: True, “4G”: False}, “SFR”: {“2G”: True, “3G”: True, “4G”: True}}
