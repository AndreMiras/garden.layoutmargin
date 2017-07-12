A set of mixins (`MarginLayout`, `AddMargin`) that adds `margin` functionality to Kivy widgets.  
&nbsp;  
![demo](http://i.imgur.com/4cCZL3t.gif)

&nbsp;  

### @ `.py` subclasses:
```python
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
