class Song(object):

    def sing_me_a_song(self, lyrics): # Cannot write only lyrics here as it prints the whole tuple while considering it as an individual object.
        for line in lyrics: # Writing self is important. Do not write *lyrics as you're not providing 2 or more lists. It is still preferable that you explicity mention the argument with a different variable though. It makes your calculation easier.
            print line

happy_bday = Song()
happy_bday.sing_me_a_song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])
bulls_on_parade = Song()
bulls_on_parade.sing_me_a_song(["They rally around tha family",
                        "With pockets full of shells"])
new_song = ["You see her when you fall asleep", "But never to touch and never to keep"]

create_new_song_object = Song()

create_new_song_object.sing_me_a_song(new_song)
