# 最小版复利计算器
# 公式: FV = P * (1 + r)^n

P = float(input("请输入本金P: "))
r = float(input("请输入年利率r(如0.05): "))
n = float(input("请输入年份n: "))

FV = P * (1 + r) ** n

print("最终金额FV:", FV)
