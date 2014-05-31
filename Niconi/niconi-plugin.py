import sublime, sublime_plugin

class NiconiCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		current_point = self.view.sel()[0].begin()
		end_point = self._get_end_point(current_point)
		start_point = self._get_start_point(current_point)

		target_region = sublime.Region(start_point, end_point)
		text = sublime.get_clipboard()

		self.view.replace(edit, target_region, text)

	def _get_start_point(self, current_point):
		for i in list(range(0, current_point))[::-1]:
			if self.view.substr(i) == '>':
				return i + 1

		return 0

	def _get_end_point(self, current_point):
		file_end_point = self.view.size()
		end_point = file_end_point

		for i in range(current_point, file_end_point):
			c = self.view.substr(i)
			if c == '<':
				return i

		return end_point
