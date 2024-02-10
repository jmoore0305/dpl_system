from Controllers.MatchController import MatchController
from DataStore import init_database


init = init_database.init_db()
controller = MatchController()

print("match exist:", controller.does_match_exist())




controller.create_match("2024-10-18", "Arena", 3, 3, 501)


print("match exist:", controller.does_match_exist())


controller.update_match("2025-10-18", "SomeArena", 4, 4, 801)


print("match exist:", controller.does_match_exist())
