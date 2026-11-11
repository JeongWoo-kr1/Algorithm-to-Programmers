# Algorithm-to-Programmers

[프로그래머스](https://school.programmers.co.kr/learn/challenges) 알고리즘 문제 풀이 기록입니다.
풀이와 함께 막혔던 부분, 오답 이유를 같이 남기고 있어요.

<!-- STATS:START -->
### 📊 풀이 현황

**총 3문제 해결** · 사용 언어 1개 · 풀이 파일 3개

> 같은 문제를 여러 언어로 풀어도 '해결한 문제 수'에는 한 번만 셉니다.

#### 언어별 사용률

| 언어 | 풀이 수 | 비율 | 그래프 |
| --- | ---: | ---: | --- |
| Python | 3 | 100.0% | `████████████████████` |

#### 레벨별 해결 수

| 레벨 | Python | 합계 | 분포 |
| --- | ---: | ---: | --- |
| Lv.0 | 2 | 2 | `█████████████░░░░░░░` |
| Lv.1 | 1 | 1 | `███████░░░░░░░░░░░░░` |
| Lv.2 | 0 | 0 | `░░░░░░░░░░░░░░░░░░░░` |
| Lv.3 | 0 | 0 | `░░░░░░░░░░░░░░░░░░░░` |
| Lv.4 | 0 | 0 | `░░░░░░░░░░░░░░░░░░░░` |
| Lv.5 | 0 | 0 | `░░░░░░░░░░░░░░░░░░░░` |

<details><summary>풀이 목록 (3)</summary>

| 레벨 | 번호 | 제목 | 풀이 |
| --- | --- | --- | --- |
| Lv.0 | [340206](https://school.programmers.co.kr/learn/courses/30/lessons/340206) | [PCCE 기출문제] 2번 / 각도 합치기 | [Python](python/Lv.0/340206.py) |
| Lv.0 | [340207](https://school.programmers.co.kr/learn/courses/30/lessons/340207) | [PCCE 기출문제] 1번 / 문자 출력 | [Python](python/Lv.0/340207.py) |
| Lv.1 | [176963](https://school.programmers.co.kr/learn/courses/30/lessons/176963) | - | [Python](python/Lv.1/176963.py) |

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
