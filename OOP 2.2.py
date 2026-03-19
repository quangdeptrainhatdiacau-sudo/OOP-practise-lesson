import math
#The volume of a sphere with radius r is 4/3*π*r^3.What is the volume of a sphere with radius 5?
radius=5
volume=4/3*math.pi*radius**3
print("The volume of a sphere:", volume)

#Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
cover_price=24.95
discount=0.4
discount_price=cover_price*(1-discount)

shipping_first = 3
shipping_rest = 0.75
total_shipping = shipping_first + (59 * shipping_rest)

total_cost=(60*discount_price)+total_shipping
print("total wholesale cost:", total_cost)

#If i leave my house at 6:52 am and run 1 miles at an easy pace (8:15 per miles), then 3 miles at tempo (7:12 per miles) and 1 mile at easy pace again, what time do i get home for breakfast
start_time_second=(6*60+52)*60
total_run_second=(8*60+15)+3*(7*60+12)+(8*60+15)
end_time_second=start_time_second+total_run_second
end_hour=end_time_second//3600
end_minutes=(end_time_second%3600)//60
end_second=end_time_second%60
print(f"{int(end_hour)}:{int(end_minutes)}:{int(end_second)}")







