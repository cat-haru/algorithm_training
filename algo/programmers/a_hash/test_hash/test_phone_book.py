"""
HOW TO TEST

$ python3 -m pytest algo/programmers/a_hash/test_hash
$ pytest algo/programmers/a_hash/test_hash
"""

import pytest

from algo.programmers.a_hash.b_phone_book import *


@pytest.mark.parametrize(
    'phone_book,expected',
    [
        (
            ["119", "97674223", "1195524421"],
            False
        ),
        (
            ["123","456","789"],
            True
        ),
        (
            ["12","123","1235","567","88"],
            False
        )
    ]
)
class TestSolution:
    def test_solution1(self, phone_book, expected):
        phone_book = phone_book.copy()
        res = solution1(phone_book)
        assert res is expected

    def test_solution2(self, phone_book, expected):
        phone_book = phone_book.copy()
        res = solution2(phone_book)
        assert res is expected

    def test_solution3(self, phone_book, expected):
        phone_book = phone_book.copy()
        res = solution3(phone_book)
        assert res is expected

    def test_solution4(self, phone_book, expected):
        phone_book = phone_book.copy()
        res = solution4(phone_book)
        assert res is expected
