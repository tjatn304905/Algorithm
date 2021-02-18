'''
1. 내장함수(x)
2. 직접 짜기
3. 재귀로 짜기
'''

# 직접 짜기
word = 'abcde'
reversed_word = ''
for i in range(1, len(word)+1):
    reversed_word += word[len(word)-i]
print(reversed_word) # edcba

# 선생님 풀이
def sol1(word):
    idx = len(word) - 1
    r_word = ''
    while idx >= 0:
        r_word += word[idx]
        idx -= 1
    return r_word
print(sol1(word))

# 재귀로 짜기
def sol2(word):
    idx = len(word) - 1
    last_char = word[idx]
    if idx == 0:
        return last_char
    word_except_last_char = word[:idx]
    return last_char + sol2(word_except_last_char)

print(sol2(word))


