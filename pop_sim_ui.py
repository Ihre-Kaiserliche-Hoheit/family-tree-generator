#from tkinter import *
#import pygame
import PySimpleGUI as sg
import population_sim

T = 0
OUTPUT_1 = 0

sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text(OUTPUT_1)],
            [sg.Button('Turn End'), sg.Button('Cancel')] ]
     
# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    
    if event == "Turn End":
        
    
window.close()
