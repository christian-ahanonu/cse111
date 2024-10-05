from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name('James', 'Brown') == 'Brown; James'
    assert make_full_name('Washington', 'George') == 'George; Washington'
    assert make_full_name('Pale', 'Snake') == 'Snake; Pale' 


def test_extract_family_name():
    assert extract_family_name('James; Brown') == 'James'
    assert extract_family_name('Washington; George') == 'Washington'
    assert extract_family_name('Pale; Snake') == 'Pale'


def test_extract_given_name():
    assert extract_given_name('James; Brown') == 'Brown'
    assert extract_given_name('Washington; George') == 'George'
    assert extract_given_name('Pale; Snake') == 'Snake'



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])