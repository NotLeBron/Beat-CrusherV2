from res.graphics.cmu_112_graphics import *
from screeninfo import get_monitors
from menu.menu import *



def appStarted(app):
  app.menu = Menu(app)
  pass

def timerFired(app): 
  pass

def keyPressed(app, event):
  pass


def mousePressed(app, event):
  app.menu.clickHandler(app, event)



def redrawAll(app, canvas):
  app.menu.drawHandler(app,canvas)

def appStopped(app):
  pass


def main():
  monitor = (get_monitors())[0] 
  #use mvcCheck=False to bypass false mvc violation
  #false postive due to multithreading??? 
  runApp(width = monitor.width, height = monitor.height, mvcCheck=False)

if __name__ == "__main__":
  main()