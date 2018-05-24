
from tkinter import *
import json
root = Tk()
#theLabel = Label(root, text = "Bot text")
#places window wherever
#theLabel.pack()
'''
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

button1 = Button(topFrame, text = "Button 1",fg = "red")
button2 = Button(topFrame, text = "Button 2",fg = "blue")
button3 = Button(topFrame, text = "Button 3",fg = "green")
button4 = Button(bottomFrame, text = "Button 4",fg = "purple")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack()
##########################
one = Label(root, text = "one", bg = "red", fg = "white")
one.pack()
#grows with x
two = Label(root, text = "tqo", bg = "green", fg = "black")
two.pack(fill=X)
#grows with y
three = Label(root, text = "tqo", bg = "blue", fg = "white")
three.pack(side=LEFT, fill=Y)

##############################
label1 = Label(root, text = "Name")
label2 = Label(root, text = "Password")
entry1 = Entry(root)
entry2 = Entry(root)
#sticky NSEW
label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

c = Checkbutton(root, text="Keep me signed in")
c.grid(columnspan=2)
'''
'''
def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if entry1.get() == 'Full Name':
       entry1.delete(0, "end") # delete all the text in the entry
       entry1.insert(0, '') #Insert blank for user input
       entry1.config(fg = 'black')
    if entry2.get() == 'Email':
       entry2.delete(0, "end") # delete all the text in the entry
       entry2.insert(0, '') #Insert blank for user input
       entry2.config(fg = 'black')
def on_focusout(event):
    if entry1.get() == '':
        entry1.insert(0, 'Full name')
        entry1.config(fg = 'grey')
    if entry2.get() == '':
        entry2.insert(0, 'Email')
        entry2.config(fg = 'grey')
'''

data = {}
data['Profile']=[]
def retrieveInput():
    name = entry1.get()
    email = entry2.get()
    phone = entry3.get()
    ads = entry4.get()
    ads2 = entry5.get()
    city=entry7.get()
    zip = entry6.get()
    state= selectedState.get()
    profName = entry8.get()
    cc = entry9.get()
    cvv = entry10.get()
    month = selectedMonth.get()
    year = selectedYear.get()

    data['Profile'].append({'name': name,
                            'email': email,
                            'phone': phone,
                            'address': ads,
                            'address2': ads2,
                            'city': city,
                            'zip': zip,
                            'state': state,
                            'profile': profName,
                            'credit card': cc,
                            'cvv': cvv,
                            'month': month,
                            'year': year
                            })
    with open('data.txt', 'w') as outfile:
        json.dump(data,outfile)
    '''print (name)
    print (pas)
    print (phone)
    print (ads)
    print(ads2)
    print (city)
    print(zip)
    print(state)
'''



STATES = [
    "AL", "AK","AZ","AR","CA",
    "CO","CT","DE","FL","GA"
    "HI","ID","IL","IN","IA",
    "KS","KY","LA","ME","MD",
    "MA","MI","MN","MS","MO",
    "MT","NE","NV","NH","NJ",
    "NM","NY","NC","ND","OH",
    "OK","OR","PA","RI","SC",
    "SD","TN","TX","UT","VT",
    "VA","WA","WV","WI","WY",

]

MONTHS = [
    "01","02","03","04","05","06",
    "07","08","09","10","11","12",
]

YEARS = [
    "2018","2019","2020","2021","2022",
    "2023","2024","2025","2026","2027","2028",
]


#button1 = Button(root, text="Print", command=printName)
#button1 = Button(root, text="Print")
#button1.bind("<Button-1>", printName)
#button1.pack()

name = Label(root, text = "Full Name")
email = Label(root, text = "Email")
phone = Label(root, text = "Phone")
address = Label(root, text = "Address")
address2 = Label(root, text = "Address 2")
zip = Label(root, text = "Zip")
city = Label(root, text = "City")
profName = Label(root, text = "Profile Name")
cc = Label(root, text = "Credit Card")
cvv = Label(root, text = "CVV")


selectedState = StringVar(root)
selectedState.set(STATES[0])
stateMenu = OptionMenu(root, selectedState, *STATES)

selectedMonth = StringVar(root)
selectedMonth.set(MONTHS[0])
monthMenu = OptionMenu(root, selectedMonth, *MONTHS)

selectedYear = StringVar(root)
selectedYear.set(MONTHS[0])
yearMenu = OptionMenu(root, selectedYear, *YEARS)


entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
entry4 = Entry(root)
entry5 = Entry(root)
entry6 = Entry(root)
entry7 = Entry(root)
entry8 = Entry(root)
entry9 = Entry(root)
entry10 = Entry(root)


#sticky NSEW
name.grid(row=0, sticky=E)
email.grid(row=1, sticky=E)
phone.grid(row=2,sticky=E)
address.grid(row=3,sticky=E)
address2.grid(row=4,sticky=E)
zip.grid(row=6,sticky=E)
city.grid(row=5,sticky=E)
profName.grid(row=7,sticky=E)
cc.grid(row = 2, column = 2,sticky = E)
cvv.grid(row=3, column =2, sticky = E)
'''
entry1.grid(row=0, column=1)
entry1.insert(0, 'Full Name')
entry1.bind('<FocusIn>', on_entry_click)
entry1.bind('<FocusOut>', on_focusout)
entry1.config(fg = 'grey')

entry2.grid(row=1, column=1)
entry2.insert(0, 'Email')
entry2.bind('<FocusIn>', on_entry_click)
entry2.bind('<FocusOut>', on_focusout)
entry2.config(fg = 'grey')
'''
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry4.grid(row=3, column=1)
entry5.grid(row=4, column=1)
entry6.grid(row=6, column=1)
stateMenu.grid(row=8, columnspan=2)
entry7.grid(row=5,column=1)
entry8.grid(row=7,column=1)
entry9.grid(row=2, column=3)
entry10.grid(row=3, column=3)
monthMenu.grid(row=4, column=3)
yearMenu.grid(row=5, column=3)


button1 = Button(root, text="save", command=retrieveInput)
button1.grid(columnspan=2)
#this is what runs it
root.mainloop()

