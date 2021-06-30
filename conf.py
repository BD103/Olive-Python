from better import better_theme_path


# Project Information
project = "Olive Python"
copyright = "2021, BD103"
author = "BD103"
release = "1.0.0"


# General Configuration
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
needs_sphinx = "4.0"
pygments_style = None


# HTML Options
html_theme = "better"
html_theme_path = [better_theme_path]
html_static_path = ["_static"]
html_baseurl = "https://olive-python.github.io"
html_permalinks_icon = "#"


# Extensions
extensions = ["sphinx.ext.githubpages", "sphinx.ext.todo", "sphinx.ext.todo"]

todo_include_todos = True
todo_link_only = True