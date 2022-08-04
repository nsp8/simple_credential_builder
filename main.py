from random import randint, shuffle
import string


def main(strength: int = 16):
    assert strength >= 8
    special_characters = "!@#$%^&*()-+_=.[]"
    all_characters = (string.ascii_lowercase,
                      string.ascii_uppercase,
                      string.digits,
                      special_characters)
    s = list()
    n = strength // len(all_characters)
    for t in all_characters:
        for _ in range(n):
            i = randint(0, len(t))
            s.append(t[i - 1])
    shuffle(s)
    credentials = "".join(s)
    print(credentials)


if __name__ == "__main__":
    main()
