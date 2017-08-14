import os
import re
filepath=raw_input()
path_=os.listdir(filepath)
for i in path_ :
	filename_pref, filename_ext = os.path.splitext(i)
	if re.search(r'[IMDB-[0-9].[0-9]]',filename_pref):
		filename_pref=re.sub(r'\[IMDB-[0-9].[0-9]]','',filename_pref)
	  	new= filename_pref+ filename_ext
		os.chdir(filepath)	
		os.rename(i,new)
	
    

	



