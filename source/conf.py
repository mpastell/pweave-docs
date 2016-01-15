import sys, os

extensions = ['sphinx.ext.todo', 'sphinx.ext.pngmath', 'sphinx.ext.autodoc', 'sphinx.ext.viewcode']

templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'
source_encoding = 'utf-8'
master_doc = 'index'

# General information about the project.
project = u'Pweave - reports from data using Python'
copyright = u'Matti Pastell. 2010 - '

# The short X.Y version.
version = '0.23'
# The full version, including alpha/beta/rc tags.
release = '0.23.2'

# List of documents that shouldn't be included in the build.
unused_docs = ['ma', 'ma2']

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

html_style = '/default.css'

# "<project> v<release> documentation".
html_title = "Pweave - reports from data with Python"

# Different theme for index
#html_additional_pages = {'index' : 'customindex.html'}

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'Pweave-literateprogrammingwithPythondoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = '12pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('docs', 'Pweave-docs.tex', u'Pweave - Reports from Data Using Python.',
  u'Matti Pastell', 'howto'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False
