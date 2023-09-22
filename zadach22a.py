from random import randint
n_set = set(randint(1, 20) 
    for i in range(int(input('Введите кол-во элементов 1го множества: '))))
print(n_set)
m_set = set(randint(1, 20) 
    for i in range(int(input('Введите кол-во элементов 2го множества: '))))
print(m_set)
s_set = sorted(n_set.intersection(m_set))
print(*s_set)