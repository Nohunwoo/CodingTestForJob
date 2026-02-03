from datetime import datetime

now = datetime.now()
formatted_time = now.strftime("%Y\n%m\n%d")
print(formatted_time) 