#!/usr/bin/env python3
"""README의 통계 영역을 풀이 폴더 기준으로 다시 만든다.

폴더 규칙 : <언어 폴더>/Lv.<레벨>/<문제번호>.<확장자>
            예) python/Lv.1/176963.py, swift/Lv.2/12345.swift
실행 방법 : python3 scripts/update_readme.py
"""

import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
START = "<!-- STATS:START -->"
END = "<!-- STATS:END -->"
LESSON_URL = "https://school.programmers.co.kr/learn/courses/30/lessons/{}"
BAR_WIDTH = 20

# 확장자 -> (표시 이름, 한 줄 주석 기호). 새 언어는 여기에 한 줄만 추가하면 된다.
LANGS = {
    ".py": ("Python", "#"),
    ".c": ("C", "//"),
    ".cpp": ("C++", "//"),
    ".swift": ("Swift", "//"),
    ".java": ("Java", "//"),
    ".js": ("JavaScript", "//"),
    ".kt": ("Kotlin", "//"),
}

LEVEL_DIR = re.compile(r"Lv\.(\d+)")


def read_title(path, comment):
    """파일 첫 줄이 주석이면 그 내용을 문제 제목으로 쓴다."""
    try:
        first = path.read_text(encoding="utf-8").splitlines()[0].strip()
    except (OSError, UnicodeDecodeError, IndexError):
        return ""
    if first.startswith("#!") or not first.startswith(comment):
        return ""
    return first[len(comment):].strip().replace("|", "\\|")


def collect():
    """(레벨, 문제번호) -> {언어: 파일 경로} 형태로 풀이를 모은다."""
    problems = defaultdict(dict)
    for path in sorted(ROOT.glob("*/Lv.*/*")):
        match = LEVEL_DIR.fullmatch(path.parent.name)
        info = LANGS.get(path.suffix.lower())
        if not (path.is_file() and match and info):
            continue
        problems[(int(match.group(1)), path.stem)][info[0]] = path
    return problems


def bar(count, total):
    filled = round(BAR_WIDTH * count / total) if total else 0
    return "`" + "█" * filled + "░" * (BAR_WIDTH - filled) + "`"


def percent(count, total):
    return f"{count / total * 100:.1f}%" if total else "0.0%"


def build(problems):
    lang_files = Counter()              # 언어별 풀이 파일 수
    level_unique = Counter()            # 레벨별 해결한 문제 수 (언어 중복 제외)
    level_lang = defaultdict(Counter)   # 레벨 x 언어

    for (level, _), files in problems.items():
        level_unique[level] += 1
        for lang in files:
            lang_files[lang] += 1
            level_lang[level][lang] += 1

    total = len(problems)
    total_files = sum(lang_files.values())
    langs = [lang for lang, _ in lang_files.most_common()]
    levels = sorted(set(range(6)) | set(level_unique))

    out = ["### 📊 풀이 현황", ""]
    out.append(f"**총 {total}문제 해결** · 사용 언어 {len(langs)}개 · 풀이 파일 {total_files}개")
    out.append("")
    out.append("> 같은 문제를 여러 언어로 풀어도 '해결한 문제 수'에는 한 번만 셉니다.")
    out.append("")

    # 언어별 사용률
    out += ["#### 언어별 사용률", "", "| 언어 | 풀이 수 | 비율 | 그래프 |", "| --- | ---: | ---: | --- |"]
    for lang in langs:
        n = lang_files[lang]
        out.append(f"| {lang} | {n} | {percent(n, total_files)} | {bar(n, total_files)} |")
    if not langs:
        out.append("| - | 0 | 0.0% | - |")
    out.append("")

    # 레벨별 해결 수
    header = ["레벨", *langs, "합계", "분포"]
    out += ["#### 레벨별 해결 수", "", "| " + " | ".join(header) + " |",
            "| --- |" + " ---: |" * (len(langs) + 1) + " --- |"]
    for level in levels:
        cells = [f"Lv.{level}"]
        cells += [str(level_lang[level][lang]) for lang in langs]
        cells += [str(level_unique[level]), bar(level_unique[level], total)]
        out.append("| " + " | ".join(cells) + " |")
    out.append("")

    # 풀이 목록
    out += [f"<details><summary>풀이 목록 ({total})</summary>", "",
            "| 레벨 | 번호 | 제목 | 풀이 |", "| --- | --- | --- | --- |"]
    for key in sorted(problems, key=lambda k: (k[0], len(k[1]), k[1])):
        level, pid = key
        files = problems[key]
        ordered = [lang for lang in langs if lang in files]
        title = ""
        for lang in ordered:
            comment = next(c for name, c in LANGS.values() if name == lang)
            title = read_title(files[lang], comment)
            if title:
                break
        number = f"[{pid}]({LESSON_URL.format(pid)})" if pid.isdigit() else pid
        links = ", ".join(f"[{lang}]({files[lang].relative_to(ROOT).as_posix()})" for lang in ordered)
        out.append(f"| Lv.{level} | {number} | {title or '-'} | {links} |")
    out += ["", "</details>"]
    return "\n".join(out)


def main():
    block = f"{START}\n{build(collect())}\n{END}"
    text = README.read_text(encoding="utf-8") if README.exists() else "# Algorithm-to-Programmers\n"
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if pattern.search(text):
        new = pattern.sub(lambda _: block, text)  # lambda: 제목 속 백슬래시 오해석 방지
    else:
        new = text.rstrip() + "\n\n" + block + "\n"
    if new != text:
        README.write_text(new, encoding="utf-8")
        print("README 갱신 완료")
    else:
        print("변경 사항 없음")


if __name__ == "__main__":
    main()
