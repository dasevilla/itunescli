import logging

from cliff.command import Command
from cliff.lister import Lister
from cliff.show import ShowOne

import itunes


class ITunesSearchBase(object):

    MEDIA_TYPES = frozenset([
        'movie',
        'podcast',
        'music',
        'musicVideo',
        'audiobook',
        'shortFilm',
        'tvShow',
        'tvSeason',
        'software',
        'ebook',
        'all',
    ])

    def config_parser(self, parser):
        parser.add_argument('query', metavar='SEARCH_QUERY')
        parser.add_argument('--country', default='US', type=str)
        parser.add_argument('--media', default='all',
            choices=self.MEDIA_TYPES)
        parser.add_argument('--entity', default=None)
        return parser

    def artwork_url(self, artwork):
        """Return the largest artwork URL possible"""
        return artwork['100'].replace('.100x100-75', '.300x300-75')


class SearchLister(Lister, ITunesSearchBase):
    """Search iTunes"""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(SearchLister, self).get_parser(prog_name)
        parser = self.config_parser(parser)
        parser.add_argument('--limit', default=100, type=int)
        return parser

    def get_data(self, parsed_args):

        results = itunes.Search(query=parsed_args.query,
            limit=parsed_args.limit,
            country=parsed_args.country,
            entity=parsed_args.entity,
            media=parsed_args.media).get()

        return (('name', 'url', 'genre', 'release_date', 'artwork', 'type'),
                ((n.get_name(), n.get_url(), n.get_genre(), n.get_release_date(), self.artwork_url(n.get_artwork()), n.type) for n in results)
                )


class SearchOne(ShowOne, ITunesSearchBase):
    """Show the first result from a search query"""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(SearchOne, self).get_parser(prog_name)
        parser = self.config_parser(parser)
        return parser

    def get_data(self, parsed_args):

        results = itunes.Search(query=parsed_args.query,
            limit=1,
            country=parsed_args.country,
            entity=parsed_args.entity,
            media=parsed_args.media).get()

        result = results[0]

        columns = ('name', 'url', 'genre', 'release_date', 'artwork', 'type')
        data = (
            result.get_name(),
            result.get_url(),
            result.get_genre(),
            result.get_release_date(),
            self.artwork_url(result.get_artwork()),
            result.type
            )

        return (columns, data)


class GetArtwork(Command, ITunesSearchBase):
    """Get the album artwork from the first result of a query"""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(GetArtwork, self).get_parser(prog_name)
        parser = self.config_parser(parser)
        return parser

    def run(self, parsed_args):

        results = itunes.Search(query=parsed_args.query,
            limit=1,
            country=parsed_args.country,
            entity=parsed_args.entity,
            media=parsed_args.media).get()

        all_artwork = results[0].get_artwork()
        artwork_url = self.artwork_url(all_artwork)
        self.app.stdout.write("%s\n" % artwork_url)
