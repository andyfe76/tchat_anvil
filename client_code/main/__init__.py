from ._anvil_designer import mainTemplate
from anvil import *
from .. import api
from ..data import data
from ..settings import settings
from ..qa import qa
from anvil.js import window


class main(mainTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    api.main_form = self
    queryString = window.location
    for attr in dir(queryString):
      print(attr, getattr(queryString, attr))
    #.search
   # urlParams = URLSearchParams(queryString)
    #print('!!', dir(queryString), queryString)
    
    api.get_api_url()
    
    self.page2form = {
      "data": data,
      "settings": settings,
      "qa": qa
    }
    self.page2instance = {}

  def menu_click(self, **kw):
    self.content_panel.clear()
    for comp in self.navbar_links.get_components():
      comp.bold = False

    sender = kw['sender']
    sender.bold = True
    page = kw['sender'].tag
    if page not in self.page2instance:
      form = self.page2form[page]
      self.page2instance[page] = form()

    self.content_panel.add_component(self.page2instance[page])
    