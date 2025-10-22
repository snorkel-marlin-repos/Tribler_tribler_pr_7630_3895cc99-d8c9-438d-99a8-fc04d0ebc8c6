from ipv8.test.base import TestBase
from pony.orm import db_session

from tribler.core.components.database.db.tribler_database import TriblerDatabase


# pylint: disable=protected-access

class TestTriblerDatabase(TestBase):
    def setUp(self):
        super().setUp()
        self.db = TriblerDatabase()

    async def tearDown(self):
        if self._outcome.errors:
            self.dump_db()

        await super().tearDown()

    @db_session
    def dump_db(self):
        print('\nPeer:')
        self.db.instance.Peer.select().show()
        print('\nResource:')
        self.db.instance.Resource.select().show()
        print('\nStatement')
        self.db.instance.Statement.select().show()
        print('\nStatementOp')
        self.db.instance.StatementOp.select().show()
        print('\nMisc')
        self.db.instance.Misc.select().show()
        print('\nTorrentHealth')
        self.db.instance.TorrentHealth.select().show()
        print('\nTracker')
        self.db.instance.Tracker.select().show()

    @db_session
    def test_set_misc(self):
        """Test that set_misc works as expected"""
        self.db.set_misc(key='key', value='value')
        assert self.db.get_misc(key='key') == 'value'

    @db_session
    def test_non_existent_misc(self):
        """Test that get_misc returns proper values"""
        # None if the key does not exist
        assert not self.db.get_misc(key='non existent')

        # A value if the key does exist
        assert self.db.get_misc(key='non existent', default=42) == 42
