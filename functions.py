from appJar import gui
from gui import Gui





class Functions:
    def __init__(self, app=gui()):
        self.app = app
        app.setGeometry("500x400")
        app.setTitle("Connection to Raspberry Py")
        app.startLabelFrame("Connect to Raspberry Py")
        app.addEntry("ip", 0,1)
        app.addSecretEntry("Password", 0,2)
        app.stopLabelFrame()
        app.setEntryDefault("ip", "Ip")
        app.setEntryDefault("Password", "Password")
        def press(btn):
            ip = str(app.getEntry("ip"))
            passw = str(app.getEntry("Password"))
            if btn=="Close":
                app.stop()
            if btn == "Connect":
                print(ip)
                print(passw)
                if passw == "zdr" and ip=="zdr":
                    app.stop()
                    gui = Gui()
                else:
                    app.errorBox("Wrong password or ip", "Wrong password or ip")
        app.addButtons(["Connect", "Close"], press)

        app.go()
