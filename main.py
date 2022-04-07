# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re
import kivy
from kivy.app import App
kivy.require('2.0.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class TipCalcBoxLayout(BoxLayout):
    # def calculateTip(self, bill, percentage, party):

    #     try:
    #         bill = float(bill)
    #         percentage = float(percentage)
    #         party = float(party)

    #         percentage /= 100

    #         self.ids.tip_amount.text = "Tip Amount: $" + "{:.2f}".format((bill * percentage) / party)

    #     run()cept:
    #         self.ids.tip_amount.text = "Enter Numbers Only"
    def calculateSplitTip(self):
        if self.ids.bill_total.text == '' or self.ids.bill_total.text == '.':
            bill = 0.0
        else:
            bill = float(self.ids.bill_total.text)

        percentage = self.ids.tip_slider.value / 100

        party_size = self.ids.split_slider.value

        tip = "{:.2f}".format((bill * percentage) / party_size)

        self.ids.split_tip_amount.text = "Split Tip: $" + tip



    def calculateTip(self):
        if self.ids.bill_total.text == '' or self.ids.bill_total.text == '.':
            bill = 0.0
        else:
            bill = float(self.ids.bill_total.text)

        percentage = self.ids.tip_slider.value / 100

        tip = "{:.2f}".format((bill * percentage))

        self.ids.tip_amount.text = "Tip: $" + tip



class FloatInput(TextInput):
    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
            if len(self.text.rsplit('.')[-1]) == 2:
                s = re.sub(pat, '', '')
        else:
            s = '.'.join(re.sub(pat, '', s) for s in substring.split('.', 1))
            if len(self.text) == 4 and substring != '.':
                s = re.sub(pat, '', '')

        return super().insert_text(s, from_undo=from_undo)


class TipCalculatorApp(App): 

    def build(self):
        pass


calcApp = TipCalculatorApp()
calcApp.run()

#on_press: tip_amount.text = "Tip Amount: $" + tip_calculator.calculateTip(total_bill.text, tip_percentage.text, party_size.text)