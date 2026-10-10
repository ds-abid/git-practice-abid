from datetime import date
from utils import add, subtract

name = "Abid Hasan"
todays_date = date.today()

print("My name is", name)
print("Today's Date :", todays_date)

print("Addition", add(10, 20))
print("Subtraction", subtract(20, 10))