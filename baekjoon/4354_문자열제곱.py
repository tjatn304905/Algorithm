# # sol1(시간초과)
#
# while True:
#     s = input()
#
#     if s == '.':
#         break
#     maximum = 1
#     # 문자열 길이의 절반부터 거꾸로 순회하며 슬라이싱
#     for i in range(len(s)//2, 0, -1):
#         temp = s[0:i]
#         # 이 임시 문자열의 길이로 총 길이가 나누어 떨어져야함
#         if len(s) % len(temp):
#             pass
#         else:
#             result = ''
#             # 몫만큼 더했을때 똑같아야함.
#             for count in range(1, len(s) // len(temp)):
#                 result += temp
#                 # 시간 단축(더하는 과정에서도 그 길이까지는 일치해야함)
#                 if s[0:len(result)] != result:
#                     break
#             else:
#                 maximum = len(s) // len(temp)
#
#     print(maximum)

# sol2
while True:
    s = input()
    if s == '.':
        break

    s_len = len(s)
    p_table = [0 for _ in range(s_len)]

    # 실패함수
    j = 0
    for i in range(1, s_len):
        while j > 0 and s[i] != s[j]:
            j = p_table[j-1]
            print(p_table, 1)
        if s[i] == s[j]:
            j += 1
            p_table[i] = j
            print(p_table, 2)


    p_len = s_len - p_table[s_len -1] # 패턴길이

    if s_len % p_len == 0: # 패턴의 길이로 나누어 떨어진다면
        print(s_len//p_len)
    else:
        print(1)