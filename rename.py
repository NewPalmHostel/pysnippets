import glob
import os

path = './hoge_hage*.pdf'

# get list
flist = glob.glob(path)

# change filenames
for file in flist:
	file_to = file.replace('hoge_hage', 'hage_hoge')
	print( file )
	print( file_to )
	### if everything is ok, uncomment the following line ###
	# os.rename(file, file_to)
