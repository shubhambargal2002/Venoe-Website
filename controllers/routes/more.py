from .more_model import Page
from fastapi import Request, Response

def handle_init_state(at: Page):
	"""
	The argument "at" is a the model that has initial values set from visual editor.
	Changing values in this "at" object will modify the intial state of the app.
	"""
	pass

def handle_page_request(at: Page, req: Request, res: Response, query: str):
	"""
	This function is called whenever a user loads this route in the browser.
	"""
	pass

def handle_event(at: Page, req: Request, res: Response):
	"""
	This function is called whenever an event is received. An event occurs when user
	performs some action such as click button.
	"""
	pass