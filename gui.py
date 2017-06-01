from appJar import gui





class Gui:
    def __init__(self, app=gui()):
        self.app = app
        #app.setBgImage("bgimg.jpg")
        font = ("Comic Sans", "20", "underline")
        app.setFont(30, font=font)
        app.setTitle("Raspberry py project")
        app.setGeometry(1398, 652)
        app.setResizable(canResize=True)
        app.startLabelFrame("",0,1)


        app.addLabel('title', "School Raspberry Py project",0,0)
        #app.addButton("Connect",func.openconnectionwindow)
        #app.addButton("Close Connection",func.close)
        app.stopLabelFrame()
        app.setLabelBg('title', "gray")
        app.startLabelFrame("Raspberry.py information",1,1)
        app.addEmptyLabel('inf1',0,0)
        app.stopLabelFrame()
        app.go()
