import anvil.http
import anvil.server
from anvil import Notification
import json

headers={
  "Content-Type":"application/json"
}

api_url = None
main_form = None

def get_api_url():
  global api_url
  api_url = anvil.server.call('get_api_url')


def _request(url, method="GET", data=None, show_indicator=True, show_notification=True):
  if data and type(data) == str: data = json.dumps(data)
  status = 200
  try:
    body = anvil.http.request(url=f"{api_url}/{url}",
      method=method,
      headers= headers, 
      data=data,
      json=True
    )
  except anvil.http.HttpError as e:
    status = e.status
    body = {"error": f"{e}: {e.content}"}
    if status == 0:
      body = {"error": "Eroare conexiune server"}
  except Exception as e:
    status = 500
    body = {"error": str(e)}
  
  if status != 200:
    print(status, body)
    if show_notification:
      Notification(f"Error {status}: {body['error']}", timeout=3).show()
    
  return status, body

def request(url, method="GET", data=None, show_indicator=True, show_notification=True):
  if show_indicator:
    status, body = _request(url, method=method, data=data, show_notification=show_notification)
  else:
    with anvil.server.no_loading_indicator:
      status, body = _request(url, method=method, data=data, show_notification=show_notification)
  return status, body

def get(url, show_indicator=True, show_notification=True):
  status, body = request(url, "GET", show_indicator=show_indicator, show_notification=show_notification)
  return status, body

def post(url, data={}, show_indicator=True, show_notification=True):
  status, body = request(url, "POST", data, show_indicator=show_indicator, show_notification=show_notification)
  return status, body

def put(url, data=None, show_indicator=True, show_notification=True):
  status, body = request(url=url, method="PUT", data=data, show_indicator=show_indicator, show_notification=show_notification)
  return status, body

def delete(url, show_indicator=True, show_notification=True):
  status, body = request(url, "DELETE", show_indicator=show_indicator, show_notification=show_notification)
  return status, body

def upload(url, file, file_name, file_content_type, show_notification=True):
  anvil.js.call_js('setLoading', True)
  global user
  upload_headers = {}
  try:
    response = main_form.call_js('upload', f"{api_url}/{url}", upload_headers, file, file_name, file_content_type)
    status = response.status
  except Exception as e:
    print(1)
    status = 500
    body = {"error": f"{str(e)}: {response.body}"}
    
  
  if status != 500:
    try:
      body = None
      body = response.body.getReader().read().value.decode('utf-8')#.replace("'", '"')
      body = json.loads(body)
    except Exception as e:
      status = 500
      body = {"error": f"{str(e)}: {response.body}"}
  
  if status != 200:
    print(body)
    if body.get('details'): 
      body['error'] = body['details']
    if show_notification:
      Notification(f"Error {status}: {body['error']}", timeout=5).show()
    
  anvil.js.call_js('setLoading', False)
  return status, body
