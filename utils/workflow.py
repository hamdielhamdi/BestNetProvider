from geo_structure import MinDist


def workflow(adr):
	url = "https://api-adresse.data.gouv.fr/search/?q="
	# init class
	mindist = MinDist(url)

	# get the geo location as a tuple x,y
	coord =  mindist.geocoord(adr)

	if not coord : 
		return False

	# read the source data
	source = mindist.read_file()
	
	# calculate the nearest point
	result = mindist.mindistance(source, coord)

	print(result)
	return  result


workflow('2 rue paul vaillant couturier')




