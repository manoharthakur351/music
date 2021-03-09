# importing installed modules
import os
import logging
import kivymd
import PIL
import webbrowser as wb
import random
# KIVY AND KIVYMD MODULES.
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty
from kivy.lang.builder import Builder
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.scrollview  import ScrollView
from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition, FadeTransition, RiseInTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.list import MDList
from kivymd.uix.navigationdrawer import MDNavigationDrawer, NavigationLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd.app import MDApp
# import my own modules
from urls import *		# module having link of websites.  
from screen import *		# modules having screen classes.
from lyout import *		# modules having layout classes


def load ():
	"""
	function to load all kivy files
	"""
	Builder.load_file("screens/sub1/sub1_a.kv")
	Builder.load_file(os.path.join("main.kv"))
	Builder.load_file("layout.kv")
	Builder.load_file("screens/menu.kv")
	Builder.load_file("screens/screen1.kv")
	Builder.load_file("screens/screen2.kv")
	Builder.load_file("screens/screen3.kv")
	Builder.load_file("screens/sub1/abt.kv")
	
	
class Manager(ScreenManager):
	'''
	root widget of main kivy file.
	that's ScreenManager.
	'''
	pass

# SCREEN(S)
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________





# MAIN APP CLASS
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
class MaiApp (MDApp):
	# dialugue box
	dialog = None
	load()
	mode= StringProperty('stop')
	# name of screen p1,,p2,p3.
	back=StringProperty()
	# title of the song on toolbar.
	tit = StringProperty()
	# path of music files.
	music = StringProperty()
	# path of text files.
	lyrics = StringProperty('app')
	# links of Google drawings images
	imag = StringProperty()
	def pla (self, music):
		'''
		this function's role is to play music
		'''
		sound=SoundLoader.load(music)
		if sound:
			if self.mode=='stop':
				sound.play()
			else:
				sound.volume = 0
				sound.stop()
			
	def textit (self,path):
		"""
		this function is to load
		and display text
		from different files
		"""
		file = open(path)
		txt = file.read()
		return txt

	def collab(self):
		'''
		function to display
		dialogue box
		'''
		if not self.dialog:
			self.dialog = MDDialog(
				title="Collaborators",
				text='•Abhishek\n•Aditya\n•Kundan\n•Manohar',
				buttons=[
					MDFlatButton(
						text="", text_color=self.theme_cls.primary_color
					),
					MDFlatButton(
						text="OK", text_color=self.theme_cls.primary_color
					)
				],
			)
		self.dialog.open()

	
	def build(self):
		'''
		overriding build function
		'''
		scrman = Manager()
		return Manager()

#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
if __name__=="__main__":
	MaiApp().run()