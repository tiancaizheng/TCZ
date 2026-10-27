import random

secret_number = random.randint(1, 100)
attempts = 0

print("我想好了一个 1 到 100 之间的数字。")

while True:
    user_input = input("请输入你的猜测：")

    if not user_input.isdigit():
        print("请输入一个正整数。")
        continue

    guess = int(user_input)
    attempts += 1

    if guess < secret_number:
        print("太小了，再试一次。")
    elif guess > secret_number:
        print("太大了，再试一次。")
    else:
        print(f"猜对了！你一共猜了 {attempts} 次。")
        break