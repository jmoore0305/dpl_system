import sys
from Views.WelcomeScreen import welcomeScreen
from PySide6.QtWidgets import QApplication
from DataStore import init_database
from DataStore import combinations_repo
import threading




if __name__ == '__main__':
    init_database.init_db()
    thread = threading.Thread(target=combinations_repo.create_checkout_combinations)
    thread.start()
    app = QApplication(sys.argv)
    myWelcomeScreen = welcomeScreen()
    app.exec()