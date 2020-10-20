def solution(X, A):
    frog, leaves = 0, [False] * (X)
    for minute, leaf in enumerate(A):
        if(leaf <= X):
            leaves[leaf - 1] = True
        while leaves[frog]:
            frog += 1
            if (frog == X): 
                return minute
    return -1


