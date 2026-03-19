import time
seconds_since_epoch = int(time.time())
days = seconds_since_epoch // 86400
remaining_seconds = seconds_since_epoch % 86400
hours = remaining_seconds // 3600
minutes = (remaining_seconds % 3600) // 60
seconds = remaining_seconds % 60
print(f"Số ngày kể từ Epoch: {days}")
print(f"Giờ hiện tại (GMT): {hours}:{minutes}:{seconds}")
