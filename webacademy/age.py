name = input("write you name: ",)
year = int(input("please write you birth year: ",))
current_year = 2018

age = current_year - year

if age < 18:
    print("Underage")
elif age < 21:
    print("Cheers")
else:
    print("Adult")




