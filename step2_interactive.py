# step2_interactive.py
# 交互版复利计算器

principal = float(input("请输入本金: "))
rate = float(input("请输入年利率(例如5%输入0.05): "))
years = int(input("请输入投资年数: "))

amount = principal * (1 + rate) ** years

print("最终金额:", round(amount, 2))