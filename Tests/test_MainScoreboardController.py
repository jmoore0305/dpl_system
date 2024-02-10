from Controllers.MainScoreboardController import MainScoreboardController
from DataStore import init_database

init = init_database.init_db()
mainScoreboardController = MainScoreboardController()

info = mainScoreboardController.get_info()

print(info)