from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class calculatorWithGUI(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Create input widgets
        self.input1 = TextInput(hint_text='Enter 1st number', multiline=False)
        self.input2 = TextInput(hint_text='Enter 2nd number', multiline=False)
        
        # Create a Label to display results
        self.result_label = Label(text="")
        
        # Create buttons and bind actions
        btn_div = Button(text='Division')
        btn_div.bind(on_press=self.div)
        
        btn_mult = Button(text='Multiplication')
        btn_mult.bind(on_press=self.mult)
        
        btn_add = Button(text='Addition')
        btn_add.bind(on_press=self.add)
        
        btn_redu = Button(text='Reduction')
        btn_redu.bind(on_press=self.redu)

        # btn_exit = Button(text='Exit')
        # btn_exit.bind(on_press=self.exit)
        
        # Add widgets to the layout
        layout.add_widget(self.input1)
        layout.add_widget(self.input2)
        layout.add_widget(self.result_label)
        layout.add_widget(btn_div)
        layout.add_widget(btn_mult)
        layout.add_widget(btn_add)
        layout.add_widget(btn_redu)
        # layout.add_widget(btn_exit)
        
        return layout

    def mult(self,instance):
        try:
            num1 = float(self.input1.text)
            num2 = float(self.input2.text)
            result = num1 * num2
            self.result_label.text = f"Result: {num1}*{num2} = {result}"
        except ValueError:
            self.result_label.text = "Invalid input. Please enter numbers."

    def div(self,instance):
        try:
            num1 = float(self.input1.text)
            num2 = float(self.input2.text)
            if num2 == 0:
                self.result_label.text = "Cannot divide by zero."
                return
            result = num1 / num2
            self.result_label.text = f"Result: {num1}/{num2} = {result}"
        except ValueError:
            self.result_label.text = "Invalid input. Please enter numbers."

    def add(self,instance):
        try:
            num1 = float(self.input1.text)
            num2 = float(self.input2.text)
            result = num1+num2
            self.result_label.text = f"Result: {num1}+{num2} = {result}"
        except ValueError:
            self.result_label.text = "Invalid input. Please enter numbers."

    def redu(self,instance):
        try:
            num1 = float(self.input1.text)
            num2 = float(self.input2.text)
            result = num1-num2
            self.result_label.text = f"Result: {num1}-{num2} = {result}"
        except ValueError:
            self.result_label.text = "Invalid input. Please enter numbers."

    def exit():
        # calculatorWithGUI.exit()
        pass

if __name__ == '__main__':
    calculatorWithGUI().run()
