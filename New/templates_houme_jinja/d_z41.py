from jinja2 import Environment, FileSystemLoader

text = """Домашнее задание выполнено!!!"""

file_loader = FileSystemLoader('template')
env = Environment(loader = file_loader)
tm=env.get_template('main.html')
msg = tm.render(tx=text, title = "Домашнее задание", h1="Страница с домашнем заданием;-)")
print(msg)