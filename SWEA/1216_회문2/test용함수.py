def pal(s):
    N = len(s)
    length_list = []
    # 길이가 홀수일때
    for j in range(1, N-1):
        idx = 1
        while j - idx >= 0 and j + idx < N and s[j - idx] == s[j + idx]:
            idx += 1
        length_list.append(idx * 2 - 1)
    # 길이가 짝수일때
    for j in range(N-1):
        if s[j] == s[j + 1]:
            idx = 1
            while j - idx >= 0 and j + 1 + idx < N and s[j - idx] == s[j + 1 + idx]:
                idx += 1
            length_list.append(idx * 2)

    maximum = 0
    for elem in length_list:
        if maximum < elem:
            maximum = elem

    return(maximum)

print(pal('asdfasdfasdffdsafdsaasdfasdfasdffdsafdsaasdfasdfasdffdsafdsaasdfasdfasdffdsafdsaasdfasdfasdffdsafdsa\
'))

