from ._anvil_designer import rowTemplate
from anvil import *
from .... import api

class row(rowTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def show_link_click(self, **event_args):
    if self.show_link.text == "Show":
      status, body = api.get(f"data/{self.item['uuid']}")
      if status == 200:
        self.show_link.text = "Hide"
        self.text.text = body['results'][0]['text']
        self.text.visible = True
    else:
      self.show_link.text = "Show"
      self.text.visible = False
