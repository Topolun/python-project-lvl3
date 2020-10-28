import logging
from page_loader import engine
from page_loader import cli
import argparse


def main():
    args = cli.get_args().parse_args()
    engine.run(args.page_adress, args.output)
    logging.info('Work is finished')


if __name__ == '__main__':
    main()
