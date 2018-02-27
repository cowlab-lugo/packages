extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'iscowalive'
copyright = u'2018, cowlab, oscarmlage'

version = '0.1'
release = '0.1'

exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'iscowalive'
epub_author = u'oscarmlage'
epub_publisher = u'oscarmlage'
epub_copyright = u'2018, cowlab, oscarmlage'

epub_exclude_files = ['search.html']
intersphinx_mapping = {'http://docs.python.org/': None}
