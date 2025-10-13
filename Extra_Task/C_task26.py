day = int(input("Enter Your Day :"))
month = int(input("Enter Your Month :"))
year = int(input("Enter Your Day :"))


if year % 400 == 0 :
        leap = True
else:
    leap = False

if month < 1 or month >12:
      print("Invalid Date")
else:
      if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12: 
            max_day = 31
      elif month == 4 or month == 6 or month == 9 or month == 11:
            max_day = 30
      elif month == 2:
            if leap:
                  max_day = 29
            else:
                  max_day = 28

if day >= 1 and day <= max_day:
        print("Valid date")
else:
        print("Invalid date")                  
                    