from ._anvil_designer import qaTemplate
from anvil import *
from .. import api
from .query import query

class qa(qaTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.refresh()

  def refresh(self, **kw):
    status, body = api.get("qa")
    if status == 200:
      self.data_panel.items = body['results']
        
  def ask_click(self, **event_args):
    alert(query(), large=True, buttons=[], dismissible=False)
    self.refresh()
