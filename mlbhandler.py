# /json/named.[endpoint].bam
import requests


class Mlbhandler:
    def __init__(self):
        base_url = "http://lookup-service-prod.mlb.com"

    def get_individual_stats(self,):
        pass

    def get_team_stats(self, season, is_all_star='N',):
        pass

    def get_roster(self, team, year):
        # List Teams

        # compare with team and year
        pass

    def get_player_stats(self, player_name):
        pass