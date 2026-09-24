# 交互版复利计算器（带输入校验）
# 公式: FV = P * (1 + r)^n


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


P = input_number("请输入本金P: ")
r = input_number("请输入年利率r(如0.05): ")
n = input_number("请输入年份n: ")

FV = P * (1 + r) ** n

print("最终金额FV:", round(FV, 2))
