# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sphinx_rtd_theme


project = '一起探索Python编程'
copyright = '2023, Mr-Huang'
author = 'Mr-Huang'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []
#extensions = ['recommonmark','sphinx_markdown_tables'] 


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'zh_CN'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
#html_theme ='sphinx_materialdesign_theme'
html_static_path = ['_static']
html_logo = '_static/logo.png'

html_sidebars = {'**': ['localtoc.html', 'sourcelink.html', 'searchbox.html']}