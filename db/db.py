
import re

class Database():
    def __init__(self, static_db_path = 'db/' ,static_db_name = 'city_names.txt'):
        self.db_path = static_db_path
        self.file_name = static_db_name
        self.data = []
    
    def contains(self, other):
        """ See if the other set is contained in our data """
        return set(other).issubset(set(self.data))

    def connect(self):
        """ Used as a friendlier connection method """ 
        self._parse_db_file()
    
    def cities(self, options = 'all'):
        response = self.data
        return response
    
    def _parse_db_file(self):
        """ Using the file path provided, We'll open the file and 
            add all the rows as item to this list """
        full_database_path = f'{self.db_path}{self.file_name}'
        values_from_file = []
        with open(full_database_path, 'r') as f:
            values_from_file = f.read().split('\n')
        self.data = self._filter_valid_fields(values_from_file)

    def _filter_valid_fields(self, proposed_strings):
        """ Make sure we're not having unsupported characters in our data """
        # Wichita, St. Paul, Fort Riley-Camp Whiteside
        regex_filter = '^[A-Za-z.\ \-]+$' 
        fields = []
        for name in proposed_strings:
            re.match(regex_filter, name) and fields.append(name)
        return fields



