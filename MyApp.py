import os
import logging
import kivymd
import PIL
import webbrowser as wb
import random
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty
from kivy.lang.builder import Builder
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.scrollview  import ScrollView
from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition, FadeTransition, RiseInTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineAvatarListItem , TwoLineAvatarListItem, ThreeLineAvatarListItem, OneLineIconListItem, TwoLineIconListItem ,ThreeLineIconListItem
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.list import MDList , OneLineAvatarListItem
from kivymd.uix.navigationdrawer import MDNavigationDrawer, NavigationLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp

	
from urls import *
from screen import *
from lyout import *


def load_sub1 ():
	Builder.load_file("screens/sub1/sub1_a.kv")
	

def load ():
	Builder.load_file(os.path.join("main.kv"))
	Builder.load_file("layout.kv")
	Builder.load_file("screens/menu.kv")
	Builder.load_file("screens/screen1.kv")
	Builder.load_file("screens/screen2.kv")
	Builder.load_file("screens/screen3.kv")
	Builder.load_file("screens/screen4.kv")
	load_sub1()
	
	
	
	


	
class Manager(ScreenManager):
	pass

# SCREEN(S)
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________





# MAIN APP CLASS
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
class MaiApp (MDApp):
	dialog = None
	load()
	mode= StringProperty('stop')
	back=StringProperty()
	tit = StringProperty()
	music = StringProperty()
	lyrics = StringProperty('app')
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
		this function is to load and display text
		from different files
		"""
		file = open(path)
		txt = file.read()
		return txt

	def show_alert_dialog(self):
		if not self.dialog:
			self.dialog = MDDialog(
				text="Discard draft?",
				buttons=[
					MDFlatButton(
						text="CANCEL", text_color=self.theme_cls.primary_color
					),
					MDFlatButton(
						text="DISCARD", text_color=self.theme_cls.primary_color
					),
				],
			)
		self.dialog.open()

	
	def build(self):
		scrman = Manager()
		return Manager()

#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
if __name__=="__main__":
	MaiApp().run()