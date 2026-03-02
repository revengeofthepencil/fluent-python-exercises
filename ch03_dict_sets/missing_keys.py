import re
import sys
import collections
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
test_file_path = SCRIPT_PATH / "tomwaits.txt"

WORD_REGEX = re.compile(r'\w+')

def main():
    print(f"missing key examples with test_file_path {test_file_path}")
    word_index1 = {}
    # try it with setdefault
    with open(test_file_path, encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_REGEX.finditer(line):
                word = match.group()
                col_no = match.start() + 1
                location = {line_no, col_no}
                word_index1.setdefault(word, []).append(location)

    for word in sorted(word_index1, key=str.upper):
        print(f"setdefault {word}: {word_index1[word]}")

    # try it with defaultdict(list) - yes, I know I'm repeating all the same code
    word_index2 = collections.defaultdict(list)
    with open(test_file_path, encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_REGEX.finditer(line):
                word = match.group()
                col_no = match.start() + 1
                location = {line_no, col_no}
                word_index2[word].append(location)

    for word in sorted(word_index2, key=str.upper):
        print(f"defaultdict {word}: {word_index2[word]}")



if __name__ == '__main__':
    main()