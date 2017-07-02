#lyrics = "Hey you"

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
        #print lyrics # Doesn't print hey you..?

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

new_song = ["You see her when you fall asleep", "But never to touch and never to keep"]

create_new_song_object = Song(new_song)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

create_new_song_object.sing_me_a_song()
