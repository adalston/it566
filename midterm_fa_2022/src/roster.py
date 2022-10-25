"""Implements Team Roster Operations"""

from asyncio.windows_events import NULL
from datetime import date
import json
import os
import string
from pathlib import Path

class Roster(object):
    """Implements Team Roster Operations"""
    def __init__(self):
        self._initialize_roster_dictionary()
        self.roster_file = NULL

    def new_roster(self):
            """Initialize new dictionary to roster data."""
            if self.dictionary != None:
                user_input = input("Save current roster? (y/n): ")
                match user_input.lower():
                    case 'y':
                        self.save_roster()
                        self._initialize_roster_dictionary()
                    case 'n':
                        self._initialize_roster_dictionary()
                    case _:
                        self._initialize_roster_dictionary()
            else:
                self._initialize_roster_dictionary()

    def load_roster(self):
        """Load roster from file."""
        self._list_roster_files()
        file_path = self._get_file_path()
        with open(file_path, 'r', encoding='UTF-8') as self.roster_file:
            self.dictionary = json.load(self.roster_file)

    def print_roster(self):
        """Print Roster to console."""
        print('----- Current Roster ----')
        if self.dictionary != None:
            for key, value in self.dictionary.items():
                if key == 'members':
                    print(f'{key.upper()}' ':   -----------------------------------------')
                    for item in value:
                        print(f'\t\t {item["name"]:25} \t {item["age"]}')
                else:
                    print(f'{key.upper()}: \t\t {value.upper()}')
        print('           -----------------------------------------')    	

    def save_roster(self):
        """Save roster to file."""
        if self.dictionary != None:
            file_path = self._get_file_path()
            with open(file_path, 'w', encoding='UTF-8') as self.roster_file:
                self.roster_file.write(json.dumps(self.dictionary))

    def add_item(self, member_name, member_age):
        """Add member to roster."""
        if (self.dictionary != None):
            self.dictionary['members'].append({'name': member_name, 'age': int(member_age)})
        else:
            print("No inventory exists. Create new inventory first.")

    def _get_file_path(self):
        """Get flle path from user."""
        f_path = input("Please enter path and filename: ")
        return f_path

    def _list_roster_files(self):
        """List all files in directory with *.json file suffix."""
        print('JSON Files found in current directory')
        root_path = os.path.relpath(Path.cwd())
        for (root, dirs, file) in os.walk(Path.cwd()):
            for f in file:
                if '.json' in f:
                    print(os.path.join(os.path.relpath(os.path.join(root, f), root_path)))

    def _initialize_roster_dictionary(self):
            print("Initializing new roster...")
            self.dictionary = {}
            self.dictionary['type'] = 'Team Roster'
            self.dictionary['date'] = date.today().isoformat()
            self.dictionary['sport'] = 'Curling'
            self.dictionary['country'] = 'USA'
            self.dictionary['members'] = []
            print("New Roster Initialized")

