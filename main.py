# def is_alive(health):
#     if health < 0:
#         return False
#     else:
#         return True
# print(is_alive(int(input())))

# def season_events(number_of_month):#Требуется ввести реальный номер месяца
#     winter = 'За окном падал белый снег.'
#     spring = 'Птицы пели прекрасные песни.'
#     summer = 'Солнце светило ярче чем когда-либо.'
#     autumn = 'Урожай был невероятным.'
#     if number_of_month == 1:
#         print( 'Вы родились в январе.',winter)
#         return ''
#     elif number_of_month == 2:
#         print( 'Вы родились в феврале.',winter)
#         return ''
#     elif number_of_month == 3:
#         print( 'Вы родились в марте.',spring)
#         return ''
#     elif number_of_month == 4:
#         print( 'Вы родились в апреле.',spring)
#         return ''
#     elif number_of_month == 5:
#         print( 'Вы родились в мае.',spring)
#         return ''
#     elif number_of_month == 6:
#         print( 'Вы родились в июне.',summer)
#         return ''
#     elif number_of_month == 7:
#         print( 'Вы родились в июле.',summer)
#         return ''
#     elif number_of_month == 8:
#         print( 'Вы родились в августе.',summer)
#         return ''
#     elif number_of_month == 9:
#         print( 'Вы родились в сентябре.',autumn)
#         return ''
#     elif number_of_month == 10:
#         print( 'Вы родились в октябре.',autumn)
#         return ''
#     elif number_of_month == 11:
#         print( 'Вы родились в ноябре.',autumn)
#         return ''
#     elif number_of_month == 12:
#         print( 'Вы родились в декабре.',winter)
#         return ''
#     else:
#         return 'Не правильный месяц.'
# print(season_events(int(input())))#Требуется ввести реальный номер месяца

# def is_divisible_by_6(number):
#     last = number % 10
#     summa = sum(int(digit) for digit in str(number))
#
#     if last % 2 == 0 and summa % 3 == 0:
#         return f"Число {number} делится на 6"
#     else:
#         return f"Число {number} неделимо на 6"
# print(is_divisible_by_6(int(input())))

# def searchsubstr(subst, st):
#     if subst.lower() in st.lower():
#         return "Есть контакт!"
#     else:
#         return "Мимо!"
# print(searchsubstr(input(),input()))

# def firstlast(letter, st):
#     firstindex = None
#     lastindex = None
#     for i in range(len(st)):
#         if st[i] == letter:
#             if firstindex is None:
#                 firstindex = i
#             lastindex = i
#     if firstindex is None:
#         return (None, None)
#     else:
#         return (firstindex, lastindex)
# # Тесты
# print(firstlast(input(),input()))

# s = input()
# def top3(s):
#     t = ([(s.count(i), i) for i in s])
#     return (sorted(set(t))[::-1][:3])
# print(top3(s))

# def shortener(st):
#     a = ""
#     s = ""
#     for i in st:
#         if i == "(":
#             s.append(i)
#         elif i == ")":
#             if s:
#                 s.pop()
#         else:
#             if not s:
#                 a += i
#     return a
# text = "Дмитрий считает, что когда текст пишут в скобках (как вот тут, например), его читать не нужно. Вот и надумал он существенно укоротить время чтения, написав функцию, которая будет удалять все, что расположено внутри скобок. Помогите ленивому Диме разработать функцию shortener(st), которая будет удалять все, что внутри скобок и сами эти скобки, возвращая очищенный текст (скобки могут быть вложенными)."
# print(shortener(text))

# import math
# def all_divisors(number):
#     s = []
#     for i in range(1, int(math.sqrt(number)) + 1):
#         if number % i == 0:
#             s.append(i)
#             if number // i != i:
#                 s.append(number // i)
#     s.sort()
#     return s
# number = int(input())
# result = all_divisors(number)
# print(result)