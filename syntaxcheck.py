import sublime, sublime_plugin

class SyntaxCheck(sublime_plugin.EventListener):
	def on_modified(self, view):
		if "Future" in view.settings().get('syntax'):
			# print status in stdout (debug only)
			print "is Future Syntax: true"

			# TODO: check last char (;)

