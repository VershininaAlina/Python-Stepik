import random

digits = "1234567890"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "#$%&*+-=?@^_"
total = ""

def random_generation_pass(total, count_pass):
    final_pass = ""
    answer1 = input("Пароль должен включать цифры? (Ответьте да/нет) \n")
    answer2 = input(
        "Пароль должен включать прописные буквы? (Ответьте да/нет) \n")
    answer3 = input(
        "Пароль должен включать строчные буквы? (Ответьте да/нет) \n")
    answer4 = input("Пароль должен включать спецсимволы ? (Ответьте да/нет)\n")
    answer5 = input("Исключить символы il1Lo0O? (Ответьте да/нет)\n")
    if answer1 == "да":
        total += digits
    if answer2 == "да":
        total += lowercase_letters
    if answer3 == "да":
        total += uppercase_letters
    if answer4 == "да":
        total += punctuation
    if answer5 == "да":
      for q in range(len(total)):
        if total[q] in "il1Lo0O" :
          total = total.replace(total[q], ' ' )  
      
    for i in range(count_pass):
        if len(total) == 0:
            print("\nНужно выбрать хотя бы 1 категорию настроек!!!")
            break
        else:
            print("\nПароль # \n", i + 1, end=" ")
            print()
            for z in range(len_pass):
                final_pass = final_pass + random.choice(total)
            print(final_pass)
            final_pass = ""
        print("_______")


print("Добро пожаловать в систему генерации пароля\n")
print("Ответьте  на пару вопросов, чтобы создать идеальный пароль\n")
print("Сколько нужно сгенерировать паролей\n")
count_pass = int(input())
print("Какой длины буду пароли\n")
len_pass = int(input())
random_generation_pass(total, count_pass)
