def filter_manually(func, collection):
    for e in collection:
        if func(e):
            yield e

if __name__ == '__main__':
    VOVELS = {'a', 'e', 'o', 'u', 'y', 'i'}

    def is_vowel(l):
        return l in VOVELS

    a = "this is a long string"
    for letter in filter(is_vowel, a):
        print(letter,end=' ')
