import pytest
from string_utils import StringUtils

##функция capitalize##
obj = StringUtils() 

def test_capitalize_string():
##позитивные сценарии##
    assert obj.capitalize("skypro") == "Skypro"
    assert obj.capitalize("12345") == "12345"
    assert obj.capitalize("добрый день") == "Добрый день"
##негативные сценарии##    
    assert obj.capitalize("") == ""
    assert obj.capitalize(" ")  == " "

##функция trim##    

def test_trim():
##позитивные сценарии##
    assert obj.trim(" skypro") == "skypro"
    assert obj.trim(" skypro ") == "skypro "
##негативные сценарии## 
    assert obj.trim("") == ""


##функция to_list##
@pytest.mark.parametrize('string, delimeter, result', [
    ("понедельник,вторник,среда", ",", ["понедельник", "вторник", "среда"] ),
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
    ("", None, [])
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = obj.to_list(string)
    else:
        res = obj.to_list(string, delimeter)
        assert res == result

##функция contains##
@pytest.mark.parametrize('string, symbol, result', [
    ("Skypro", "S", True),
    ("Skypro", "L", False),
    ("Скайпро", "S", False)
])
def test_contains(string, symbol,result):
    res = obj.contains(string, symbol)
    assert res == result

##метод delete_symbol##
@pytest.mark.parametrize('string, symbol, result', [
##позитивные сценарии## 
    ("Skypro", "S", "kypro"),
    ("Skypro", "Sky", "pro"),
    ("Скайпро", "Скайпро", ""),
##негативные сценарии## 
    ("Skypro", "", "Skypro"),
    ("Skypro", "U", "Skypro")
])
def test_delete_sumbol(string, symbol, result):
    res = obj.delete_symbol(string, symbol)
    assert res == result

##метод starts_with##
@pytest.mark.parametrize('string, symbol, result', [
##позитивные сценарии## 
    ("Skypro", "S", True),
    ("Skypro", "K", False),
    ("12345", "1", True),
##негативные сценарии## 
    ("Skypro", "s", False),
    ("skypro", "S", False)
])
def test_starts_with(string, symbol, result):
    res = obj.starts_with(string, symbol)
    assert res == result

# ##метод end_with##
@pytest.mark.parametrize('string, symbol, result', [
##позитивные сценарии## 
    ("Skypro", "o", True),
    ("Skypro", "k", False),
    ("12345", "5", True),
##негативные сценарии## 
    ("Skypro", "s", False),
    ("skypro", "a", False),
    ("", " ", False)
])
def test_end_with(string, symbol, result):
    res = obj.end_with(string, symbol)
    assert res == result

# ##метод is_empty##
@pytest.mark.parametrize('string, result', [
##позитивные сценарии## 
    ("", True),
    (" ", True),
    ("   ", True),
##негативные сценарии## 
    ("Skypro", False),
    ("skypro skyeng", False),
    ("111", False)
])
def test_is_empty(string, result):
    res = obj.is_empty(string)
    assert res == result

##метод list_to_string##
@pytest.mark.parametrize('lst, joiner, result', [
##позитивные сценарии## 
    (["понедельник","вторник","среда"], ",", "понедельник,вторник,среда"),
    (["Санкт", "Петербург"], "-", "Санкт-Петербург"),
##негативные сценарии## 
    ([], None, ""),
    ([], "skyeng", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = obj.list_to_string(lst)
    else:
        res =obj.list_to_string(lst, joiner)
        assert res == result
