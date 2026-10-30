##zadacha1
price = float(input())
discount1 = float(input())
discount2 = float(input())

price = price - price * discount1 / 100
price = price - price * discount2 / 100

print(f"{price:.2f}")

##zadacha2
km_traveled_by_bus = float(input("Enter the number of kilometers traveled by bus: "))
km_traveled_by_taxi = float(input("Enter the number of kilometers traveled by taxi: "))

bus_price_per_km = input("Enter the price per kilometer for the bus travel: ")
taxi_price_per_km = input("Enter the price per kilometer for the taxi travel: ")

total_km = km_traveled_by_bus + km_traveled_by_taxi
total_cost = km_traveled_by_bus * float(bus_price_per_km) + km_traveled_by_taxi * (taxi_price_per_km)

print(f"{total_km:.2f}")
print(f"{total_cost:.2f}")

##zadacha3
hours_worked = input("Enter the number of hours worked: ")
hourly_wage = input("Enter the hourly wage: ")
bonus_percentage =input("Enter the bonus percentage: ")
maintenance_percentage = input("Enter the maintenance percentage: ")  

salary = float(hours_worked) * float(hourly_wage)
bonus = salary * float(bonus_percentage) / 100
maintenance_cost = salary * float(maintenance_percentage) / 100

total_salary = salary + bonus - maintenance_cost
print(f"The total salary is: {total_salary:.2f}")

##zadacha4
food_cost = input("Enter the cost of food: ")
drink_cost = input("Enter the cost of drinks: ")
tax_percentage = input("Enter the tax percentage: ")

total_cost = float(food_cost) + float(drink_cost)
tax_amount = total_cost * float(tax_percentage) / 100
final_amount = total_cost + tax_amount

print(f"The final amount to be paid is: {final_amount:.2f}")

##zadacha5
length = input("Enter the length of the parallelepiped: ")
width = input("Enter the width of the parallelepiped: ")
height = input("Enter the height of the parallelepiped: ")
volume = float(length) * float(width) * float(height)
total_area = 2 * (float(length) * float(width) + float(length) * float(height) + float(width) * float(height))
print(f"The volume of the parallelepiped is: {volume:.3f}")
print(f"The total area of the parallelepiped is: {total_area:.3f}")                                             

##zadacha6
liter_first_juice = float(input("Enter the number of liters of the first juice: "))
price_first_juice = float(input("Enter the price per liter of the first juice: "))

liter_second_juice = float(input("Enter the number of liters of the second juice: "))
price_second_juice = float(input("Enter the price per liter of the second juice: "))

total_liters = liter_first_juice + liter_second_juice

total_cost = (liter_first_juice * price_first_juice) + (liter_second_juice * price_second_juice)

average_price = total_cost / total_liters

print(f"{total_liters:.2f}")
print(f"{average_price:.2f}")

##zadacha7
distance = float(input("Enter the distance in kilometers: "))
speed = float(input("Enter the speed in kilometers per hour: "))
break_time = float(input("Enter the break time in hours: "))

travel_time = distance / speed * 60

total_time = travel_time + break_time * 60

print(f"{total_time:.2f}")

##zadacha8
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))    

windows_doors = float(input("Enter the area of windows and doors: "))   
coverage = float(input("Enter the coverage of the paint per square meter: "))
price = float(input("Enter the price of the paint per liter: "))

wall_area = 2 * (length * height + width * height) - windows_doors

paint_area = wall_area - coverage

liters = paint_area / coverage

total_cost = liters * price

print(f"{liters:.2f}")
print(f"{total_cost:.2f}")

##zadacha9
grade1 = float(input("Enter the first grade: "))
weight1 = float(input("Enter the weight of the first grade: "))

grade2 = float(input("Enter the second grade: "))
weight2 = float(input("Enter the weight of the second grade: "))

grade3 = float(input("Enter the third grade: "))
weight3 = float(input("Enter the weight of the third grade: "))

final_grade = (grade1 * weight1 + grade2 * weight2 + grade3 * weight3) / (weight1 + weight2 + weight3)

print(f"The final grade is: {final_grade:.2f}")

##zadacha10
money = float(input("Enter the amount of money: "))
interest_rate = float(input("Enter the interest rate (as a percentage): "))
years = float(input("Enter the number of years: "))

interest = money * (interest_rate / 100) * years

total_amount = money + interest

print(f"The total amount after {years} years is: {total_amount:.2f}")       
print(f"The interest earned after {years} years is: {interest:.2f}")

##zadacha11
seconds = int(input("Enter the number of seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60

remaining_seconds = seconds % 60

print(hours)
print(minutes)
print(remaining_seconds)    

###zadacha12
import math

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
title_area = float(input("Enter the area of the title: "))
reserve = float(input("Enter the reserve percentage: "))
title_price = float(input("Enter the price of the title: "))

floor_area = length * width
title_needed = floor_area / title_area
title_with_reserve = title_needed + (1 + reserve / 100)
title_count = math.ceil(title_with_reserve)
total_cost = title_count * title_price

print(title_count)
print(f"{total_cost:.2f}")

###zadacha13
power = float(input("Enter the power of the engine in horsepower: "))
hours = float(input("Enter the number of hours the engine runs: "))
days = float(input("Enter the number of days the engine runs: "))
price = float(input("Enter the price of fuel per liter: "))

energy = power / 1000 * hours * days

total_price = energy * price                

print(f"{energy:.2f}")
print(f"{total_price:.2f}")

###zadacha14
distance1 = float(input("Enter the distance of the first trip in kilometers: "))    
speed1 = float(input("Enter the speed of the first trip in kilometers per hour: "))

distance2 = float(input("Enter the distance of the second trip in kilometers: "))
speed2 = float(input("Enter the speed of the second trip in kilometers per hour: "))

time1 = distance1 / speed1
time2 = distance2 / speed2              

total_distance = distance1 + distance2
total_time = time1 + time2

average_speed = total_distance / total_time

print(f"{total_time:.2f}")
print(f"{average_speed:.2f}")


##zadacha15
products = int(input("Enter the number of products: "))
selling_price = float(input("Enter the selling price of the product: "))
delivery_cost = float(input("Enter the delivery cost of the product: "))
extra_cost = float(input("Enter the extra cost of the product: "))

total_income = products * selling_price

total_cost = products * (delivery_cost + extra_cost)

profit = total_income - total_cost

print(f"The total income is: {total_income:.2f}")
print(f"The total cost is: {total_cost:.2f}")
print(f"The profit is: {profit:.2f}")


