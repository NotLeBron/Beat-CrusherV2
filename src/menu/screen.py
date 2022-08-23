

from abc import ABC, abstractmethod


class Screen(ABC):
  def __init__(self, screenName, app):
    pass
  

  @abstractmethod
  def clickHandler(self, app, event):
    pass

  @abstractmethod
  def draw(self, app, canvas):
    pass


  def isClicked_back(self, app, event, screen='title'):

    if (app.width*.95 <= event.x and event.x <= app.width*.99 and
        app.height*.02 <= event.y and event.y <= app.height*.05):
        app.backBtn = 'red' if (app.backBtn == 'black') else 'black'
        app.currScreen = screen
        return True

    return False


  def drawBackBtn(self, app, canvas):
    canvas.create_rectangle(app.width*.95, app.height*.02, app.width*.99, app.height*.05, outline='black')
    canvas.create_text((app.width*.95 + app.width*.99)/2, (app.height*.02 + app.height*.05)/2, text="Back", fill="black", font=('Helvetica ' + app.stats_fontSize))


