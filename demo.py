###  Kivy Config  ###
from kivy.config import Config
Config.set("graphics", "width",  "1000")
Config.set("graphics", "height", "1000")

###  App  ###
from layout_mixins import MarginLayout, AddMargin, Add_BackgroundColor

###  PyPi  ###
from kivy.app             import App
from kivy.uix.button      import Button
from kivy.uix.boxlayout   import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.clock           import Clock


########################################################################################################################################################################################################################################################################################################~{#
#//////|   SubClasses   |///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////g2#
########################################################################################################################################################################################################################################################################################################~}#

class MarginButton(Button, AddMargin):
	def __init__(self, **kwargs):
		Button.__init__(self, **kwargs)
		AddMargin.__init__(self)

class MarginBoxLayout(MarginLayout, BoxLayout, Add_BackgroundColor):
	def __init__(self, **kwargs):
		MarginLayout.__init__(self)
		BoxLayout.__init__(self, **kwargs)
		Add_BackgroundColor.__init__(self)

class MarginFloatLayout(MarginLayout, FloatLayout, Add_BackgroundColor):
	def __init__(self, **kwargs):
		MarginLayout.__init__(self)
		FloatLayout.__init__(self, **kwargs)
		Add_BackgroundColor.__init__(self)


########################################################################################################################################################################################################################################################################################################~{#
#//////|   Demo   |/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////g2#
########################################################################################################################################################################################################################################################################################################~}#

class DemoLayout(BoxLayout):
	pass


class Demo(App):
	title = ""

	def build(self):
		return DemoLayout()

	#!!!!!!!!!!!!!!
	#!!!  NOTE  !!!
	#!!!!!!!!!!!!!!
	# All of the code below is unrelated to the actual implementation of the MarginLayout Mixin.
	# These are just tests to make sure that margin & size updates work properly,
	# and as such, I didn't spend much time optimizing them for best-practices/efficiency/readability.

	def on_start(self):
		self.boxButton         = self.root.ids["boxButton"        ]
		self.floatLayout       = self.root.ids["floatLayout"      ]
		self.floatLayout_Label = self.root.ids["floatLayout_Label"]
		self.floatButtons = [x for x in self.floatLayout.children]
		self.set_BoxOffsets()
		Clock.schedule_interval(self.test_Layouts, 0.01)

	def test_Layouts(self, *args):
		self.test_FloatLayout()
		self.test_BoxLayout()

	#####################################################################################################################################################################################################################################################################################################~>{#
	#//////|   >   BoxLayout Test   |/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////g2#
	#####################################################################################################################################################################################################################################################################################################~>}#

	def set_BoxOffsets(self):
		self.boxOffsets = []
		sides = [None, 0, 1, 2, 3]
		for i in range(len(sides)):
			addGroup      = [0.4,  0.4,  0.4,  0.4 ]
			subtractGroup = [-0.4, -0.4, -0.4, -0.4]
			cancelIndex = sides[i]
			if(cancelIndex != None):
				addGroup[cancelIndex], subtractGroup[cancelIndex] = (0, 0)
			self.boxOffsets += ([addGroup for i in range(self.steps)] + [subtractGroup for i in range(self.steps)])

	marginCycle1 = 0
	def test_BoxLayout(self, *args):
		i = self.marginCycle1 % len(self.boxOffsets)
		m = [float(x.replace("%", "")) for x in self.boxButton.margin]
		o = self.boxOffsets[i]
		marginPairs = (m[0], o[0]), (m[1], o[1]), (m[2], o[2]), (m[3], o[3])
		margin = ["{0:.1f}".format(a + b) + "%" for a,b in marginPairs]
		self.boxButton.margin = margin
		marginText = ["{0:.0f}".format(float(x.replace("%", ""))) + "%" for x in self.boxButton.margin]
		self.boxButton.text = f"size_hint: (0.5, 1)\nmargin: {marginText}"
		self.marginCycle1 += 1

	#####################################################################################################################################################################################################################################################################################################~>{#
	#//////|   >   FloatLayout Test   |///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////g2#
	#####################################################################################################################################################################################################################################################################################################~>}#

	offsetCycle  = 0
	marginCycle2 = -1
	steps        = 40
	floatOffsets = [2.5 for i in range(steps)] + [-2.5 for i in range(steps)]
	margins2     = [(30, 30, 30, 30), (0, 30, 30, 30), (30, 0, 30, 30), (30, 30, 0, 30), (30, 30, 30, 0)]

	def test_FloatLayout(self):
		i = self.offsetCycle % len(self.floatOffsets)
		if(i == 0):
			self.marginCycle2 += 1
		j = self.marginCycle2 % len(self.margins2)
		self.floatLayout_Label.text = "FloatLayout:  margin = " + str(self.margins2[j])
		for button in self.floatButtons:
			button.size = (button.width + self.floatOffsets[i], button.height + self.floatOffsets[i])
			button.margin = self.margins2[j]
		self.offsetCycle += 1


Demo().run()
