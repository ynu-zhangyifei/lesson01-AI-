# 单利 vs 复利 对比计算器
# 复利公式: FV = P * (1 + r)^n
# 单利公式: FV = P * (1 + r * n)


def input_number(prompt):
    """循环提示，直到用户输入合法的非负数字"""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("输入不合法，请输入数字！")
            continue
        if value < 0:
            print("输入不能为负数，请重新输入！")
            continue
        return value


def main():
    P = input_number("请输入本金P: ")
    r = input_number("请输入年利率r(如0.05): ")

    # 对比固定年限
    years = [10, 20, 30]

    print()
    print(f"本金: {P:.2f}    年利率: {r:.2%}")
    print("-" * 50)
    print(f"{'年份':<6}{'单利本息':>14}{'复利本息':>14}{'复利多赚':>14}")
    print("-" * 50)

    for n in years:
        simple = P * (1 + r * n)
        compound = P * (1 + r) ** n
        diff = compound - simple
        print(f"{n:<6}{simple:>14,.2f}{compound:>14,.2f}{diff:>14,.2f}")

    print("-" * 50)
    print("结论：时间越长，复利相对单利的优势越明显。")


if __name__ == "__main__":
    main()
