import vpython as vp
from vpython import *

canvas(background=vp.color.white)
top = vp.sphere(pos=vp.vector(0, 0.5, 0), radius=0.01)
theta = 52*vp.pi/180
L = 1
ball = vp.sphere(pos=top.pos + vp.vector(L*vp.sin(theta), -L*vp.cos(theta), 0), radius=0.05,trail_type="points", color=vp.color.red, make_trail=True)
string = vp.cylinder(pos=top.pos, axis=ball.pos - top.pos, radius=0.005)

dalpha = 0.01
alpha = 0

while alpha < 2*vp.pi:
    rate(100)
    ball.rotate(origin=vector(0,0,0), axis=vp.vector(0,1,0), angle=dalpha)
    string.rotate(origin=vector(0,0,0), axis=vp.vector(0,1,0), angle=dalpha)
    alpha = alpha + dalpha

# scene.waitfor('click')

# while True:
#     rate(60)https://stackoverflow.com/questions/57549723/how-do-i-launch-jupyter-notebook-from-my-terminal