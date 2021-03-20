def plusMinus(arr):
    pos_cnt = 0
    neg_cnt = 0
    zero_cnt = 0

    for num in arr:
        if num > 0:
            pos_cnt += 1
        elif num < 0:
            neg_cnt += 1
        else:
            zero_cnt += 1

    print(f"{pos_cnt/len(arr)}\n{neg_cnt/len(arr)}\n{zero_cnt/len(arr)}")

if __name__ == '__main__':
    n = int(input())

    arr = [int(num) for num in input().rstrip().split()]

    plusMinus(arr)