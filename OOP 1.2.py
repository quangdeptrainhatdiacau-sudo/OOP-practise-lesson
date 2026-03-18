#Tong so giay trong 42 phut 42 giay
second=(42*60+42)
print("Total second",second)

#Tong so miles trong 10 kilometers'
kilometers=10
miles=kilometers/1.61
print("Total miles in 10 kilometers:",miles)

#Thoi gian trung binh
pace_in_seconds =second/miles
pace_minutes=int(pace_in_seconds//60)
pace_seconds=int(pace_in_seconds%60)
print(f"1. Average Pace: {pace_minutes} minutes {pace_seconds} second_per_miles")

#Van toc trung binh
total_hours=second/3600
mph=miles/total_hours
print(f"2. Average Speed: {mph} miles per hour")
