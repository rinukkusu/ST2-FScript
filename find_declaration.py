import sublime, sublime_plugin
import re

class find_declaration(sublime_plugin.TextCommand):
	def run(self, edit):
		if "Future" in self.view.settings().get('syntax'):
			pos = self.view.sel()[0]

			if pos.end() == pos.begin():
				pos = self.view.word(self.view.sel()[0])

			text = self.view.substr(pos)

			linepos = self.view.line(pos)
			wholeline = self.view.substr(linepos)

			scrollreg = sublime.Region(0,0);
			bFound = False

			if wholeline.find('Call:' + text) > 0:
				r = self.view.find_all('FUNCTION\:\s(int|void|BOOL|double|CString|CTable|CDateTime|CMoney)\s(' + text + ')')
				if len(r) > 0:
					scrollreg = r[0]
					bFound = True
			else:
				r = self.view.find_all('(int|BOOL|double|CString|CTable|CDateTime|CMoney)\s(' + text + ').*;')
				if len(r) > 0:
					for reg in r:
						if reg.end() < pos.begin():
							scrollreg = reg
							bFound = True

			if bFound == True:
				self.view.sel().add(scrollreg)
				self.view.show(scrollreg, True)
			else:
				sublime.error_message('Es konnte keine Deklaration fuer "' + text + '" gefunden werden.')
		else:
			sublime.error_message('Keine FutureScript-Datei.')

class goto_script(sublime_plugin.TextCommand):
	def run(self, edit):
		if "Future" in self.view.settings().get('syntax'):
			pos = self.view.sel()[0]

			if pos.end() == pos.begin():
				pos = self.view.word(self.view.sel()[0])

			text = self.view.substr(pos)
			r = self.view.find(r'SCRIPT\:' + text + '.*', 0)
			if r is not None:
				self.view.sel().add(r)
				self.view.show(r, True)
			else:
				sublime.error_message('Definition nicht in diesem Script.')
