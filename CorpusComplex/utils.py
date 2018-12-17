
# coding: utf-8

import requests
from bs4 import BeautifulSoup


def permute(s):
    result = [[s]]
    for i in range(1, len(s)):
        first = [s[:i]]
        rest = s[i:]
        for p in permute(rest):
            result.append(first + p)
    return result


def naver_search(rawNoun):
    basic_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    # 파싱
    html = requests.get(basic_url+rawNoun, headers=headers).text
    soup = BeautifulSoup(html, "lxml")
    mainPack = str(soup.find('div', 'main_pack'))

    # 파워링크
    plAd = str(soup.find('div', "ad_section section _pl_section bg_type_v2"))
    # 비즈사이트
    bzAd = str(soup.find('div', "ad_section section _bz_section bg_type_v2"))
    # 파워콘텐츠
    bgAd = str(soup.find('div', "ad_section section bg_type_v2"))

    count = mainPack.count(rawNoun) - plAd.count(rawNoun) - \
        bzAd.count(rawNoun) - bgAd.count(rawNoun)

    return count


def evaluate(x):
    answer, pred = x
    count = 0
    for w in answer.split(' '):
        if w in pred.split(' '):
            count += 1
    return count / len(answer.split(' '))
