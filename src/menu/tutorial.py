from menu.screen import Screen


class Tutorial(Screen):
  def __init__(self, screenName, app):
    pass


  def isClicked_back(self, app, event):
    if (app.width*.95 <= event.x and event.x <= app.width*.99 and
        app.height*.02 <= event.y and event.y <= app.height*.05):
        app.backBtn = 'red' if (app.backBtn == 'black') else 'black'
        app.currScreen = 'title'
        return True
  


  def clickHandler(self, app, event):
    clicks = [
      super().isClicked_back
    ]

    for click in clicks:
      if click(app, event): return


  def draw(self, app, canvas):
    super().drawBackBtn(app, canvas)