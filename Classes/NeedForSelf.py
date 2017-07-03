lyrics = "Hey you"

class Song(object):

    def __init__(self, lyric):
        self.lyric = lyric
        print lyrics # prints hey you because that's a global variable
        # If you were to write
        ''' lyrics = 'hey you'

            Class Song(object)
                def __init__(self)
                    print lyrics
            happy_bday = Song()

            The above code would print only hey you.
        '''

    def sing_me_a_song(self):
        for line in self.lyric:
            print line

happy_bday = Song(["Happy birthday to you", # We need to write these lyrics here because __init__ takes arguments which are lyrics.
                   "I don't want to get sued", # These lyrics written in the function wouldn't work because function sing_me_a_song takes self as argument
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

new_song = ["You see her when you fall asleep", "But never to touch and never to keep"]

create_new_song_object = Song(new_song)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

create_new_song_object.sing_me_a_song()
