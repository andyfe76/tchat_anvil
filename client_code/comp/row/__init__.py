from ._anvil_designer import rowTemplate
from anvil import *
from ... import api

class row(rowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def source_lnk_click(self, **event_args):
    status, body = api.get(f"data/{self.item['uuid']}")
    if status == 200:
      alert(body['results'][0]['text'], large=True)
