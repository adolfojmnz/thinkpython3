import string

def remove_punctuation(s):
    punctuation = '°!"#$%&/()=?¡¿|´+*¨´{}[]_-:.;,¬\\^^~``¬¬¬|°!1"'
    s_sans_punctuation = ""
    for letter in s:
        if letter not in punctuation:
            s_sans_punctuation += letter
    return s_sans_punctuation


def remove_punctuation_v2(s):
    s_without_punctuation = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punctuation += letter
    return s_without_punctuation

my_story = """
Pythons are constrictors, which means that they will 'squeeze' the life
out of their prey. They coil themselves around their prey and with
each breath the creature takes the snake will squeeze a little tighter
until they stop breathing completely. Once the heart stops the prey
is swallowed whole. The entire animal is digested in the snake's
stomach except for fur or feathers. What do you think happens to the fur,
feathers, beaks, and eggshells? The 'extra stuff' gets passed out as ---
you guessed it --- snake POOP! """

wds = remove_punctuation(my_story).split()
print(wds)
