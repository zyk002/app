from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LeapYearApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.input = TextInput(hint_text='请输入年份', multiline=False, font_size=24)
        self.result = Label(text='结果显示在这里', font_size=24)
        btn = Button(text='判断是否为闰年', font_size=24, on_press=self.check)
        layout.add_widget(self.input)
        layout.add_widget(btn)
        layout.add_widget(self.result)
        return layout

    def check(self, instance):
        try:
            i = int(self.input.text)
            if (i % 4==0 and i % 100!=0) or (i % 400==0):
                self.result.text = f"{i}年 是闰年 ✅"
            else:
                self.result.text = f"{i}年 是平年 ❌"
        except:
            self.result.text = "请输入正确年份！⚠️"

LeapYearApp().run()