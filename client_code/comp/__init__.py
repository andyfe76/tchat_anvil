from ._anvil_designer import compTemplate
from anvil import *
from .. import api

class comp(compTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    api.get_api_url()

  def ask_click(self, **event_args):
    status, body = api.post(f"qa?query={self.question.text}")
    if status == 200:
      self.response = body['results'][0]
      self.answer.text = self.response['response']
      self.answer.visible = True
      self.sources_grid.visible = True
      self.sources_panel.items = self.response['sources']
