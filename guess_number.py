"""猜数字小游戏。

电脑随机生成一个 1 到 100 之间的整数，
玩家不断输入猜测，程序提示“大了”或“小了”，
直到猜中为止，并统计玩家一共猜了几次。

运行方式：
    py guess_number.py
"""

import random


def main():
    print("=" * 40)
    print("      猜数字小游戏（1-100）")
    print("=" * 40)
    print("电脑已经想好了一个 1 到 100 之间的整数。")
    print("请输入你猜的数字，我会提示“大了”或“小了”。\n")

    # randint(1, 100) 会生成 1 到 100（含两端）的随机整数。
    answer = random.randint(1, 100)
    guess_count = 0

    while True:
        user_input = input("请输入你猜的数字：").strip()

        # isdigit() 用来检查输入是不是纯数字，避免程序因错误输入崩溃。
        if not user_input.isdigit():
            print("输入无效，请输入 1 到 100 之间的整数。\n")
            continue

        guess = int(user_input)

        if guess < 1 or guess > 100:
            print("超出范围了，请输入 1 到 100 之间的整数。\n")
            continue

        # 只有输入有效时，才把它算作一次猜测。
        guess_count += 1

        if guess > answer:
            print("大了，再试试。\n")
        elif guess < answer:
            print("小了，再试试。\n")
        else:
            print(f"\n恭喜你，猜中了！答案就是 {answer}。")
            print(f"你一共猜了 {guess_count} 次。")
            break


if __name__ == "__main__":
    main()
