from menu.screen import Screen


class SoloStats(Screen):
  def __init__(self, screenName, app):
    pass
  


  def clickHandler(self, app, event):
    clicks = [
      super().isClicked_back
    ]

    for click in clicks:
      if ((click == super().isClicked_back) and (click(app,event,'stats'))): return
      elif click(app,event): return


  def draw(self, app, canvas):
    super().drawBackBtn(app, canvas)