def permutations(n):

    all_permutations = [[(1, )]]

    for i in range(2, n+1):
        all_permutations.append([])
        for perm in all_permutations[i-2]:
            for j in range(i):
                all_permutations[i-1].append(perm[:j] + (i, ) + perm[j:])

    all_permutations[-1].sort()
    return all_permutations[-1]


def correctbracketsequences(n, open_cnt=0, close_cnt=0, seq='', seq_list=None):
    if seq_list is None:
        seq_list = []
    if open_cnt + close_cnt == 2 * n:
        seq_list.append(seq)
        return
    if open_cnt < n:
         correctbracketsequences(n, open_cnt + 1, close_cnt, seq + '(', seq_list)
    if open_cnt > close_cnt:
        correctbracketsequences(n, open_cnt, close_cnt + 1, seq + ')', seq_list)
    return seq_list
