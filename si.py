#simple interest calculator 
p= int(input("please input the principal; " ))
r = int(input("please input the rate in percentage; "))
t = int(input("please input the time in years; "))

I = (p*r*t)/100

print(f"the simple interest will be;  {I}")

A=p+I

print(f"the Amount to be paid after 10years will be ;{A}")
