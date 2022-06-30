import turtle
t = turtle.Turtle()
t.ht()
t.speed(0)
t.pensize(15)

#Variables
a = 90 #angle
ti = a*4/45 #tilt
r = 30 #radius
d = 40 #letter's length
dp = r #distance for pos
ps = t.width() #pensize
##Small
r_s = 30/2
d_s = 40/2
dp_s = (r_s*2+d_s)/2
ps_s = t.width()/2

#C
t.color(255, 106, 3)
t.lt(a)
t.circle(r, a*2)
t.fd(d)
t.circle(r, a*2)

#Pos1
t.penup()
t.goto(dp+r*2, t.ycor())
t.pendown()

#O
t.color(254, 200, 66)
for i in range(2):
  t.fd(d)
  t.circle(r, a*2)

#Pos2
t.penup()
t.goto(t.xcor()+dp, t.ycor()-r)
x1 = t.xcor()
t.pendown()

#D
t.color(4, 49, 90)
t.rt(a)
t.fd(ps)
t.color(8, 205, 125)
t.fd(r-ps)
t.circle(r, a)
t.fd(d)
t.circle(r, a)
xy1 = t.pos()
t.penup()
t.goto(x1-ps/2, r)
t.pendown()
t.color(4, 49, 90)
t.bk(ps)
t.penup()
t.goto(xy1)
t.pendown()
t.color(8, 205, 125)
t.fd(r-ps)
t.penup()
t.goto(x1, r-ps)
t.pendown()
t.lt(a)
t.color(218, 59, 178)
t.fd(d+r)

#Pos3
t.penup()
t.goto(t.xcor()+r*5, t.ycor()-ps)
t.pendown()

#E
t.color(255, 106, 3)
t.rt(a)
t.fd(r)
t.circle(-r, a)
t.fd(d)
t.penup()
t.goto(r*9, r)
t.pendown()
t.color(218, 24, 0)
t.lt(a)
t.fd(r)
t.circle(r, a*2-a/3)
t.color(218, 59, 178)
t.circle(r, a/3)
t.fd(r)

#Pos4
t.penup()
t.goto(r*2, -(d+r)-((r_s*2+d_s)*2))
t.pendown()

#F
t.pensize(ps_s)
t.color("black")
t.lt(a-ti)
t.fd(r_s*2+d_s)
t.rt(a-ti*2)
t.fd(dp_s)
t.penup()
t.goto(r*2+3.49066, -(d+r)-((r_s*2+d_s)*3/2))
t.pendown()
t.fd(dp_s)

#Pos5
t.penup()
t.goto(t.xcor()+dp_s*2, -(d+r)-((r_s*2+d_s)*2-r_s))
t.pendown()

#O
t.lt(a-ti*2)
for i in range(2):
  t.fd(d_s)
  t.circle(r_s, a*2)

#Pos6
t.penup()
t.goto(t.xcor()+dp_s, -(d+r)-((r_s*2+d_s)*2))
t.pendown()

#R
t.fd(dp_s*2)
t.rt(a-ti*2)
t.fd(r_s-ps_s)
t.circle(-r_s, a*2)
t.fd(r_s)
t.lt((a-ti*2)+a/3*2)
t.fd(r)

#Pos7
t.penup()
t.goto(-r*5, -(d+r)-((r_s*2+d_s)*3)-(r*2+d))
t.pendown()
t.seth(90)

#A
t.pensize(ps)
t.color(2, 178, 227)
t.fd(d+r)
t.circle(-r, a*2)
t.fd(d+r)
st_xy = (t.xcor(), t.ycor()-55)
t.penup()
t.goto(-r*5, -(d+r)-((r_s*2+d_s)*3)-(r+d-d/4))
t.pendown()
t.lt(a)
t.color(0, 48, 50)
t.fd(ps)
t.penup()
t.goto(-r*3-ps/2, t.ycor())
t.pendown()
t.fd(ps/2)
t.color(255, 67, 56)
t.penup()
t.goto(-r*5+ps, t.ycor())
t.pendown()
t.fd(r*2-(ps*2))

#Pos8
t.penup()
t.goto(t.xcor()+ps+r, -(d+r)-((r_s*2+d_s)*3))
t.pendown()

#L
t.color(2, 178, 227)
t.right(a)
t.fd(r*2+d)
t.lt(a)
t.color(8, 40, 150)
t.fd(ps)
t.color(218, 59, 178)
t.fd(r*2-ps)


#Pos9
t.penup()
t.goto(r-ps/2, t.ycor()+(r*2+d))
t.pendown()

#B
t.color(8, 40, 150)
t.fd(ps*3/2)
t.color(218, 59, 178)
t.fd(r)
t.circle(-r*2/3, a*2-a/3)
xy2 = t.pos()
a1 = t.heading()
t.circle(-r, a/3)
t.penup()
t.goto(t.xcor()+ps, t.ycor())
t.pendown()
t.color(254, 197, 52)
t.rt(a*2)
t.circle(-r, a*2)
t.fd(r)
xy3 = (t.xcor()-ps, t.ycor())
xy4 = (t.xcor()-ps, t.ycor()+r*2)
xy5 = (t.xcor()-ps, t.ycor()+ps)
t.penup()
t.goto(xy2)
t.pendown()
t.color(218, 45, 49)
t.seth(a1)
t.circle(-r, a/3)
t.fd(r-ps)
t.penup()
t.goto(xy3)
t.pendown()
t.rt(a)
t.color(0, 132, 42)
t.fd(ps)
t.penup()
t.goto(xy4)
t.pendown()
t.color(0, 34, 43)
t.fd(ps)
t.color(2, 178, 227)
t.fd(r/3)
t.penup()
t.goto(xy5)
t.pendown()
t.fd(r)

#Pos10
t.penup()
t.goto(r*5, -(d+r)-((r_s*2+d_s)*3)-(r*2+d))
t.pendown()
t.seth(90)

#A
t.pensize(ps)
t.color(2, 178, 227)
t.fd(d+r)
t.circle(-r, a*2)
t.fd(d+r)
t.penup()
t.goto(r*5, -(d+r)-((r_s*2+d_s)*3)-(r+d-d/4))
t.pendown()
t.lt(a)
t.color(0, 48, 50)
t.fd(ps)
t.penup()
t.goto(r*7-ps/2, t.ycor())
t.pendown()
t.fd(ps/2)
t.color(255, 67, 56)
t.penup()
t.goto(r*5+ps, t.ycor())
t.pendown()
t.fd(r*2-(ps*2))


#Pos11
t.penup()
t.goto(r*8+ps, -(d+r)-((r_s*2+d_s)*3)-(r*2+d))
t.pendown()

#N
t.color(1, 47, 97)
t.lt(a)
t.fd(r+d)
xy6 = (t.xcor(), t.ycor()+ps)
xy7 = (t.xcor(), t.ycor())
t.penup()
t.goto(xy6)
t.pendown()
t.color(218, 59, 178)
t.circle(r/(64/32), a)
t.penup()
t.goto(xy7)
t.pendown()
t.color(1, 47, 97)
t.rt(a)
t.circle(-r, a/2)
t.color(2, 208, 125)
t.circle(-r, a*2-a/2)
t.fd(r+d)

#Pos12
t.penup()
t.goto(r*11+ps, -(d+r)-((r_s*2+d_s)*3)-(r*2+d))
xy8 = (t.xcor()+ps/2, t.ycor())
xy9 = (t.xcor(), t.ycor()+r*2+d)
xy10 = (t.xcor()+ps/2, t.ycor()+r*2+d)
t.pendown()

#I #FOR may need to be edited
t.color(253, 52, 39)
t.lt(a)
t.fd(ps*2)
t.penup()
t.goto(r*11+ps*2, t.ycor())
t.pendown()
t.color(2, 178, 227)
t.lt(a)
t.fd(r*2+d)
t.penup()
t.goto(xy8)
t.pendown()
t.color(0, 48, 50)
t.rt(a)
t.fd(ps)
t.penup()
t.goto(xy9)
t.pendown()
t.color(253, 52, 39)
t.fd(ps*2)
t.penup()
t.goto(xy10)
t.pendown()
t.color(0, 48, 50)
t.fd(ps)

#Pos13
t.penup()
t.goto(r*13+ps, -(d+r)-((r_s*2+d_s)*3)-(r*2+d))
t.pendown()
t.seth(90)

#A
t.color(2, 178, 227)
t.fd(d+r)
t.circle(-r, a*2)
t.fd(d+r)
t.penup()
t.goto(r*13+ps, -(d+r)-((r_s*2+d_s)*3)-(r+d-d/4))
t.pendown()
t.lt(a)
t.color(0, 48, 50)
t.fd(ps)
t.penup()
t.goto(r*15-ps/2+ps, t.ycor())
t.pendown()
t.fd(ps/2)
t.color(255, 67, 56)
t.penup()
t.goto(r*13+ps*2, t.ycor())
t.pendown()
t.fd(r*2-(ps*2))

#Subtitle
t.penup()
t.goto(st_xy)
t.pendown()
t.color(28, 30, 33)
t.write("Powered by alphaPlan & Code.X", font = ("Segoe UI", 27, "normal"))