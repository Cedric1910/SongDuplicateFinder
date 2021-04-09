# SongDuplicateFinder V1.0.0

As many DJs will know one of the biggest problems with owning 1000+ songs is that duplicate tracks will quickly build up as we buy more music tracks/albums
from different sources or simply forget we already own a track as we re-download it. Because of this I created a program which will take an exported 
rekordbox playlist.txt file and then check each song inside the playlist against each other
with a SequenceMatcher to decide if the two songs are similar enough to each other based on a users specified RATIO. Then it will output all of the 
similar songs, allowing you to go back into rekordbox and search up the duplicates to free up space. 

# To run this program (you will need to have Python installed) 
1. Click 'clone' and save the repository to a known location on your computer. 
2. Open a Terminal and change to the repository. 
3. Copy in your exported playlist .txt file into the repository.
4. For simplicity sake change the name ofyour exported .txt to 'playlist', otherwise go into the FindDuplicates.py source code and change the 
   global variable 'file_name' with your .txt file.  
5. Run the command 'python FindDuplicates.py > output.txt' 
6. open output.txt when the program has finished to see the results. (This may take a couple minutes based on the amount of songs in your playlist)


# Bugs or problems
If any bugs do occur while running my program feel free to message me and include your playlist.txt file as well as your error message so 
I can pinpoint the error quicker. 
