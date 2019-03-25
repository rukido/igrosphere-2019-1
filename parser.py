import re


def read_file(file_path):
    with open(file_path, 'r')as f:
        return f.read()


def filter_lines(regexp, lines):
    return [line for line in lines if re.match(regexp, line)]


if __name__ == "__main__":
    filename = "coverage-error.log"
    regexp = r"\[\d\d\d\d\.\d\d\.\d\d \d\d:\d\d:d\d\].+"
    lines = read_file(filename)
    print("Author is m.struk")
    print(filter_lines(regexp, lines))
