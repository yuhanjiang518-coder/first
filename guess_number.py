"""
猜数字小游戏（单文件版）

玩法：
    电脑在 1 到 100 之间随机选一个整数，玩家不断输入自己猜的数字。
    每次猜完，程序会提示"大了"或"小了"，直到猜中为止，
    最后统计玩家一共猜了多少次。

代码阅读顺序（从下往上看也行）：
    main()  ->  play()  ->  read_guess()  ->  make_answer()
"""

import random  # 需要用到随机数

LOW = 1     # 数字范围下限
HIGH = 100  # 数字范围上限


def make_answer():
    """让电脑随机产生一个答案，返回 1~100 之间的整数。"""
    return random.randint(LOW, HIGH)


def read_guess():
    """
    读取玩家输入的一次猜测。

    返回情况：
        猜的数字是合法整数 -> 返回这个整数
        输入不合法（不是数字，或超出范围）-> 返回 None，让上层重新问
    """
    text = input("请输入你猜的数字（1-100）：").strip()

    if not text.isdigit():                      # 比如输入了 abc、空行、-5
        print("输入无效，请输入一个 1-100 的整数。")
        return None

    number = int(text)
    if number < LOW or number > HIGH:           # 数字对但不是整数范围里
        print(f"超出范围了，请输入 {LOW} 到 {HIGH} 之间的整数。")
        return None

    return number


def play():
    """玩一整局，返回本局猜的次数。"""
    answer = make_answer()   # 电脑心里想的那个数
    count = 0                # 玩家已经猜了几次

    print(f"\n我想好了一个 {LOW} 到 {HIGH} 之间的数字，来猜猜看吧！")

    while True:
        guess = read_guess()
        if guess is None:        # 这轮输入不合法，不算次数，重新问
            continue

        count = count + 1        # 只有合法的一次猜测才计数

        if guess > answer:
            print("大了")
        elif guess < answer:
            print("小了")
        else:
            print(f"猜中了！答案就是 {answer}，你一共猜了 {count} 次。")
            break                # 猜中，跳出循环，本局结束

    return count


def main():
    """程序入口：可以连续玩多局，直到玩家不想玩了。"""
    while True:
        play()
        again = input("再来一局吗？（输入 y 再来，其他任意键退出）：").strip().lower()
        if again != "y":
            print("游戏结束，再见！")
            break


if __name__ == "__main__":   # 只有直接运行本文件时才启动游戏
    main()
