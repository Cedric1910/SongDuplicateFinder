# This program is designed to take a txt file as input containing all songs in a users
# rekordbox library that he/she has. From here the program will clean up the input file into
# individual tracks and then compare each song against each other using a sequence matcher 
# to see if the song is a duplicate to another. 
# (note: this is not a perfect solution, the program will make some mistakes)
# Author: Cedric Stephani 
# Version: 1.0.0

from difflib import SequenceMatcher
import itertools
import re

#GLOBAL VARS
file_name = "all_music.txt"
RATIO = 0.9

# This function will take in all the tracks as a list input and then sort through each one 
# comparing it with all the other tracks in the list to determine if the two are similar 
# enough. If the tracks are similar enough based on a ratio then it will output the two tracks 
# and the given ratio. 
def CheckSimilarity(tracks, tracks_simple):
	similar_tracks = []
	for a, b in itertools.combinations(tracks_simple, 2):
		seq = SequenceMatcher(a=a,b=b)
		if(seq.ratio() >= RATIO):
			track = str(a)+' // '+str(b)+', RATIO: '+str(seq.ratio())
			similar_tracks.append(track)

	return similar_tracks

# This function will take in all the tracks as a list input and then perform some simplifications on them allowing for the sequence
# matcher to get a better ratio result in return.
def SimplifyTrackTittles(tracks):
	for x in range(len(tracks)):
		tracks[x] = tracks[x].lower() #get rid of any uppercase letters 
		replacement_chars = ['-','_',',','	','  '] #replace characters which could be used as spaces in the track name
		for char in replacement_chars: 
			tracks[x] = tracks[x].replace(char, ' ')
		# A list of substrings which can be considered as 'spam' in the track title
		# and give a higher match percentage when comparing tracks.
		spam_phrases = ['[www.slider.kz]','(original mix)','(extended mix)']
		for phrase in spam_phrases:
			tracks[x] = tracks[x].replace(phrase,' ')

	return tracks

# This function takes in all the unedited tracks as input will then isolate the track tittle of each song in the users 
# playlist, before returning it as a 'new' list
def getTrackTittles(tracks):
	for x in range(1,len(tracks)):
		tracks[x] = tracks[x].replace(b'\x00', b'').decode('latin-1')
	tracks = filter(None, tracks) #take away all the empty elements if there are any 
	del(tracks[0]) #takes away the first element which is just the descriptions

	# #For loop which splits each track into the rekordbox categories and then isolates the track tittle 
	for x in range(len(tracks)):
		tracks[x] = tracks[x].split('	')
		tracks[x] = tracks[x][1]

	return tracks


def main():
	# Opens the file and splits the lines into an array
	try:
		with open(file_name, 'r') as file: # Change this line with the text file you want to open. 
			inputFile = file.read().splitlines()

		tracks = getTrackTittles(inputFile)
		tracks_simple = SimplifyTrackTittles(tracks)
		similar_tracks = CheckSimilarity(tracks, tracks_simple)

		#Output similar files (save to output file to make it look nicer)
		print("Found the following tracks based on an input ratio of: "+str(RATIO)+"\n")
		for st in similar_tracks:
			print(st+"\n")
		

	except IOError:
		print("The file could not be found. Check file path")
		return; 
	except UnicodeDecodeError as UED:
		print("while decoding the input file an error occured. One of more songs has characters not suitable for decoding.")
		print("error: "+str(UED))
		return; 
	except:
		print("An unexpected error has occured, and the program could not succeed. Please try again or contact admin.")
		return; 


if __name__ == "__main__":
    main()