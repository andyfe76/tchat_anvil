from ._anvil_designer import queryTemplate
from anvil import *
from ... import api

class query(queryTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.response = None

  def ask_click(self, **event_args):
    status, body = api.post(f"qa?query={self.question.text}")
    if status == 200:
      self.response = body['results'][0]
      self.answer.text = self.response['response']
      self.sources_panel.items = self.response['sources']
      self.answer_lbl.visible = True
      self.answer.visible = True
      self.sources_lbl.visible = True
      self.sources_grid.visible = True

  def close_click(self, **event_args):
    self.raise_event("x-close-alert", value=self.response)
