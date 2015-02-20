import sublime
import sublime_plugin
import re

class get_scripts(sublime_plugin.TextCommand):
	"""lists all scripts in the document with fast switch"""
	def run(self, edit):
		self.scripts = self.list_all_scripts()
		#sublime.error_message('\n'.join(scripts))
		if self.scripts:
			self.view.window().show_quick_panel(self.scripts, self.on_select)

	def on_select(self, index):
		chosenscript = self.scripts[index]
		m = re.search(r'(\d+)', chosenscript)
		if m:
			scriptnr = m.group(1)
			r = self.view.find(r'SCRIPT\:' + scriptnr + r',.*', 0)
			if r is not None:
				self.view.sel().add(r)
				self.view.show(r, True)

	def list_all_scripts(self):
		messages = []
		regions = []

		single_region = self.view.find(r'SCRIPT\:.*',0)
		while single_region:
			regions.append(single_region)
			single_region = self.view.find(r'SCRIPT\:.*', single_region.end())
		
		if regions is not None:
			for reg in regions:
				linetext = self.view.substr(reg)
				#sublime.error_message(linetext)
				m = re.search(r'SCRIPT\:(\d+),(.+?),|SCRIPT\:(\d+),(.*)', linetext)
				if m:
					if m.group(1):
						message = m.group(1) + ' - ' + m.group(2)
					else:
						message = m.group(3) + ' - ' + m.group(4)
					messages.append(message)

		return messages

