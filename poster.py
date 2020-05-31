from turtle import *
speed(-100)
screen=Screen()
screen.setup(400,400)
colours={
  'verylime':'#A7E30E',
  'reallyraspberry':'#FA057F'
}

screen.bgcolor(colours['verylime'])
dot(390)
color(colours['reallyraspberry'])
style=('Ariel',40,'bold')
penup()
left(90)
forward(80)
right(180)
write('Live',font=style,align='center')
forward(40)
write('Long',font=style,align='center')
forward(40)
write('and',font=style,align='center')
forward(40)
write('Prosper',font=style,align='center')
hideturtle()
