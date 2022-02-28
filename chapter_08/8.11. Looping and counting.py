def count_letter(text, letter):
    count = 0
    for c in text:
        if c == letter:
            count += 1
    print(count)

count_letter('banana', 'a')