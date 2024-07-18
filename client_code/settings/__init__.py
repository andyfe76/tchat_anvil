from ._anvil_designer import settingsTemplate
from anvil import *
from .. import api

class settings(settingsTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    status, body = api.get('settings')
    if status == 200:
      self.item = body['results'][0]

  def save_click(self, **event_args):
    print(self.item)
    status, body = api.put("settings", self.item)
    if status == 200:
      self.item = body['results'][0]
      self.refresh_data_bindings()
