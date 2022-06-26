import argparse
import ascii_art


__VERSION__ = '1.0.0-beta'


PROG = 'python ascii_art'
DESCRIPTION = f'ASCII character art (version {__VERSION__}) by Yu-Cheng Lin (ylin@nycu.edu.tw)'
REQUIRED = [
    {
        'keys': ['-i', '--image'],
        'properties': {
            'type': str,
            'required': True,
            'help': 'path to the image',
        }
    },
]
OPTIONAL = [
    {
        'keys': ['-w', '--white-background'],
        'properties': {
            'action': 'store_true',
            'help': 'white background',
        }
    },
    {
        'keys': ['-y', '--height'],
        'properties': {
            'type': int,
            'required': False,
            'default': 100,
            'help': 'number of lines for display height (default: %(default)s)',
        }
    },
    {
        'keys': ['-h', '--help'],
        'properties': {
            'action': 'help',
            'help': 'show this help message',
        }
    },
    {
        'keys': ['-v', '--version'],
        'properties': {
            'action': 'version',
            'version': __VERSION__,
            'help': 'show version',
        }
    },
]


class EntryPoint:

    parser: argparse.ArgumentParser

    def main(self):
        self.set_parser()
        self.add_required_arguments()
        self.add_optional_arguments()
        self.run()

    def set_parser(self):
        self.parser = argparse.ArgumentParser(
            prog=PROG,
            description=DESCRIPTION,
            add_help=False,
            formatter_class=argparse.RawTextHelpFormatter)

    def add_required_arguments(self):
        group = self.parser.add_argument_group('required arguments')
        for item in REQUIRED:
            group.add_argument(*item['keys'], **item['properties'])

    def add_optional_arguments(self):
        group = self.parser.add_argument_group('optional arguments')
        for item in OPTIONAL:
            group.add_argument(*item['keys'], **item['properties'])

    def run(self):
        args = self.parser.parse_args()
        ascii_art.AsciiArt().main(
            file=args.image,
            white_background=args.white_background,
            height=args.height
        )


if __name__ == '__main__':
    EntryPoint().main()
