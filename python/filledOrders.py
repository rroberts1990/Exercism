import requests

def getTotalGoals(team, year):
    url = "https://jsonmock.hackerrank.com/api/football_matches?year={year}&team{n}={team}&page={page}"
    
    resp = requests.get(url.format(year=year, n=2, team=team,page=1))
    print(resp)


getTotalGoals("Barcelona", 2011)