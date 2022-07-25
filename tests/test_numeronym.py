from numeronym import extended_numeronym, my_numeronym


def test_my_numeronym():
    numeronym = my_numeronym("ab")
    assert numeronym == "ab"


def test_extended_numeronyms():
    numeronyms = extended_numeronym(["institutionalization", "intercrystallization", "ab",
                                     "interdifferentiation", "internationalization", "abcd", "abbd"])
    print(numeronyms)
    assert numeronyms == ['i18n', 'in17n', 'ab', 'int16n', 'inte15n', 'a2d', 'ab1d']

