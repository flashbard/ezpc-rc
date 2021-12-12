from notifypy import notify
import yaml
import notify

class ProfileRepository:
    # Collection of profiles as read from the specified file
    def __init__(self, path="config/profiles.yaml", enable_notifications=True):
        self._data = []
        self._load_profiles_from_file(path)
        self._current = self._data[0]
        self._base = self._data[0]
        self._index = 0
        self._enable_notifications = enable_notifications
    
    def _load_profiles_from_file(self, path):
        with open(path, "r") as stream:
            self._data = yaml.safe_load(stream)["profiles"]

    def load_next_profile(self):
        try:
            self._index += 1
            self._current = self._data[self._index]
        except IndexError:
            # Done navigating all profiles -> Reset to first profile
            self._index = 0
            self._current = self._data[self._index]

        if self._enable_notifications:
            notify.create_notification(title=self._current["name"], message=f'{self._current["name"]} profile enabled')

    @property
    def base(self):
        return self._base

    @property
    def current(self):
        return self._current
