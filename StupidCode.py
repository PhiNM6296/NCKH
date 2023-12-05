import os
import time
from pyfiglet import Figlet

f = Figlet(font='slant')
word = 'FUCK YOU HUY NGUYEN'
curr_word = ''
for char in word:
   #os.system('clear') #assuming the platform is linux, clears the screen
    curr_word += char
    print(f.renderText(curr_word))
    time.sleep(0.5)
    
'''import turtle

# Khởi tạo màn hình đồ họa
screen = turtle.Screen()
screen.setup(width=800, height=600)

# Khởi tạo đối tượng turtle
pen = turtle.Turtle()
pen.speed(1)  # Tốc độ vẽ


pen.penup()
pen.goto(-300, 200)  # Đặt vị trí bắt đầu vẽ
pen.pendown()
pen.write("CON", align="left", font=("Arial", 48, "bold"))

pen.penup()
pen.goto(-300, 100)  # Đặt vị trí bắt đầu vẽ
pen.pendown()
pen.write("LỢN", align="left", font=("Arial", 48, "bold"))
# Vẽ chữ 'huy'
pen.penup()
pen.goto(-300, 0)  # Đặt vị trí bắt đầu vẽ
pen.pendown()
pen.write("HUY", align="left", font=("Arial", 48, "bold"))

# Vẽ chữ 'nguyễn'
pen.penup()
pen.goto(-300, -100)  # Đặt vị trí bắt đầu vẽ
pen.pendown()
pen.write("NGUYỄN", align="left", font=("Arial", 48, "bold"))

pen.penup()
pen.goto(-300, -200)  # Đặt vị trí bắt đầu vẽ
pen.pendown()
pen.write("NGÁO VC", align="left", font=("Arial", 48, "bold"))
# Dừng chương trình khi nhấn vào màn hình
screen.exitonclick()'''


