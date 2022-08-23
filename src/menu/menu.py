

from menu.screen import Screen
from menu.title import Title
from menu.tutorial import Tutorial
from menu.stats.stats import Stats
from menu.stats.partyStats import PartyStats
from menu.stats.playerStats import PlayerStats
from menu.stats.soloStats import SoloStats

class Menu(object):
  def __init__(self, app):

    app.currScreen = 'title'
    self.titleScreen = Title('title', app)
    self.statScreen = Stats('stats', app)
    self.tutorialScreen = Tutorial('stats', app)
    self.playerStatScreen = PlayerStats('stats', app)
    self.soloStatScreen = SoloStats('stats', app)
    self.partyStatScreen = PartyStats('stats', app)

  def clickHandler(self, app, event):
    match app.currScreen:
      case 'title':
        self.titleScreen.clickHandler(app,event)
      case 'stats':
        self.statScreen.clickHandler(app, event)
      case 'tutorial':
        self.tutorialScreen.clickHandler(app, event)
      case 'partyStats':
        self.partyStatScreen.clickHandler(app, event)
      case 'playerStats':
        self.playerStatScreen.clickHandler(app, event)
      case 'soloStats':
        self.soloStatScreen.clickHandler(app, event)

    return app

  def drawHandler(self, app, canvas):
    match app.currScreen:
      case 'title':
        self.titleScreen.draw(app,canvas)
      case 'stats':
        self.statScreen.draw(app, canvas)
      case 'tutorial':
        self.tutorialScreen.draw(app, canvas)
      case 'partyStats':
        self.partyStatScreen.draw(app, canvas)
      case 'playerStats':
        self.playerStatScreen.draw(app, canvas)
      case 'soloStats':
        self.soloStatScreen.draw(app, canvas)

    return app



