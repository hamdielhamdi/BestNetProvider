import pandas as pd
try : 
	from local_process import ProcessLD
except  : 
	from .local_process import ProcessLD
import sys


def process_all(update): # main workflow 

	pr =  ProcessLD()
	if not update: 								# update  = False
		if not pr.check_source_exist():			# check if file dosn't exist in locate path 
			pr.download_source()				# file not exist --> download a new one
	else : 										# update  = True
		pr.download_source()					# download last version

	df = pr.read_df()							# read --> convert --read : used to do one op in each iter
	pr.save_to_csv()							# save to pandas csv format 
	df = pr.read_df()

	df = pr.map_provider(df)					# map operator id with name
	
	df.to_csv('source.csv')						# save file 


if __name__ == "__main__":
	# update : use existing file or download new one  
	if len(sys.argv) < 1 :
		update  = 0
	else : 
		update = 1

	process_all(update)



