from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from PIL import Image, ImageTk  
from tkinter import Label, Tk

import pyttsx3
import speech_recognition as sr
import os
from PIL import ImageTk, Image

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Declare entry as a global variable
entry = None

def text_to_speech():
    
    #Use the text-to-speech engine to convert text into speech
    text = input_text.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)

    setvoice()

    if text:
        if speed == 'Fast':
            engine.setProperty('rate', 250)
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)

        engine.say(text)
        engine.runAndWait()  

    
          
    # root.after(1000, lambda: speak_button.config(state=NORMAL))    

def download():
    #Use the text-to-speech engine to convert text into speech
    text = input_text.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text , "text.mp3")
        else:
            engine.setProperty('voice', voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text , "text.mp3")

    setvoice()

    if text:
        if speed == 'Fast':
            engine.setProperty('rate', 250)
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)

        engine.say(text)
        engine.runAndWait()  



def speech_to_text():
    # Display "Listening" when the button is pressed
    text.delete(1.0, END)
    text.insert(END, "Listening")

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        try:
            # Listen to the user's speech with a timeout of 10 seconds
            audio = recognizer.listen(source, timeout=10)
            # Recognize speech using Google Web Speech API
            recognized_text = recognizer.recognize_google(audio)
            # Display the recognized text in the text box
            text.delete(1.0, END)
            text.insert(END, recognized_text)
        except sr.WaitTimeoutError:
            # Display a message if no speech is recognized within 10 seconds
            text.delete(1.0, END)
            text.insert(END, "No speech is recognized within 10 seconds.")
        except sr.RequestError as e:
            # Display an error message if there is a request error
            text.delete(1.0, END)
            text.insert(END, f"Recognition error: {e}")

    return ""



# GUI
root = Tk()

#icon
mic_image = Image.open("micbutton (1).png")
mic_btn = ImageTk.PhotoImage(mic_image)

# COLORS
background="#06283D"   
framebg="#EDEDED"
framefg="#06283D"
button_color = "#EE0000" 
text_color = "white"
activebackground =  "#EE0000"



root.geometry("655x455")
root.config(bg=background)
root.title("Voice Scripter")
root.resizable(FALSE,FALSE)

#icon image
img_icon = PhotoImage(file="icons8-mic-94.png")
root.iconphoto(FALSE,img_icon)

#TOP FRAME 
top_frame = Frame(root , bg="white" , width=655  , height=65)
top_frame.pack()

logo = PhotoImage(file="micbutton (1).png")
Label(top_frame, image=logo, bg="white").place(x=10, y=5)

def tab1():
    def Text_to_Voice():
        global input_text    # Declare entry as a global variable
        global speed_combobox    # Declare entry as a global variable
        global gender_combobox
        global speak_button
        label1.destroy()
        label2.destroy()
        button1.destroy()
        button2.destroy()

        def back():
          
            speak_button.destroy()
            Text_to_Voice_label.destroy()
            Text_to_Voice_buttonback.destroy()
            save_button.destroy()
            speak_button.destroy()
            input_text.destroy()
            speed_label.destroy()
            voice_label.destroy()
            gender_combobox.destroy()
            speed_combobox.destroy()
            Text_to_Voice_f2.destroy()
            input_label.destroy()
            tab1()

       
        Text_to_Voice_label = Label(top_frame , text="Text to Voice Converter" , font="arial 20 bold" , bg="white" , fg=background)
        Text_to_Voice_label.place(x=70 ,y=15)

        input_label =Label(root ,text="Type Text here:", font="Helvetica 10 bold" , bg=background , fg="white")
        input_label.place(x=60 , y=90 )

        input_text = Text(root , font="Robote 15" , bg="white" ,relief=GROOVE ,wrap=WORD )
        input_text.place(x=60 , y=120 , width=300 ,height=150)
        
        
        Text_to_Voice_f2 = Frame(width=500, height=150, relief=RIDGE, bg="white" ,background=background)
        Text_to_Voice_f2.pack(side=RIGHT)
        Text_to_Voice_f2.place(x=450, y=100)

      

        voice_label =Label(root , text="VOICE" , font="arial 12 bold" , bg=background ,fg="white")
        voice_label.place(x=400 , y=120)
        speed_label =Label(root , text="SPEED" , font="arial 12 bold" , bg=background ,fg="white")
        speed_label.place(x=530 , y=120)

        # GENDER selection
        gender_combobox = Combobox(root , values=["Male" , "Female"],font="arial 12" , state='r' , width=8 ) 
        gender_combobox.place(x=400 , y=150)
        gender_combobox.set("Male")

        #SPEED Seleection
        speed_combobox = Combobox(root , values=["Fast" , "Normal" , "Slow"],font="arial 12" , state='r' , width=8 ) 
        speed_combobox.place(x=530 , y=150)
        speed_combobox.set("Normal")

        #speak button
        speak_img = ImageTk.PhotoImage(file="voice-on-01.png")

        speak_button = Button(  text="Speak", font=("arial", 12),command=text_to_speech, activebackground=activebackground , width=9,fg=text_color ,bg=button_color)
        speak_button.place(x=400 , y=200 )
        # speak_button.place(x=430 , y=200 )

        #SAVE BUTTON 
        save_button = Button(  text="Save", font=("arial", 12), activebackground=activebackground ,bg=button_color, width=9,fg=text_color , command=download )
        save_button.place(x=530 , y=200 )

        #Back button
        Text_to_Voice_buttonback = Button(root, text="BACK", font=("Helvetica", 10), activebackground=activebackground,
                                           command=back, bg=button_color, padx=5, pady=5, fg=text_color)
        Text_to_Voice_buttonback.pack(side=BOTTOM, pady=20)


    def Voice_to_Text():
        global text
        label1.destroy()
        label2.destroy()
        button1.destroy()
        button2.destroy()

        def back():
            
            speak_button.destroy()
            Voice_to_Text_label.destroy()
            Voice_to_Text_buttonback.destroy()
            text.destroy()
            tab1()

        
        Voice_to_Text_label = Label(top_frame , text="Voice To Text Converter" , font="arial 20 bold" , bg="white" , fg=background)
        Voice_to_Text_label.place(x=70 ,y=15)

        #Speak buttn
        speak_button = Button(text="Speak" ,command=speech_to_text, font=("Helvetica", 14), bg=button_color, fg=text_color , activebackground=activebackground , relief=RAISED)
        speak_button.place(x=300 , y=110)

        text = Text(root , font="Robote 15" , bg="white" ,relief=GROOVE ,wrap=WORD )
        text.place(x=180 , y=160 , width=300 ,height=150)

        Voice_to_Text_buttonback = Button(root, text="BACK", font=("Helvetica", 10), activebackground=activebackground,
                                        command=back, bg=button_color, padx=5, pady=5, fg=text_color )
        Voice_to_Text_buttonback.pack(side=BOTTOM, pady=20)    

    label1 = Label(top_frame , text="Welcome To Voice Scripter" , font="arial 20 bold" , bg="white" , fg=background)
    label1.place(x=70 ,y=15)

    label2 = Label(root, text='Please Select Anyone:', font=("Helvetica", 16, "bold"), padx=10, pady=5, fg=text_color, bg=background)
    label2.pack(pady=10)

    button1 = Button(root, text="Voice to Text Converter", font=("Helvetica", 14), activebackground=activebackground,
                     command=Voice_to_Text, padx=10, bg=button_color, fg=text_color)
    button1.pack(pady=10)

    button2 = Button(root, text="Text to Voice Converter", font=("Helvetica", 14), activebackground=activebackground,
                     command=Text_to_Voice, padx=10, bg=button_color, fg=text_color)
    button2.pack(pady=10)

# Call the function to initialize the GUI
tab1()


# Start the GUI event loop
root.mainloop()
