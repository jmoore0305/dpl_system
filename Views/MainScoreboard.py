from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import *
from PySide6.QtWidgets import QGraphicsColorizeEffect, QMainWindow
from Controllers.MainScoreboardController import MainScoreboardController
from Controllers.PlayerController import PlayerController
class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self._MainScoreboardController = MainScoreboardController()
        player_controller = PlayerController()
        self.PlayerOne = player_controller.get_player_one()
        self.PlayerTwo = player_controller.get_player_two()
        self.setupUi()

    def setupUi(self):
        # Importing custom font and adding it to this program
        id = QFontDatabase.addApplicationFont(".\\Assets\\Super Boys.ttf")
        if id < 0:
            print("Error")
        families = QFontDatabase.applicationFontFamilies(id)

        self.setObjectName("Main_Window")
        self.resize(552, 482)
        self.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop: 0 rgba(235,181,212,1.000), stop:1 rgba(142,221,241,1.000))")

        # DON'T MESS WITH THIS, THIS DOES NOT NEED THE DATABASE
        self.MainWindowWidget = QtWidgets.QWidget(parent=self)
        self.MainWindowWidget.setObjectName("MainWindowWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.MainWindowWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.MainWindowStackedWidget = QtWidgets.QStackedWidget(parent=self.MainWindowWidget)
        self.MainWindowStackedWidget.setObjectName("MainWindowStackedWidget")

        # Main scoreboard
        self.DartsThrown = QtWidgets.QWidget()
        self.DartsThrown.setObjectName("DartsThrown")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.DartsThrown)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.DartsThrownTitle = QtWidgets.QLabel(parent=self.DartsThrown)
        self.DartsThrownTitle.setMinimumSize(QtCore.QSize(0, 79))
        font = QtGui.QFont(families[0])
        font.setPointSize(36)
        self.DartsThrownTitle.setFont(font)
        self.DartsThrownTitle.setObjectName("DartsThrownTitle")
        self.verticalLayout_3.addWidget(self.DartsThrownTitle)
        self.DartThrownGrid = QtWidgets.QGridLayout()
        self.DartThrownGrid.setSpacing(0)
        self.DartThrownGrid.setObjectName("DartThrownGrid")
        self.label_RedWinningThrows = QtWidgets.QLabel(parent=self.DartsThrown)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_RedWinningThrows.sizePolicy().hasHeightForWidth())
        self.label_RedWinningThrows.setSizePolicy(sizePolicy)
        self.label_RedWinningThrows.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "border-left: 2px solid black;\n"
                                                "border-top: 2px solid black;\n"
                                                "border-right: 4px solid black;\n"
                                                "border-bottom:2px solid black")
        self.label_RedWinningThrows.setObjectName("label_RedWinningThrows")
        self.DartThrownGrid.addWidget(self.label_RedWinningThrows, 1, 3, 1, 1)
        self.label_RedLegs = QtWidgets.QLabel(parent=self.DartsThrown)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_RedLegs.sizePolicy().hasHeightForWidth())
        self.label_RedLegs.setSizePolicy(sizePolicy)
        self.label_RedLegs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 2px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:2px solid black")
        self.label_RedLegs.setObjectName("label_RedLegs")
        self.DartThrownGrid.addWidget(self.label_RedLegs, 1, 1, 1, 1)
        self.label_RedName = QtWidgets.QLabel(parent=self.DartsThrown)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_RedName.sizePolicy().hasHeightForWidth())
        self.label_RedName.setSizePolicy(sizePolicy)
        self.label_RedName.setMinimumSize(QtCore.QSize(0, 60))
        self.label_RedName.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 4px solid black;\n"
                                        "border-top: 2px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:2px solid black")
        self.label_RedName.setObjectName("label_RedName")
        self.DartThrownGrid.addWidget(self.label_RedName, 1, 0, 1, 1)
        self.label_Legs = QtWidgets.QLabel(parent=self.DartsThrown)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_Legs.sizePolicy().hasHeightForWidth())
        self.label_Legs.setSizePolicy(sizePolicy)
        self.label_Legs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 4px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:2px solid black")
        self.label_Legs.setObjectName("label_Legs")
        self.DartThrownGrid.addWidget(self.label_Legs, 0, 1, 1, 1)
        self.label_Competitors = QtWidgets.QLabel(parent=self.DartsThrown)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_Competitors.sizePolicy().hasHeightForWidth())
        self.label_Competitors.setSizePolicy(sizePolicy)
        self.label_Competitors.setMinimumSize(QtCore.QSize(0, 25))
        self.label_Competitors.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border :3px solid black;"
                                        "border-width : 4px 2px 2px 4px;"
                                        "border-top-left-radius :15px;"
                                        "border-top-right-radius : 0px; "
                                        "border-bottom-left-radius : 0px; "
                                        "border-bottom-right-radius : 0px")
        self.label_Competitors.setObjectName("label_Competitors")
        self.DartThrownGrid.addWidget(self.label_Competitors, 0, 0, 1, 1)
        self.label_Score = QtWidgets.QLabel(parent=self.DartsThrown)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_Score.sizePolicy().hasHeightForWidth())
        self.label_Score.setSizePolicy(sizePolicy)
        self.label_Score.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 4px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:2px solid black")
        self.label_Score.setObjectName("label_Score")
        self.DartThrownGrid.addWidget(self.label_Score, 0, 2, 1, 1)
        self.label_WinningThrows = QtWidgets.QLabel(parent=self.DartsThrown)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_WinningThrows.sizePolicy().hasHeightForWidth())
        self.label_WinningThrows.setSizePolicy(sizePolicy)
        self.label_WinningThrows.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "border :3px solid black;"
                                                "border-width : 4px 4px 2px 2px;"
                                                "border-top-left-radius : 0px;"
                                                 "border-top-right-radius : 15px; "
                                                "border-bottom-left-radius : 0px; "
                                                "border-bottom-right-radius : 0px")
        self.label_WinningThrows.setObjectName("label_WinningThrows")
        self.DartThrownGrid.addWidget(self.label_WinningThrows, 0, 3, 1, 1)
        self.label_RedScore = QtWidgets.QLabel(parent=self.DartsThrown)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_RedScore.sizePolicy().hasHeightForWidth())
        self.label_RedScore.setSizePolicy(sizePolicy)
        self.label_RedScore.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 2px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:2px solid black")
        self.label_RedScore.setObjectName("label_RedScore")
        self.DartThrownGrid.addWidget(self.label_RedScore, 1, 2, 1, 1)
        self.label_GreenName = QtWidgets.QLabel(parent=self.DartsThrown)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_GreenName.sizePolicy().hasHeightForWidth())
        self.label_GreenName.setSizePolicy(sizePolicy)
        self.label_GreenName.setMinimumSize(QtCore.QSize(0, 60))
        self.label_GreenName.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "border :3px solid black;"
                                             "border-width : 2px 2px 4px 4px;"
                                             "border-top-left-radius :0px;"
                                             "border-top-right-radius : 0px; "
                                             "border-bottom-left-radius : 15px; "
                                             "border-bottom-right-radius : 0px")
        self.label_GreenName.setObjectName("label_GreenName")
        self.DartThrownGrid.addWidget(self.label_GreenName, 2, 0, 1, 1)
        self.label_GreenLegs = QtWidgets.QLabel(parent=self.DartsThrown)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_GreenLegs.sizePolicy().hasHeightForWidth())
        self.label_GreenLegs.setSizePolicy(sizePolicy)
        self.label_GreenLegs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-left: 2px solid black;\n"
                                            "border-top: 2px solid black;\n"
                                            "border-right: 2px solid black;\n"
                                            "border-bottom:4px solid black")
        self.label_GreenLegs.setObjectName("label_GreenLegs")
        self.DartThrownGrid.addWidget(self.label_GreenLegs, 2, 1, 1, 1)
        self.label_GreenScore = QtWidgets.QLabel(parent=self.DartsThrown)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_GreenScore.sizePolicy().hasHeightForWidth())
        self.label_GreenScore.setSizePolicy(sizePolicy)
        self.label_GreenScore.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-left: 2px solid black;\n"
                                            "border-top: 2px solid black;\n"
                                            "border-right: 2px solid black;\n"
                                            "border-bottom:4px solid black")
        self.label_GreenScore.setObjectName("label_GreenScore")
        self.DartThrownGrid.addWidget(self.label_GreenScore, 2, 2, 1, 1)
        self.label_GreenWinningThrows = QtWidgets.QLabel(parent=self.DartsThrown)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_GreenWinningThrows.sizePolicy().hasHeightForWidth())
        self.label_GreenWinningThrows.setSizePolicy(sizePolicy)
        self.label_GreenWinningThrows.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "border :3px solid black;"
                                           "border-width : 2px 4px 4px 2px;"
                                           "border-top-left-radius :0px;"
                                           "border-top-right-radius : 0px; "
                                           "border-bottom-left-radius : 0px; "
                                           "border-bottom-right-radius : 15px")
        self.label_GreenWinningThrows.setObjectName("label_GreenWinningThrows")
        self.DartThrownGrid.addWidget(self.label_GreenWinningThrows, 2, 3, 1, 1)
        self.verticalLayout_3.addLayout(self.DartThrownGrid)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(15, -1, 15, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        # Red's dart throw history table
        self.RedSubLayout = QtWidgets.QVBoxLayout()
        self.RedSubLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.RedSubLayout.setObjectName("RedSubLayout")
        self.RedDartsThrown = QtWidgets.QLabel(parent=self.DartsThrown)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RedDartsThrown.sizePolicy().hasHeightForWidth())
        self.RedDartsThrown.setSizePolicy(sizePolicy)
        font = QtGui.QFont(families[0])
        font.setPointSize(14)
        self.RedDartsThrown.setFont(font)
        self.RedDartsThrown.setStyleSheet("color: rgb(255, 0, 0);")
        self.RedDartsThrown.setObjectName("RedDartsThrown")
        self.RedSubLayout.addWidget(self.RedDartsThrown)
        self.RedDartBoxLayout = QtWidgets.QHBoxLayout()
        self.RedDartBoxLayout.setSpacing(0)
        self.RedDartBoxLayout.setObjectName("RedDartBoxLayout")
        self.RedDartBox = QtWidgets.QLabel(parent=self.DartsThrown)
        self.RedDartBox.setMinimumSize(QtCore.QSize(50, 50))
        self.RedDartBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "border :3px solid black;"
                                           "border-width : 4px 2px 4px 4px;"
                                           "border-top-left-radius :15px;"
                                           "border-top-right-radius : 0px; "
                                           "border-bottom-left-radius : 15px; "
                                           "border-bottom-right-radius : 0px")
        self.RedDartBox.setText("")
        self.RedDartBox.setObjectName("RedDartBox")
        self.RedDartBoxLayout.addWidget(self.RedDartBox)
        self.RedDartBox_2 = QtWidgets.QLabel(parent=self.DartsThrown)
        self.RedDartBox_2.setMinimumSize(QtCore.QSize(50, 50))
        self.RedDartBox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 4px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:4px solid black")
        self.RedDartBox_2.setText("")
        self.RedDartBox_2.setObjectName("RedDartBox_2")
        self.RedDartBoxLayout.addWidget(self.RedDartBox_2)
        self.RedDartBox_3 = QtWidgets.QLabel(parent=self.DartsThrown)
        self.RedDartBox_3.setMinimumSize(QtCore.QSize(50, 50))
        self.RedDartBox_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 4px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:4px solid black")
        self.RedDartBox_3.setText("")
        self.RedDartBox_3.setObjectName("RedDartBox_3")
        self.RedDartBoxLayout.addWidget(self.RedDartBox_3)
        self.RedDartBox_4 = QtWidgets.QLabel(parent=self.DartsThrown)
        self.RedDartBox_4.setMinimumSize(QtCore.QSize(50, 50))
        self.RedDartBox_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 4px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:4px solid black")
        self.RedDartBox_4.setText("")
        self.RedDartBox_4.setObjectName("RedDartBox_4")
        self.RedDartBoxLayout.addWidget(self.RedDartBox_4)
        self.RedDartBox_5 = QtWidgets.QLabel(parent=self.DartsThrown)
        self.RedDartBox_5.setMinimumSize(QtCore.QSize(50, 50))
        self.RedDartBox_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 4px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:4px solid black")
        self.RedDartBox_5.setText("")
        self.RedDartBox_5.setObjectName("RedDartBox_5")
        self.RedDartBoxLayout.addWidget(self.RedDartBox_5)
        self.RedDartBox_6 = QtWidgets.QLabel(parent=self.DartsThrown)
        self.RedDartBox_6.setMinimumSize(QtCore.QSize(50, 50))
        self.RedDartBox_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 4px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:4px solid black")
        self.RedDartBox_6.setText("")
        self.RedDartBox_6.setObjectName("RedDartBox_6")
        self.RedDartBoxLayout.addWidget(self.RedDartBox_6)
        self.RedDartBox_7 = QtWidgets.QLabel(parent=self.DartsThrown)
        self.RedDartBox_7.setMinimumSize(QtCore.QSize(50, 50))
        self.RedDartBox_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 4px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:4px solid black")
        self.RedDartBox_7.setText("")
        self.RedDartBox_7.setObjectName("RedDartBox_7")
        self.RedDartBoxLayout.addWidget(self.RedDartBox_7)
        self.RedDartBox_8 = QtWidgets.QLabel(parent=self.DartsThrown)
        self.RedDartBox_8.setMinimumSize(QtCore.QSize(50, 50))
        self.RedDartBox_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 4px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:4px solid black")
        self.RedDartBox_8.setText("")
        self.RedDartBox_8.setObjectName("RedDartBox_8")
        self.RedDartBoxLayout.addWidget(self.RedDartBox_8)
        self.RedDartBox_9 = QtWidgets.QLabel(parent=self.DartsThrown)
        self.RedDartBox_9.setMinimumSize(QtCore.QSize(50, 50))
        self.RedDartBox_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 4px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:4px solid black")
        self.RedDartBox_9.setText("")
        self.RedDartBox_9.setObjectName("RedDartBox_9")
        self.RedDartBoxLayout.addWidget(self.RedDartBox_9)
        self.RedDartBox_10 = QtWidgets.QLabel(parent=self.DartsThrown)
        self.RedDartBox_10.setMinimumSize(QtCore.QSize(50, 50))
        self.RedDartBox_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border :3px solid black;"
                                      "border-width : 4px 4px 4px 2px;"
                                      "border-top-left-radius :0px;"
                                      "border-top-right-radius : 15px; "
                                      "border-bottom-left-radius : 0px; "
                                      "border-bottom-right-radius : 15px")
        self.RedDartBox_10.setText("")
        self.RedDartBox_10.setObjectName("RedDartBox_10")
        self.RedDartBoxLayout.addWidget(self.RedDartBox_10)
        self.RedSubLayout.addLayout(self.RedDartBoxLayout)
        self.verticalLayout_5.addLayout(self.RedSubLayout)

        # Green's dart thrown match history table
        self.GreenSubLayout = QtWidgets.QVBoxLayout()
        self.GreenSubLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.GreenSubLayout.setObjectName("GreenSubLayout")
        self.GreenDartsThrown = QtWidgets.QLabel(parent=self.DartsThrown)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GreenDartsThrown.sizePolicy().hasHeightForWidth())
        self.GreenDartsThrown.setSizePolicy(sizePolicy)
        font = QtGui.QFont(families[0])
        font.setPointSize(14)
        self.GreenDartsThrown.setFont(font)
        self.GreenDartsThrown.setStyleSheet("color: rgb(0, 169, 0);")
        self.GreenDartsThrown.setObjectName("GreenDartsThrown")
        self.GreenSubLayout.addWidget(self.GreenDartsThrown)
        self.GreenDartBoxLayout = QtWidgets.QHBoxLayout()
        self.GreenDartBoxLayout.setSpacing(0)
        self.GreenDartBoxLayout.setObjectName("GreenDartBoxLayout")
        self.GreenDartBox = QtWidgets.QLabel(parent=self.DartsThrown)
        self.GreenDartBox.setMinimumSize(QtCore.QSize(50, 50))
        self.GreenDartBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border :3px solid black;"
                                         "border-width : 4px 2px 4px 4px;"
                                         "border-top-left-radius :15px;"
                                         "border-top-right-radius : 0px; "
                                         "border-bottom-left-radius : 15px; "
                                         "border-bottom-right-radius : 0px")
        self.GreenDartBox.setText("")
        self.GreenDartBox.setObjectName("GreenDartBox")
        self.GreenDartBoxLayout.addWidget(self.GreenDartBox)
        self.GreenDartBox_2 = QtWidgets.QLabel(parent=self.DartsThrown)
        self.GreenDartBox_2.setMinimumSize(QtCore.QSize(50, 50))
        self.GreenDartBox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 4px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:4px solid black")
        self.GreenDartBox_2.setText("")
        self.GreenDartBox_2.setObjectName("GreenDartBox_2")
        self.GreenDartBoxLayout.addWidget(self.GreenDartBox_2)
        self.GreenDartBox_3 = QtWidgets.QLabel(parent=self.DartsThrown)
        self.GreenDartBox_3.setMinimumSize(QtCore.QSize(50, 50))
        self.GreenDartBox_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 4px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:4px solid black")
        self.GreenDartBox_3.setText("")
        self.GreenDartBox_3.setObjectName("GreenDartBox_3")
        self.GreenDartBoxLayout.addWidget(self.GreenDartBox_3)
        self.GreenDartBox_4 = QtWidgets.QLabel(parent=self.DartsThrown)
        self.GreenDartBox_4.setMinimumSize(QtCore.QSize(50, 50))
        self.GreenDartBox_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 4px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:4px solid black")
        self.GreenDartBox_4.setText("")
        self.GreenDartBox_4.setObjectName("GreenDartBox_4")
        self.GreenDartBoxLayout.addWidget(self.GreenDartBox_4)
        self.GreenDartBox_5 = QtWidgets.QLabel(parent=self.DartsThrown)
        self.GreenDartBox_5.setMinimumSize(QtCore.QSize(50, 50))
        self.GreenDartBox_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 4px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:4px solid black")
        self.GreenDartBox_5.setText("")
        self.GreenDartBox_5.setObjectName("GreenDartBox_5")
        self.GreenDartBoxLayout.addWidget(self.GreenDartBox_5)
        self.GreenDartBox_6 = QtWidgets.QLabel(parent=self.DartsThrown)
        self.GreenDartBox_6.setMinimumSize(QtCore.QSize(50, 50))
        self.GreenDartBox_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 4px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:4px solid black")
        self.GreenDartBox_6.setText("")
        self.GreenDartBox_6.setObjectName("GreenDartBox_6")
        self.GreenDartBoxLayout.addWidget(self.GreenDartBox_6)
        self.GreenDartBox_7 = QtWidgets.QLabel(parent=self.DartsThrown)
        self.GreenDartBox_7.setMinimumSize(QtCore.QSize(50, 50))
        self.GreenDartBox_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 4px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:4px solid black")
        self.GreenDartBox_7.setText("")
        self.GreenDartBox_7.setObjectName("GreenDartBox_7")
        self.GreenDartBoxLayout.addWidget(self.GreenDartBox_7)
        self.GreenDartBox_8 = QtWidgets.QLabel(parent=self.DartsThrown)
        self.GreenDartBox_8.setMinimumSize(QtCore.QSize(50, 50))
        self.GreenDartBox_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 4px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:4px solid black")
        self.GreenDartBox_8.setText("")
        self.GreenDartBox_8.setObjectName("GreenDartBox_8")
        self.GreenDartBoxLayout.addWidget(self.GreenDartBox_8)
        self.GreenDartBox_9 = QtWidgets.QLabel(parent=self.DartsThrown)
        self.GreenDartBox_9.setMinimumSize(QtCore.QSize(50, 50))
        self.GreenDartBox_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-left: 2px solid black;\n"
                                        "border-top: 4px solid black;\n"
                                        "border-right: 2px solid black;\n"
                                        "border-bottom:4px solid black")
        self.GreenDartBox_9.setText("")
        self.GreenDartBox_9.setObjectName("GreenDartBox_9")
        self.GreenDartBoxLayout.addWidget(self.GreenDartBox_9)
        self.GreenDartBox_10 = QtWidgets.QLabel(parent=self.DartsThrown)
        self.GreenDartBox_10.setMinimumSize(QtCore.QSize(50, 50))
        self.GreenDartBox_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border :3px solid black;"
                                        "border-width : 4px 4px 4px 2px;"
                                        "border-top-left-radius :0px;"
                                        "border-top-right-radius : 15px; "
                                        "border-bottom-left-radius : 0px; "
                                        "border-bottom-right-radius : 15px")
        self.GreenDartBox_10.setText("")
        self.GreenDartBox_10.setObjectName("GreenDartBox_10")
        self.GreenDartBoxLayout.addWidget(self.GreenDartBox_10)
        self.GreenSubLayout.addLayout(self.GreenDartBoxLayout)
        self.verticalLayout_5.addLayout(self.GreenSubLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 4)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 4)
        self.MainWindowStackedWidget.addWidget(self.DartsThrown)

        self.gridLayout.addWidget(self.MainWindowStackedWidget, 0, 0, 1, 1)

        self.setCentralWidget(self.MainWindowWidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    # Function to resize the scoreboard and keep everything in order
    def retranslateUi(self):
        # Importing custom font
        # Importing custom font and adding it to this program
        id = QFontDatabase.addApplicationFont(".\\Assets\\Super Boys.ttf")
        if id < 0:
            print("Error")
        families = QFontDatabase.applicationFontFamilies(id)

        # DON'T MESS WITH THIS EITHER, THIS DOES NOT NEED THE DATABASE
        self.DartsThrownTitle.setText("Main Scoreboard")
        self.DartsThrownTitle.setStyleSheet("background:transparent")
        self.label_Competitors.setText("Competitors")
        self.label_Competitors.setFont(QFont(families[0], 14))
        self.label_Score.setText("Score")
        self.label_Score.setFont(QFont(families[0], 14))
        self.label_WinningThrows.setText("Winning Throws")
        self.label_WinningThrows.setFont(QFont(families[0], 14))
        self.label_Legs.setText("Legs Won")
        self.label_Legs.setFont(QFont(families[0], 14))
        self.RedDartsThrown.setText(self.PlayerOne.get_last_name() + "," + self.PlayerOne.get_first_name() + ": Darts Thrown")

        color_effect = QGraphicsColorizeEffect()
        color_effect.setColor(QColor(qRgb(255, 0, 0)))
        self.RedDartsThrown.setGraphicsEffect(color_effect)
        self.RedDartsThrown.setStyleSheet("background:transparent")
        self.GreenDartsThrown.setText(self.PlayerTwo.get_last_name() + "," + self.PlayerTwo.get_first_name() + ": Darts Thrown")

        self.GreenDartsThrown.setStyleSheet("background:transparent")
        color_effect2 = QGraphicsColorizeEffect()
        color_effect2.setColor(QColor(qRgb(2, 153, 9)))
        self.GreenDartsThrown.setGraphicsEffect(color_effect2)

        # Labels with font for Competitor Info Scoreboard, this is the part of the code that may be needing stuff from the
        # database. The parts where it says ".setText()" for the "TextLabel" is stuff being pulled from the database. I have
        # already labeled what each is so it should be easier hopefully.
        # Player 1 Winning Throws
        self.label_RedWinningThrows.setText("")  # Setting to empty string
        self.label_RedWinningThrows.setFont(QFont(families[0], 12))

        # Player 1 Legs
        self.label_RedLegs.setText(str(self.PlayerOne.get_legs_won()))  # Setting to empty string
        self.label_RedLegs.setFont(QFont(families[0], 12))

        # Player 1 Name
        self.label_RedName.setText(str(self.PlayerOne.get_first_name()))  # Setting to empty string
        self.label_RedName.setFont(QFont(families[0], 12))

        # Player 1 Score
        self.label_RedScore.setText(str(self.PlayerOne.get_score()))  # Setting to empty string
        self.label_RedScore.setFont(QFont(families[0], 12))

        # Player 2 Name
        self.label_GreenName.setText(str(self.PlayerTwo.get_first_name()))  # Setting to empty string
        self.label_GreenName.setFont(QFont(families[0], 12))

        # Player 2 Legs
        self.label_GreenLegs.setText(str(self.PlayerTwo.get_legs_won()))  # Setting to empty string
        self.label_GreenLegs.setFont(QFont(families[0], 12))

        # Player 2 Score
        self.label_GreenScore.setText(str(self.PlayerTwo.get_score()))  # Setting to empty string
        self.label_GreenScore.setFont(QFont(families[0], 12))

        # Player 2 Winning Throws
        self.label_GreenWinningThrows.setText("")  # Setting to empty string
        self.label_GreenWinningThrows.setFont(QFont(families[0], 12))

        # Player 1's Dart History. Everything is ordered according to the number.
        self.RedDartBox.setText("")
        self.RedDartBox.setFont(QFont(families[0], 12))
        self.RedDartBox_2.setText("")
        self.RedDartBox_2.setFont(QFont(families[0], 12))
        self.RedDartBox_3.setText("")
        self.RedDartBox_3.setFont(QFont(families[0], 12))
        self.RedDartBox_4.setText("")
        self.RedDartBox_4.setFont(QFont(families[0], 12))
        self.RedDartBox_5.setText("")
        self.RedDartBox_5.setFont(QFont(families[0], 12))
        self.RedDartBox_6.setText("")
        self.RedDartBox_6.setFont(QFont(families[0], 12))
        self.RedDartBox_7.setText("")
        self.RedDartBox_7.setFont(QFont(families[0], 12))
        self.RedDartBox_8.setText("")
        self.RedDartBox_8.setFont(QFont(families[0], 12))
        self.RedDartBox_9.setText("")
        self.RedDartBox_9.setFont(QFont(families[0], 12))
        self.RedDartBox_10.setText("")
        self.RedDartBox_10.setFont(QFont(families[0], 12))

        # Player 2's Dart History. Everything is ordered according to the number.
        self.GreenDartBox.setText("")
        self.GreenDartBox.setFont(QFont(families[0], 12))
        self.GreenDartBox_2.setText("")
        self.GreenDartBox_2.setFont(QFont(families[0], 12))
        self.GreenDartBox_3.setText("")
        self.GreenDartBox_3.setFont(QFont(families[0], 12))
        self.GreenDartBox_4.setText("")
        self.GreenDartBox_4.setFont(QFont(families[0], 12))
        self.GreenDartBox_5.setText("")
        self.GreenDartBox_5.setFont(QFont(families[0], 12))
        self.GreenDartBox_6.setText("")
        self.GreenDartBox_6.setFont(QFont(families[0], 12))
        self.GreenDartBox_7.setText("")
        self.GreenDartBox_7.setFont(QFont(families[0], 12))
        self.GreenDartBox_8.setText("")
        self.GreenDartBox_8.setFont(QFont(families[0], 12))
        self.GreenDartBox_9.setText("")
        self.GreenDartBox_9.setFont(QFont(families[0], 12))
        self.GreenDartBox_10.setText("")
        self.GreenDartBox_10.setFont(QFont(families[0], 12))

    def update_main_scoreboard(self):
        self.label_RedScore.setText(str(self.PlayerOne.get_score()))
        self.label_GreenScore.setText(str(self.PlayerTwo.get_score()))  # Setting to empty string
        self.label_RedLegs.setText(str(self.PlayerOne.get_legs_won()))  # Setting to empty string
        self.label_GreenLegs.setText(str(self.PlayerTwo.get_legs_won()))  # Setting to empty string
        if self.PlayerOne.get_on_track_for_perfect() is True:
            self.label_RedName.setText(str(self.PlayerOne.get_first_name() + "★"))  # Setting to empty string
        else:
            self.label_RedName.setText(str(self.PlayerOne.get_first_name()))  # Setting to empty string
        if self.PlayerTwo.get_on_track_for_perfect() is True:
            self.label_GreenName.setText(str(self.PlayerTwo.get_first_name() + "★"))  # Setting to empty string
        else:
            self.label_GreenName.setText(str(self.PlayerTwo.get_first_name()))  # Setting to empty string

        #self.label_RedName.setText(str(self.PlayerOne.get_first_name()))  # Setting to empty string
        #self.label_GreenName.setText(str(self.PlayerTwo.get_first_name()))  # Setting to empty string
        self.label_RedWinningThrows.setText(str(self.PlayerOne.get_winning_combination()))  # Setting to empty string
        self.label_GreenWinningThrows.setText(str(self.PlayerTwo.get_winning_combination()))  # Setting to empty string
        self.RedDartsThrown.setText(self.PlayerOne.get_last_name() + ", " + self.PlayerOne.get_first_name() + ": Darts Thrown")
        self.GreenDartsThrown.setText(self.PlayerTwo.get_last_name() + ", " + self.PlayerTwo.get_first_name() + ": Darts Thrown")

        throws = self.PlayerOne.get_dart_throws()

        red_dart_boxes = [
            self.RedDartBox_10, self.RedDartBox_9, self.RedDartBox_8,
            self.RedDartBox_7, self.RedDartBox_6, self.RedDartBox_5,
            self.RedDartBox_4, self.RedDartBox_3, self.RedDartBox_2,
            self.RedDartBox
        ]


        for i, dart_box in enumerate(red_dart_boxes):
            if i < len(throws):
                dart_box.setText(throws[i])
            else:
                dart_box.setText("")

        throws_two = self.PlayerTwo.get_dart_throws()

        green_dart_boxes = [
            self.GreenDartBox_10, self.GreenDartBox_9, self.GreenDartBox_8,
            self.GreenDartBox_7, self.GreenDartBox_6, self.GreenDartBox_5,
            self.GreenDartBox_4, self.GreenDartBox_3, self.GreenDartBox_2,
            self.GreenDartBox
        ]

        for i, dart_box in enumerate(green_dart_boxes):
            if i < len(throws_two):
                dart_box.setText(throws_two[i])
            else:
                dart_box.setText("")