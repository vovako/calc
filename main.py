from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

ww = 230
wh = 320

from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', ww)
Config.set('graphics', 'height', wh)

bgWindow = (1, .90, .76, 1)
fsBtn = 30
fsBtn2 = 40
bgcBtn = [.61, .8, 1, 1]
colorBtn = [0, 0, 0, 1]
colorResultBtn = [.57, 1, .53, 1]
colorOperatBtn = [.99, .97, .59, 1]
colorDeleteBtn = [1, .59, .51, 1]

from kivy.core.window import Window
Window.clearcolor = bgWindow

class CalcApp(App):
	def build(self):
		self.formula = '0'
		bl = BoxLayout(orientation='vertical', padding=[10])
		gl = GridLayout(cols=4, spacing=3, size_hint = (1, .65))
		
		self.lbl = Label(text='0', font_size=28, size_hint=(1, .35), text_size=(ww - 20, wh * .35 - 20), halign='right', valign='center', color=[0, 0, 0, 1])
		bl.add_widget(self.lbl)

		gl.add_widget(Button(text='Clear', on_press=self.clear, background_color=colorDeleteBtn, background_normal= '', color=colorBtn))
		gl.add_widget(Widget())
		gl.add_widget(Widget())
		gl.add_widget(Button(text='⌫', on_press=self.backSpace, font_name='DejaVuSans.ttf',  font_size=17, background_color=colorDeleteBtn, background_normal= '', color=colorBtn))

		gl.add_widget(Button(text='7', on_press=self.add_number, font_size=fsBtn, background_color=bgcBtn, background_normal= '', color=colorBtn))
		gl.add_widget(Button(text='8', on_press = self.add_number, font_size=fsBtn, background_color=bgcBtn, background_normal= '', color=colorBtn))
		gl.add_widget(Button(text='9', on_press = self.add_number, font_size=fsBtn, background_color=bgcBtn, background_normal= '', color=colorBtn))
		gl.add_widget(Button(text='×', on_press=self.add_operatinon, font_size=fsBtn, background_color=colorOperatBtn, background_normal= '', color=colorBtn))

		gl.add_widget(Button(text='4', on_press = self.add_number, font_size=fsBtn, background_color=bgcBtn, background_normal= '', color=colorBtn))
		gl.add_widget(Button(text='5', on_press = self.add_number, font_size=fsBtn, background_color=bgcBtn, background_normal= '', color=colorBtn))
		gl.add_widget(Button(text='6', on_press = self.add_number, font_size=fsBtn, background_color=bgcBtn, background_normal= '', color=colorBtn))
		gl.add_widget(Button(text='÷', on_press = self.add_operatinon, font_size=fsBtn, background_color=colorOperatBtn, background_normal= '', color=colorBtn))

		gl.add_widget(Button(text='1', on_press = self.add_number, font_size=fsBtn, background_color=bgcBtn, background_normal= '', color=colorBtn))
		gl.add_widget(Button(text='2', on_press = self.add_number, font_size=fsBtn, background_color=bgcBtn, background_normal= '', color=colorBtn))
		gl.add_widget(Button(text='3', on_press = self.add_number, font_size=fsBtn, background_color=bgcBtn, background_normal= '', color=colorBtn))
		gl.add_widget(Button(text='+', on_press = self.add_operatinon, font_size=fsBtn, background_color=colorOperatBtn, background_normal= '', color=colorBtn))

		gl.add_widget(Button(text='.', on_press = self.add_number, font_size=fsBtn2, background_color=bgcBtn, background_normal= '', color=colorBtn))
		gl.add_widget(Button(text='0', on_press = self.add_number, font_size=fsBtn, background_color=bgcBtn, background_normal= '', color=colorBtn))
		gl.add_widget(Button(text='=', on_press = self.get_result, font_size=fsBtn, background_color=colorResultBtn, background_normal= '', color=colorBtn))
		gl.add_widget(Button(text='-', on_press = self.add_operatinon, font_size=fsBtn2, background_color=colorOperatBtn, background_normal= '', color=colorBtn))

		bl.add_widget(gl)
		return bl


	def update_label(self):
		self.lbl.text = self.formula

	def add_number(self, example):
		if (self.formula == '0'):
			self.formula = ''
		self.formula += str(example.text)
		self.update_label()

	def add_operatinon(self, example):
		if (str(example.text).lower() == '×'):
			self.formula += '*'
		elif (str(example.text).lower() == '÷'):
			self.formula += '/'
		else:
			self.formula += str(example.text)

		self.update_label()

	def get_result(self, example):
		try:
			self.lbl.text = str(eval(self.lbl.text))
			self.formula = str(eval(self.lbl.text))
		except:
			self.lbl.text = 'Error value'
			self.formula = '0'

	def clear(self, example):
		self.formula = '0'
		self.update_label()

	def backSpace(self, example):
		if (self.formula[:-1] != ''):
			self.formula = self.formula[:-1]
		else:
			self.formula = '0'
		self.update_label()


if __name__ == "__main__":
	CalcApp().run()
