basic = float(input("Enter Basic Salary: "))

hra = basic * 20 / 100
da = basic * 15 / 100
pf = basic * 8 / 100

net = basic + hra + da - pf

print("HRA =", hra)
print("DA =", da)
print("PF =", pf)
print("Net Salary =", net)