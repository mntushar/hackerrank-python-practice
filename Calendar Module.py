import calendar


m, d, y = map(int, input().split())
w = calendar.weekday(y, m, d)
w_name = calendar.day_name[w]
print(w_name.upper())