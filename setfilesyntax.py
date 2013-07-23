import sublime, sublime_plugin
import re


class SetFileSyntax(sublime_plugin.EventListener):
	def on_load(self, view):
		r = view.find_all(r'SCRIPT\:')
		if len(r) > 0:
			view.settings().set('detect_slow_plugins', False)
			view.set_syntax_file('Packages/Future Script/Future.tmLanguage')
			view.set_encoding('Western (Windows 1252)')