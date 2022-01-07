#Google also uses a similar code 
#Libraries needed
import phonenumbers
import tkinter as tk
from tkinter import *
from phonenumbers import carrier, timezone, geocoder

#the widgets
def CreateWidgets():
    inunLabel = Label(root, text="Enter Phone Number with country code: ", bg="slateblue4")
    inunLabel.grid(row=0, column=0, padx=10, pady=5)
    inunEntry = Entry(root, width=20, textvariable=numberInput, bg="slateblue3")
    inunEntry.grid(row=0, column=1, padx=10, pady=5, columnspan=2)

    numberLabel = Label(root, text="NATIONAL NUMBER: ",bg="slateblue4")
    numberLabel.grid(row=3, column=0, padx=10, pady=5)
    root.numberLabel = Label(root, width=20, bg="slateblue3")
    root.numberLabel.grid(row=3, column=1, padx=10, pady=5, columnspan=2)

    providerLabel = Label(root, text="SERVICE PROVIDER: ",bg="slateblue4")
    providerLabel.grid(row=4, column=0, padx=10, pady=5)
    root.providerLabel = Label(root, width=20, bg="slateblue3")
    root.providerLabel.grid(row=4, column=1, padx=10, pady=5, columnspan=2)

    timezoneLabel = Label(root, text="TIMEZONE: ", bg="slateblue4")
    timezoneLabel.grid(row=6, column=0, padx=10, pady=5)
    root.timezoneLabel = Label(root, width=20, bg="slateblue3")
    root.timezoneLabel.grid(row=6, column=1, padx=10, pady=5, columnspan=2)

    validLabel = Label(root, text="VALID NUMBER: ", bg="slateblue4")
    validLabel.grid(row=7, column=0, padx=10, pady=5)
    root.validLabel = Label(root, width=20, bg="slateblue3")
    root.validLabel.grid(row=7, column=1, padx=10, pady=5, columnspan=2)

    #Creating the "FETCH" Button to get the details
    getDetailsButton = Button(root, text="FETCH", command = getDetails, bg="green")
    getDetailsButton.grid(row=1, column=1, padx=5, pady=5)
    clearButton = Button(root, text="CLEAR", command = clearEntries, bg="red")
    clearButton.grid(row=1, column=2, padx=5, pady=5)

def getDetails():
    phone_number = numberInput.get()
    phone_number = phonenumbers.parse(phone_number)
    #Phone carrier/Telecom
    phone_number_carrier = carrier.name_for_number(phone_number, "en")
    #nationale number
    national_number = phone_number.national_number
    #getting region of phone number
    phone_number_country = geocoder.description_for_number(phone_number, "en")
    #getting timezone of phone number
    phone_number_timezone = timezone.time_zones_for_number(phone_number)
    #validating phone number
    phone_number_valid = phonenumbers.is_valid_number(phone_number)

    #Clearing former phonenumber entries if there are any when clear is hit
    root.numberLabel.config(text="")
    root.providerLabel.config(text="")
    root.timezoneLabel.config(text="")
   
    #Previewing new results
    root.numberLabel.config(text=str(national_number))
    root.providerLabel.config(text=str(phone_number_carrier))
    root.timezoneLabel.config(text=str(phone_number_timezone))
    root.validLabel.config(text=str(phone_number_valid))
    
def clearEntries():
    root.numberLabel.config(text="")
    root.providerLabel.config(text="")
    root.timezoneLabel.config(text="")
    root.validLabel.config(text="")

root = tk.Tk()
root.title("Phone Number Details Checker")
root.config(background="darkslateblue")
root.geometry("445x250")
root.resizable(False, False)
numberInput = StringVar()
CreateWidgets()
#infinite loop that keeps application running
root.mainloop()
