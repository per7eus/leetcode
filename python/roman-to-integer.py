dict_num = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}





def main(s:str) -> int:
    result = 0 
    for i in range(len(s) - 1):
        if dict_num.get(s[i]) < dict_num.get(s[i + 1]):
            result -= dict_num.get(s[i])
            continue
        result += dict_num.get(s[i])
    
    result += dict_num.get(s[-1])
    return result



if __name__ == "__main__":
    print(main("MCMXCIV"))