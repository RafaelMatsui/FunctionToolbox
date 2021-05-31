def spin_words(sentence):
    return ' '.join([i[::-1] if len(i) > 4 else i for i in sentence.split(' ')])


def anagrams(word, words):
    anagrams = []
    for i in words:
        if sorted(i) == sorted(word):
            anagrams.append(i)
    return anagrams

