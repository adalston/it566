"""Implements Team Roster Operations"""

from asyncio.windows_events import NULL
from datetime import date


class Roster(object):
    """Implements Team Roster Operations"""
    def __init__(self):
        self._initialize_roster_dictionary()
        self.inventory_file = NULL

    def new_roster(self):
            """Initialize new dictionary to roster data."""
            if self.dictionary != None:
                user_input = input("Save current roster? (y/n): ")
                match user_input.lower():
                    case 'y':
    #                   self.save_roster()
                        self._initialize_roster_dictionary()
                    case 'n':
                        self._initialize_roster_dictionary()
                    case _:
                        self._initialize_roster_dictionary()
            else:
                self._initialize_roster_dictionary()

    def _initialize_roster_dictionary(self):
            print("Initializing new roster...")
            self.dictionary = {}
            self.dictionary['type'] = 'Team Roster'
            self.dictionary['date'] = date.today().isoformat()
            self.dictionary['sport'] = 'Curling'
            self.dictionary['country'] = 'USA'
            self.dictionary['members'] = []
            print("New Roster Initialized")

