def solution(s,numRows):
    arr = [""]*numRows

    def down(newArr):
        for val in range(len(newArr)):
            arr[val] += newArr[val]
    def up(newArr):
        for val in range(len(newArr)):
            arr[-val-2] += newArr[val]

    while len(s)!=0 :
        down(s[:numRows])
        s = s[numRows:]

        up(s[:numRows-2])
        s = s[numRows-2:]

    ret  =""
    for x in range(numRows):
        ret += arr[x]

    print(ret)

solution("PAYPALISHIRING",3)