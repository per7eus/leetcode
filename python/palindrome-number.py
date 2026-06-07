def main(x:int):
    x = str(x)
    for i in range(len(x)/2):
        if x[i] != x[-i -1]:
                        return False
    return False
        return True



if __name__ == "__main__":
    print(main(241235141346134))2