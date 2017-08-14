Auto-IMDB-Rating-Tagger

This program will search the video files in the given path by the user and Extract the execet movie_name/TV Series_name from the file_name.based on this file name it scrape the IMDB rating from imdb.com and rename the file_name with the original file_name and rating tag.   

 Instructions 

 1.If you didn't istalled pip
 	+This program file requires guessit, To install guessit and pip run the command in your terminal. 
 	- sudo apt-get install python-pip
 	- sudo pip install guessit
	- sudo pip install --upgrade google-api-python-client 
 2.Create google search API with your google account and get 'my_api_key' and 'my_cse_id'.While you are creating mention www.imdb.com site in the google console search.
 3.Download the archive and extract the .py file
 4.paste your 'my_api_key' and 'my_cse_id' in the python code and save the file.
 5.Open the terminal and type $python imdb_tag.py
 6.select the path of the movie or TV series Episode folder
 7.Wait till it complete

 Youtube Demo



1.This works for all language movies and TV Series.
2.Requires Python 2.7.6 and above versions with module dependenices installed.
3.May not work for some movie name whcih had name with single letter[Working on it]
4.It currently search for rating based on movie name and Extracting series name,season number and eposide number for TV Series.

Basic instroduction for people interested in imporving this scraper.

Following takes place 
	1.Read all video files from the given path, stores the file_names in a list.
	2.Iterating throught each name in the list, sent a get request at Google search site:imdb.com/title with the query file_name
	3.Scrape the IMBD rating from the result and tag to the orignal file_name.
	4.finally rename the file_name with the new name which has a IMDB rating.


