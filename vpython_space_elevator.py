from vpython import *
import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

scene.width = screen_width
scene.height = screen_height
scene.background = color.black

G = 6.67e-11
M = 5.97e24
R = 6.371e6
w = 2*pi/(86164)

Rg = (G*M/(w**2))**(1/3)

scene.lights = []
# scene.lights = scene.lights + [distant_light(direction=vector(1,0,0))]
distant_light(direction=vector(0,-1,0))

earth = sphere(pos=vector(0,0,0), radius=R, texture=textures.earth, shininess=0)
earth.rotate(origin=vector(0,0,0), axis=vector(1,0,0), angle=pi/2)

p1 = sphere(pos=vector(Rg/2, 0, 0), radius=R/10, color=color.magenta, make_trail=True)
p1.m = 1
v1s = sqrt(G*M/p1.pos.x)
p1.p = p1.m*vector(0,v1s,0)

p2 = sphere(pos=vector(Rg, 0, 0), radius=R/10, color=color.cyan, make_trail=True)
p2.m = 1
v2s = sqrt(G*M/p2.pos.x)
p2.p = p2.m*vector(0,v2s,0)
h = 144000e3

tower = cylinder(pos=vector(R, 0, 0), axis=vector(h,0 ,0), radius=R/20, color=color.yellow)

t = 0 
dt = 5

while t < 200*60:
    rate(500)
    earth.rotate(origin=vector(0,0,0), axis=vector(0,0,1), angle=w*dt)
    tower.rotate(origin=vector(0,0,0), axis=vector(0,0,1), angle=w*dt)
    F1 = -G*M*p1.m*norm(p1.pos)/mag(p1.pos)**2
    p1.p = p1.p + F1*dt
    p1.pos = p1.pos + (p1.p/p1.m)*dt
    F2 = -G*M*p2.m*norm(p2.pos)/mag(p2.pos)**2
    p2.p = p2.p + F2*dt
    p2.pos = p2.pos + (p2.p/p2.m)*dt
    t += dt

scene.waitfor('click')
