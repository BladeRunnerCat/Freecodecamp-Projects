week_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_day(start_day, days_to_add):
    if start_day != None:
        start_day = start_day.capitalize()
        start_index = week_names.index(start_day)
        new_index = (start_index + days_to_add) % len(week_names)
        return week_names[new_index]
    return 0

def seconds(time):
    first, last = time.split(':')
    first = int(first)
    last = int(last)
    result = first * 60 + last

    return result

def add_time(start, duration, day = None):

    #strip PM or AM
    PA = start[-2:]
    start = start[:-3]
    days = 0

    #turn the minutes to seconds add the seconds
    new_time = (seconds(start) + seconds(duration)) // 60
    new_minutes = (seconds(start) + seconds(duration)) % 60
    while new_time >= 12:
        if PA == "PM":
            new_time -= 12
            PA = "AM"
            days += 1
        else:
            new_time -= 12
            PA = "PM"

    result_week = get_day(day, days)

    if new_time == 0:
        new_time = 12

    new_time = f"{new_time}:{new_minutes:02d} {PA}"
    if result_week != 0:
        new_time += f", {result_week}"
    if days == 1:
        new_time += " (next day)" 
    if days > 1:
        new_time += f" ({days} days later)" 
    
    return new_time
