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
    
    api.get_api_url()
    if "#comp" in window.location.href:
      alert('go')
      open_form('comp')
      return
    
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

  def form_show(self, **event_args):
    pass
    # url = self.call_js("get_url")
    # print('url', url, dict(url))
    