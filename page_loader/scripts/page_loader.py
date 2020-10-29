import logging
from page_loader import engine
from page_loader import cli


def main():
    args = cli.get_args().parse_args()
    cli.set_log(args.log)
    engine.run(args.page_adress, args.output)
    logging.info('Work is finished')


if __name__ == '__main__':
    main()
