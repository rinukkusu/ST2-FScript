import sublime, sublime_plugin
import re


class SetFileSyntax(sublime_plugin.EventListener):
	def on_load(self, view):
		# prevent error message
		view.settings().set('detect_slow_plugins', False)

		r = view.find(r'SCRIPT\:', 0)
		if r is not None:
			view.set_syntax_file('Packages/Future Script/Future.tmLanguage')
			view.set_encoding('Western (Windows 1252)')

		# enable detection again
		view.settings().set('detect_slow_plugins', True)