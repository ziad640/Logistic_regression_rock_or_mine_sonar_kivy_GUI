from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import numpy as np
import pickle

# Load the trained model
with open('sonar_rock_vs_mine_model.pkl', 'rb') as file:
    model = pickle.load(file)

class SonarApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text="Enter the 60 features separated by commas:")
        self.layout.add_widget(self.label)
        
        self.input_text = TextInput(multiline=False)
        self.layout.add_widget(self.input_text)
        
        self.predict_button = Button(text="Predict")
        self.predict_button.bind(on_press=self.predict)
        self.layout.add_widget(self.predict_button)
        
        self.result_label = Label(text="")
        self.layout.add_widget(self.result_label)
        
        return self.layout

    def predict(self, instance):
        # Get input data
        input_data = self.input_text.text.split(',')
        try:
            input_data = np.asarray(input_data, dtype=float).reshape(1, -1)
            # Predict using the loaded model
            prediction = model.predict(input_data)

            if prediction[0] == 'R':
                result = 'The object is a Rock'
            else:
                result = 'The object is a Mine'
        except:
            result = "Invalid input data. Please enter 60 numerical values separated by commas."

        # Display the result
        self.result_label.text = result

if __name__ == "__main__":
    SonarApp().run()
