text_ = """
There’s no evidence that dark matter interacts with any other force but gravity
Most of the universe is made of one of two kinds of mysterious substances, 
called dark matter and dark energy. From all the evidence, these two cosmic
components only interact with “normal” matter through the gravitational force.
And a recent nuclear experiment reveals no presence of any dark contamination in
the bonds between atomic nuclei to a level twenty times better than previously recorded.

The stuff you and me are made out of is called “normal” matter, despite the fact that it 
makes up less than 5% of all the matter and energy in the universe. Besides people, planets, 
stars, and random gas clouds, the cosmos is also composed of dark matter and dark energy.

We can’t see the dark matter directly (hence the name), but we know it’s out there based on
its gravitational relationships with everything else. It makes stars orbit faster than they 
would otherwise inside galaxies, it makes galaxies zip around faster inside of clusters, 
and it shapes and sculpts the largest structures in the universe.

And as for dark energy, that’s just the name we give to the accelerated expansion of the universe,
and that’s about all we know about it.

As far as we’ve been able to measure, dark matter only connects to normal matter through 
its gentle gravitational whispers and subtle tugs. But we don’t know for sure if dark matter
also talks to normal through one of the other three fundamental forces (strong nuclear, 
weak nuclear, or electromagnetic) or if there are new, fifth forces of nature floating around. 
One way to poke at this is to very carefully measure various atomic and nuclear properties and 
compare those properties to what we expect from known physics. If there’s a major discrepancy, 
it could be a sign that there’s more to the dark side of the universe.
"""

# Removes all punctuation from the string.
# Breaks the string into a list of words.
# Counts the number of words in your text that contain the letter “e”.
# Percentage of the words that contain the letter "e".
# Your text contains 243 words, of which 109 (44.8%) contain an "e".


import string

def remove_punctuations(s):
    print('Print the text without punctuations')
    s_without_punctuation = ''
    for i in s:
        if i not in string.punctuation:
            s_without_punctuation = s_without_punctuation + i
    return s_without_punctuation

def split_in_list(s):
    count = 0
    for i in range(len(s.split())):
        count += 1
    return count

def count_letter_x(s, letter):
    count = 0
    for i in s.split():
        if letter in i:
            count += 1
    return count

def percentage(text, letter):
    x = count_letter_x(text, letter)
    y = split_in_list(text)
    value = x / y * 100
    return f'Your text contains {y} words, of which {x} ({value:{1}.{4}}%) contains the letter "{letter}".'

def call_the_functions(text, letter):
    print(remove_punctuations(text))
    print(f'Words in the text: {split_in_list(text)}')
    print(f'Words with the letter "e": {count_letter_x(text, letter)}')
    print(percentage(text, letter))


call_the_functions(text_, 'e')
