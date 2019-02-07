"""
string_maker test
"""


import pytest
import text_formatter


def test_string_maker_length():
    length = 10
    text_length_10 = text_formatter.string_maker(length=length)
    assert len(text_length_10('12345')) == length


def test_string_maker_length_over():
    length = 10
    text_length_10 = text_formatter.string_maker(length=length)
    assert len(text_length_10('1234567890123')) == length


def test_string_maker_align_left():
    test_word = 'AAAAA'
    length = 20
    text_align_left = text_formatter.string_maker(length=length)
    assert text_align_left(test_word) == test_word.ljust(length, ' ')


def test_string_maker_align_right():
    test_word = 'AAAAA'
    length = 20
    text_align_right = text_formatter.string_maker(
        length=length, align='RIGHT')
    assert text_align_right(test_word) == test_word.rjust(length, ' ')


def test_string_maker_align_center():
    test_word = 'AAAAA'
    length = 20
    text_align_center = text_formatter.string_maker(length=length, align='MID')
    assert text_align_center(test_word) == test_word.center(length, ' ')


def test_string_maker_align_center_padding_star():
    test_word = 'AAAAA'
    length = 20
    padding = '*'
    text_align_center_padding_star = text_formatter.string_maker(
        length=length, align='MID', padding=padding)
    assert text_align_center_padding_star(test_word) \
        == test_word.center(length, padding)


def test_number_maker_int_length():
    length = 10
    text_length_10 = text_formatter.number_maker(length=length)
    assert len(text_length_10(12345)) == length


def test_number_maker_float_length():
    test_number = 12345678.1
    length = 10
    text_length = text_formatter.number_maker(length=length)
    assert len(text_length(test_number)) == length


def test_number_maker_int_length_over():
    length = 10
    text_length_10 = text_formatter.number_maker(length=length)
    assert len(text_length_10(1234567890123)) == length


def test_number_maker_float_length_over():
    length = 10
    text_length_10 = text_formatter.number_maker(length=length)
    assert len(text_length_10(123456789.123)) == length


def test_number_maker_align_left():
    test_number = 12345.1
    result_text = '12345.10'
    length = 20
    text_align_left = text_formatter.number_maker(
        length=length, align='LEFT', precision='2')
    assert text_align_left(test_number) == result_text.ljust(length, ' ')


def test_number_maker_align_right():
    test_number = 12345.1
    result_text = '12345.10'
    length = 20
    text_align_left = text_formatter.number_maker(
        length=length, align='RIGHT', precision='2')
    assert text_align_left(test_number) == result_text.rjust(length, ' ')


def test_number_maker_align_right_padding_zero():
    test_number = 12345.1
    length = 20
    padding = '0'
    text_align_right_padding_zero = text_formatter.number_maker(
        length=length, align='RIGHT', padding=padding, precision=1)
    assert text_align_right_padding_zero(test_number) \
        == str(test_number).rjust(length, padding)
