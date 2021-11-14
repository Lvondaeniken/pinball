from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.image import Image
from kivy.clock import Clock

class MyMenu(BoxLayout):
    def test(self):
        print("jhelel")
        self.ids.btn1.text = "lol"
        self.ids.image1.source= "bier.jpg"  
        self.ids.image2.source= "bier.jpg"  
        self.ids.image3.source= "bier.jpg"  
        self.ids.image4.source= "bier.jpg"  
        self.ids.image5.source= "bier.jpg"  
        self.ids.image6.source= "bier.jpg"  
        self.ids.image7.source= "bier.jpg"  
        self.ids.image8.source= "bier.jpg"  
        self.ids.image9.source= "bier.jpg"  
    
    def toggle_image(self):
        if self.ids.image2.source=="white.jpg":
            self.ids.image1.source= "bier.jpg"  
            self.ids.image2.source= "bier.jpg"  
            self.ids.image3.source= "bier.jpg"  
            self.ids.image4.source= "bier.jpg"  
            self.ids.image5.source= "bier.jpg"  
            self.ids.image6.source= "bier.jpg"  
            self.ids.image7.source= "bier.jpg"  
            self.ids.image8.source= "bier.jpg"  
            self.ids.image9.source= "bier.jpg"  
        else:
            self.ids.image1.source= "white.jpg"  
            self.ids.image2.source= "white.jpg"  
            self.ids.image3.source= "white.jpg"  
            self.ids.image4.source= "white.jpg"  
            self.ids.image5.source= "white.jpg"  
            self.ids.image6.source= "white.jpg"  
            self.ids.image7.source= "white.jpg"  
            self.ids.image8.source= "white.jpg"  
            self.ids.image9.source= "white.jpg"  

    def update(self):
        self.toggle_image()

class PinballApp(App):
    def build(self):
        m = MyMenu()
        return m

    def hello(self):
        print("hello")
        window = MyMenu()
        window.add_widget(Label("hello"))

if __name__ == '__main__':
    PinballApp().run()