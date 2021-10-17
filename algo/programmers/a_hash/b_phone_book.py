"""
problem category : Hash (LEVEL 2)
https://programmers.co.kr/learn/courses/30/lessons/42577

## 문제 설명
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

* 구조대 : 119
* 박준영 : 97 674 223
* 지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

## 제한 사항
* phone_book의 길이는 1 이상 1,000,000 이하입니다.
  * 각 전화번호의 길이는 1 이상 20 이하입니다.
  * 같은 전화번호가 중복해서 들어있지 않습니다.

## 입출력 예제

----------------------------------+-------
phone_book                        | return
----------------------------------+-------
["119", "97674223", "1195524421"] | false
["123","456","789"]	              | true
["12","123","1235","567","88"]    | false
----------------------------------+-------

## 입출력 예 설명
입출력 예 #1
앞에서 설명한 예와 같습니다.

입출력 예 #2
한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.

입출력 예 #3
첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.
"""

from algo.common.utils import TimeProfiler


@TimeProfiler(is_nano = True)
def solution1(phone_book):
    answer = True

    for target_idx, target_num in enumerate(phone_book):
        for verifi_idx, verifi_num in enumerate(phone_book):

            if (target_idx != verifi_idx) and (len(target_num) <= len(verifi_num)):
                idx = verifi_num.find(target_num)
                if idx == 0:
                    answer = False

    return answer


@TimeProfiler(is_nano = True)
def solution2(phone_book):
    answer = True

    for target_idx, target_num in enumerate(phone_book):
        for verifi_idx, verifi_num in enumerate(phone_book):

            if (target_idx != verifi_idx) and (len(target_num) <= len(verifi_num)):
                idx = verifi_num.find(target_num)
                if idx == 0:
                    answer = False

    return answer


@TimeProfiler(is_nano = True)
def solution3(phone_book):
    answer = True

    sorted_phone_book = sorted(phone_book)

    for cur_idx, cur_num in enumerate(sorted_phone_book[:-1]):
        next_num = sorted_phone_book[cur_idx+1]

        if len(cur_num) <= len(next_num):
            pos = next_num.find(cur_num)
            if pos == 0:
                answer = False
    return answer


@TimeProfiler(is_nano = True)
def solution4(phone_book):
    answer = True

    sorted_phone_book = sorted(phone_book)

    for cur_idx, cur_num in enumerate(sorted_phone_book[:-1]):
        next_num = sorted_phone_book[cur_idx+1]

        if len(cur_num) <= len(next_num):
            if next_num.startswith(cur_num):
                answer = False
    return answer
