# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3

"""This module exports the Gfortran plugin class."""

# Since SublimeLinter is loaded after SublimeFortran, we need to manually import Linter
from SublimeLinter.lint import Linter, util


class Gfortran(Linter):
    """Provides an interface to gfortran."""
    error_stream = util.STREAM_BOTH
    cmd = 'gfortran -cpp -fsyntax-only -Wall ${file}'
    multiline = True
    defaults = {
        'selector': 'source.modern-fortran keyword.control.module.fortran'}
    regex = (
        # filename:line:col: is common for multiline and single line warnings
        r'^[^:]*:(?P<line>\d+)[:.](?P<col>\d+):'
        # Then we either have a space or (a newline, a newline, some source code, a newline, a col number, a newline)
        r'(?:\s|$\r?\n^$\r?\n^.*$\r?\n^\s*\d$\r?\n)'
        # Finally we have (Error|Warning): message to the end of the line
        r'(?:(?P<error>Error|Fatal\sError)|(?P<warning>Warning)): (?P<message>.*$)'
    )
    on_stderr = True