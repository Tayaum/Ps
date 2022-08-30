try:
	import re
	import basic
	from rich.console import Console

	print = Console().print
	def rich_color(text):
		if not str(basic.Number('0'))[0] == str(text):
			replace_text = {'"': '[green]"[/]'}
			text = repr(text)
			for item in replace_text:
				text = text.replace(item, replace_text[item])
			for item in re.findall('"(.*?)"', text):
				text = text.replace(item, '[green]' + item + '[/]')
			return text
		else:
			return '[black]Null'
	while True:
		print('[blue]>>> ', end='')
		text = input('')
		if text.strip() == "": continue
		result, error = basic.run("[blue]" + '<stdin>' + '[red]', text)

		if error:
			print("[red]" + error.as_string(), highlight=False)
		elif result:
			if len(result.elements) == 1:
				result = rich_color(result.elements[0])
				print(result, highlight=False)
			else:
				result = rich_color(result)
				print(result, highlight=False)
except KeyboardInterrupt:
    exit(2)