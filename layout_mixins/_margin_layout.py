###  StdLib  ###
from typing import NamedTuple

###  PyPi  ###
from kivy.properties import AliasProperty, ObjectProperty


########################################################################################################################################################################################################################################################################################################~{#
#//////|   Add_Margin   |///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////g2#
########################################################################################################################################################################################################################################################################################################~}#

class Add_Margin:
  margin = ObjectProperty()
  _last_X       = None
  _last_Y       = None
  _last_Width   = None
  _last_Height  = None
  _last_MarginX = None
  _last_MarginY = None

  def __init__(self):
    self.margin = (0, 0, 0, 0)


########################################################################################################################################################################################################################################################################################################~{#
#//////|   MarginLayout   |/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////g2#
########################################################################################################################################################################################################################################################################################################~}#

class _Sides(NamedTuple):
  primary:  str
  center:   str
  inverted: str

_X_SIDES = _Sides("left",   "center_x", "right")
_Y_SIDES = _Sides("bottom", "center_y", "top"  )


class MarginLayout:

  #####################################################################################################################################################################################################################################################################################################~>{#
  #//////|   >   Overrides   |//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////g2#
  #####################################################################################################################################################################################################################################################################################################~>}#

  def add_widget(self, widget, index=0):
    widget.fbind("margin", self._trigger_layout)
    return super().add_widget(widget, index)

  def do_layout(self, *args):
    self._trigger_layout.cancel()
    super().do_layout(*args)
    self._apply_Margins()
    self._trigger_layout.cancel()

  #####################################################################################################################################################################################################################################################################################################~>{#
  #//////|   >   _apply_Margins   |/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////g2#
  #####################################################################################################################################################################################################################################################################################################~>}#

  def _apply_Margins(self):

    def get_MarginValue(child, i, value):
      if isinstance(value, str):
        if("%" in value):
          maxSizes = [child.width, child.height, child.width, child.height]
          percentage = float(value.replace("%", "").strip()) / 100
          value = maxSizes[i] * percentage
        else:
          raise ValueError(
            f"\n\t'{child.__class__.__name__}' instance contains an invalid margin value:"
            f"\n\t\t{child.margin}"
            f"\n\t\t<str> '{value}, index={i}"
            f"\n\tMargin values must be one of the following types:"
            f"\n\t\t[int, float, str]"
            f"\n\t\t(String values will be parsed as percentages, and must contain a '%' symbol at the end. EG: '15%')"
          )
      return value

    def get_MarginValues(child):
      if hasattr(child, "margin"):
        return (get_MarginValue(child, i, x) for i, x in enumerate(child.margin))
      else:
        return (0, 0, 0, 0)

    def update_Child(child, key, value):
      if  (key == "_last_X"     ): child.x      = child._last_X      = value
      elif(key == "_last_Y"     ): child.y      = child._last_Y      = value
      elif(key == "_last_Width" ): child.width  = child._last_Width  = value
      elif(key == "_last_Height"): child.height = child._last_Height = value
      elif(key == "_last_MarginX"): child._last_MarginX = value
      elif(key == "_last_MarginY"): child._last_MarginY = value

    def get_Initial_Position(margin, position, size):
      position += margin[0]
      size -= sum(margin)
      return position, size

    def update_SizeHint_Widget(child, margin, position, lastPosition_Key, size, lastSize_Key):
      position, size = get_Initial_Position(margin, position, size)
      update_Child(child, lastPosition_Key, position)
      update_Child(child, lastSize_Key, size)

    def update_Sized_Widget(
      child, sides,
      position, position_Hint, lastPosition, lastPosition_Key,
      size,     size_Hint,     lastSize,     lastSize_Key,
      margin, lastMargin, lastMargin_Key,
    ):
      if(lastSize == None):
        position, size = get_Initial_Position(margin, position, size)
      else:
        if(margin != lastMargin) and (position_Hint == sides.primary):
          difference = (lastMargin[0] - margin[0])
          position -= difference
        if(size != lastSize) and (position_Hint == sides.inverted):
          difference = size - lastSize
          position -= (difference + (margin[1] - difference))
        elif(position_Hint == sides.inverted):
          position -= margin[1]
      update_Child(child, lastPosition_Key, position)
      update_Child(child, lastSize_Key,     size    )
      update_Child(child, lastMargin_Key,   margin  )

    def apply_Margins(
      child, sides,
      position, position_Hint, lastPosition, lastPosition_Key,
      size,     size_Hint,     lastSize,     lastSize_Key,
      margin, lastMargin, lastMargin_Key,
    ):
      if(size_Hint):
        update_SizeHint_Widget(child, margin, position, lastPosition_Key, size, lastSize_Key)
      else:
        update_Sized_Widget(
          child, sides,
          position, position_Hint, lastPosition, lastPosition_Key,
          size,     size_Hint,     lastSize,     lastSize_Key,
          margin, lastMargin, lastMargin_Key,
        )

    for child in self.children:
      if hasattr(child, "margin"):

        left, top, right, bottom = get_MarginValues(child)
        x_Margin, y_Margin = ((left, right), (bottom, top))
        x_Hint, y_Hint = child.pos_hint if(child.pos_hint) else(None, None)
        w_Hint, h_Hint = child.size_hint

        apply_Margins(
          child=child, sides=_X_SIDES,
          position=child.x, position_Hint=x_Hint, lastPosition=child._last_X, lastPosition_Key="_last_X",
          size=child.width, size_Hint=w_Hint,     lastSize=child._last_Width, lastSize_Key="_last_Width",
          margin=x_Margin, lastMargin=child._last_MarginX, lastMargin_Key="_last_MarginX",
        )

        apply_Margins(
          child=child, sides=_Y_SIDES,
          position=child.y,  position_Hint=y_Hint, lastPosition=child._last_Y,  lastPosition_Key="_last_Y",
          size=child.height, size_Hint=h_Hint,     lastSize=child._last_Height, lastSize_Key="_last_Height",
          margin=y_Margin, lastMargin=child._last_MarginY, lastMargin_Key="_last_MarginY",
        )

