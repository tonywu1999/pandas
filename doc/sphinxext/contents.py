"""Sphinx extension for verifying titles following capitalization convention

Usage::

   .. contents:: Table of contents:

This will be replaced with Hello World
"""
from docutils import nodes
from docutils.parsers.rst import Directive


class HelloWorld(Directive):

    def run(self):
        z = 0

        if z == 0:
            self.warning("build failed due to incorrect capitalization")
            
        paragraph_node = nodes.paragraph(text='Hello World!')
        return [paragraph_node]


def setup(app):
    app.add_directive("contents", HelloWorld)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
