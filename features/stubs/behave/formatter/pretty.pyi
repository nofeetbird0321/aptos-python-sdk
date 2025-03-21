from _typeshed import Incomplete
from behave.formatter.ansi_escapes import escapes as escapes
from behave.formatter.ansi_escapes import up as up
from behave.formatter.base import Formatter as Formatter
from behave.model_core import Status as Status
from behave.model_describe import escape_cell as escape_cell
from behave.model_describe import escape_triple_quotes as escape_triple_quotes
from behave.textutil import indent as indent

DEFAULT_WIDTH: int
DEFAULT_HEIGHT: int

def get_terminal_size(): ...

class MonochromeFormat:
    def text(self, text): ...

class ColorFormat:
    status: Incomplete
    def __init__(self, status) -> None: ...
    def text(self, text): ...

class PrettyFormatter(Formatter):
    name: str
    description: str
    stream: Incomplete
    monochrome: Incomplete
    show_source: Incomplete
    show_timings: Incomplete
    show_multiline: Incomplete
    formats: Incomplete
    display_width: Incomplete
    steps: Incomplete
    statement: Incomplete
    indentations: Incomplete
    step_lines: int
    def __init__(self, stream_opener, config) -> None: ...
    def reset(self) -> None: ...
    def uri(self, uri) -> None: ...
    def feature(self, feature) -> None: ...
    def background(self, background) -> None: ...
    def scenario(self, scenario) -> None: ...
    def replay(self) -> None: ...
    def step(self, step) -> None: ...
    def match(self, match) -> None: ...
    def result(self, step) -> None: ...
    def arg_format(self, key): ...
    def format(self, key): ...
    def eof(self) -> None: ...
    def table(self, table) -> None: ...
    def doc_string(self, doc_string) -> None: ...
    def color(self, cell, statuses, _color): ...
    def indented_text(self, text, proceed): ...
    def calculate_location_indentations(self) -> None: ...
    def print_statement(self) -> None: ...
    def print_steps(self) -> None: ...
    def print_step(self, status, arguments, location, proceed) -> None: ...
    def print_tags(self, tags, indentation) -> None: ...
    def print_comments(self, comments, indentation) -> None: ...
    def print_description(
        self, description, indentation, newline: bool = True
    ) -> None: ...
