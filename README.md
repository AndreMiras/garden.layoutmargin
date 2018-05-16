# garden.layoutmargin

A set of mixins (`MarginLayout`, `AddMargin`) that adds `margin` functionality to Kivy widgets.  


![demo](http://i.imgur.com/4cCZL3t.gif)


## How to use

### @ `.py` subclasses:
```python
from layoutmargin import AddMargin, MarginLayout


class MarginBoxLayout(MarginLayout, BoxLayout):
  pass

    
class MarginButton(AddMargin, Button):
  pass
```

&nbsp;

### @ `.kv` layout:
```yaml
MarginBoxLayout:
    
    MarginButton:
      margin: (30, 10, 30, 10) # integer / float
      
    MarginButton:
      margin: ("10%", "10%", "10%", "10%") # percentage of total widget size
      
    MarginButton:
      margin: (30, "10%", 30, "10%") # mixed
      
    # margin: (left, top, right, bottom)
```

## Install
```
pip install https://github.com/AndreMiras/garden.layoutmargin/archive/develop.zip
```

## Credits
Forked from [Enteleform/-Kivy-MarginLayout-Demo](https://github.com/Enteleform/-Kivy-MarginLayout-Demo).
