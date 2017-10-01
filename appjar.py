# import the library
from appJar import gui
# create a GUI variable called app
app = gui()
# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "red")

app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")

def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)
app.addButtons(["Submit", "Cancel"], press)

app.startSubWindow("Menu")
app.addLabel("Menu", "Welcome to the Main Menu, select an option")
app.start.addButton("quit", press)
app.start.stopSubWindow()

# start the GUI
app.go()
