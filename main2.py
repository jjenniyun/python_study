def tax_calc(money):
  return money * 0.35


def pay_tax(tax):
  print("thank you for paying", tax)


# tax_calc(15000)
pay_tax(tax_calc(150))


def say_hello(user_name="anonymous"):  # 파라미터에 기본값 부여
  print("hello", user_name)


say_hello("jenny")
say_hello()


def plus(a=1, b=1):
  print(a + b)


def minus(a=1, b=1):
  print(a - b)


def multiply(a=1, b=1):
  print(a * b)


def divide(a=1, b=1):
  print(a / b)


def power(a=1, b=1):
  print(a**b)


plus()
minus()
multiply()
divide()
power(10, 2)

my_name = "jisu"
my_age = 21
my_color_eyes = "brown"

print(
  f"Hello {my_name}, I have {my_age} years in the earth, {my_color_eyes} is my eye color"
)


# 주스 메이커(22.12.20)
def make_juice(fruit):
  return f"{fruit}+🍸"


def add_ice(juice):
  return f"{juice}+🧊"


def add_sugar(iced_juice):
  return f"{iced_juice}+🍧"


juice = make_juice("🍇")
print(juice)
cold_juice = add_ice(juice)
print(cold_juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)

a = "jenny"
if a == "jenny":
  print("True!")

password_correct = False

if password_correct:
  print("Here is your money")
else:
  print("Wrong password")

  winner = 5
  if winner > 10:
    print("Winner is greater than 10")
  elif winner < 10:
    print("Winner is less than 10")
  else:
    print("Winner is 10")

  winner = 5
  if winner < 10:
    print("Run!")
  else:
    print("Else")

# age = int(input("How old are you?"))

#if age < 18:
#print("You can't drink")
#elif age >= 18 and age <= 35:
#print("You drink beer!")
#else:
# print("Go ahead!")

from random import randint  # 라이브러리 실행: 모듈 실행

print("Welcome to Python Casino")
pc_choice = randint(1, 100)

playing = True

while playing:
  user_choice = int(input("Choose number 1~100: "))
  if user_choice == pc_choice:
    print("You won!")
    playing = False
  elif user_choice > pc_choice:
    print("Lower!")
  elif user_choice < pc_choice:
    print("Higher!")
"""
distance = 0
while distance < 20:
  print("I'm running:", distance, "km")
  distance += 1
"""