from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import *
from PySide6.QtWidgets import QGraphicsColorizeEffect
from Controllers.PlayerController import PlayerController

class Match_Window(object):
    def __init__(self):
        player_controller = PlayerController()
        self.PlayerOne = player_controller.get_player_one()
        self.PlayerTwo = player_controller.get_player_two()
    def setupUi(self, MainWindow):

        # Importing custom font
        id = QFontDatabase.addApplicationFont(".\\Assets\\Super Boys.ttf")
        if id < 0: print("Error")
        families = QFontDatabase.applicationFontFamilies(id)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(552, 482)
        MainWindow.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop: 0 rgba(235,181,212,1.000), stop:1 rgba(142,221,241,1.000))")

        # DON'T MESS WITH THIS, THIS DOES NOT NEED THE DATABASE
        self.MainWindowWidget = QtWidgets.QWidget(parent=MainWindow)
        self.MainWindowWidget.setObjectName("MainWindowWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.MainWindowWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.MainWindowStackedWidget = QtWidgets.QStackedWidget(parent=self.MainWindowWidget)
        self.MainWindowStackedWidget.setObjectName("MainWindowStackedWidget")

        # Match info main scoreboard
        self.MatchInfo = QtWidgets.QWidget()
        self.MatchInfo.setObjectName("MatchInfo")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.MatchInfo)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.MatchInfoTitle = QtWidgets.QLabel(parent=self.MatchInfo)
        self.MatchInfoTitle.setMinimumSize(QtCore.QSize(0, 79))
        font = QtGui.QFont(families[0])
        font.setPointSize(36)
        self.MatchInfoTitle.setFont(font)
        self.MatchInfoTitle.setObjectName("MatchInfoTitle")
        self.verticalLayout_4.addWidget(self.MatchInfoTitle)
        self.MatchInfoTable = QtWidgets.QGridLayout()
        self.MatchInfoTable.setSpacing(0)
        self.MatchInfoTable.setObjectName("MatchInfoTable")
        self.miLTS = QtWidgets.QLabel(parent=self.MatchInfo)
        self.miLTS.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "border-left: 2px solid black;\n"
                                "border-top: 4px solid black;\n"
                                "border-right: 2px solid black;\n"
                                "border-bottom:2px solid black")
        self.miLTS.setObjectName("miLTS")
        self.MatchInfoTable.addWidget(self.miLTS, 0, 1, 1, 1)
        self.miHTS = QtWidgets.QLabel(parent=self.MatchInfo)
        self.miHTS.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "border-left: 2px solid black;\n"
                                "border-top: 4px solid black;\n"
                                "border-right: 2px solid black;\n"
                                "border-bottom:2px solid black")
        self.miHTS.setObjectName("miHTS")
        self.MatchInfoTable.addWidget(self.miHTS, 0, 3, 1, 1)
        self.miATS = QtWidgets.QLabel(parent=self.MatchInfo)
        self.miATS.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "border-left: 2px solid black;\n"
                                "border-top: 4px solid black;\n"
                                "border-right: 2px solid black;\n"
                                "border-bottom:2px solid black")
        self.miATS.setObjectName("miATS")
        self.MatchInfoTable.addWidget(self.miATS, 0, 2, 1, 1)
        self.mi180s = QtWidgets.QLabel(parent=self.MatchInfo)
        self.mi180s.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border :3px solid black;"
                                    "border-width : 4px 4px 2px 2px;"
                                    "border-top-left-radius :0px;"
                                    "border-top-right-radius : 15px; "
                                    "border-bottom-left-radius : 0px; "
                                    "border-bottom-right-radius : 0px")
        self.mi180s.setObjectName("mi180s")
        self.MatchInfoTable.addWidget(self.mi180s, 0, 4, 1, 1)
        self.miPlayerRed = QtWidgets.QLabel(parent=self.MatchInfo)
        self.miPlayerRed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 4px solid black;\n"
                                        "border-top: 2px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:2px solid black")
        self.miPlayerRed.setObjectName("miPlayerRed")
        self.MatchInfoTable.addWidget(self.miPlayerRed, 1, 0, 1, 1)
        self.miLTSRed = QtWidgets.QLabel(parent=self.MatchInfo)
        self.miLTSRed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-left: 2px solid black;\n"
                                    "border-top: 2px solid black;\n"
                                    "border-right: 2px solid black;\n"
                                    "border-bottom:2px solid black")
        self.miLTSRed.setObjectName("miLTSRed")
        self.MatchInfoTable.addWidget(self.miLTSRed, 1, 1, 1, 1)
        self.miATSRed = QtWidgets.QLabel(parent=self.MatchInfo)
        self.miATSRed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-left: 2px solid black;\n"
                                    "border-top: 2px solid black;\n"
                                    "border-right: 2px solid black;\n"
                                    "border-bottom:2px solid black\n"
                                    "")
        self.miATSRed.setObjectName("miATSRed")
        self.MatchInfoTable.addWidget(self.miATSRed, 1, 2, 1, 1)
        self.miHTSRed = QtWidgets.QLabel(parent=self.MatchInfo)
        self.miHTSRed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-left: 2px solid black;\n"
                                    "border-top: 2px solid black;\n"
                                    "border-right: 2px solid black;\n"
                                    "border-bottom:2px solid black")
        self.miHTSRed.setObjectName("miHTSRed")
        self.MatchInfoTable.addWidget(self.miHTSRed, 1, 3, 1, 1)
        self.mi180sRed = QtWidgets.QLabel(parent=self.MatchInfo)
        self.mi180sRed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-left: 2px solid black;\n"
                                    "border-top: 2px solid black;\n"
                                    "border-right: 4px solid black;\n"
                                    "border-bottom:2px solid black")
        self.mi180sRed.setObjectName("mi180sRed")
        self.MatchInfoTable.addWidget(self.mi180sRed, 1, 4, 1, 1)
        self.miPlayer = QtWidgets.QLabel(parent=self.MatchInfo)
        self.miPlayer.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border :3px solid black;"
                                    "border-width : 4px 2px 2px 4px;"
                                    "border-top-left-radius :15px;"
                                    "border-top-right-radius : 0px; "
                                    "border-bottom-left-radius : 0px; "
                                    "border-bottom-right-radius : 0px")
        self.miPlayer.setObjectName("miPlayer")
        self.MatchInfoTable.addWidget(self.miPlayer, 0, 0, 1, 1)
        self.miPlayerGreen = QtWidgets.QLabel(parent=self.MatchInfo)
        self.miPlayerGreen.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border :3px solid black;"
                                        "border-width : 2px 2px 4px 4px;"
                                        "border-top-left-radius :0px;"
                                        "border-top-right-radius : 0px; "
                                        "border-bottom-left-radius : 15px; "
                                        "border-bottom-right-radius : 0px")
        self.miPlayerGreen.setObjectName("miPlayerGreen")
        self.MatchInfoTable.addWidget(self.miPlayerGreen, 2, 0, 1, 1)
        self.miLTSGreen = QtWidgets.QLabel(parent=self.MatchInfo)
        self.miLTSGreen.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-left: 2px solid black;\n"
                                    "border-top: 2px solid black;\n"
                                    "border-right: 2px solid black;\n"
                                    "border-bottom:4px solid black")
        self.miLTSGreen.setObjectName("miLTSGreen")
        self.MatchInfoTable.addWidget(self.miLTSGreen, 2, 1, 1, 1)
        self.miATSGreen = QtWidgets.QLabel(parent=self.MatchInfo)
        self.miATSGreen.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-left: 2px solid black;\n"
                                    "border-top: 2px solid black;\n"
                                    "border-right: 2px solid black;\n"
                                    "border-bottom:4px solid black")
        self.miATSGreen.setObjectName("miATSGreen")
        self.MatchInfoTable.addWidget(self.miATSGreen, 2, 2, 1, 1)
        self.miHTSGreen = QtWidgets.QLabel(parent=self.MatchInfo)
        self.miHTSGreen.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-left: 2px solid black;\n"
                                    "border-top: 2px solid black;\n"
                                    "border-right: 2px solid black;\n"
                                    "border-bottom:4px solid black")
        self.miHTSGreen.setObjectName("miHTSGreen")
        self.MatchInfoTable.addWidget(self.miHTSGreen, 2, 3, 1, 1)
        self.mi180sGreen = QtWidgets.QLabel(parent=self.MatchInfo)
        self.mi180sGreen.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border :3px solid black;"
                                        "border-width : 2px 4px 4px 2px;"
                                        "border-top-left-radius :0px;"
                                        "border-top-right-radius : 0px; "
                                        "border-bottom-left-radius : 0px; "
                                        "border-bottom-right-radius : 15px")
        self.mi180sGreen.setObjectName("mi180sGreen")
        self.MatchInfoTable.addWidget(self.mi180sGreen, 2, 4, 1, 1)
        self.MatchInfoTable.setRowStretch(0, 2)
        self.MatchInfoTable.setRowStretch(1, 4)
        self.MatchInfoTable.setRowStretch(2, 4)
        self.verticalLayout_4.addLayout(self.MatchInfoTable)
        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 9)
        self.MainWindowStackedWidget.addWidget(self.MatchInfo)
        self.gridLayout.addWidget(self.MainWindowStackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.MainWindowWidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Function to resize the scoreboard and keep everything in order
    def retranslateUi(self, MainWindow):
        # Importing custom font
        id = QFontDatabase.addApplicationFont(".\\Assets\\Super Boys.ttf")
        if id < 0: print("Error")
        families = QFontDatabase.applicationFontFamilies(id)
        _translate = QtCore.QCoreApplication.translate

        # DON'T MESS WITH THIS EITHER, THIS DOES NOT NEED THE DATABASE
        self.MatchInfoTitle.setText(_translate("MainWindow", "Match Info"))
        self.MatchInfoTitle.setStyleSheet("background:transparent")
        self.miLTS.setText(_translate("MainWindow", "Lowest Turn Score"))
        self.miLTS.setFont(QFont(families[0], 14))
        self.miHTS.setText(_translate("MainWindow", "Highest Turn Score"))
        self.miHTS.setFont(QFont(families[0], 14))
        self.miATS.setText(_translate("MainWindow", "Average Turn Score"))
        self.miATS.setFont(QFont(families[0], 14))
        self.mi180s.setText(_translate("MainWindow", "# of 180\'s"))
        self.mi180s.setFont(QFont(families[0], 14))
        self.miPlayer.setText(_translate("MainWindow", "Player"))
        self.miPlayer.setFont(QFont(families[0], 14))

        # Labels with font for Competitor Info Scoreboard, this is the part of the code that may be needing stuff from the
        # database. The parts where it says ".setText()" for the "TextLabel" is stuff being pulled from the database. I have
        # already labeled what each is so it should be easier hopefully.

        # Player 1 Name
        self.miPlayerRed.setText(str(self.PlayerOne.get_last_name() + ", " + self.PlayerOne.get_first_name()))
        self.miPlayerRed.setFont(QFont(families[0], 12))
        # Player 1 Lowest Turn Score
        self.miLTSRed.setText(str(self.PlayerOne.get_lowest_turn_score()))
        self.miLTSRed.setFont(QFont(families[0], 12))
        # Player 1 Average Turn Score
        self.miATSRed.setText(str(self.PlayerOne.get_average_turn_score()))
        self.miATSRed.setFont(QFont(families[0], 12))
        # Player 1 Highest Turn Score
        self.miHTSRed.setText(str(self.PlayerOne.get_highest_turn_score()))
        self.miHTSRed.setFont(QFont(families[0], 12))
        # Player 1 # of 180's
        self.mi180sRed.setText(str(self.PlayerOne.get_num_180s()))
        self.mi180sRed.setFont(QFont(families[0], 12))
        # Player 2 Name
        self.miPlayerGreen.setText(str(self.PlayerTwo.get_last_name() + ", " + self.PlayerTwo.get_first_name()))
        self.miPlayerGreen.setFont(QFont(families[0], 12))
        # Player 2 Least Turn Score
        self.miLTSGreen.setText(str(self.PlayerTwo.get_lowest_turn_score()))
        self.miLTSGreen.setFont(QFont(families[0], 12))
        # Player 2 Average Turn Score
        self.miATSGreen.setText(str(self.PlayerTwo.get_average_turn_score()))
        self.miATSGreen.setFont(QFont(families[0], 12))
        # Player 2 Highest Turn Score
        self.miHTSGreen.setText(str(self.PlayerTwo.get_highest_turn_score()))
        self.miHTSGreen.setFont(QFont(families[0], 12))
        # Player 2 # of 180's
        self.mi180sGreen.setText(str(self.PlayerTwo.get_num_180s()))
        self.mi180sGreen.setFont(QFont(families[0], 12))


    def update_match_scoreboard(self):
        self.miPlayerRed.setText(str(self.PlayerOne.get_last_name() + ", " + self.PlayerOne.get_first_name()))
        self.miLTSRed.setText(str(self.PlayerOne.get_lowest_turn_score()))
        self.miATSRed.setText(str(self.PlayerOne.get_average_turn_score()))
        self.miHTSRed.setText(str(self.PlayerOne.get_highest_turn_score()))
        self.mi180sRed.setText(str(self.PlayerOne.get_num_180s()))

        self.miPlayerGreen.setText(str(self.PlayerTwo.get_last_name() + ", " + self.PlayerTwo.get_first_name()))
        self.miLTSGreen.setText(str(self.PlayerTwo.get_lowest_turn_score()))
        self.miATSGreen.setText(str(self.PlayerTwo.get_average_turn_score()))
        self.miHTSGreen.setText(str(self.PlayerTwo.get_highest_turn_score()))
        self.mi180sGreen.setText(str(self.PlayerTwo.get_num_180s()))
