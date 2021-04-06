import requests

class PlayerStats:
    def __init__(self, ones=None, twos=None, threes=None):
        self.ones = ones
        self.twos = twos
        self.threes = threes

    @staticmethod
    def generate_response(username, platform):
        """Call tracker API and fetch player stats"""
        url = f'https://api.tracker.gg/api/v2/rocket-league/standard/profile/{platform}/{username}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.198 Safari/537.36'}
        response = requests.get(url, headers=headers)

        if not response.ok:
            print(f"API failed with a {response.status_code} response - aborting")
            return

        raw_response_data = response.json().get("data", {})
        return raw_response_data

    def extract_player_stats_from_response(self, raw_response_data):
        """Extract the player data from API response"""
        self.ones = raw_response_data['segments'][1]['stats']['rating']['value']
        self.twos = raw_response_data['segments'][2]['stats']['rating']['value']
        self.threes = raw_response_data['segments'][3]['stats']['rating']['value']

    def tracker_data_print(self):
        """Print the results tracker results"""
        print(
              f"1v1 MMR: {self.ones}\n"
              f"2v2 MMR: {self.twos}\n"
              f"3v3 MMR: {self.threes}\n"
              )