staples = {
    '[': ']',
    '(': ')',
    '{': '}',
}


def main(s:str):
    while s != "":
        for i in range(len(s) - 1):
            if staples.get(s[i]) == s[i + 1]:
                s = s[:i] + s[i + 2:]
                break
        else:
            return False
    return True



if __name__ == "__main__":
    print(main("()"))