import pandas as pd

class CountryCodes:
    def __init__(self):
        self.data = pd.read_csv(__file__.replace('countrycodes.py', 'data.csv'))

    def get_country_code(self, country_name):
        country_name = country_name.title()
        row = self.data[self.data['Country'] == country_name]
        if not row.empty:
            return row.iloc[0]['Code']
        else:
            return None
