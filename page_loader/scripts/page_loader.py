import logging
from page_loader import engine
from page_loader import cli
from page_loader import logging as log
from page_loader.errors import KnownError
import sys


def main():
    try:
        args = cli.get_args().parse_args()
        log.set_log(args.log)
        engine.run(args.page_adress, args.output)
    except KnownError as err:
        logging.debug(err.__cause__)
        logging.error(str(err))
        sys.exit(1)


if __name__ == '__main__':
    main()
