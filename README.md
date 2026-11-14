# Algorithm-to-Programmers

[프로그래머스](https://school.programmers.co.kr/learn/challenges) 알고리즘 문제 풀이 기록입니다.
풀이와 함께 막혔던 부분, 오답 이유를 같이 남기고 있어요.

<!-- STATS:START -->
### 📊 풀이 현황

![해결한 문제 10개](https://img.shields.io/badge/%ED%95%B4%EA%B2%B0%ED%95%9C_%EB%AC%B8%EC%A0%9C-10%EA%B0%9C-brightgreen?style=for-the-badge) ![사용 언어 2개](https://img.shields.io/badge/%EC%82%AC%EC%9A%A9_%EC%96%B8%EC%96%B4-2%EA%B0%9C-blue?style=for-the-badge)

> 같은 문제를 여러 언어로 풀어도 '해결한 문제 수'에는 한 번만 셉니다.

#### 언어별 사용률

![Python 10개 · 90.9%](https://img.shields.io/badge/Python-10%EA%B0%9C_%C2%B7_90.9%25-3776AB?style=for-the-badge&logo=python&logoColor=white) ![JavaScript 1개 · 9.1%](https://img.shields.io/badge/JavaScript-1%EA%B0%9C_%C2%B7_9.1%25-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white)

#### 레벨별 해결 수

![Lv.0 7](https://img.shields.io/badge/Lv.0-7-8E9AAF?style=flat-square) ![Lv.1 3](https://img.shields.io/badge/Lv.1-3-4CAF50?style=flat-square) ![Lv.2 0](https://img.shields.io/badge/Lv.2-0-D0D5DB?style=flat-square) ![Lv.3 0](https://img.shields.io/badge/Lv.3-0-D0D5DB?style=flat-square) ![Lv.4 0](https://img.shields.io/badge/Lv.4-0-D0D5DB?style=flat-square) ![Lv.5 0](https://img.shields.io/badge/Lv.5-0-D0D5DB?style=flat-square)

<details><summary>풀이 목록 (10)</summary>

| 레벨 | 번호 | 제목 | 풀이 |
| --- | --- | --- | --- |
| Lv.0 | [120802](https://school.programmers.co.kr/learn/courses/30/lessons/120802) | 두 수의 합 구하기 | [Python](python/Lv.0/120802.py) |
| Lv.0 | [120803](https://school.programmers.co.kr/learn/courses/30/lessons/120803) | 두 수의 차 구하기 | [Python](python/Lv.0/120803.py) |
| Lv.0 | [120804](https://school.programmers.co.kr/learn/courses/30/lessons/120804) | 두 수의 곱 구하기 | [Python](python/Lv.0/120804.py), [JavaScript](JavaScript/Lv.0/120804.js) |
| Lv.0 | [120805](https://school.programmers.co.kr/learn/courses/30/lessons/120805) | 몫 구하기 | [Python](python/Lv.0/120805.py) |
| Lv.0 | [340205](https://school.programmers.co.kr/learn/courses/30/lessons/340205) | [PCCE 기출문제] 3번 / 수 나누기 | [Python](python/Lv.0/340205.py) |
| Lv.0 | [340206](https://school.programmers.co.kr/learn/courses/30/lessons/340206) | [PCCE 기출문제] 2번 / 각도 합치기 | [Python](python/Lv.0/340206.py) |
| Lv.0 | [340207](https://school.programmers.co.kr/learn/courses/30/lessons/340207) | [PCCE 기출문제] 1번 / 문자 출력 | [Python](python/Lv.0/340207.py) |
| Lv.1 | [12912](https://school.programmers.co.kr/learn/courses/30/lessons/12912) | 두 정수 사이의 합 | [Python](python/Lv.1/12912.py) |
| Lv.1 | [12931](https://school.programmers.co.kr/learn/courses/30/lessons/12931) | 자릿수 더하기 | [Python](python/Lv.1/12931.py) |
| Lv.1 | [176963](https://school.programmers.co.kr/learn/courses/30/lessons/176963) | 추억 점수 | [Python](python/Lv.1/176963.py) |

</details>
<!-- STATS:END -->

## 📁 폴더 구조

```
<언어>/Lv.<레벨>/<문제번호>.<확장자>

python/Lv.1/176963.py
c/Lv.1/176963.c
swift/Lv.2/12345.swift
```

- 파일 첫 줄에 `# 문제 제목` (C, Swift 등은 `// 문제 제목`) 주석을 적으면 풀이 목록에 제목이 표시됩니다.
- 새 언어를 추가하려면 `scripts/update_readme.py` 상단의 `LANGS`에 확장자를 한 줄 추가하세요.

## 🔄 README 갱신 방법

위의 `📊 풀이 현황`은 직접 고치지 않고 스크립트가 만듭니다.

```
python3 scripts/update_readme.py
```

`main` 브랜치에 push하면 GitHub Actions(`.github/workflows/update-readme.yml`)가 같은 작업을 자동으로 실행합니다.
