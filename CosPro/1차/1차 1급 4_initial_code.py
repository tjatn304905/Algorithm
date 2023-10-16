#You may use import as below.
import math

def my_solution(num):
    # Write code here.
    answer = num + 1
    i = 1
    j = 0
    k = j
    while math.remainder(answer, i) == 0:
        k = j
        j += i
        i *= 10
    answer += k
    return answer

def solution(num):
    # Write code here.
    num += 1
    answer = ''.join('1' if x == '0' else x for x in str(num))
    return answer

#The following is code to output testcase.
num = 9949999
ret = solution(num)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")