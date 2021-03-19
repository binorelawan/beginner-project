hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
total_mins = dura + mins

if total_mins >= 60:
    mins = total_mins % 60
    hour += total_mins // 60
else:
    mins = total_mins
    hour

print(hour, mins)

if hour >= 24:
    hour = hour % 24
else:
    hour

print(hour,':',mins, sep='')