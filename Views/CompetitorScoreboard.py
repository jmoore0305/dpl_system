from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import *
from PySide6.QtWidgets import QGraphicsColorizeEffect
from Controllers.PlayerController import PlayerController

class Competitor_Window(object):
    def __init__(self):
        player_controller = PlayerController()
        self.PlayerOne = player_controller.get_player_one()
        self.PlayerTwo = player_controller.get_player_two()
    def setupUi(self, MainWindow):
        # Importing custom font that we are using throughout this project

        id = QFontDatabase.addApplicationFont(".\\Assets\\Super Boys.ttf")
        if id < 0: print("Error")
        families = QFontDatabase.applicationFontFamilies(id)

        # Setting up the Main Window widget
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(552, 482)
        MainWindow.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop: 0 rgba(235,181,212,1.000), stop:1 rgba(142,221,241,1.000))")
        self.MainWindowWidget = QtWidgets.QWidget(parent=MainWindow)
        self.MainWindowWidget.setObjectName("MainWindowWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.MainWindowWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.MainWindowStackedWidget = QtWidgets.QStackedWidget(parent=self.MainWindowWidget)
        self.MainWindowStackedWidget.setObjectName("MainWindowStackedWidget")


        # Competitor Info Screen, everything from here on down is just laying everything out so note for Justin: don't worry
        # about this portion of the code. Your main part is really the retranslation part.
        self.CompetitorInfo = QtWidgets.QWidget()
        self.CompetitorInfo.setObjectName("CompetitorInfo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.CompetitorInfo)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.CompetitorInfoTitle = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.CompetitorInfoTitle.setMinimumSize(QtCore.QSize(0, 79))
        font = QtGui.QFont(families[0])
        font.setPointSize(36)
        self.CompetitorInfoTitle.setFont(font)
        self.CompetitorInfoTitle.setObjectName("CompetitorInfoTitle")
        self.verticalLayout_2.addWidget(self.CompetitorInfoTitle)
        self.CompetitorInfoTable = QtWidgets.QGridLayout()
        self.CompetitorInfoTable.setSpacing(0)
        self.CompetitorInfoTable.setObjectName("CompetitorInfoTable")
        self.ciFNRed = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.ciFNRed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-left: 4px solid black;\n"
                                    "border-top: 2px solid black;\n"
                                    "border-right: 2px solid black;\n"
                                    "border-bottom:2px solid black")
        self.ciFNRed.setObjectName("ciFNRed")
        self.CompetitorInfoTable.addWidget(self.ciFNRed, 1, 0, 1, 1)
        self.ciFN = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.ciFN.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "border :3px solid black;"
                                "border-width : 4px 2px 2px 4px;"
                                "border-top-left-radius :15px;"
                                "border-top-right-radius : 0px; "
                                "border-bottom-left-radius : 0px; "
                                "border-bottom-right-radius : 0px")
        self.ciFN.setObjectName("ciFN")
        self.CompetitorInfoTable.addWidget(self.ciFN, 0, 0, 1, 1)
        self.ciLW = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.ciLW.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "border-left: 2px solid black;\n"
                                "border-top: 4px solid black;\n"
                                "border-right: 2px solid black;\n"
                                "border-bottom:2px solid black")
        self.ciLW.setObjectName("ciLW")
        self.CompetitorInfoTable.addWidget(self.ciLW, 0, 3, 1, 1)
        self.ciCR = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.ciCR.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "border-left: 2px solid black;\n"
                                "border-top: 4px solid black;\n"
                                "border-right: 2px solid black;\n"
                                "border-bottom:2px solid black")
        self.ciCR.setObjectName("ciCR")
        self.CompetitorInfoTable.addWidget(self.ciCR, 0, 2, 1, 1)
        self.ciLN = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.ciLN.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "border-left: 2px solid black;\n"
                                "border-top: 4px solid black;\n"
                                "border-right: 2px solid black;\n"
                                "border-bottom:2px solid black")
        self.ciLN.setObjectName("ciLN")
        self.CompetitorInfoTable.addWidget(self.ciLN, 0, 1, 1, 1)
        self.ci180s = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.ci180s.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "border :3px solid black;"
                                "border-width : 4px 4px 2px 2px;"
                                "border-top-left-radius : 0px;"
                                "border-top-right-radius : 15px; "
                                "border-bottom-left-radius : 0px; "
                                "border-bottom-right-radius : 0px")
        self.ci180s.setObjectName("ci180s")
        self.CompetitorInfoTable.addWidget(self.ci180s, 0, 5, 1, 1)
        self.ciAvgSS = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.ciAvgSS.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-left: 2px solid black;\n"
                                    "border-top: 4px solid black;\n"
                                    "border-right: 2px solid black;\n"
                                    "border-bottom:2px solid black")
        self.ciAvgSS.setObjectName("ciAvgSS")
        self.CompetitorInfoTable.addWidget(self.ciAvgSS, 0, 4, 1, 1)
        self.ciLNRed = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.ciLNRed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-left: 2px solid black;\n"
                                    "border-top: 2px solid black;\n"
                                    "border-right: 2px solid black;\n"
                                    "border-bottom:2px solid black")
        self.ciLNRed.setObjectName("ciLNRed")
        self.CompetitorInfoTable.addWidget(self.ciLNRed, 1, 1, 1, 1)
        self.ciAvgSSRed = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.ciAvgSSRed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-left: 2px solid black;\n"
                                    "border-top: 2px solid black;\n"
                                    "border-right: 2px solid black;\n"
                                    "border-bottom:2px solid black")
        self.ciAvgSSRed.setObjectName("ciAvgSSRed")
        self.CompetitorInfoTable.addWidget(self.ciAvgSSRed, 1, 4, 1, 1)
        self.ciCRRed = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.ciCRRed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-left: 2px solid black;\n"
                                    "border-top: 2px solid black;\n"
                                    "border-right: 2px solid black;\n"
                                    "border-bottom:2px solid black")
        self.ciCRRed.setObjectName("ciCRRed")
        self.CompetitorInfoTable.addWidget(self.ciCRRed, 1, 2, 1, 1)
        self.ciLWRed = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.ciLWRed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-left: 2px solid black;\n"
                                    "border-top: 2px solid black;\n"
                                    "border-right: 2px solid black;\n"
                                    "border-bottom:2px solid black")
        self.ciLWRed.setObjectName("ciLWRed")
        self.CompetitorInfoTable.addWidget(self.ciLWRed, 1, 3, 1, 1)
        self.ci180sRed = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.ci180sRed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-left: 2px solid black;\n"
                                    "border-top: 2px solid black;\n"
                                    "border-right: 4px solid black;\n"
                                    "border-bottom:2px solid black")
        self.ci180sRed.setObjectName("ci180sRed")
        self.CompetitorInfoTable.addWidget(self.ci180sRed, 1, 5, 1, 1)
        self.ciFNGreen = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.ciFNGreen.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                  "border :3px solid black;"
                                  "border-width : 2px 2px 4px 4px;"
                                  "border-top-left-radius : 0px;"
                                  "border-top-right-radius : 0px; "
                                  "border-bottom-left-radius : 15px; "
                                  "border-bottom-right-radius : 0px")
        self.ciFNGreen.setObjectName("ciFNGreen")
        self.CompetitorInfoTable.addWidget(self.ciFNGreen, 2, 0, 1, 1)
        self.ciLNGreen = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.ciLNGreen.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-left: 2px solid black;\n"
                                    "border-top: 2px solid black;\n"
                                    "border-right: 2px solid black;\n"
                                    "border-bottom:4px solid black")
        self.ciLNGreen.setObjectName("ciLNGreen")
        self.CompetitorInfoTable.addWidget(self.ciLNGreen, 2, 1, 1, 1)
        self.ciCRGreen = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.ciCRGreen.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-left: 2px solid black;\n"
                                    "border-top: 2px solid black;\n"
                                    "border-right: 2px solid black;\n"
                                    "border-bottom:4px solid black")
        self.ciCRGreen.setObjectName("ciCRGreen")
        self.CompetitorInfoTable.addWidget(self.ciCRGreen, 2, 2, 1, 1)
        self.ciLWGreen = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.ciLWGreen.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-left: 2px solid black;\n"
                                    "border-top: 2px solid black;\n"
                                    "border-right: 2px solid black;\n"
                                    "border-bottom:4px solid black")
        self.ciLWGreen.setObjectName("ciLWGreen")
        self.CompetitorInfoTable.addWidget(self.ciLWGreen, 2, 3, 1, 1)
        self.ciAvgSSGreen = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.ciAvgSSGreen.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 2px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:4px solid black")
        self.ciAvgSSGreen.setObjectName("ciAvgSSGreen")
        self.CompetitorInfoTable.addWidget(self.ciAvgSSGreen, 2, 4, 1, 1)
        self.ci180sGreen = QtWidgets.QLabel(parent=self.CompetitorInfo)
        self.ci180sGreen.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "border :3px solid black;"
                                     "border-width : 2px 4px 4px 2px;"
                                     "border-top-left-radius : 0px;"
                                     "border-top-right-radius : 0px; "
                                     "border-bottom-left-radius : 0px; "
                                     "border-bottom-right-radius : 15px")
        self.ci180sGreen.setObjectName("ci180sGreen")
        self.CompetitorInfoTable.addWidget(self.ci180sGreen, 2, 5, 1, 1)
        self.verticalLayout_2.addLayout(self.CompetitorInfoTable)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 9)
        self.MainWindowStackedWidget.addWidget(self.CompetitorInfo)
        self.gridLayout.addWidget(self.MainWindowStackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.MainWindowWidget)
        self.retranslateUi(MainWindow)
        self.MainWindowStackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Function to resize the scoreboard and keep everything in order
    def retranslateUi(self, MainWindow):
        # Importing custom font
        id = QFontDatabase.addApplicationFont(".\\Assets\\Super Boys.ttf")
        if id < 0: print("Error")
        families = QFontDatabase.applicationFontFamilies(id)


        _translate = QtCore.QCoreApplication.translate

        # DON'T MESS WITH THIS EITHER, THIS DOES NOT NEED THE DATABASE
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CompetitorInfoTitle.setText(_translate("MainWindow", "Competitor Info"))
        self.CompetitorInfoTitle.setStyleSheet("background:transparent")
        self.ciFN.setText(_translate("MainWindow", "First Name"))
        self.ciFN.setFont(QFont(families[0], 14))
        self.ciLW.setText(_translate("MainWindow", "Last Win"))
        self.ciLW.setFont(QFont(families[0], 14))
        self.ciCR.setText(_translate("MainWindow", "Current Rank"))
        self.ciCR.setFont(QFont(families[0], 14))
        self.ciLN.setText(_translate("MainWindow", "Last Name"))
        self.ciLN.setFont(QFont(families[0], 14))
        self.ci180s.setText(_translate("MainWindow", "# 180\'s in Season"))
        self.ci180s.setFont(QFont(families[0], 14))
        self.ciAvgSS.setText(_translate("MainWindow", "Avg. Score For Season"))
        self.ciAvgSS.setFont(QFont(families[0], 14))

        # Labels with font for Competitor Info Scoreboard, this is the part of the code that may be needing stuff from the
        # database. The parts where it says ".setText()" for the "TextLabel" is stuff being pulled from the database. I have
        # already labeled what each is so it should be easier hopefully.


        # Player 1 Average Score for Season
        self.ciAvgSSRed.setText(_translate("MainWindow", "TextLabel"))
        self.ciAvgSSRed.setFont(QFont(families[0], 12))
        # Player 1 Current Rank
        self.ciCRRed.setText(_translate("MainWindow", "TextLabel"))
        self.ciCRRed.setFont(QFont(families[0], 12))
        # Player 1 Last Win
        self.ciLWRed.setText(_translate("MainWindow", "TextLabel"))
        self.ciLWRed.setFont(QFont(families[0], 12))
        # Player 1 # of 180s
        self.ci180sRed.setText(_translate("MainWindow", "TextLabel"))
        self.ci180sRed.setFont(QFont(families[0], 12))





        # Player 2 Current Rank
        self.ciCRGreen.setText(_translate("MainWindow", "TextLabel"))
        self.ciCRGreen.setFont(QFont(families[0], 12))
        # Player 2 Last Win
        self.ciLWGreen.setText(_translate("MainWindow", "TextLabel"))
        self.ciLWGreen.setFont(QFont(families[0], 12))
        # Player 2 Average Score for Season
        self.ciAvgSSGreen.setText(_translate("MainWindow", "TextLabel"))
        self.ciAvgSSGreen.setFont(QFont(families[0], 12))
        # Player 2 # of 180's
        self.ci180sGreen.setText(_translate("MainWindow", "TextLabel"))
        self.ci180sGreen.setFont(QFont(families[0], 12))


        #Setting up the stuff for the first time the window is opened
        self.ciFNRed.setText(str(self.PlayerOne.get_first_name()))
        self.ciFNRed.setFont(QFont(families[0], 12))

        # Player 1 Legs
        self.ciFNGreen.setText(str(self.PlayerTwo.get_first_name()))
        self.ciFNGreen.setFont(QFont(families[0], 12))

        self.ciLNRed.setText(str(self.PlayerOne.get_last_name()))
        self.ciFNGreen.setFont(QFont(families[0], 12))

        self.ciLNGreen.setText(str(self.PlayerTwo.get_last_name()))
        self.ciFNGreen.setFont(QFont(families[0], 12))

    def update_competitor_scoreboard(self):


        self.ciFNRed.setText(str(self.PlayerOne.get_first_name()))
        self.ciLNRed.setText(str(self.PlayerOne.get_last_name()))
        self.ciAvgSSRed.setText(str(self.PlayerOne.get_average_score_for_season()))
        self.ci180sRed.setText(str(self.PlayerOne.get_number_of_180s_for_season()))
        self.ciCRRed.setText(str(self.PlayerOne.get_current_rank_for_season()))
        self.ciLWRed.setText(str(self.PlayerOne.get_last_win_for_season()))


        self.ciFNGreen.setText(str(self.PlayerTwo.get_first_name()))
        self.ciLNGreen.setText(str(self.PlayerTwo.get_last_name()))
        self.ciAvgSSGreen.setText(str(self.PlayerTwo.get_average_score_for_season()))
        self.ci180sGreen.setText(str(self.PlayerTwo.get_number_of_180s_for_season()))
        self.ciCRGreen.setText(str(self.PlayerTwo.get_current_rank_for_season()))
        self.ciLWGreen.setText(str(self.PlayerTwo.get_last_win_for_season()))



