staples = {
    '[': ']',
    '(': ')',
    '{': '}',
}


def main(string:str):
    while string != "":
        for i in range(len(string) - 1):
            if staples.get(string[i]) == string[i + 1]:
                string = string[:i] + string[i + 2:]
                break
        else:
            return False
    return True



if __name__ == "__main__":
    print(main("()"))