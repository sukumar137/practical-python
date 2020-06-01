# bounce.py
#
# Exercise 1.5
drop_height=100
for i in range(10):
    bounce_height=drop_height*(3/5)
    drop_height=bounce_height
    print(round(bounce_height,4))
