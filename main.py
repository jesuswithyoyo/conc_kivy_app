import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from numpy import size
from requests import get
from transformers import pipeline
import torch.nn.functional as F
import time
import sys
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget


class CustomeBoxLayout(BoxLayout):
    orientation='vertical'
    def __init__(self, **Kwargs):
        super(CustomeBoxLayout,self).__init__(**Kwargs)
        
       
        text_input = TextInput(text = "", multiline=True)        
        button_ai = Button(text = "Send to AI for Judgement")

        button_ai.bind(on_press = lambda button: self.click_button_ai(text_input.text))

        self.add_widget(text_input)
        self.add_widget(button_ai)

    def preSend(instance):
        


    def click_button_ai(self,text):
        print("This is what has been sent to AI: ",text)

        # AI Send
        model_name = 'distilbert-base-uncased-finetuned-sst-2-english'
        classifier = pipeline('sentiment-analysis', model=model_name)
        # AI Results
        results = classifier([(text)])

        for results in results:
            results = results

        for value in results.values():
            value = value

        perc = (value)

        la = results.get('label')

        if (la == 'POSITIVE'):
            print('{:,.2%}'.format(perc) + "  NOT A CUNT")

            def popupNotCunt(instance):
                print('Popup', instance, 'is being dismissed but is prevented!')
                return True
            popup = Popup(title='Cunt or NOT Cunt',
                size_hint=(None,None), size=(400,115),
                content=Label(text='{:,.2%}'.format(perc) + "  NOT CUNT"),
                auto_dismiss=True)
            popup.bind(on_press=popup.dismiss)
            popup.open()

        else:
            print('{:,.2%}'.format(perc) + "  IS A CUNT")
            
            def popupCunt(instance):
                print('Popup', instance, 'is being dismissed but is prevented!')
                return True
            popup = Popup(title='Cunt or NOT Cunt',
                size_hint=(None,None), size=(400,115),
                content=Label(text='{:,.2%}'.format(perc) + "  CUNT"),
                auto_dismiss=True)
            popup.bind(on_press=popup.dismiss)
            popup.open()

    
class DumbNerdApp(App):
    def build(self):
        return CustomeBoxLayout()

if __name__ == "__main__":
    app = DumbNerdApp()
    app.run()
