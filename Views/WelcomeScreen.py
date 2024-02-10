from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from Controllers.PlayerController import PlayerController
from Controllers.MatchController import MatchController
from Views.ScorersInterface import Ui_MainWindow
from Views.CompetitorScoreboard import Competitor_Window
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtWidgets import QMessageBox, QWidget
from Controllers.MaintainPlayersController import MaintainPlayersController


# Author: Michelle Patel
# Note for next time: Add error checking elements and comment code


# Third Window, match info

class Ui_MainWindow2(object):

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.maintainPlayersController = MaintainPlayersController()
        player_list_exist = self.maintainPlayersController.does_player_list_exist()

        if player_list_exist:
            pass
        else:
            self.maintainPlayersController.load_player_list()

        self._myWelcomeScreen = welcomeScreen
        id = QFontDatabase.addApplicationFont(".\\Assets\\Super Boys.ttf")
        if id < 0: print("Error")
        families = QFontDatabase.applicationFontFamilies(id)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(728, 559)
        MainWindow.setStyleSheet(
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop: 0 rgba(235,181,212,1.000), stop:1 rgba(142,221,241,1.000))")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.selectPlayerLayout = QtWidgets.QHBoxLayout()
        self.selectPlayerLayout.setObjectName("selectPlayerLayout")
        self.SelectPlayerLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.SelectPlayerLabel.setObjectName("SelectPlayerLabel")
        self.SelectPlayerLabel.setStyleSheet("background-color: transparent;")
        self.SelectPlayerLabel.setFont(QFont(families[0], 30))
        self.selectPlayerLayout.addWidget(self.SelectPlayerLabel)
        self.selectPlayerComboBox = QtWidgets.QComboBox(parent=self.centralwidget)

        list = self.maintainPlayersController.get_player_list()
        self.selectPlayerComboBox.addItem("")
        for player in list:
            self.selectPlayerComboBox.addItem(player['first_name'] + " " + player['last_name'])

        self.selectPlayerComboBox.setStyleSheet("background-color: white")
        self.selectPlayerComboBox.setFont(QFont(families[0], 30))
        self.selectPlayerComboBox.setStyleSheet("border :3px solid black;"
                                "background-color: white;")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectPlayerComboBox.sizePolicy().hasHeightForWidth())
        self.selectPlayerComboBox.setSizePolicy(sizePolicy)
        self.selectPlayerComboBox.setObjectName("selectPlayerComboBox")
        self.selectPlayerLayout.addWidget(self.selectPlayerComboBox)
        self.verticalLayout.addLayout(self.selectPlayerLayout)
        self.playerInfoGrid = QtWidgets.QGridLayout()
        self.playerInfoGrid.setSpacing(0)
        self.playerInfoGrid.setObjectName("playerInfoGrid")
        self.PlayerCR = QtWidgets.QLabel(parent=self.centralwidget)
        self.PlayerCR.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-left: 2px solid black;\n"
"border-top: 2px solid black;\n"
"border-right: 2px solid black;\n"
"border-bottom:4px solid black")
        self.PlayerCR.setObjectName("PlayerCR")
        self.playerInfoGrid.addWidget(self.PlayerCR, 1, 2, 1, 1)
        self.PlayerLW = QtWidgets.QLabel(parent=self.centralwidget)
        self.PlayerLW.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-left: 2px solid black;\n"
"border-top: 2px solid black;\n"
"border-right: 2px solid black;\n"
"border-bottom:4px solid black")
        self.PlayerLW.setObjectName("PlayerLW")
        self.playerInfoGrid.addWidget(self.PlayerLW, 1, 3, 1, 1)
        self.Player180s = QtWidgets.QLabel(parent=self.centralwidget)
        self.Player180s.setStyleSheet("background-color: rgb(255, 255, 255);"
                                    "border :3px solid black;"
                                    "border-width : 2px 4px 4px 2px;"
                                    "border-top-left-radius : 0px;"
                                    "border-top-right-radius : 0px; "
                                    "border-bottom-left-radius : 0px; "
                                    "border-bottom-right-radius : 15px;")
        self.Player180s.setObjectName("Player180s")
        self.playerInfoGrid.addWidget(self.Player180s, 1, 4, 1, 1)
        self.PlayerLN = QtWidgets.QLabel(parent=self.centralwidget)
        self.PlayerLN.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-left: 2px solid black;\n"
"border-top: 2px solid black;\n"
"border-right: 2px solid black;\n"
"border-bottom:4px solid black")
        self.PlayerLN.setObjectName("PlayerLN")
        self.playerInfoGrid.addWidget(self.PlayerLN, 1, 1, 1, 1)
        self.PlayerFN = QtWidgets.QLabel(parent=self.centralwidget)
        self.PlayerFN.setStyleSheet("background-color: rgb(255, 255, 255);"
                                   "border :3px solid black;"
                                   "border-width : 2px 2px 4px 4px;"
                                   "border-top-left-radius : 0px;"
                                   "border-top-right-radius : 0px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 0px")
        self.PlayerFN.setObjectName("PlayerFN")
        self.playerInfoGrid.addWidget(self.PlayerFN, 1, 0, 1, 1)
        self.TitleFN = QtWidgets.QLabel(parent=self.centralwidget)
        self.TitleFN.setStyleSheet("background-color: rgb(255, 255, 255);"
                                "border :3px solid black;"
                                "border-width : 4px 2px 2px 4px;"
                                "border-top-left-radius : 15px;"
                                "border-top-right-radius : 0px; "
                                "border-bottom-left-radius : 0px; "
                                "border-bottom-right-radius : 0px")
        self.TitleFN.setObjectName("TitleFN")
        self.playerInfoGrid.addWidget(self.TitleFN, 0, 0, 1, 1)
        self.TitleLW = QtWidgets.QLabel(parent=self.centralwidget)
        self.TitleLW.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-left: 2px solid black;\n"
"border-top: 4px solid black;\n"
"border-right: 2px solid black;\n"
"border-bottom:2px solid black")
        self.TitleLW.setObjectName("TitleLW")
        self.playerInfoGrid.addWidget(self.TitleLW, 0, 3, 1, 1)
        self.TitleCR = QtWidgets.QLabel(parent=self.centralwidget)
        self.TitleCR.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-left: 2px solid black;\n"
"border-top: 4px solid black;\n"
"border-right: 2px solid black;\n"
"border-bottom:2px solid black")
        self.TitleCR.setObjectName("TitleCR")
        self.playerInfoGrid.addWidget(self.TitleCR, 0, 2, 1, 1)
        self.TitleLN = QtWidgets.QLabel(parent=self.centralwidget)
        self.TitleLN.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-left: 2px solid black;\n"
"border-top: 4px solid black;\n"
"border-right: 2px solid black;\n"
"border-bottom:2px solid black")
        self.TitleLN.setObjectName("TitleLN")
        self.playerInfoGrid.addWidget(self.TitleLN, 0, 1, 1, 1)
        self.Title180s = QtWidgets.QLabel(parent=self.centralwidget)
        self.Title180s.setStyleSheet("background-color: rgb(255, 255, 255);"
                                   "border :3px solid black;"
                                   "border-width : 4px 4px 2px 2px;"
                                   "border-top-left-radius : 0px;"
                                   "border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 0px; "
                                   "border-bottom-right-radius : 0px;")
        self.Title180s.setObjectName("Title180s")
        self.playerInfoGrid.addWidget(self.Title180s, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.playerInfoGrid)
        self.deletePlayerLayout = QtWidgets.QHBoxLayout()
        self.deletePlayerLayout.setObjectName("deletePlayerLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.deletePlayerLayout.addItem(spacerItem)
        self.deletePlayerButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.deletePlayerButton.clicked.connect(self.deletePlayer)
        self.deletePlayerButton.setStyleSheet("border: 3px solid black;" 
                                        "background-color: crimson;" 
                                        "border-top-left-radius :5px;" 
                                        "border-top-right-radius : 5px;" 
                                        "border-bottom-left-radius : 5px;"
                                        "border-bottom-right-radius : 5px")
        self.deletePlayerButton.setFont(QFont(families[0], 15))
        self.deletePlayerButton.setObjectName("deletePlayerButton")
        self.deletePlayerLayout.addWidget(self.deletePlayerButton)
        self.verticalLayout.addLayout(self.deletePlayerLayout)
        self.CreatePlayerGrid = QtWidgets.QGridLayout()
        self.CreatePlayerGrid.setObjectName("CreatePlayerGrid")
        self.FNLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.FNLineEdit.setStyleSheet("border: 3px solid black;" 
                                        "background-color: white;" 
                                        "border-top-left-radius :5px;" 
                                        "border-top-right-radius : 5px;" 
                                        "border-bottom-left-radius : 5px;"
                                        "border-bottom-right-radius : 5px")
        self.FNLineEdit.setFont(QFont(families[0], 15))
        self.FNLineEdit.setObjectName("FNLineEdit")
        self.CreatePlayerGrid.addWidget(self.FNLineEdit, 1, 1, 1, 1)
        self.FirstNameLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.FirstNameLabel.setFont(QFont(families[0], 15))
        self.FirstNameLabel.setStyleSheet("background-color: transparent")
        self.FirstNameLabel.setObjectName("FirstNameLabel")
        self.CreatePlayerGrid.addWidget(self.FirstNameLabel, 1, 0, 1, 1)
        self.LastNameLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.LastNameLabel.setStyleSheet("background-color: transparent")
        self.LastNameLabel.setObjectName("LastNameLabel")
        self.LastNameLabel.setFont(QFont(families[0], 15))
        self.CreatePlayerGrid.addWidget(self.LastNameLabel, 1, 2, 1, 1)
        self.CreatePlayerLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.CreatePlayerLabel.setStyleSheet("background-color: transparent")
        self.CreatePlayerLabel.setFont(QFont(families[0], 15))
        self.CreatePlayerLabel.setObjectName("CreatePlayerLabel")
        self.CreatePlayerGrid.addWidget(self.CreatePlayerLabel, 0, 0, 1, 1)
        self.LNLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.LNLineEdit.setObjectName("LNLineEdit")
        self.LNLineEdit.setStyleSheet("border: 3px solid black;"
                                      "background-color: white;"
                                      "border-top-left-radius :5px;"
                                      "border-top-right-radius : 5px;"
                                      "border-bottom-left-radius : 5px;"
                                      "border-bottom-right-radius : 5px")
        self.LNLineEdit.setFont(QFont(families[0], 15))
        self.CreatePlayerGrid.addWidget(self.LNLineEdit, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.CreatePlayerGrid)
        self.createPlayerLayout = QtWidgets.QHBoxLayout()
        self.createPlayerLayout.setObjectName("createPlayerLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.createPlayerLayout.addItem(spacerItem1)
        self.createPlayerButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.createPlayerButton.clicked.connect(self.createPlayer)
        self.createPlayerButton.setObjectName("createPlayerButton")
        self.backButton = QtWidgets.QPushButton(parent = self.centralwidget)
        self.backButton.clicked.connect(self.getWelcomeScreen)
        self.createPlayerLayout.addWidget(self.backButton)
        self.createPlayerLayout.addWidget(self.createPlayerButton)
        self.createPlayerButton.setStyleSheet("border: 3px solid black;"
                                              "background-color: lightgreen;"
                                              "border-top-left-radius :5px;"
                                              "border-top-right-radius : 5px;"
                                              "border-bottom-left-radius : 5px;"
                                              "border-bottom-right-radius : 5px")
        self.backButton.setStyleSheet("border: 3px solid black;"
                                              "background-color: lightgreen;"
                                              "border-top-left-radius :5px;"
                                              "border-top-right-radius : 5px;"
                                              "border-bottom-left-radius : 5px;"
                                              "border-bottom-right-radius : 5px")
        self.createPlayerButton.setFont(QFont(families[0], 15))
        self.backButton.setFont(QFont(families[0], 15))
        self.verticalLayout.addLayout(self.createPlayerLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(3, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def createPlayer(self):
        if self.FNLineEdit.text() == "" or self.LNLineEdit.text() == "":
            parent_widget = QWidget()
            QMessageBox.warning(parent_widget, 'Selection Required', 'Please enter a name first.')
            return
        firstName = self.FNLineEdit.text()
        lastName = self.LNLineEdit.text()
        self.maintainPlayersController.add_player_to_list(firstName, lastName)
        parent_widget = QWidget()
        QMessageBox.information(parent_widget, 'Created Player', 'Player ' + firstName + ' ' + lastName + ' created successfully!')
        self.updateList()
        return

    def updateList(self):
        self.selectPlayerComboBox.clear()
        list = self.maintainPlayersController.get_player_list()
        for player in list:
            self.selectPlayerComboBox.addItem(player['first_name'] + " " + player['last_name'])
    def deletePlayer(self):
        parent_widget = QWidget()
        list = self.maintainPlayersController.get_player_list()
        if len(list) == 0:
            parent_widget = QWidget()
            QMessageBox.warning(parent_widget, 'Selection Required', 'Nothing to delete.')
            return

        parent_widget = QWidget()
        reply = QMessageBox.question(parent_widget, 'Message', 'Are you sure you want to delete ' + self.selectPlayerComboBox.currentText() + '?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            name = self.selectPlayerComboBox.currentText()
            firstName, lastName = name.split()
            self.maintainPlayersController.remove_player_from_list(firstName, lastName)

            self.updateList()
            QMessageBox.information(parent_widget, 'Remove Player',
                                    'Player deleted successfully!')
        else:
            return

    def getWelcomeScreen(self):
        self._myWelcomeScreen = welcomeScreen()
        self._myWelcomeScreen.show()
        self.MainWindow.hide()









    def center(self):
        x = self.frameGeometry()
        y = self.screen().availableGeometry().center()
        x.moveCenter(y)
        self.move(x.topLeft())


    def retranslateUi(self, MainWindow):
        id = QFontDatabase.addApplicationFont(".\\Assets\\Super Boys.ttf")
        if id < 0: print("Error")
        families = QFontDatabase.applicationFontFamilies(id)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        # NEED TO GET THIS INFO FROM THE DATABASE
        self.PlayerCR.setText(_translate("MainWindow", " "))
        self.PlayerCR.setFont(QFont(families[0], 15))
        self.PlayerLW.setText(_translate("MainWindow", " "))
        self.PlayerLW.setFont(QFont(families[0], 15))
        self.Player180s.setText(_translate("MainWindow", " "))
        self.Player180s.setFont(QFont(families[0], 15))
        self.PlayerLN.setText(_translate("MainWindow", " "))
        self.PlayerLN.setFont(QFont(families[0], 15))
        self.PlayerFN.setText(_translate("MainWindow", " "))
        self.PlayerFN.setFont(QFont(families[0], 15))

        # DON'T NEED TO WORRY ABOUT THIS
        self.SelectPlayerLabel.setText(_translate("MainWindow", "Player: "))
        self.TitleFN.setText(_translate("MainWindow", "First Name"))
        self.TitleFN.setFont(QFont(families[0], 20))
        self.TitleLW.setText(_translate("MainWindow", "Last Win"))
        self.TitleLW.setFont(QFont(families[0], 20))
        self.TitleCR.setText(_translate("MainWindow", "Current Rank"))
        self.TitleCR.setFont(QFont(families[0], 20))
        self.TitleLN.setText(_translate("MainWindow", "Last Name"))
        self.TitleLN.setFont(QFont(families[0], 20))
        self.Title180s.setText(_translate("MainWindow", "# 180\'s in Season"))
        self.Title180s.setFont(QFont(families[0], 20))
        self.deletePlayerButton.setText(_translate("MainWindow", "Delete Player"))
        self.FirstNameLabel.setText(_translate("MainWindow", "First Name:"))
        self.LastNameLabel.setText(_translate("MainWindow", "Last Name:"))
        self.CreatePlayerLabel.setText(_translate("MainWindow", "Create Player:"))
        self.createPlayerButton.setText(_translate("MainWindow", "Create Player"))
        self.backButton.setText(_translate("MainWindow", "Back"))


class Window3(QMainWindow):
    def __init__(self, window2):
        super().__init__()




        self.my_selection_city = None
        self.my_selection_scoreboard = None
        self.my_selection_start_score = None
        self.scorers_interface_main_window = None
        self._myMatchController = MatchController()
        self._myWindow2 = window2
        self._myScorersInterface = None
        self.myMatchDate = None
        self.myArena = None
        self.myCity = None
        self.myNumOfLegs = None
        self.myTotalMatches = None
        self.myStartingScore = None
        self.myStartingScoreboard = None
        self.scoreboard_selection = None
        self.main_window()


    def main_window(self):
        # Importing custom font and adding it to this program
        id = QFontDatabase.addApplicationFont(".\\Assets\\Super Boys.ttf")
        if id < 0: print("Error")
        families = QFontDatabase.applicationFontFamilies(id)

        # Label to let user know that this form is the match information
        matchLabel = QLabel("Match Info", self)
        matchLabel.setFont(QFont(families[0], 50))
        matchLabel.setGeometry(200, 20, 500, 100)
        matchLabel.setStyleSheet("background:transparent")

        # Match Date label so user knows to enter a date
        matchDateLabel = QLabel("Match Date:", self)
        matchDateLabel.setFont(QFont(families[0], 30))
        matchDateLabel.setGeometry(20, 120, 300, 100)
        matchDateLabel.setStyleSheet("background:transparent")




        # Textbox to hold the date
        self.matchDate = QDateEdit(self)
        self.matchDate.setGeometry(350, 150, 300, 50)
        self.matchDate.setFont(QFont(families[0], 30))
        d = QDate(2023, 10, 8)
        self.matchDate.setDate(d)
        self.matchDate.setStyleSheet(
            "border: 4px solid black;" "background-color: white;" "border-top-left-radius :10px;" " border-top-right-radius : 10px; " "border-bottom-left-radius : 10px; ""border-bottom-right-radius : 10px")




        # Location label so user knows to enter a location
        locationLabel = QLabel("Location:", self)
        locationLabel.setFont(QFont(families[0], 30))
        locationLabel.setGeometry(20, 220, 300, 100)
        locationLabel.setStyleSheet("background:transparent")

        cities = ['London', 'Birmingham', 'Leeds', 'Glasgow', 'Sheffield', 'Bradford', 'Liverpool', 'Edinburgh', 'Manchester', 'Bristol', 'Kirklees', 'Fife', 'Wirral', 'North Lanarkshire', 'Wakefield']

        # Textbox for the name of the city
        self.cityTextBox = QComboBox(self)
        self.cityTextBox.addItem(' ')
        for n in cities:
            self.cityTextBox.addItem(n)
        self.cityTextBox.move(350, 250)
        self.cityTextBox.resize(300, 50)
        self.cityTextBox.setFont(QFont(families[0], 20))
        self.cityTextBox.setStyleSheet(
            "border: 2px solid black;" "background-color: white;" "border-top-left-radius :10px;" " border-top-right-radius : 10px; " "border-bottom-left-radius : 10px; ""border-bottom-right-radius : 10px")

        self.cityTextBox.currentIndexChanged.connect(self.update_selection_city)



        # Legs label so user knows to enter number of legs
        legsLabel = QLabel("Number of Legs:", self)
        legsLabel.setFont(QFont(families[0], 30))
        legsLabel.setGeometry(20, 320, 300, 100)
        legsLabel.setStyleSheet("background:transparent")





        # Textbox for the number of legs
        self.numLegsTextBox = QSpinBox(self)
        self.legsText = self.numLegsTextBox.text()
        self.numLegsTextBox.move(350, 350)
        self.numLegsTextBox.resize(300, 50)
        self.numLegsTextBox.setRange(1, 50)
        self.numLegsTextBox.setFont(QFont(families[0], 20))
        self.numLegsTextBox.setStyleSheet(
            "border: 2px solid black;" "background-color: white;" "border-top-left-radius :10px;" " border-top-right-radius : 10px; " "border-bottom-left-radius : 10px; ""border-bottom-right-radius : 10px")
        self.numLegsTextBox.valueChanged.connect(self.ensure_odd_legs)




        # Matches label so user knows to enter number of matches
        matchesLabel = QLabel("Total Matches:", self)
        matchesLabel.setFont(QFont(families[0], 30))
        matchesLabel.setGeometry(20, 420, 300, 100)
        matchesLabel.setStyleSheet("background:transparent")




        # Textbox for the number of matches
        self.numMatchesTextBox = QSpinBox(self)
        self.numMatchesTextBox.move(350, 450)
        self.numMatchesTextBox.resize(300, 50)
        self.numMatchesTextBox.setRange(1, 25)
        self.numMatchesTextBox.setFont(QFont(families[0], 20))
        self.numMatchesTextBox.setStyleSheet(
            "border: 2px solid black;" "background-color: white;" "border-top-left-radius :10px;" " border-top-right-radius : 10px; " "border-bottom-left-radius : 10px; ""border-bottom-right-radius : 10px")
        self.numMatchesTextBox.valueChanged.connect(self.ensure_odd_matches)



        # Matches label so user knows to enter number of matches
        startingScoreLabel = QLabel("Starting Score:", self)
        startingScoreLabel.setFont(QFont(families[0], 30))
        startingScoreLabel.setGeometry(20, 520, 300, 100)
        startingScoreLabel.setStyleSheet("background:transparent")

        self.startingScoreOptions = QComboBox(self)
        self.startingScoreOptions.addItem('')
        self.startingScoreOptions.addItem('801')
        self.startingScoreOptions.addItem('501')
        self.startingScoreOptions.addItem('301')
        self.startingScoreOptions.setGeometry(350, 550, 300, 50)
        self.startingScoreOptions.setFont(QFont(families[0], 30))
        self.startingScoreOptions.setStyleSheet(
            "border: 2px solid black;" "background-color: white;" "border-top-left-radius :10px;" " border-top-right-radius : 10px; " "border-bottom-left-radius : 10px; ""border-bottom-right-radius : 10px")
        self.startingScoreOptions.currentIndexChanged.connect(self.update_selection_start_score)


        scoreboardLabel = QLabel("Scoreboard:", self)
        scoreboardLabel.setFont(QFont(families[0], 30))
        scoreboardLabel.setGeometry(20, 650, 300, 100)
        scoreboardLabel.setStyleSheet("background:transparent")

        # Starting scoreboard drop down
        self.startingBoardOptions = QComboBox(self)
        self.startingBoardOptions.addItem('')
        self.startingBoardOptions.addItem('Main Scoreboard')
        self.startingBoardOptions.addItem('Match Scoreboard')
        self.startingBoardOptions.addItem('Competitor Scoreboard')
        self.startingBoardOptions.setGeometry(350, 680, 300, 50)
        self.startingBoardOptions.setFont(QFont(families[0], 20))
        self.startingBoardOptions.setStyleSheet(
            "border: 2px solid black;" "background-color: white;" "border-top-left-radius :10px;" " border-top-right-radius : 10px; " "border-bottom-left-radius : 10px; ""border-bottom-right-radius : 10px")
        self.startingBoardOptions.currentIndexChanged.connect(self.update_selection_scoreboard)


        # Finish button once all previous and current information is correct and user is ready to move on. This will trigger the new screens to appear (dartboard, scorers interface, and main scoreboard)
        finishBtn = QPushButton('Finish', self)
        finishBtn.clicked.connect(self.window4)
        finishBtn.resize(finishBtn.sizeHint())
        finishBtn.setGeometry(490, 800, 200, 70)
        finishBtn.setFont(QFont(families[0], 30))
        finishBtn.setStyleSheet(
            "border: 4px solid black;" "background-color: lightgreen;" "border-top-left-radius :10px;" " border-top-right-radius : 10px; " "border-bottom-left-radius : 10px; ""border-bottom-right-radius : 10px")

        # Back button in case user wants to go back and change the information from previously
        backBtn = QPushButton('Back', self)
        backBtn.clicked.connect(self.window2)
        backBtn.resize(backBtn.sizeHint())
        backBtn.setGeometry(280, 800, 200, 70)
        backBtn.setFont(QFont(families[0], 30))
        backBtn.setStyleSheet(
            "border: 4px solid black;" "background-color: lightgreen;" "border-top-left-radius :10px;" " border-top-right-radius : 10px; " "border-bottom-left-radius : 10px; ""border-bottom-right-radius : 10px")

        # Main window settings. Setting the size, centering it on the center of the screen, setting the title, etc.
        self.resize(700, 900)
        self.center()
        self.setWindowTitle('Match Info')
        self.setFixedSize(700, 900)


    def ensure_odd_matches(self):
        if self.numMatchesTextBox.value() % 2 == 0:
            self.numMatchesTextBox.setValue(self.numMatchesTextBox.value() + 1)

    def ensure_odd_legs(self):
        if self.numLegsTextBox.value() % 2 == 0:
            self.numLegsTextBox.setValue(self.numLegsTextBox.value() + 1)

    def update_selection_city(self, index):
        self.my_selection_city = self.cityTextBox.currentText()
    def update_selection_scoreboard(self, index):
        self.my_selection_scoreboard = self.startingBoardOptions.currentText()
    def update_selection_start_score(self, index):
        self.my_selection_start_score = self.startingScoreOptions.currentText()

    def get_user_selection(self):
        return self.my_selection_scoreboard

    # Function to go back to player info screen
    def window2(self):
        self._myWindow2.show()
        self.hide()

    # Function if the button to finish was pressed
    def window4(self):
        if self.my_selection_city == None or self.my_selection_city.strip() == '' or self.my_selection_start_score == None or self.my_selection_start_score.strip() == '':
            QMessageBox.warning(self, "Incomplete Information", "Please select both a location and a starting score.",
                                QMessageBox.StandardButton.Ok)
            return
        # This will actually call main scoreboard, scorer's interface, and dart board screens to appear and get the values from each textbox

        self.myMatchDate = self.matchDate.text()
        self.myNumOfLegs = self.numLegsTextBox.text()
        self.myTotalMatches = self.numMatchesTextBox.text()

        match_exist = self._myMatchController.does_match_exist()


        if match_exist:
            self._myMatchController.update_match(self.myMatchDate, self.my_selection_city,
                                                 self.myNumOfLegs, self.myTotalMatches, self.my_selection_start_score)
        else:
            self._myMatchController.create_match(self.myMatchDate, self.my_selection_city,
                                                 self.myNumOfLegs, self.myTotalMatches, self.my_selection_start_score)

        self.scoreboard_selection = self.get_user_selection()

        if self._myScorersInterface is None:
            self.scorers_interface_main_window = QMainWindow()
            self._myScorersInterface = Ui_MainWindow()
            self._myScorersInterface.setupUi(self.scorers_interface_main_window, self.scoreboard_selection)
        self.scorers_interface_main_window.show()

        self.hide()


    # Function for if they click the 'x', and asking if they are really sure they want to quit
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure you want to quit?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        x = self.frameGeometry()
        y = self.screen().availableGeometry().center()
        x.moveCenter(y)
        self.move(x.topLeft())

    # Function to paint the gradient and boarder of the background
    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.GlobalColor.black, 10, Qt.PenStyle.SolidLine)
        painter.setPen(pen)
        grad1 = QLinearGradient(25, 400, 700, 900)
        grad1.setColorAt(0.0, QColor(235, 181, 212))
        grad1.setColorAt(1.0, QColor(142, 221, 241))
        painter.setBrush(QBrush(grad1))
        painter.drawRect(0, 0, 700, 900)































# Second Window, this is the actual player names
# Second Window, this is the actual player names
class Window2(QMainWindow):
    def __init__(self, welcomeScreen):
        super().__init__()
        self._myPlayerController = PlayerController()
        self.maintainPlayersController = MaintainPlayersController()
        player_list_exist = self.maintainPlayersController.does_player_list_exist()

        if player_list_exist:
            pass
        else:
            self.maintainPlayersController.load_player_list()
        self._myWelcomeScreen = welcomeScreen
        self._myWindow3 = None
        self.p1FName = None
        self.p1LName = None
        self.p2FName = None
        self.p2LName = None
        self.main_window()

    def main_window(self):

        # Importing custom font and adding it to this program
        id = QFontDatabase.addApplicationFont(".\\Assets\\Super Boys.ttf")
        if id < 0: print("Error")
        families = QFontDatabase.applicationFontFamilies(id)

        player1Label = QLabel("Player 1", self)
        player1Label.setFont(QFont(families[0], 50))
        player1Label.setGeometry(225, 50, 500, 100)
        player1Label.setStyleSheet("background:transparent")

        player1FNameLabel = QLabel("Player 1 Name:", self)
        player1FNameLabel.setFont(QFont(families[0], 30))
        player1FNameLabel.setGeometry(20, 150, 300, 100)
        player1FNameLabel.setStyleSheet("background:transparent")

        self.fNameTextbox = QComboBox(self)
        self.fNameTextbox.move(300, 182)
        self.fNameTextbox.resize(350, 40)
        self.fNameTextbox.setFont(QFont(families[0], 20))
        self.fNameTextbox.setStyleSheet(
            "border: 2px solid black;" "background-color: white;" "border-top-left-radius :10px;" " border-top-right-radius : 10px; " "border-bottom-left-radius : 10px; ""border-bottom-right-radius : 10px")

        player2Label = QLabel("Player 2", self)
        player2Label.setFont(QFont(families[0], 50))
        player2Label.setGeometry(225, 450, 500, 100)
        player2Label.setStyleSheet("background:transparent")

        player2FNameLabel = QLabel("Player 2 Name:", self)
        player2FNameLabel.setFont(QFont(families[0], 30))
        player2FNameLabel.setGeometry(20, 550, 300, 100)
        player2FNameLabel.setStyleSheet("background:transparent")

        self.f2NameTextbox = QComboBox(self)
        self.f2NameTextbox.move(300, 582)
        self.f2NameTextbox.resize(350, 40)
        self.f2NameTextbox.setFont(QFont(families[0], 20))
        self.f2NameTextbox.setStyleSheet(
            "border: 2px solid black;" "background-color: white;" "border-top-left-radius :10px;" " border-top-right-radius : 10px; " "border-bottom-left-radius : 10px; ""border-bottom-right-radius : 10px")

        self.fNameTextbox.addItem("")
        self.f2NameTextbox.addItem("")

        player_list_exist = self.maintainPlayersController.does_player_list_exist()
        if player_list_exist:
            pass
        else:
            self.maintainPlayersController.load_player_list()

        self.f2NameTextbox.clear()
        self.fNameTextbox.clear()
        list = self.maintainPlayersController.get_player_list()
        self.f2NameTextbox.addItem("")
        self.fNameTextbox.addItem("")
        for player in list:
            self.f2NameTextbox.addItem(player['first_name'] + " " + player['last_name'])
            self.fNameTextbox.addItem(player['first_name'] + " " + player['last_name'])


        nextBtn = QPushButton('Next', self)
        nextBtn.clicked.connect(self.window3)
        nextBtn.resize(nextBtn.sizeHint())
        nextBtn.setGeometry(490, 800, 200, 70)
        nextBtn.setFont(QFont(families[0], 30))
        nextBtn.setStyleSheet(
            "border: 4px solid black;" "background-color: lightgreen;" "border-top-left-radius :10px;" " border-top-right-radius : 10px; " "border-bottom-left-radius : 10px; ""border-bottom-right-radius : 10px")

        backBtn = QPushButton('Back', self)
        backBtn.clicked.connect(self.window1)
        backBtn.resize(backBtn.sizeHint())
        backBtn.setGeometry(280, 800, 200, 70)
        backBtn.setFont(QFont(families[0], 30))
        backBtn.setStyleSheet(
            "border: 4px solid black;" "background-color: lightgreen;" "border-top-left-radius :10px;" " border-top-right-radius : 10px; " "border-bottom-left-radius : 10px; ""border-bottom-right-radius : 10px")

        self.resize(700, 900)
        self.center()
        self.setWindowTitle('Info')
        self.setFixedSize(700, 900)


    # Defining the next window after the player info screen
    def window3(self):

        if self.fNameTextbox.currentIndex() == 0 or self.f2NameTextbox.currentIndex() == 0:
            QMessageBox.warning(self, 'Selection Required', 'Please select players for both Player 1 and Player 2.')
            return

        if self.fNameTextbox.currentText() == self.f2NameTextbox.currentText():
            QMessageBox.warning(self, 'Selection Required', 'Player 1 and Player 2 must be different players. Try again.')
            return

        selected_player1 = self.fNameTextbox.currentText().split()
        selected_player2 = self.f2NameTextbox.currentText().split()

        self.p1FName, self.p1LName = selected_player1
        self.p2FName, self.p2LName = selected_player2


        players_exist = self._myPlayerController.do_players_exist()

        if players_exist:
            self._myPlayerController.update_players(self.p1FName, self.p1LName, self.p2FName, self.p2LName)
        else:
            self._myPlayerController.create_players(self.p1FName, self.p1LName, self.p2FName, self.p2LName)

        if self._myWindow3 is None:
            self._myWindow3 = Window3(self)
        self._myWindow3.show()
        self.hide()





    def window1(self):
        self._myWelcomeScreen.show()
        self.hide()

    # Function to ask user if they are sure if they want to close the application
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure you want to quit?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.GlobalColor.black, 10, Qt.PenStyle.SolidLine)
        painter.setPen(pen)
        grad1 = QLinearGradient(25, 400, 700, 900)
        grad1.setColorAt(0.0, QColor(235, 181, 212))
        grad1.setColorAt(1.0, QColor(142, 221, 241))
        painter.setBrush(QBrush(grad1))
        painter.drawRect(0, 0, 700, 900)

    # This function's job is to center the welcome screen for any screen type
    def center(self):
        x = self.frameGeometry()
        y = self.screen().availableGeometry().center()
        x.moveCenter(y)
        self.move(x.topLeft())

















# Welcome Screen
#This has the start, settings, and exit buttons
class welcomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_window()
        self._myWindow2 = None
        self.myPlayerMaintenance = None
        self.maintainPlayersController = MaintainPlayersController()
        player_list_exist = self.maintainPlayersController.does_player_list_exist()

        if player_list_exist:
            pass
        else:
            self.maintainPlayersController.load_player_list()


    def main_window(self):
        # Importing custom font and adding it to this program
        id = QFontDatabase.addApplicationFont(".\\Assets\\Super Boys.ttf")
        if id < 0: print("Error")
        families = QFontDatabase.applicationFontFamilies(id)

        # QuitBtn is the button that will handle the user closing the application
        quitBtn = QPushButton('Quit', self)
        quitBtn.clicked.connect(QApplication.instance().quit)
        quitBtn.resize(quitBtn.sizeHint())
        quitBtn.setGeometry(250, 760, 200, 70)
        quitBtn.setFont(QFont(families[0], 30))
        quitBtn.setStyleSheet(
            "border: 4px solid black;" "background-color: indianred;" "border-top-left-radius :10px;" " border-top-right-radius : 10px; " "border-bottom-left-radius : 10px; ""border-bottom-right-radius : 10px")

        # StartBtn is the button that will handle the next window to pop up
        startBtn = QPushButton('Start', self)
        startBtn.clicked.connect(self.window2)
        startBtn.resize(quitBtn.sizeHint())
        startBtn.setGeometry(250, 600, 200, 70)
        startBtn.setFont(QFont(families[0], 30))
        startBtn.setStyleSheet(
            "border: 4px solid black;" "background-color: lightgreen;" "border-top-left-radius :10px;" " border-top-right-radius : 10px; " "border-bottom-left-radius : 10px; ""border-bottom-right-radius : 10px")

        # StartBtn is the button that will handle the next window to pop up
        editPlayersBtn = QPushButton('Players', self)
        editPlayersBtn.clicked.connect(self.window5)
        editPlayersBtn.resize(quitBtn.sizeHint())
        editPlayersBtn.setGeometry(250, 680, 200, 70)
        editPlayersBtn.setFont(QFont(families[0], 30))
        editPlayersBtn.setStyleSheet(
            "border: 4px solid black;" "background-color: lightblue;" "border-top-left-radius :10px;" " border-top-right-radius : 10px; " "border-bottom-left-radius : 10px; ""border-bottom-right-radius : 10px")

        self.label = QLabel(self)
        self.pixmap = QPixmap('.\\Assets\\Logo.png')
        self.label.setPixmap(self.pixmap)
        self.label.setStyleSheet("background:transparent")
        self.label.setGeometry(100, 50, 500, 500)

        self.label2 = QLabel("The #1 score keeper for darts!", self)
        self.label2.setFont(QFont(families[0], 20))
        self.label2.setGeometry(160, 400, 500, 100)
        self.label2.setStyleSheet("background:transparent")

        self.resize(700, 900)
        self.center()
        self.setWindowTitle('BullseyeScoreboard')
        self.setFixedSize(700, 900)
        self.setStyleSheet("background-color: ghostwhite")
        self.show()

    def window5(self):
        if self.myPlayerMaintenance is None:
            self.player_maintenance_window = QMainWindow()
            self.myPlayerMaintenance = Ui_MainWindow2()
            self.myPlayerMaintenance.setupUi(self.player_maintenance_window)
        self.player_maintenance_window.show()


        self.hide()

    # Defining the next window after the welcome screen
    # This will go to the player info screen
    def window2(self):
        if self._myWindow2 is None:
            self._myWindow2 = Window2(self)
        self._myWindow2.show()
        self.hide()

    # Function to ask user if they are sure if they want to close the application
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure you want to quit?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

        # This function's job is to center the welcome screen for any screen type

    def center(self):
        x = self.frameGeometry()
        y = self.screen().availableGeometry().center()
        x.moveCenter(y)
        self.move(x.topLeft())

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.GlobalColor.black, 10, Qt.PenStyle.SolidLine)
        painter.setPen(pen)
        grad1 = QLinearGradient(25, 400, 700, 900)
        grad1.setColorAt(0.0, QColor(235, 181, 212))
        grad1.setColorAt(1.0, QColor(142, 221, 241))
        painter.setBrush(QBrush(grad1))
        painter.drawRect(0, 0, 700, 900)


