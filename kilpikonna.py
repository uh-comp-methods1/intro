from ipycanvas import MultiCanvas, hold_canvas
from IPython import display as ipydisp
import numpy as np
from time import sleep

class _State():
    '''Data structure to store Turtle's state'''
    def __init__(self):
        canvas_size = 300
        self.speed = 4
        self.angular_speed_multiplier = 2
        self.animation_freq = 1/50
        self.canvas = MultiCanvas(2, width=canvas_size, height=canvas_size)
        self.bg = self.canvas[0]
        self.fg = self.canvas[1]
        self.bg.fill_style = 'lightgray'
        self.fg.fill_style = 'red'
_s = _State()

def reset():
    '''Clear the drawing and return Turtle to the center'''
    _s.x = _s.canvas.width / 2
    _s.y = _s.x
    _s.a = 0
    _s.bg.fill_rect(0, 0, _s.canvas.width)
    _draw_turtle()

def speed(s):
    '''Set Turtle's speed to s (must be strictly positive)'''
    _s.speed = s
         
def display_turtle():
    '''Show a canvas for drawing'''
    reset()
    ipydisp.display(_s.canvas)

def right(n):
    '''Turn Turtle n degrees to right'''
    num_steps = int(np.ceil(np.abs(n) / (_s.speed * _s.angular_speed_multiplier)))
    ns = np.linspace(0, n, num_steps + 1)
    dns = ns[1:] - ns[:-1]
    for dn in dns:
        with hold_canvas(_s.canvas):
            _s.a += dn
            _s.a %= 360
            _draw_turtle()
        sleep(_s.animation_freq)

def left(n):
    '''Turn Turtle n degrees to left'''
    right(-n)
    
def forward(n):
    '''Move Turtle forward by n units'''
    angle = np.deg2rad(_s.a)
    num_steps = int(np.ceil(np.abs(n) / _s.speed))
    ns = np.linspace(0, n, num_steps + 1)
    dns = ns[1:] - ns[:-1]
    dx = np.cos(angle)
    dy = np.sin(angle)
    for dn in dns:
        x, y = dn*dx + _s.x, dn*dy + _s.y
        with hold_canvas(_s.canvas):
            _s.bg.stroke_line(_s.x, _s.y, x, y)
            _s.x, _s.y = x, y
            _draw_turtle()
        sleep(_s.animation_freq)

def backward(n):
    '''Move Turtle backward by n units'''
    forward(-n)

## Drawing the Turtle

def _rot_mat(theta):
    '''Rotation matrix'''
    return np.array([
[np.cos(theta), -np.sin(theta)],
[np.sin(theta),  np.cos(theta)],
    ])

# Vertices forming the triangle depicting the Turtle
_vertices = np.array([
[-1,  1],
[-1, -1],
[ 2,  0],
])
        
def _draw_turtle():
    scale = 4    
    p = np.array([_s.x, _s.y])
    angle = np.deg2rad(_s.a)
    R = _rot_mat(angle)
    ws = []
    for v in _vertices:
        ws.append(scale * R @ v + p)
    _s.fg.clear()
    _s.fg.fill_polygon(ws)
    