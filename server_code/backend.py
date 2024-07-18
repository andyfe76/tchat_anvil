import anvil.server
import anvil.secrets

@anvil.server.callable
def get_api_url():
  return anvil.secrets.get_secret("api_url")

