def year(a):
    if a%4==0:
        print("leap")
    elif a%100==0:
        print("not leap")
    elif a%400==0:
        print("leap")
    else:
        print("invalid year")
year(2000)
year(2025)
