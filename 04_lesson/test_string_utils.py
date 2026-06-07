import pytest
from string_utils import StringUtils

utils = StringUtils()

# Тесты для метода capitalize

def test_capitalize_positive():
    """Позитивный тест: нормальная строка, первая буква становится заглавной"""
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("hello world") == "Hello world"
    assert utils.capitalize("123abc") == "123abc"

def test_capitalize_negative():
    """Негативные сценарии: пустая строка, строка из пробелов, уже заглавная"""
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "
    assert utils.capitalize("SKYPRO") == "Skypro"
    assert utils.capitalize("skypro") == "Skypro"

# Тесты для метода trim (удаление пробелов в начале)

def test_trim_positive():
    """Позитивный тест: удаление ведущих пробелов"""
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("  hello  ") == "hello  "
    assert utils.trim("no spaces") == "no spaces"

def test_trim_negative():
    """Негативные сценарии: пустая строка, только пробелы, строка без пробелов"""
    assert utils.trim("") == ""
    assert utils.trim("     ") == ""
    assert utils.trim("text") == "text"

# Тесты для метода contains (проверка наличия символа)

def test_contains_positive():
    """Позитивный тест: символ присутствует"""
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("SkyPro", "k") is True
    assert utils.contains("12345", "3") is True
    assert utils.contains("abc", "") is True     # Возвращает True при поиске пустой строки      

def test_contains_negative():
    """Негативные сценарии: символ отсутствует, пустая строка с непустым символом"""
    assert utils.contains("SkyPro", "U") is False
    assert utils.contains("", "a") is False        
    assert utils.contains("abc", "d") is False
    assert utils.contains("SkyPro", "Pro") is True   
    assert utils.contains("SkyPro", "pro") is False  # регистр важен

# Тесты для метода delete_symbol (удаление подстроки)

def test_delete_symbol_positive():
    """Позитивный тест: удаление символов/подстрок"""
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert utils.delete_symbol("hello world", "o") == "hell wrld"
    assert utils.delete_symbol("aaaaa", "a") == ""

def test_delete_symbol_negative():
    """Негативные сценарии: символ отсутствует, пустая строка"""
    assert utils.delete_symbol("SkyPro", "Z") == "SkyPro"
    assert utils.delete_symbol("", "a") == ""
    assert utils.delete_symbol("abc", "") == "abc"