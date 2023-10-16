#You may use import as below.
#import math

def solution(pos):
    # Write code here.
    # alphabet_to_num = {"A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6", "G": "7", "H": "8"}
    # x = int(alphabet_to_num[pos[0]])
    # y = int(pos[1])

    x = ord(pos[0]) - ord('A')
    y = ord(pos[1]) - ord('1')

    move = [2, -2, 1, -1]

    answer = 0

    for i in move:
        for j in move:
            if abs(i) + abs(j) == 3:
                if x + i >= 0 and x + i < 8:
                    if y + j >= 0 and y + j < 8:
                        answer += 1
    return answer

#The following is code to output testcase.
pos = "A7"
ret = solution(pos)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")