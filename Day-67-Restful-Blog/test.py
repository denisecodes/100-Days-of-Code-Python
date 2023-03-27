from datetime import datetime as dt

now = dt.now().date().strftime("%B %d, %Y")
print(now)