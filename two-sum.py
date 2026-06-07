def main(nums: list, target: int) -> list:
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []



if __name__ == '__main__':
    print(main([0,4,3,0], 0))