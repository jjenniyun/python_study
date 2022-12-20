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


# 주스 메이커
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
