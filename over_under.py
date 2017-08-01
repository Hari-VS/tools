import random
import pygal

# script to simulate a lot of seasons given certain win probabilities

def main():
    # win probabilities
    games = [ .78, .31, .8, .81, .7, .27, .15, .71, .53, .47, .15, .59]
    i = 0
    seasons = []
    # update for number of simulated seasons
    while i < 100000:
        seasons.append(sim_season(games))
        i += 1
    season_frequencies = []
    # update for number of games
    for value in range(0, 13):
        frequency = seasons.count(value)
        season_frequencies.append(frequency)
    hist = pygal.Bar()
    hist.title = "Win Distribution"
    hist.x_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    hist.add('Seasons', season_frequencies)
    # update for difference file location
    hist.render_to_file('/tmp/season_visual.svg')
    i = 0
    while i < len(season_frequencies):
        print(season_frequencies[i])
        i += 1

def sim_season(games):
    wins = 0
    i = 0
    while i < len(games):
        if win(games[i]):
            wins += 1
        i += 1
    return wins

def win(p):
    return True if random.random() < p else False

main()
