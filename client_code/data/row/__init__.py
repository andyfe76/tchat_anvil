from ._anvil_designer import rowTemplate
from anvil import *
from datetime import datetime
from ... import api

class row(rowTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.added_at.text = datetime.fromtimestamp(self.item['added_at']).strftime("%m/%d/%Y")
    self.text.text = self.item['text']

  def edit_click(self, **event_args):
    if self.edit.icon == "fa:pencil":
      self.edit.icon = "fa:check"
      self.edit.foreground = "green"
      self.text.enabled = True
    else:
      self.item['text'] = self.text.text
      embed = confirm("Run embedding on the document?")
      status, body = api.put(f"data/{self.item['uuid']}?embed={embed}", self.item)
      if status == 200:
        self.item = body['results'][0]
      self.edit.icon = "fa:pencil"
      self.edit.foreground = ""
      self.text.enabled = False

  def delete_click(self, **event_args):
    if confirm("Are you sure?"):
      status, body = api.delete(f"data/{self.item['uuid']}")
      if status == 200:
        self.remove_from_parent()

  def embed_run_click(self, **event_args):
    status, body = api.post(f"data/{self.item['uuid']}/embed")
    if status == 200:
      self.item = body['results'][0]
      self.refresh_data_bindings()
