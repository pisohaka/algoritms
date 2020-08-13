def SynchronizingTables(N: int, ids, salary):
    s_ids = sorted(ids)
    s_salary = sorted(salary)
    table = {}
    for i in range(N):
        table[s_ids[i]] = s_salary[i]
    result_salary = []
    for id_ in ids:
        result_salary.append(table[id_])
    return result_salary
