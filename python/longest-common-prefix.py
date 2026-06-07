# 
def main(strs:list[str]):
    
    min_str = min(strs, key=len)
    
    result = ""

    for i in range(len(min_str)):
        flag = True
        for str in strs:
            if min_str[:i + 1] != str[:i + 1]:
                flag = False
        
        if not flag:
            break 
        result += min_str[i]
    
    return result

if __name__ == "__main__":
    print(main(["flower","flow","flight"]))