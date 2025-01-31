import os.path
import sys


def find_d(args: list[str]):
    if len(args) >= 2:
        for index, it in enumerate(args):
            if (it == '-d') & (len(args) > index):
                return args[index + 1]
    return 0


def find_l(args: list[str]):
    if len(args) >= 2:
        for index, it in enumerate(args):
            if (it == '-l') & (len(args) > index):
                return args[index + 1]
    return 0


def find_n(args: list[str]):
    if len(args) >= 2:
        for index, it in enumerate(args):
            if (it == '-n') & (len(args) > index):
                return int(args[index + 1])
    else:
        print('Вы не указали параметр -l')
    return 200


def find_file(args: list[str]):
    if len(args) >= 2:
        for index, it in enumerate(args):
            if (it == '-f') & (len(args) > index):
                return args[index + 1]
    else:
        print('Вы не указали параметр -f')
    return 0


def write_substrings(string_list: list[str]):
    for it, string in enumerate(string_list):
        print('Substring #', it, ":")
        print(string)


def split_string(string: str, n: int):
    string_list = string.split()
    string_len = 0
    melt = 0
    new_str_list = []
    new_str = ""
    for substring in string_list:
        if substring.find("@") != -1:
            melt = 1

        if (string_len + len(substring) < n) | melt == 1:
            string_len = string_len + len(substring) + 1
            new_str = new_str + ' ' + substring
        else:
            new_str_list.append(new_str)
            new_str = ""
            string_len = 0
            
        if (substring.find(":") != -1) & melt:
            melt = 0
    return new_str_list


def read_file(filename: str):
    if os.path.getsize(filename) > 0:
        file = open(filename, encoding="utf8")
        string = file.readlines()
        file.close()
        return string
    else:
        print('Файл пуст(')
        return 0


def main():
    print('dz_bat_1')
    n = find_n(sys.argv)
    filename = find_file(sys.argv)

    print('Выбранный файл:', filename)
    print('Длина строки:', n)

    string_list = []
    text = ''
    strings = read_file(filename)
    for it in strings:
        text += it

    string_splited = split_string(text, n)
    for i in string_splited:
        string_list.append(i)
    write_substrings(string_list)


if __name__ == '__main__':
    main()
