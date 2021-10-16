"""
HOW TO TEST

$ python3 -m pytest algo/programmers/a_hash/test_hash
$ pytest algo/programmers/a_hash/test_hash
"""

import pytest

from algo.programmers.a_hash.a_marathon import solution1, solution2, solution3, solution4


@pytest.mark.parametrize(
    'participant,completion,expected',
    [
        (
            ['leo', 'kiki', 'eden'],
            ['eden', 'kiki'],
            'leo'
        ),
        (
            ['marina', 'josipa', 'nikola', 'vinko', 'filipa'],
            ['josipa', 'filipa', 'marina', 'nikola'],
            'vinko'
        ),
        (
            ['mislav', 'stanko', 'mislav', 'ana'],
            ['stanko', 'ana', 'mislav'],
            'mislav'
        )
    ]
)
class TestSolution:
    def test_solution1(self, participant, completion, expected):
        participant = participant.copy()
        completion = completion.copy()
        # cProfile.run('solution1(participant, completion)')
        res = solution1(participant, completion)
        assert res is expected

    def test_solution2(self, participant, completion, expected):
        participant = participant.copy()
        completion = completion.copy()
        res = solution2(participant, completion)
        assert res is expected

    def test_solution3(self, participant, completion, expected):
        participant = participant.copy()
        completion = completion.copy()
        res = solution3(participant, completion)
        assert res is expected

    def test_solution4(self, participant, completion, expected):
        participant = participant.copy()
        completion = completion.copy()
        res = solution4(participant, completion)
        assert res is expected
