year = 1800

if not year % 4  and year % 100:
    print("Year is leap")
elif not year % 400 :
    print("Year is leap")
else:
    print("Year is not leap")
    
