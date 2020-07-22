from turtle import *
import sys
color('red', 'yellow')

length = int(sys.argv[1])
angle = int(sys.argv[2])
begin_fill()
while True:
#    forward(100)
    forward(length)
#    left(135)
    left(angle)
    if abs(pos()) < 1:
        break
end_fill()
done()