from ._anvil_designer import dataTemplate
from anvil import *
from .. import api

class data(dataTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.refresh()

  def refresh(self, **kw):
    status, body = api.get("data")
    if status == 200:
      self.data_panel.items = body['results']

  def upload_data_change(self, files, **event_args):
    self.upload_data.clear()
    embed = confirm("Run embedding on the documents?")
    
    with Notification(f"Uploading {len(files)} files"):
      items = self.data_panel.items
      count = 0
      for file in files:
        status, body = api.upload(f"data/upload?embed={embed}", file.get_bytes(), file.name, file.content_type)
        if status == 200:
          items.insert(0, body['results'][0])
        count += 1
        print(count, len(files))
    self.data_panel.items = items

