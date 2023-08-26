from PyPDF2.pdf import PdfFileReader
from PySimpleGUI.PySimpleGUI import *
import pyttsx3
import PySimpleGUI as sg
import PyPDF2
from tkinter.filedialog import *

#Initialize Player
player = pyttsx3.init()

#Set Voice to player
voices = player.getProperty('voices')
player.setProperty('voice', voices[1].id)

#Set Speed of Voice
player.setProperty("rate", 100)

#GUI
layout = [[sg.Text('Choose PDF File to read'), sg.Button('Choose')],[sg.Button('Play'), sg.Button('Cancel')]]
window = sg.Window('Input', layout)

while True:
    event, values = window.read()
    
    #Cancle Button
    if event == 'Cancel':
        print("Closing")
        player.stop()
        window.close()

    #Choose button to get PDF
    if event == "Choose":
        book = askopenfilename()

    if event=="play":
        pdfreader=PyPDF2.PdfFileReader(book)
        pages=pdfreader.numPages
        for num in range(0,pages):
            page=pdfreader.getPage(num)
            text=page.extractText()
            player.say(Text)
            player.runAndWait()