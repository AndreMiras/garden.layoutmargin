###  PyPi  ###
from kivy.properties import ObjectProperty
from kivy.graphics   import Color, Rectangle


class Add_BackgroundColor:
  background_color = ObjectProperty()
  def __init__(self, **kwargs):
    self.bind(background_color=set_CanvasColor)


def set_CanvasColor(layout, color):
  def update_Rect(layout, size):
    layout.rect.pos  = layout.pos
    layout.rect.size = layout.size
  with layout.canvas.before:
    Color(*color)
    layout.rect = Rectangle(size=layout.size, pos=layout.pos)
  layout.bind(size=update_Rect, pos=update_Rect)

