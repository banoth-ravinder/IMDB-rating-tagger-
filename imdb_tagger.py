import glob
import urllib2
#import requests
import lxml
import lxml.html
import os
import re
import guessit
import fnmatch
import sys
import Tkinter, tkFileDialog
from googleapiclient.discovery import build
from urllib2 import urlopen
from lxml import etree as ET
from guessit import guessit

#url = "http://www.imdbapi.com/?t=" + searchstring + "&y="+year

my_api_key = "Google API Key"
my_cse_id = "CSE Id"


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

root = Tkinter.Tk()
root.withdraw()
path = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a Directory')

'''
print'Give the path where you have to search Example: /home/banoth/Desktop'
path=raw_input()
'''
files=os.listdir(path)

extensions=("*.mp4","*.webm","*.avi","*.mkv","*.flv","*.vob","*.ogv","*.ogg","*.wmv","*.yuv","*.rm","*.rmvb","*.asf","*.amv","*.mpeg","*.svi","*.3gp","*.mxf","*.flv")

for filename in files:
	for i in extensions :	
	    if fnmatch.fnmatch(filename,i):
			try:
				if re.search(r'[IMDB-[0-9].[0-9]]',filename):
					print filename+' already ADDED'
				else :
					filedata=guessit(filename)
		 			#len(filedata)
		 		
					print filedata['title']
					moviename=filedata['title']
					
					if filedata['type']=='movie' :
						results = google_search(moviename +' movie'+' site:imdb.com/title', my_api_key, my_cse_id, num=10)


					if filedata['type']=='episode' :
						episodename=filedata['episode_title']
						#print episodename
						print 'Season- '+str( filedata['season']) 
						print 'Episode- '+str(filedata['episode'])
						#results = google_search(moviename+ episodename+' site:imdb.com/title', my_api_key, my_cse_id, num=10) 
						results = google_search(moviename+' season '+ str(filedata['season'])+' episode '+ str(filedata['episode'])+' site:imdb.com/title', my_api_key, my_cse_id ,num=10)
						
					result = results[0]
						
					link = result['link']
						
					root=lxml.html.parse(link)
			

					lyrics_object_list = root.xpath(".//div[@class='ratingValue']")
					lyrics_object = lyrics_object_list[0]
					text=lyrics_object.text_content()
					x=text[1:4]
				
					filename_pref, filename_ext = os.path.splitext(filename)
					new_filename=filename_pref+'['+'IMDB-'+x+']'+filename_ext
				
					os.chdir(path)
					os.rename(filename,new_filename)
					print 'IMDB rating added to '+filename
					

			except Exception,e :
				print e
				print filename+' got ERROR'
                   
					   					 
					  		

