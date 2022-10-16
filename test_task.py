import time
n_customers = 999999
n_first_id = 1
n = len(str(n_customers))

#создадим словарь ID для теста функций
ID = {n_id: (n-len(str(n_id)))*"0" + str(n_id) for n_id in range(n_first_id, n_customers)}
#Функция, которая подсчитывает число покупателей, попадающих в каждую группу,
#если нумерация ID сквозная и начинается с 0.
#пример такого словаря
#1)1 000001
#2)2 000002
#3)3 000003
#4)4 000004

def number_buyersgroup_idstarts_from0(n_customers):
    n_group = 0
    #в данный список будет заполняться номера групп принадлещему данному id
    list_n_group = []
    #в цикле заполняются номера групп
    for n_id in range(1, n_customers):
        #счетаем сумму всех чисел
        while n_id > 0:
            n_group += n_id % 10
            n_id //= 10
        list_n_group.append(n_group)
        n_group = 0
    #находим одинаковые группы в списке и считаем их количество    
    n_group_n_customers={}
    for i in list_n_group:
        if i in n_group_n_customers:
            n_group_n_customers[i] += 1
        else:
            n_group_n_customers[i] = 1
    return(n_group_n_customers)

start_time = time.time()
print(number_buyersgroup_idstarts_from0(n_customers))
print("Time: %s seconds" % (time.time() - start_time))

n_customers = 999999
n_first_id = 100001
n = len(str(n_customers))
#создадим словарь ID для теста функций
ID = {n_id: (n-len(str(n_id)))*"0" + str(n_id) for n_id in range(n_first_id, n_customers)}
#Функция, которая подсчитывает число покупателей, попадающих в каждую группу,
#если ID начинается с произвольного числа.
#пример такого словаря
#1)100001 100001
#2)100002 100002
#3)100003 100003
#4)100004 100004

def number_buyersgroup_idstarts_with_arbitrary_number(n_customers, n_first_id):
    n_group = 0
    list_n_group = []
    for n_id in range(n_first_id, n_customers - n_first_id + 1):
        while n_id > 0:
            n_group += n_id % 10
            n_id //= 10
        list_n_group.append(n_group)
        n_group = 0
        
    n_group_n_customers={}
    for i in list_n_group:
        if i in n_group_n_customers:
            n_group_n_customers[i] += 1
        else:
            n_group_n_customers[i] = 1
    return(n_group_n_customers)
start_time = time.time()
print(number_buyersgroup_idstarts_with_arbitrary_number(n_customers, n_first_id))
print("Time: %s seconds" % (time.time() - start_time))
