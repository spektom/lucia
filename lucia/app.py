import os
import sys
import logging
from lucia.args import AppArgs
from lucia.chat import Chat
from lucia.console import Console


def main():
    logging.basicConfig(
        level=logging.INFO,
        format=
        '%(asctime)s.%(msecs)03d %(levelname)s %(filename)s:%(lineno)s %(funcName)s(): %(message)s'
    )
    opts = AppArgs()
    os.makedirs(opts.state_dir, exist_ok=True)

    chat = Chat(opts)
    if opts.interface == 'console':
        Console(chat).run()
    else:
        raise NotImplementedError('Interface {0} not implemented'.format(
            opts.interface))


if __name__ == '__main__':
    sys.exit(main())
