from ._anvil_designer import mainTemplate
from anvil import *
from .. import api
from ..data import data
from ..settings import settings

class main(mainTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    api.main_form = self
    
    api.get_api_url()
    
    self.page2form = {
      "data": data,
      "settings": settings()
    }

  def menu_click(self, **kw):
    self.content_panel.clear()
    for comp in self.navbar_links.get_components():
      comp.bold = False

    sender = kw['sender']
    sender.bold = True
    page = kw['sender'].tag
    form = self.page2form[page]
    self.content_panel.add_component(form())
    
    