letter_counts = {}

for letter in "Mississipi":
    letter_counts[letter] = letter_counts.get(letter, 0) + 1
