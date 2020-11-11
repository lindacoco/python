print("hello")

# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)

#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True

# pb = ["123","456","78978","777","55555"]
# print(pb)
# solution(pb)

# #해쉬 정석
# def solution(phone_book):
#     answer = True
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 answer = False
#     return answer


# def solution(phoneBook):
#     phoneBook.sort(key=lambda x: len(x))
#     for a in range(len(phoneBook)):
#         for b in range(a+1, len(phoneBook)):
#             if phoneBook[b][:len(phoneBook[a])] == phoneBook[a]:
#                 return False
#     return True

# jump to python
# 3
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
# i = 1
# sum = 0
# while i <= 1000 :
#   if i % 3 == 0 :
#     sum += i
#   i += 1

# print (sum)

# while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
# *
# **
# ***
# ****
# *****
# i = 1
# while i <=5 :
#   print("*"*i) 
#   i += 1

# # Q4
# # for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
# for i in range(1,101):
#   print(i, end=" ")

# Q5
# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.
# score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# sum = 0
# for i in range(0,len(score)):
#   sum += i 

# print(round(sum/ (len(score)+1),2))
# Q6
# 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.

# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)
# 위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.
# numbers = [1, 2, 3, 4, 5]
# result = [(n*2) for n in numbers if n % 2 == 1]
# print(result)

# chater4 
# Q1
# 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.

# def is_odd(n) :
#   if n % 2 == 0 :
#     return "even"
#   else:
#     return "odd"

# print(is_odd(6))

# Q2
# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)

# ※ 평균 값을 구할 때 len 함수를 사용해 보자.
# sum = 0
# def get_average(*args):
#     global sum
#     for i in range(0,len(args)):
#       sum += args[i]
#     return sum / (len(args))

# print(get_average(1,2,3,4))


# Q3
# 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.

# input1 = input("첫번째 숫자를 입력하세요:")
# input2 = input("두번째 숫자를 입력하세요:")

# total = int(input1) + int(input2)
# print("두 수의 합은 %s 입니다" % total)

# 첫번째 숫자를 입력하세요:3
# 두번째 숫자를 입력하세요:6
# 두 수의 합은 36 입니다
# 3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다. 이 프로그램의 오류를 수정해 보자.

# ※ int 함수를 사용해 보자.

# Q4
# 다음 중 출력 결과가 다른 것 한 개를 골라 보자.

# print("you" "need" "python")
# print("you"+"need"+"python")
# print("you", "need", "python")
# print("".join(["you", "need", "python"]))
# Q5
# 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.

f1 = open("test.txt", 'w')
f1.write("Life is too short")

f2 = open("test.txt", 'r')
m = f2.readlines()
for line in m :
  print(line)
f2.close()
# 이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.

# Q6
# 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)

# Q7
# 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

# Life is too short
# you need java
# ※ replace 함수를 사용해 보자.