# import the library
from appJar import gui
# create a GUI variable called app
app = gui()
# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "red")

def press(btn):
	print(btn)

app.addLabel("Menu", "Welcome to the Main Menu, select an option")
app.addButton("quit", press)

# start the GUI
app.go()
