from page_loader import engine
from page_loader import cli


def main():
    args = cli.get_args()
    print(engine.run(args.page_adress, args.output))


if __name__ == '__main__':
    main()
