
# test using this in the terminal        
# python3 -m pytest -v tests/nodupes_tests.py                  
# pytest -v tests/nodupes_tests.py 

class NoDuplesPlaylist:
    def __init__(self, initial_songs=None):
        self.songs = []
        self.num_songs = 0
        
        if initial_songs:
            for song in initial_songs:
                self.insert_song(song)

    
    def search_by_title(self, song_title):
        for idx in range(self.num_songs):
            if self.songs[idx].title == song_title:
                return idx
        return -1

    def insert_song(self, song):
        if self.search_by_title(song.title) != -1:
            return 

        self.songs = self.songs + [song]
        
        self.num_songs = self.num_songs + 1



    def delete_by_title(self, title):
        for idx in range(self.num_songs):
            if self.songs[idx].title == title:

                for i in range(idx, self.num_songs - 1):
                    self.songs[i] = self.songs[i + 1]

                self.songs[self.num_songs - 1] = None

                self.num_songs = self.num_songs - 1
                return True
            
        return False


    def traverse(self):
        for song in self.songs:
            print(song)