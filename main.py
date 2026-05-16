from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class LeapApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.input = TextInput(hint_text='输入年份')
        self.label = Label(text='结果显示')

        btn = Button(text='判断')

        btn.bind(on_press=self.check)

        layout.add_widget(self.input)
        layout.add_widget(btn)
        layout.add_widget(self.label)

        return layout

    def check(self, instance):
        try:
            year = int(self.input.text)

            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                self.label.text = "闰年"
            else:
                self.label.text = "平年"

        except:
            self.label.text = "请输入正确年份"

LeapApp().run()