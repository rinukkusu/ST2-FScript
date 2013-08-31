import sublime, sublime_plugin
import re


class SyntaxCheck(sublime_plugin.EventListener):
	def on_pre_save(self, view):
		if "Future" in view.settings().get('syntax'):
			if view.settings().get('SyntaxCheckOnSave'):
				# print status in stdout (debug only)
				print "is Future Syntax: true"

				# TODO: check last char (;)
				lines = re.split("\n", view.substr(sublime.Region(0, view.size())))
				print "lines:", len(lines)

				errors = "";

				cl = 0 # current line
				while cl < len(lines):
					line = lines[cl]
					last_ch = lines[cl][len(lines[cl])-1:]

					if last_ch not in ['{', ';']:
						errors += "missing semicolon on line " + str(cl+1) + "\r\n"

					cl += 1

				if len(errors) > 0: # display errors
					sublime.error_message(errors)
