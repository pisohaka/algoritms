def SumOfThe(N: int, data):
    for i in range(N):
        tmp = data.copy()
        sum_ = tmp[i]
        tmp.pop(i)
        if sum_ == sum(tmp):
            return sum_
