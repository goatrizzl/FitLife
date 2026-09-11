print("Welcome to our application: FitLife MVP")
print("-" * 40)
user_name = input("Please put your name: ")
user_name = user_name.title()
user_age = input("Please put your age: ")
user_age = int(user_age)


print("-" * 40)
print("Now, we need to know your weight and height")
user_weight = float(input("Please enter your weight (in kg): "))
user_height = input("Please enter your height (in cm): ")
user_height = float(user_height)


bmi = user_weight / (user_height ** 2)  # Расчет индекса массы тела
bmi = round(bmi, 1)  # Сохраняем значение с одной цифрой после запятой


water_ml = user_weight * 30  # Вычисляем норму воды в день (мл)
water_l = water_ml / 1000
# Округлим литры воды до двух знаков для аккуратного вывода
water_l = round(water_l, 2)


print("=" * 40)
print(f"Welcome to FitLife MVP: You are {user_name}, {user_age}, years old")
print(f"Here are your body measurements: {user_weight}kilo; {user_height} cm.")
print(f"Here is your BMI: {bmi}")
print("You need", water_l, "l. of water a day to close the reccomended intake")
print("Thank you for using our application! :)")
print("=" * 40)
