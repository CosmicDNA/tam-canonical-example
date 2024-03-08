# Full text in example/simple_app.py
import os, re
from aiohttp import web
from aiohttp_tokenauth import token_auth_middleware
from aiohttp_middlewares import cors_middleware
from aiohttp_middlewares.cors import DEFAULT_ALLOW_HEADERS, DEFAULT_ALLOW_METHODS

class WebApp:
	app: web.Application
	secret: str
	def __init__(self, secret) -> None:
		self.app = web.Application(middlewares=[
			cors_middleware(
				origins=[re.compile(r"^https?\:\/\/localhost?(:[0-9]*)?")],
				allow_methods=DEFAULT_ALLOW_METHODS,
				allow_headers=DEFAULT_ALLOW_HEADERS
			),
			token_auth_middleware(user_loader=self.app_loader, auth_scheme='Token', request_property='app')
		])
		self.app.router.add_route("GET", "/protocol", self.example_path)
		self.secret = secret

	async def example_path(self, request):
		return web.json_response(request['app'])

	async def app_loader(self, token: str):
		"""Checks that token is valid

		It's the callback that will get the token from "Authorization" header.
		It can check that token is exist in a database or some another place.

		Args:
				token (str): A token from "Authorization" http header.

		Returns:
				Dict or something else. If the callback returns None then
				the aiohttp.web.HTTPForbidden will be raised.
		"""
		app = None
		if token == self.secret:
				app = {'status': 'connected'}
		return app

	def start(self):
		web.run_app(self.app)


if __name__ == '__main__':
	webApp = WebApp(os.getenv('SECRET'))
	webApp.start()