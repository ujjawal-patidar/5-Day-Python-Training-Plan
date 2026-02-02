# import sys
# for i in sys.path:
#     print(i)

import math as m
# print(math.e)
# print(m.floor(3.14))
# print(m.ceil(3.14))


import random

# # Generate a random integer in a given range (inclusive)
# print(f"Random integer between 1 and 100: {random.randint(1, 100)}")

# # Generate a random float between 0.0 and 1.0
# print(f"Random float between 0 and 1: {random.random()}")

# # Choose a random element from a sequence
# fruits = ['apple', 'banana', 'cherry', 'date']
# print(f"Randomly selected fruit: {random.choice(fruits)}")

# # Shuffle a list in-place
# deck = list(range(1, 11))
# random.shuffle(deck)
# print(f"Shuffled deck: {deck}")


# import datetime

# # Get the current date and time
# now = datetime.datetime.now()
# print(f"Current date and time: {now}")

# # Get today's date only
# today = datetime.date.today()
# print(f"Today's date: {today}")

# # Create a specific date
# specific_date = datetime.date(2025, 1, 15)
# print(f"A specific date: {type(specific_date)}")

# # Format the date into a string
# # %Y=Year, %m=Month, %d=Day, %H=Hour, %M=Minute
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(f"Formatted date and time: {formatted_date}")

# # Calculate a future date (add a timedelta)
# one_week = datetime.timedelta(weeks=1)
# next_week = now + one_week
# print(f"One week from now: {next_week}")



# from collections import Counter, deque

# # Counter: Count hashable objects
# counts = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
# print(f"Counts of fruits: {counts}")
# print(f"Count of 'apple': {counts['apple']}")

# # deque: A double-ended queue for fast appends and pops from either end
# d = deque(['task1', 'task2', 'task3'])
# print(f"Initial deque: {d}")

# d.append('task4')        # Append to the right
# d.appendleft('task0')    # Append to the left
# print(f"Deque after appends: {d}")

# d.pop()                  # Pop from the right
# d.popleft()              # Pop from the left
# print(f"Deque after pops: {d}")
