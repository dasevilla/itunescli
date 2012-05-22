import logging
import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


class ITunesApp(App):

    log = logging.getLogger(__name__)

    def __init__(self):
        super(ITunesApp, self).__init__(
            description='Query the iTunes search API',
            version='0.1',
            command_manager=CommandManager('itunes.search'),
            )


def main(argv=sys.argv[1:]):
    myapp = ITunesApp()
    return myapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
