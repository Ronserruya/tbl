import os
import csv

import click
import rapidtables

from typing import List, Optional


def find_max_column_width(headers: List[str]) -> int:
    try:
        console_width = os.get_terminal_size(0).columns
    except OSError:  # get_terminal_size does not work inside of pycharm, so this is just for developing
        console_width = 173

    keys_count = len(headers)
    len_separator = 3  # space before, after, and one |
    # The biggest size that can fit all keys + all separators
    max_width = (console_width - 1 - keys_count * len_separator) / keys_count
    return int(max_width)


def print_tbl(file: str, explicit_headers: Optional[List[str]], select: Optional[List[str]], format: str):
    try:
        with open(file) as file:
            reader = csv.reader(file)
            try:
                headers = explicit_headers or next(reader)
            except StopIteration:
                raise click.UsageError("csv file is empty")

            if len(set(headers)) != len(headers):
                raise click.UsageError("tbl does not support duplicate headers")

            if select is not None:
                # Verify that at least some of the selected headers are present
                if len(set(headers).intersection(set(select))) == 0:
                    raise click.UsageError("The selected headers dont match any of the headers found. ({})\n"
                                           "Hint: Headers are case sensitive"
                                           .format(headers))

            selected_headers = select or headers

            # Create a list of dictionaries with the data
            table = [{h: v for h, v in zip(headers, row)
                      if h in selected_headers}
                     for row in reader]
    except FileNotFoundError:
        raise click.FileError(file, "Not found")

    rapidtables.print_table(table,
                            tablefmt=format,
                            wrap_text=True,
                            max_column_width=find_max_column_width(selected_headers),
                            allow_multiline=True,
                            align=rapidtables.ALIGN_LEFT)
