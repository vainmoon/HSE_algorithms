def get_grouped_anagrams(strs):
    grouped_anagrams = {}
    for s in strs:
        letter_counter = {}
        for letter in s:
            if letter not in letter_counter:
                letter_counter[letter] = 1
            else:
                letter_counter[letter] += 1

        letter_counter = frozenset(letter_counter.items())

        if letter_counter not in grouped_anagrams:
            grouped_anagrams[letter_counter] = [s]
        else:
            grouped_anagrams[letter_counter].append(s)

    return list(grouped_anagrams.values())
