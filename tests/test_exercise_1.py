from scripts.exercise_1 import Person, create_person_objects, get_april_birthdays, test

people = test()


def test_get_april_birthday_returns_april_bds():
    assert get_april_birthdays(people) == 11
