from menu.stats.partyStats import *
from menu.stats.playerStats import *
from menu.stats.soloStats import *
from menu.screen import Screen


class Stats(Screen):
  def __init__(self, screenName, app):
    super().__init__(screenName, app)

    app.playerBtn_stats = 'black'
    app.soloBtn_stats = 'black'
    app.partyBtn_stats = 'black'
    app.backBtn = 'black'
    app.stats_fontSize = str(int(app.width/160))

  def clickHandler(self, app, event):
    clicks = [
      self.isClicked_solo,
      self.isClicked_party,
      self.isClicked_player,
      super().isClicked_back
    ]
    
    for click in clicks:
      if click(app,event): return

  def isClicked_solo(self, app, event):

    if (app.width/2*1.03 <= event.x and event.x <= app.width*.725 and
        app.height*.345 <= event.y and event.y <= app.height*.51):
        app.soloBtn_stats = 'red' if (app.soloBtn_stats == 'black') else 'black'
        app.currScreen='soloStats'
        return True
        
    return False

  def isClicked_party(self, app, event):

    if (app.width*.275 <= event.x and event.x <= app.width/2*.97 and
        app.height*.57 <= event.y and event.y <= app.height*.735):
        app.partyBtn_stats = 'red' if (app.partyBtn_stats == 'black') else 'black'
        app.currScreen='partyStats'
        return True
        
    return False

  def isClicked_player(self, app, event):

    if (app.width*.275 <= event.x and event.x <= app.width/2*.97 and
        app.height*.345 <= event.y and event.y <= app.height*.51):
        app.playerBtn_stats = 'red' if (app.playerBtn_stats == 'black') else 'black'
        app.currScreen='playerStats'
        return True

    return False


  def draw(self, app, canvas):
    app.fontSize = str(int(app.width/80))
    app.stats_fontSize = str(int(app.width/160))

    #player
    canvas.create_rectangle(app.width*.275,  app.height*.345, app.width/2*.97, app.height*.51, width=5, outline=app.playerBtn_stats)
    canvas.create_text((app.width*.275 + app.width/2*.97)/2, (app.height*.345 + app.height*.51)/2, text="Player", fill="black", font=('Helvetica ' + app.fontSize))

    #party
    canvas.create_rectangle(app.width*.275,  app.height*.57, app.width/2*.97, app.height*.735, width=5, outline=app.partyBtn_stats)
    canvas.create_text((app.width*.275 + app.width/2*.97)/2, (app.height*.57 + app.height*.735)/2, text="Party", fill="black", font=('Helvetica ' + app.fontSize))

    #solo
    canvas.create_rectangle(app.width/2*1.03, app.height*.345, app.width*.725, app.height*.51, width=5, outline=app.soloBtn_stats)
    canvas.create_text((app.width/2*1.03 +  app.width*.725)/2, (app.height*.345 + app.height*.51)/2, text="Solo", fill="black", font=('Helvetica ' + app.fontSize))
    
    #TBD
    canvas.create_rectangle(app.width/2*1.03, app.height*.57, app.width*.725, app.height*.735, width=5, outline='black')
    canvas.create_text((app.width/2*1.03 +  app.width*.725)/2, (app.height*.57 + app.height*.735)/2, text="", fill="black", font=('Helvetica ' + app.fontSize))

    #back btn
    super().drawBackBtn(app, canvas)


