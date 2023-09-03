from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
class InstrScr():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        info = Label(text = "Тут буде відображена інформація про додаток")
        lb_name = Label(text = "Введіть ім'я:")
        input_text_name = TextInput()
        lb_age = Label(text = "Введіть вік:")
        input_text_age = TextInput()
        start = Button(text = "Почати", size_hint=(0.3, 0.2), pos_hint = {'center_x': 0.5})
        line_h_1 = BoxLayout(size_hint = (0.7, None), height = "35sp")
        line_h_2 = BoxLayout(size_hint = (0.7, None), height = "35sp")
        line_h_1.add_widget(lb_name)
        line_h_1.add_widget(input_text_name)
        line_h_2.add_widget(lb_age)
        line_h_2.add_widget(input_text_age)
        line_v = BoxLayout(orientation = "vertical", padding = 8, spacing = 20)
        line_v.add_widget(info)
        line_v.add_widget(line_h_1)
        line_v.add_widget(line_h_2)
        line_v.add_widget(start)
        self.add_widget(line_v)



class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name="instr"))
        return sm
app = HeartCheck()
app.run()


