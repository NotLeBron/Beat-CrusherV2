from menu.stats.stats import *

from menu.screen import *

class Title(Screen):
  def __init__(self, screenName, app):
    super().__init__(screenName, app)

    app.soloBtn_color = 'black'
    app.tutBtn_color = 'black'
    app.partyBtn_color = 'black'
    app.statBtn_color = 'black'

    app.settingBtn_color = 'black'
    app.credBtn_color = 'black'

    app.fontSize = str(int(app.width/80))

    app.currScreen = 'title'
  

  def clickHandler(self, app, event):
    clicks = [
      self.isClicked_settings,
      self.isClicked_credits,
      self.isClicked_solo,
      self.isClicked_tut,
      self.isClicked_party,
      self.isClicked_stats
    ]
    
    for click in clicks:
      if click(app,event): 
        return


  def isClicked_settings(self, app, event):

    if (0 <= event.x and event.x <= app.width/2 and
        app.height*.9 <= event.y and event.y <= app.height):
        app.settingBtn_color = 'red' if (app.settingBtn_color == 'black') else 'black'
        return True
        
    return False


  def isClicked_credits(self, app, event):

    if (app.width/2 <= event.x and event.x <= app.width and
        app.height*.9 <= event.y and event.y <= app.height):
        app.credBtn_color = 'red' if (app.credBtn_color == 'black') else 'black'
        return True
        
    return False


  def isClicked_solo(self, app, event):

    if (app.width*.275 <= event.x and event.x <= app.width/2*.97 and
        app.height*.345 <= event.y and event.y <= app.height*.51):
        app.soloBtn_color = 'red' if (app.soloBtn_color == 'black') else 'black'
        return True
        
    return False


  def isClicked_tut(self, app, event):

    if (app.width*.32 <= event.x and event.x <= app.width/2*.97 and
        app.height*.54 <= event.y and event.y <= app.height*.652):
        app.tutBtn_color = 'red' if (app.tutBtn_color == 'black') else 'black'
        app.currScreen = 'tutorial'
        return True
        
    return False


  def isClicked_party(self, app, event):

    if (app.width/2*1.03 <= event.x and event.x <= app.width*.725 and
        app.height*.345 <= event.y and event.y <= app.height*.51):
        app.partyBtn_color = 'red' if (app.partyBtn_color == 'black') else 'black'
        return True
        
    return False


  def isClicked_stats(self, app, event):

    if (app.width/2*1.03 <= event.x and event.x <= app.width*.68 and
        app.height*.54 <= event.y and event.y <= app.height*.652):
        app.currScreen = 'stats'
        return True
    return False

  def draw(self, app, canvas):
    app.fontSize = str(int(app.width/80))

    #setting
    canvas.create_rectangle(0, app.height*.9, app.width/2, app.height, width=5, outline=app.settingBtn_color)
    canvas.create_text((app.width)/4, (app.height + app.height*.9)/2, text="Settings", fill="black", font=('Helvetica ' + app.fontSize))

    #credits
    canvas.create_rectangle(app.width/2, app.height*.9, app.width, app.height, width=5, outline=app.credBtn_color)
    canvas.create_text((app.width)*.75, (app.height + app.height*.9)/2, text="Credits", fill="black", font=('Helvetica ' + app.fontSize))

    #solo btn
    canvas.create_rectangle(app.width*.275,  app.height*.345, app.width/2*.97, app.height*.51, width=5, outline=app.soloBtn_color)
    canvas.create_text((app.width*.275 + app.width/2*.97)/2, (app.height*.345 + app.height*.51)/2, text="Solo", fill="black", font=('Helvetica ' + app.fontSize))

    #how to play
    canvas.create_rectangle(app.width*.32, app.height*.54, app.width/2*.97, app.height*.652, width=5, outline=app.tutBtn_color)
    canvas.create_text((app.width*.32 + app.width/2*.97)/2, (app.height*.54 + app.height*.652)/2, text="Tutorial", fill="black", font=('Helvetica ' + app.fontSize))

    #party btn
    canvas.create_rectangle(app.width/2*1.03, app.height*.345, app.width*.725, app.height*.51, width=5, outline=app.partyBtn_color)
    canvas.create_text((app.width/2*1.03 +  app.width*.725)/2, (app.height*.345 + app.height*.51)/2, text="Party", fill="black", font=('Helvetica ' + app.fontSize))

    #stats
    canvas.create_rectangle(app.width/2*1.03, app.height*.54, app.width*.68, app.height*.652, width=5, outline=app.statBtn_color)
    canvas.create_text((app.width/2*1.03 + app.width*.68)/2, (app.height*.54 + app.height*.652)/2, text="Stats", fill="black", font=('Helvetica ' + app.fontSize))
