from address import extract_city,extract_state,extract_zipcode

import pytest

def test_extract_city():
    assert extract_city('23 melborne street, Abuja, AB 90210') == "Abuja"
    assert extract_city('32 cambridge street, Rexburg, RE 29319') == 'Rexburg'
    assert extract_city('34 charles street, Kano, KA 95923') == 'Kano'


def test_extract_state():
    assert extract_state('23 melborne street, Abuja, AB 90210') == "AB"
    assert extract_state('32 cambridge street, Rexburg, RE 29319') == 'RE'
    assert extract_state('34 charles street, Kano, KA 95923') == 'KA'
    

def test_extract_zipcode():
    assert extract_zipcode('23 melborne street, Abuja, AB 90210') == "90210"
    assert extract_zipcode('32 cambridge street, Rexburg, RE 29319') == '29319'
    assert extract_zipcode('34 charles street, Kano, KA 95923') == '95923'


pytest.main(["-v", "--tb=line", "-rN", __file__])