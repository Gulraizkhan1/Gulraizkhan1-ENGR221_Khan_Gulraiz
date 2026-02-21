"""
Author: Gulraiz Khan
Filename: noduplesplaylist.py
Description: Implementation of a class that gets rid of duplicate songs in a playlist
Date: Feb 16, 2026
"""




# test using this in the terminal                      
# pytest -v tests/nodupes_tests.py


# The constructor takes initial songs which is set to None 
class NoDuplesPlaylist:
   def __init__(self, initial_songs=None):
       # The song plalist is set to empty list and the num_songs counter is set 0
       self.songs = []
       self.num_songs = 0
      
      # This checks if the initial songs are given
      # The for loop uses the insert_song method to check for duplicates
       if initial_songs:
           for song in initial_songs:
               self.insert_song(song)


  # This method search for the songs index in the playlist from its title
   def search_by_title(self, song_title):
       # The for loop iterates through the playslist using num_songs
       for idx in range(self.num_songs):
           # If it find the title we are looking for then it returns the index of that song
           if self.songs[idx].title == song_title:
               return idx
       # If it doesn't find the song, then the method returns -1
       return -1


   # This method insert a new song into the playlist and then increases the size of the playlist
   def insert_song(self, song):
       # The if statement checks if the new song that we are inserting is different
       # than the songs already inside the playlist
       # It does this by calling the search_by_title method and looks at the ouput of that method
       if self.search_by_title(song.title) != -1:
           return

       # If the if statement is false then we know that the song is new 
       # We then add the new song to the end of the playlist
       self.songs = self.songs + [song]
      
       # Finally, we increase the num_songs by 1 for the new song      
       self.num_songs = self.num_songs + 1





   # This method delete a song from the playlist and moves the remaining songs to fill the gap
   def delete_by_title(self, song_title):
       # This calls the search_by_title method and stores the index or -1 to index to remove
       idx_to_remove = self.search_by_title(song_title)

       # If the index to remove is -1 meaning the song isn't in the playlist, then return False
       if idx_to_remove == -1:
           return False
       
       # If song is found then traverse through the playlist from the index where we found the song 
       # to the second to last song index in the playlist
       for idx in range(idx_to_remove, self.num_songs - 1):
           
           # Move every song that is to the right of the deleted song, back to one postion to the left  
           self.songs[idx] = self.songs[idx + 1]

       # This gets rid of the extra space in the playlist, since we deleetd the song
       self.num_songs = self.num_songs - 1
       
       # This sets the last spot of the playlist to None
       self.songs[self.num_songs] = None

       return True
       




   # This method traverses through the playlist and prints all the songs
   def traverse(self):
       # The for loop iterates through the playlist and prints every song in it
       for song in self.songs:
           print(song)