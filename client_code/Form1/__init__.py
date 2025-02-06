from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def btnClothing_click(self, **event_args):
    """This method is called when the component is clicked."""
    self.temperature = int(self.sldTemp.value) #Store the slider value inside of a temperature variable as an int

    if(self.temperature < 10): #If temp is below 10, say wear a warm jacket
      result = "Wear a warm jacket. "
    elif(self.temperature >= 10 and self.temperature <= 20): #Between 10 and 20 say wear a sweater
      result = "Wear a sweater. "
    else: #Wear light clothing if between 20 to 40
      result = "Wear light clothing. "

    if self.checkRaining.checked == True: #If the raining box is checked, say to bring an umbrella
      result += "Also make sure to bring an umbrella. "

    if self.radPanel.selected_value == "casual": #If casual radio box is checked
      result += "For today, Jeans and T-Shirt should be fine."
    elif self.radPanel.selected_value == "sports": #If sports radio box is checked
      result += "Finally, make sure to wear sportswear and comfortable shoes."
    elif self.radPanel.selected_value == "formal": #If formal radio box is checked
      result += "Finally, consider wearing a suit or dress."

    #We appeneded to the result string, concatenating the message so that it becomes a full sentence based on what was inputted.

    self.lblResult.text = result #Display the result in a label
    
    pass

  def sldTemp_change(self, **event_args):
    """This method is called when the value of the component is changed""" 
    self.lblSlider.text = f'{self.sldTemp.value}°C' #Display the slider value on the text for user accessibility
    pass
