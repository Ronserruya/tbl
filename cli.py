import click
from typing import List, Optional

from main import print_tbl


def validate_headers(ctx, param, value: str) -> Optional[List[str]]:
    if value is None:
        return value
    if len(value) in [0, 1]:
        raise click.BadParameter("Cannot be empty")
    separator = value[0]
    headers = value.split(separator)[1:]
    # Check for stuff like @a@@c
    if '' in headers:
        raise click.BadParameter("Cannot be empty")
    if len(headers) != len(set(headers)):
        raise click.BadParameter("tbl does not support duplicate headers")
    return headers


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(context_settings=CONTEXT_SETTINGS)  # Add -h for help
@click.argument('file', default='example.csv')
@click.option('--headers', help='Explicitly state the headers\n'  # \n\b is needed to leave an empty line
                                'Use any character as a separator, e.g #name#age#job.\n\b',
              default=None, callback=validate_headers)
@click.option('--select', help='List of headers, only those columns will be printed.\n'
                               'Use any character as a separator, e.g #name#age.\n\b',
              default=None, callback=validate_headers)
@click.option('--format', type=click.Choice(['rstgrid', 'rst', 'md', 'simple']),
              default='rstgrid', show_default=True, help='What format to use when printing\n\b')
def main(file, headers, select, format):
    """Prettifies and prints FILE."""
    print_tbl(file, headers, select, format)


main()