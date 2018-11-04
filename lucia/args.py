import argparse
from . import version


class AppArgs(object):
    def __init__(self):
        parser = argparse.ArgumentParser(
            prog='lucia',
            description='Lucia v{0}'.format(version),
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        required = parser.add_argument_group('required arguments')
        self.add_args(parser, required)
        self.options = vars(parser.parse_args())

    def add_args(self, optional, required):
        optional.add_argument(
            '--version',
            action='version',
            version='%(prog)s {0}'.format(version))

        optional.add_argument(
            '--interface',
            default='console',
            help='Interaction interface (console, http)')

        optional.add_argument(
            '--data-dir',
            default='/data',
            help='Data directory where all training sets are placed'
        )

        optional.add_argument(
            '--state-dir',
            default='/tmp/lucia',
            help='Data directory where all trained models are placed'
        )

    def __getattr__(self, name):
        if name in self.options:
            return self.options[name]
        raise AttributeError('No such argument: {0}'.format(name))
