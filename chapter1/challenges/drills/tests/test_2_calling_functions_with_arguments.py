from lib._2_calling_functions_with_arguments import *

def test_starts_with_letter():
    assert starts_with_the_letter_a("Apple") == True
    assert starts_with_the_letter_a("JavaScript") == False


def test_ends_with_letter():
    assert ends_with_the_letter_a("Java") == True
    assert ends_with_the_letter_a("JAVA") == True
    assert ends_with_the_letter_a("Server") == False


def test_contains_substring():
    assert contains_hello("Hello World") == True
    assert contains_hello("Municipal Waste") == False
    assert contains_hello("I just called to say hello") == True


def test_swap_hello_with_goodbye():
    assert substitute_hello_with_goodbye("hello folks") == "goodbye folks"
    assert substitute_hello_with_goodbye(
        "Say hello to my little friend") == "Say goodbye to my little friend"


def test_remove_x():
    assert remove_x("xoxo") == "oo"
    assert remove_x("OXO CUBE") == "OO CUBE"
    assert remove_x("xx") == ""
    assert remove_x("x") == ""
    assert remove_x("") == ""


def test_returns_first_half():
    assert first_half("Coding") == "Cod"
    assert first_half("sunburnt") == "sunb"


def test_second_half():
    assert second_half("Sampling") == "ling"
    assert second_half("Headlamp") == "lamp"
