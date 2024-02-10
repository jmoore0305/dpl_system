from DataStore import init_database
from DataStore import league_and_season_stats_repo


init = init_database.init_db()

league_and_season_stats_repo.add_stats(300.5, 301.5, 350, 351)


stats = league_and_season_stats_repo.get_all_stats()
print(stats)


stat_id = league_and_season_stats_repo.get_last_stat_id()

league_and_season_stats_repo.update_stats(stat_id, avg_score_season=466.0)

stats = league_and_season_stats_repo.get_all_stats()
print(stats)



