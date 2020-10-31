import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Page load')
    parser.add_argument(
        '-L', '--log',
        default='ERROR', help="Set level of the log's messages"
        )
    parser.add_argument(
        '-o', '--output',
        default='.', help='path to save a file'
        )
    parser.add_argument(
        'page_adress',
        help='adress of page for download'
        )
    return parser
