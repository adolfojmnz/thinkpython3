def how_many_words(xs):
    count = 0
    for i in xs:
        if len(i) == 5:
           count += 1
    print(count)


xs = ["Hello", "Astro", "Venus", "Pluto", "Titan"]
how_many_words(xs)
