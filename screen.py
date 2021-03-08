from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition, FadeTransition, RiseInTransition
from kivymd.app import MDApp
class subscreenone(Screen):
	"""
	
	"""
	def ch_sc (self,s):
		switch(s)

class MenuScreen(Screen):
	"""
	
	"""
	
	pass

class profilescreenone(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("menu")
	

class profilescreentwo(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("menu")

class profilescreenthree(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("menu")

class profilescreenfour(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("menu")

class subscreentwo(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("menu")




def switch (screen_name):
	MDApp.get_running_app().root.current = screen_name
	MDApp.get_running_app().root.transition = NoTransition()
	MDApp.get_running_app().root.transition.direction="right"
	#MDApp.get_running_app().root.transition.duration=0.1