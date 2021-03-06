from pupa.models.organization import Organization


class Jurisdiction(object):
    """ Base class for a jurisdiction """

    # schema objects
    name = None
    url = None
    chambers = {}
    sessions = []
    feature_flags = []
    building_maps = []

    # non-db properties
    scrapers = {}
    default_scrapers = {}
    parties = []
    other_names = []
    parent_id = None
    ignored_scraped_sessions = []

    # internal settings
    _party_cache = {}

    def get_db_object(self):
        return {'name': self.name,
                'url': self.url,
                'chambers': self.chambers,
                'sessions': self.sessions,
                'feature_flags': self.feature_flags,
                'building_maps': self.building_maps}

    def get_party(self, party_name):
        if not self._party_cache:
            for party in self.parties:
                self._party_cache[party['name']] = Organization(party['name'], _id=party['id'])
        try:
            return self._party_cache[party_name]
        except KeyError:
            raise ValueError('no such party: ' + party_name)

    def get_session_list(self):
        raise NotImplementedError('get_session_list is not implemented')

    def extract_text(self):
        raise NotImplementedError('extract_text is not implemented')
