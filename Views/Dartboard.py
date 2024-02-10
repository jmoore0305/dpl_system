import sys


from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QApplication, QGridLayout, QWidget, QLabel
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice
from random import randrange
from Controllers.ScorersInterfaceController import ScorersInterfaceController

class Widget(QWidget):
    def __init__(self, scorer_interfaceIn):
        super().__init__()
        self.main_scoreboard = None
        self.scorer_interface = scorer_interfaceIn

        self.setMinimumSize(800, 600)
        self.donuts = []
        self.chart_view = QChartView()
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart = self.chart_view.chart()
        self.chart.legend().setVisible(False)
        self.chart.setAnimationOptions(QChart.AllAnimations)

        self.scorersInterfaceController = ScorersInterfaceController()
        self.scorersInterfaceController.create_starting_scores()

        self.setup_donuts6()
        self.setup_donuts5()
        self.setup_donuts4()
        self.setup_donuts3()
        self.setup_donuts2()
        self.setup_donuts1()
        self.setup_donuts0()

        # create main layout
        self.main_layout = QGridLayout(self)
        self.main_layout.addWidget(self.chart_view, 1, 1)
        self.setLayout(self.main_layout)

    #def set_main_scoreboard(self, main_scoreboard):
    #    self.main_scoreboard = main_scoreboard

    def setup_donuts0(self):
        donut0 = QPieSeries()
        value = randrange(1, 2)

        donut0.setPieStartAngle(10)
        donut0.setPieEndAngle(370)

        slc0_1 = QPieSlice(str(1), value)
        slc0_1.setColor(QColor(0, 0, 0))
        slc0_1.setLabelVisible(True)
        slc0_1.setBorderColor(QColor(235, 235, 235))
        slc0_1.setLabelColor(QColor(235, 235, 235))
        slc0_1.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_2 = QPieSlice(str(18), value)
        slc0_2.setColor(QColor(0, 0, 0))
        slc0_2.setLabelVisible(True)
        slc0_2.setBorderColor(QColor(235, 235, 235))
        slc0_2.setLabelColor(QColor(235, 235, 235))
        slc0_2.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_3 = QPieSlice(str(4), value)
        slc0_3.setColor(QColor(0, 0, 0))
        slc0_3.setLabelVisible(True)
        slc0_3.setBorderColor(QColor(235, 235, 235))
        slc0_3.setLabelColor(QColor(235, 235, 235))
        slc0_3.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_4 = QPieSlice(str(13), value)
        slc0_4.setColor(QColor(0, 0, 0))
        slc0_4.setLabelVisible(True)
        slc0_4.setBorderColor(QColor(235, 235, 235))
        slc0_4.setLabelColor(QColor(235, 235, 235))
        slc0_4.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_5 = QPieSlice(str(6), value)
        slc0_5.setColor(QColor(0, 0, 0))
        slc0_5.setLabelVisible(True)
        slc0_5.setBorderColor(QColor(235, 235, 235))
        slc0_5.setLabelColor(QColor(235, 235, 235))
        slc0_5.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_6 = QPieSlice(str(10), value)
        slc0_6.setColor(QColor(0, 0, 0))
        slc0_6.setLabelVisible(True)
        slc0_6.setBorderColor(QColor(235, 235, 235))
        slc0_6.setLabelColor(QColor(235, 235, 235))
        slc0_6.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_7 = QPieSlice(str(15), value)
        slc0_7.setColor(QColor(0, 0, 0))
        slc0_7.setLabelVisible(True)
        slc0_7.setBorderColor(QColor(235, 235, 235))
        slc0_7.setLabelColor(QColor(235, 235, 235))
        slc0_7.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_8 = QPieSlice(str(2), value)
        slc0_8.setColor(QColor(0, 0, 0))
        slc0_8.setLabelVisible(True)
        slc0_8.setBorderColor(QColor(235, 235, 235))
        slc0_8.setLabelColor(QColor(235, 235, 235))
        slc0_8.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_9 = QPieSlice(str(17), value)
        slc0_9.setColor(QColor(0, 0, 0))
        slc0_9.setLabelVisible(True)
        slc0_9.setBorderColor(QColor(235, 235, 235))
        slc0_9.setLabelColor(QColor(235, 235, 235))
        slc0_9.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_10 = QPieSlice(str(3), value)
        slc0_10.setColor(QColor(0, 0, 0))
        slc0_10.setLabelVisible(True)
        slc0_10.setBorderColor(QColor(235, 235, 235))
        slc0_10.setLabelColor(QColor(235, 235, 235))
        slc0_10.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_11 = QPieSlice(str(19), value)
        slc0_11.setColor(QColor(0, 0, 0))
        slc0_11.setLabelVisible(True)
        slc0_11.setBorderColor(QColor(235, 235, 235))
        slc0_11.setLabelColor(QColor(235, 235, 235))
        slc0_11.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_12 = QPieSlice(str(7), value)
        slc0_12.setColor(QColor(0, 0, 0))
        slc0_12.setLabelVisible(True)
        slc0_12.setBorderColor(QColor(235, 235, 235))
        slc0_12.setLabelColor(QColor(235, 235, 235))
        slc0_12.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_13 = QPieSlice(str(16), value)
        slc0_13.setColor(QColor(0, 0, 0))
        slc0_13.setLabelVisible(True)
        slc0_13.setBorderColor(QColor(235, 235, 235))
        slc0_13.setLabelColor(QColor(235, 235, 235))
        slc0_13.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_14 = QPieSlice(str(8), value)
        slc0_14.setColor(QColor(0, 0, 0))
        slc0_14.setLabelVisible(True)
        slc0_14.setBorderColor(QColor(235, 235, 235))
        slc0_14.setLabelColor(QColor(235, 235, 235))
        slc0_14.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_15 = QPieSlice(str(11), value)
        slc0_15.setColor(QColor(0, 0, 0))
        slc0_15.setLabelVisible(True)
        slc0_15.setBorderColor(QColor(235, 235, 235))
        slc0_15.setLabelColor(QColor(235, 235, 235))
        slc0_15.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_16 = QPieSlice(str(14), value)
        slc0_16.setColor(QColor(0, 0, 0))
        slc0_16.setLabelVisible(True)
        slc0_16.setBorderColor(QColor(235, 235, 235))
        slc0_16.setLabelColor(QColor(235, 235, 235))
        slc0_16.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_17 = QPieSlice(str(9), value)
        slc0_17.setColor(QColor(0, 0, 0))
        slc0_17.setLabelVisible(True)
        slc0_17.setBorderColor(QColor(235, 235, 235))
        slc0_17.setLabelColor(QColor(235, 235, 235))
        slc0_17.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_18 = QPieSlice(str(12), value)
        slc0_18.setColor(QColor(0, 0, 0))
        slc0_18.setLabelVisible(True)
        slc0_18.setBorderColor(QColor(235, 235, 235))
        slc0_18.setLabelColor(QColor(235, 235, 235))
        slc0_18.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_19 = QPieSlice(str(5), value)
        slc0_19.setColor(QColor(0, 0, 0))
        slc0_19.setLabelVisible(True)
        slc0_19.setBorderColor(QColor(235, 235, 235))
        slc0_19.setLabelColor(QColor(235, 235, 235))
        slc0_19.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_20 = QPieSlice(str(20), value)
        slc0_20.setColor(QColor(0, 0, 0))
        slc0_20.setLabelVisible(True)
        slc0_20.setBorderColor(QColor(235, 235, 235))
        slc0_20.setLabelColor(QColor(235, 235, 235))
        slc0_20.setLabelPosition(QPieSlice.LabelInsideTangential)

        slc0_1.clicked.connect(lambda: self.handle_slice0_click1(slc0_1))
        slc0_2.clicked.connect(lambda: self.handle_slice0_click2(slc0_2))
        slc0_3.clicked.connect(lambda: self.handle_slice0_click3(slc0_3))
        slc0_4.clicked.connect(lambda: self.handle_slice0_click4(slc0_4))
        slc0_5.clicked.connect(lambda: self.handle_slice0_click5(slc0_5))
        slc0_6.clicked.connect(lambda: self.handle_slice0_click6(slc0_6))
        slc0_7.clicked.connect(lambda: self.handle_slice0_click7(slc0_7))
        slc0_8.clicked.connect(lambda: self.handle_slice0_click8(slc0_8))
        slc0_9.clicked.connect(lambda: self.handle_slice0_click9(slc0_9))
        slc0_10.clicked.connect(lambda: self.handle_slice0_click10(slc0_10))
        slc0_11.clicked.connect(lambda: self.handle_slice0_click11(slc0_11))
        slc0_12.clicked.connect(lambda: self.handle_slice0_click12(slc0_12))
        slc0_13.clicked.connect(lambda: self.handle_slice0_click13(slc0_13))
        slc0_14.clicked.connect(lambda: self.handle_slice0_click14(slc0_14))
        slc0_15.clicked.connect(lambda: self.handle_slice0_click15(slc0_15))
        slc0_16.clicked.connect(lambda: self.handle_slice0_click16(slc0_16))
        slc0_17.clicked.connect(lambda: self.handle_slice0_click17(slc0_17))
        slc0_18.clicked.connect(lambda: self.handle_slice0_click18(slc0_18))
        slc0_19.clicked.connect(lambda: self.handle_slice0_click19(slc0_19))
        slc0_20.clicked.connect(lambda: self.handle_slice0_click20(slc0_10))

        donut0.append(slc0_1)
        donut0.append(slc0_2)
        donut0.append(slc0_3)
        donut0.append(slc0_4)
        donut0.append(slc0_5)
        donut0.append(slc0_6)
        donut0.append(slc0_7)
        donut0.append(slc0_8)
        donut0.append(slc0_9)
        donut0.append(slc0_10)
        donut0.append(slc0_11)
        donut0.append(slc0_12)
        donut0.append(slc0_13)
        donut0.append(slc0_14)
        donut0.append(slc0_15)
        donut0.append(slc0_16)
        donut0.append(slc0_17)
        donut0.append(slc0_18)
        donut0.append(slc0_19)
        donut0.append(slc0_20)

        donut0.setHoleSize(.9)
        donut0.setPieSize(1)
        self.donuts.append(donut0)
        self.chart_view.chart().addSeries(donut0)


    def handle_slice0_click1(self, slice):
        print(f"Clicked on 1")
    def handle_slice0_click2(self, slice):
        print(f"Clicked on 18")
    def handle_slice0_click3(self, slice):
        print(f"Clicked on 4")
    def handle_slice0_click4(self, slice):
        print(f"Clicked on 13")
    def handle_slice0_click5(self, slice):
        print(f"Clicked on 6")
    def handle_slice0_click6(self, slice):
        print(f"Clicked on 10")
    def handle_slice0_click7(self, slice):
        print(f"Clicked on 15")
    def handle_slice0_click8(self, slice):
        print(f"Clicked on 2")
    def handle_slice0_click9(self, slice):
        print(f"Clicked on 17")
    def handle_slice0_click10(self, slice):
        print(f"Clicked on 3")
    def handle_slice0_click11(self, slice):
        print(f"Clicked on 19")
    def handle_slice0_click12(self, slice):
        print(f"Clicked on 7")
    def handle_slice0_click13(self, slice):
        print(f"Clicked on 16")
    def handle_slice0_click14(self, slice):
        print(f"Clicked on 8")
    def handle_slice0_click15(self, slice):
        print(f"Clicked on 11")
    def handle_slice0_click16(self, slice):
        print(f"Clicked on 14")
    def handle_slice0_click17(self, slice):
        print(f"Clicked on 9")
    def handle_slice0_click18(self, slice):
        print(f"Clicked on 12")
    def handle_slice0_click19(self, slice):
        print(f"Clicked on 5")
    def handle_slice0_click20(self, slice):
        print(f"Clicked on 20")

    def setup_donuts1(self):
        donut1 = QPieSeries()
        value = randrange(1, 2)

        donut1.setPieStartAngle(10)
        donut1.setPieEndAngle(370)

        slc1_1 = QPieSlice(str(value), value)
        slc1_1.setBorderWidth(2)
        slc1_1.setColor(QColor(85, 163, 57))
        slc1_1.setBorderColor(QColor(235, 235, 235))

        slc1_2 = QPieSlice(str(value), value)
        slc1_2.setBorderWidth(2)
        slc1_2.setColor(QColor(168, 50, 50))
        slc1_2.setBorderColor(QColor(235, 235, 235))

        slc1_3 = QPieSlice(str(value), value)
        slc1_3.setBorderWidth(2)
        slc1_3.setColor(QColor(85, 163, 57))
        slc1_3.setBorderColor(QColor(235, 235, 235))

        slc1_4 = QPieSlice(str(value), value)
        slc1_4.setBorderWidth(2)
        slc1_4.setColor(QColor(168, 50, 50))
        slc1_4.setBorderColor(QColor(235, 235, 235))

        slc1_5 = QPieSlice(str(value), value)
        slc1_5.setBorderWidth(2)
        slc1_5.setColor(QColor(85, 163, 57))
        slc1_5.setBorderColor(QColor(235, 235, 235))

        slc1_6 = QPieSlice(str(value), value)
        slc1_6.setBorderWidth(2)
        slc1_6.setColor(QColor(168, 50, 50))
        slc1_6.setBorderColor(QColor(235, 235, 235))

        slc1_7 = QPieSlice(str(value), value)
        slc1_7.setBorderWidth(2)
        slc1_7.setColor(QColor(85, 163, 57))
        slc1_7.setBorderColor(QColor(235, 235, 235))

        slc1_8 = QPieSlice(str(value), value)
        slc1_8.setBorderWidth(2)
        slc1_8.setColor(QColor(168, 50, 50))
        slc1_8.setBorderColor(QColor(235, 235, 235))

        slc1_9 = QPieSlice(str(value), value)
        slc1_9.setBorderWidth(2)
        slc1_9.setColor(QColor(85, 163, 57))
        slc1_9.setBorderColor(QColor(235, 235, 235))

        slc1_10 = QPieSlice(str(value), value)
        slc1_10.setBorderWidth(2)
        slc1_10.setColor(QColor(168, 50, 50))
        slc1_10.setBorderColor(QColor(235, 235, 235))

        slc1_11 = QPieSlice(str(value), value)
        slc1_11.setBorderWidth(2)
        slc1_11.setColor(QColor(85, 163, 57))
        slc1_11.setBorderColor(QColor(235, 235, 235))

        slc1_12 = QPieSlice(str(value), value)
        slc1_12.setBorderWidth(2)
        slc1_12.setColor(QColor(168, 50, 50))
        slc1_12.setBorderColor(QColor(235, 235, 235))

        slc1_13 = QPieSlice(str(value), value)
        slc1_13.setBorderWidth(2)
        slc1_13.setColor(QColor(85, 163, 57))
        slc1_13.setBorderColor(QColor(235, 235, 235))

        slc1_14 = QPieSlice(str(value), value)
        slc1_14.setBorderWidth(2)
        slc1_14.setColor(QColor(168, 50, 50))
        slc1_14.setBorderColor(QColor(235, 235, 235))

        slc1_15 = QPieSlice(str(value), value)
        slc1_15.setBorderWidth(2)
        slc1_15.setColor(QColor(85, 163, 57))
        slc1_15.setBorderColor(QColor(235, 235, 235))

        slc1_16 = QPieSlice(str(value), value)
        slc1_16.setBorderWidth(2)
        slc1_16.setColor(QColor(168, 50, 50))
        slc1_16.setBorderColor(QColor(235, 235, 235))

        slc1_17 = QPieSlice(str(value), value)
        slc1_17.setBorderWidth(2)
        slc1_17.setColor(QColor(85, 163, 57))
        slc1_17.setBorderColor(QColor(235, 235, 235))

        slc1_18 = QPieSlice(str(value), value)
        slc1_18.setBorderWidth(2)
        slc1_18.setColor(QColor(168, 50, 50))
        slc1_18.setBorderColor(QColor(235, 235, 235))

        slc1_19 = QPieSlice(str(value), value)
        slc1_19.setBorderWidth(2)
        slc1_19.setColor(QColor(85, 163, 57))
        slc1_19.setBorderColor(QColor(235, 235, 235))

        slc1_20 = QPieSlice(str(value), value)
        slc1_20.setBorderWidth(2)
        slc1_20.setColor(QColor(168, 50, 50))
        slc1_20.setBorderColor(QColor(235, 235, 235))

        slc1_1.clicked.connect(lambda: self.handle_slice_click1(slc1_1))
        slc1_2.clicked.connect(lambda: self.handle_slice_click2(slc1_2))
        slc1_3.clicked.connect(lambda: self.handle_slice_click3(slc1_3))
        slc1_4.clicked.connect(lambda: self.handle_slice_click4(slc1_4))
        slc1_5.clicked.connect(lambda: self.handle_slice_click5(slc1_5))
        slc1_6.clicked.connect(lambda: self.handle_slice_click6(slc1_6))
        slc1_7.clicked.connect(lambda: self.handle_slice_click7(slc1_7))
        slc1_8.clicked.connect(lambda: self.handle_slice_click8(slc1_8))
        slc1_9.clicked.connect(lambda: self.handle_slice_click9(slc1_9))
        slc1_10.clicked.connect(lambda: self.handle_slice_click10(slc1_10))
        slc1_11.clicked.connect(lambda: self.handle_slice_click11(slc1_11))
        slc1_12.clicked.connect(lambda: self.handle_slice_click12(slc1_12))
        slc1_13.clicked.connect(lambda: self.handle_slice_click13(slc1_13))
        slc1_14.clicked.connect(lambda: self.handle_slice_click14(slc1_14))
        slc1_15.clicked.connect(lambda: self.handle_slice_click15(slc1_15))
        slc1_16.clicked.connect(lambda: self.handle_slice_click16(slc1_16))
        slc1_17.clicked.connect(lambda: self.handle_slice_click17(slc1_17))
        slc1_18.clicked.connect(lambda: self.handle_slice_click18(slc1_18))
        slc1_19.clicked.connect(lambda: self.handle_slice_click19(slc1_19))
        slc1_20.clicked.connect(lambda: self.handle_slice_click20(slc1_10))

        donut1.append(slc1_1)
        donut1.append(slc1_2)
        donut1.append(slc1_3)
        donut1.append(slc1_4)
        donut1.append(slc1_5)
        donut1.append(slc1_6)
        donut1.append(slc1_7)
        donut1.append(slc1_8)
        donut1.append(slc1_9)
        donut1.append(slc1_10)
        donut1.append(slc1_11)
        donut1.append(slc1_12)
        donut1.append(slc1_13)
        donut1.append(slc1_14)
        donut1.append(slc1_15)
        donut1.append(slc1_16)
        donut1.append(slc1_17)
        donut1.append(slc1_18)
        donut1.append(slc1_19)
        donut1.append(slc1_20)
        donut1.setHoleSize(0.85)
        donut1.setPieSize(1)
        self.donuts.append(donut1)
        self.chart_view.chart().addSeries(donut1)


    def handle_slice_click1(self, slice):
        print(f"Clicked on 2 x 1")
        self.scorersInterfaceController.update_game_state(multiplier=2, value=1, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        self.scorer_interface.update_all()

    def handle_slice_click2(self, slice):
        print(f"Clicked on 2 x 18")
        self.scorersInterfaceController.update_game_state(multiplier=2, value=18, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        self.scorer_interface.update_all()

    def handle_slice_click3(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=4, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 4")
        self.scorer_interface.update_all()

    def handle_slice_click4(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=13, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 13")
        self.scorer_interface.update_all()

    def handle_slice_click5(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=6, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 6")
        self.scorer_interface.update_all()

    def handle_slice_click6(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=10, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 10")
        self.scorer_interface.update_all()

    def handle_slice_click7(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=15, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 15")
        self.scorer_interface.update_all()

    def handle_slice_click8(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=2, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 2")
        self.scorer_interface.update_all()

    def handle_slice_click9(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=17, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 17")
        self.scorer_interface.update_all()

    def handle_slice_click10(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=3, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 3")
        self.scorer_interface.update_all()

    def handle_slice_click11(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=19, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 19")
        self.scorer_interface.update_all()

    def handle_slice_click12(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=7, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 7")
        self.scorer_interface.update_all()

    def handle_slice_click13(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=16, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 16")
        self.scorer_interface.update_all()

    def handle_slice_click14(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=8, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 8")
        self.scorer_interface.update_all()

    def handle_slice_click15(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=11, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 11")
        self.scorer_interface.update_all()

    def handle_slice_click16(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=14, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 14")
        self.scorer_interface.update_all()

    def handle_slice_click17(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=9, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 9")
        self.scorer_interface.update_all()

    def handle_slice_click18(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=12, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 12")
        self.scorer_interface.update_all()

    def handle_slice_click19(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=5, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 5")
        self.scorer_interface.update_all()

    def handle_slice_click20(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=20, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 20")
        self.scorer_interface.update_all()

#*************************************************************************************************************************************

    def setup_donuts2(self):
        donut2 = QPieSeries()
        value = randrange(1, 2)

        donut2.setPieStartAngle(10)
        donut2.setPieEndAngle(370)

        slc2_1 = QPieSlice(str(value), value)
        slc2_1.setBorderWidth(2)
        slc2_1.setColor(QColor(240, 238, 228))
        slc2_1.setBorderColor(QColor(235, 235, 235))
        slc2_1.setLabelVisible(True)
        slc2_1.setLabel('20')

        slc2_2 = QPieSlice(str(value), value)
        slc2_2.setBorderWidth(2)
        slc2_2.setColor(QColor(0, 0, 0))
        slc2_2.setBorderColor(QColor(235, 235, 235))
        slc2_2.setLabelVisible(True)
        slc2_2.setLabel('1')

        slc2_3 = QPieSlice(str(value), value)
        slc2_3.setBorderWidth(2)
        slc2_3.setColor(QColor(240, 238, 228))
        slc2_3.setBorderColor(QColor(235, 235, 235))

        slc2_4 = QPieSlice(str(value), value)
        slc2_4.setBorderWidth(2)
        slc2_4.setColor(QColor(0, 0, 0))
        slc2_4.setBorderColor(QColor(235, 235, 235))

        slc2_5 = QPieSlice(str(value), value)
        slc2_5.setBorderWidth(2)
        slc2_5.setColor(QColor(240, 238, 228))
        slc2_5.setBorderColor(QColor(235, 235, 235))

        slc2_6 = QPieSlice(str(value), value)
        slc2_6.setBorderWidth(2)
        slc2_6.setColor(QColor(0, 0, 0))
        slc2_6.setBorderColor(QColor(235, 235, 235))

        slc2_7 = QPieSlice(str(value), value)
        slc2_7.setBorderWidth(2)
        slc2_7.setColor(QColor(240, 238, 228))
        slc2_7.setBorderColor(QColor(235, 235, 235))

        slc2_8 = QPieSlice(str(value), value)
        slc2_8.setBorderWidth(2)
        slc2_8.setColor(QColor(0, 0, 0))
        slc2_8.setBorderColor(QColor(235, 235, 235))

        slc2_9 = QPieSlice(str(value), value)
        slc2_9.setBorderWidth(2)
        slc2_9.setColor(QColor(240, 238, 228))
        slc2_9.setBorderColor(QColor(235, 235, 235))

        slc2_10 = QPieSlice(str(value), value)
        slc2_10.setBorderWidth(2)
        slc2_10.setColor(QColor(0, 0, 0))
        slc2_10.setBorderColor(QColor(235, 235, 235))

        slc2_11 = QPieSlice(str(value), value)
        slc2_11.setBorderWidth(2)
        slc2_11.setColor(QColor(240, 238, 228))
        slc2_11.setBorderColor(QColor(235, 235, 235))

        slc2_12 = QPieSlice(str(value), value)
        slc2_12.setBorderWidth(2)
        slc2_12.setColor(QColor(0, 0, 0))
        slc2_12.setBorderColor(QColor(235, 235, 235))

        slc2_13 = QPieSlice(str(value), value)
        slc2_13.setBorderWidth(2)
        slc2_13.setColor(QColor(240, 238, 228))
        slc2_13.setBorderColor(QColor(235, 235, 235))

        slc2_14 = QPieSlice(str(value), value)
        slc2_14.setBorderWidth(2)
        slc2_14.setColor(QColor(0, 0, 0))
        slc2_14.setBorderColor(QColor(235, 235, 235))

        slc2_15 = QPieSlice(str(value), value)
        slc2_15.setBorderWidth(2)
        slc2_15.setColor(QColor(240, 238, 228))
        slc2_15.setBorderColor(QColor(235, 235, 235))

        slc2_16 = QPieSlice(str(value), value)
        slc2_16.setBorderWidth(2)
        slc2_16.setColor(QColor(0, 0, 0))
        slc2_16.setBorderColor(QColor(235, 235, 235))

        slc2_17 = QPieSlice(str(value), value)
        slc2_17.setBorderWidth(2)
        slc2_17.setColor(QColor(240, 238, 228))
        slc2_17.setBorderColor(QColor(235, 235, 235))

        slc2_18 = QPieSlice(str(value), value)
        slc2_18.setBorderWidth(2)
        slc2_18.setColor(QColor(0, 0, 0))
        slc2_18.setBorderColor(QColor(235, 235, 235))

        slc2_19 = QPieSlice(str(value), value)
        slc2_19.setBorderWidth(2)
        slc2_19.setColor(QColor(240, 238, 228))
        slc2_19.setBorderColor(QColor(235, 235, 235))

        slc2_20 = QPieSlice(str(value), value)
        slc2_20.setBorderWidth(2)
        slc2_20.setColor(QColor(0, 0, 0))
        slc2_20.setBorderColor(QColor(235, 235, 235))

        slc2_1.clicked.connect(lambda: self.handle_slice_click2_1(slc2_1))
        slc2_2.clicked.connect(lambda: self.handle_slice_click2_2(slc2_2))
        slc2_3.clicked.connect(lambda: self.handle_slice_click2_3(slc2_3))
        slc2_4.clicked.connect(lambda: self.handle_slice_click2_4(slc2_4))
        slc2_5.clicked.connect(lambda: self.handle_slice_click2_5(slc2_5))
        slc2_6.clicked.connect(lambda: self.handle_slice_click2_6(slc2_6))
        slc2_7.clicked.connect(lambda: self.handle_slice_click2_7(slc2_7))
        slc2_8.clicked.connect(lambda: self.handle_slice_click2_8(slc2_8))
        slc2_9.clicked.connect(lambda: self.handle_slice_click2_9(slc2_9))
        slc2_10.clicked.connect(lambda: self.handle_slice_click2_10(slc2_10))
        slc2_11.clicked.connect(lambda: self.handle_slice_click2_11(slc2_11))
        slc2_12.clicked.connect(lambda: self.handle_slice_click2_12(slc2_12))
        slc2_13.clicked.connect(lambda: self.handle_slice_click2_13(slc2_13))
        slc2_14.clicked.connect(lambda: self.handle_slice_click2_14(slc2_14))
        slc2_15.clicked.connect(lambda: self.handle_slice_click2_15(slc2_15))
        slc2_16.clicked.connect(lambda: self.handle_slice_click2_16(slc2_16))
        slc2_17.clicked.connect(lambda: self.handle_slice_click2_17(slc2_17))
        slc2_18.clicked.connect(lambda: self.handle_slice_click2_18(slc2_18))
        slc2_19.clicked.connect(lambda: self.handle_slice_click2_19(slc2_19))
        slc2_20.clicked.connect(lambda: self.handle_slice_click2_20(slc2_10))

        donut2.append(slc2_1)
        donut2.append(slc2_2)
        donut2.append(slc2_3)
        donut2.append(slc2_4)
        donut2.append(slc2_5)
        donut2.append(slc2_6)
        donut2.append(slc2_7)
        donut2.append(slc2_8)
        donut2.append(slc2_9)
        donut2.append(slc2_10)
        donut2.append(slc2_11)
        donut2.append(slc2_12)
        donut2.append(slc2_13)
        donut2.append(slc2_14)
        donut2.append(slc2_15)
        donut2.append(slc2_16)
        donut2.append(slc2_17)
        donut2.append(slc2_18)
        donut2.append(slc2_19)
        donut2.append(slc2_20)
        donut2.setHoleSize(0.55)
        donut2.setPieSize(1)
        donut2.setLabelsVisible(False)
        self.donuts.append(donut2)
        self.chart_view.chart().addSeries(donut2)


    def handle_slice_click2_1(self, slice):
        print(f"Clicked on 1 x 1 (outer)")
        self.scorersInterfaceController.update_game_state(multiplier=1, value=1, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        self.scorer_interface.update_all()

    def handle_slice_click2_2(self, slice):
        print(f"Clicked on 1 x 18 (outer)")
        self.scorersInterfaceController.update_game_state(multiplier=1, value=18, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        self.scorer_interface.update_all()

    def handle_slice_click2_3(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=4, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 4 (outer)")
        self.scorer_interface.update_all()

    def handle_slice_click2_4(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=13, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 13 (outer)")
        self.scorer_interface.update_all()

    def handle_slice_click2_5(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=6, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 6 (outer)")
        self.scorer_interface.update_all()

    def handle_slice_click2_6(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=10, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 10 (outer)")
        self.scorer_interface.update_all()

    def handle_slice_click2_7(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=15, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 15 (outer)")
        self.scorer_interface.update_all()

    def handle_slice_click2_8(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=2, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 2 (outer)")
        self.scorer_interface.update_all()

    def handle_slice_click2_9(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=17, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 17 (outer)")
        self.scorer_interface.update_all()

    def handle_slice_click2_10(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=3, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 3 (outer)")
        self.scorer_interface.update_all()

    def handle_slice_click2_11(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=19, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 19 (outer)")
        self.scorer_interface.update_all()

    def handle_slice_click2_12(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=7, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 7 (outer)")
        self.scorer_interface.update_all()

    def handle_slice_click2_13(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=16, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 16 (outer)")
        self.scorer_interface.update_all()

    def handle_slice_click2_14(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=8, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 8 (outer)")
        self.scorer_interface.update_all()

    def handle_slice_click2_15(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=11, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 11 (outer)")
        self.scorer_interface.update_all()

    def handle_slice_click2_16(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=14, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 14 (outer)")
        self.scorer_interface.update_all()

    def handle_slice_click2_17(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=9, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 9 (outer)")
        self.scorer_interface.update_all()

    def handle_slice_click2_18(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=12, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 12 (outer)")
        self.scorer_interface.update_all()

    def handle_slice_click2_19(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=5, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 5 (outer)")
        self.scorer_interface.update_all()

    def handle_slice_click2_20(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=20, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 20 (outer)")
        self.scorer_interface.update_all()


#********************************************************************************************************************************

    def setup_donuts3(self):
        donut3 = QPieSeries()
        value = randrange(1, 2)

        donut3.setPieStartAngle(10)
        donut3.setPieEndAngle(370)

        slc3_1 = QPieSlice(str(value), value)
        slc3_1.setBorderWidth(2)
        slc3_1.setColor(QColor(85, 163, 57))
        slc3_1.setBorderColor(QColor(235, 235, 235))

        slc3_2 = QPieSlice(str(value), value)
        slc3_2.setBorderWidth(2)
        slc3_2.setColor(QColor(168, 50, 50))
        slc3_2.setBorderColor(QColor(235, 235, 235))

        slc3_3 = QPieSlice(str(value), value)
        slc3_3.setBorderWidth(2)
        slc3_3.setColor(QColor(85, 163, 57))
        slc3_3.setBorderColor(QColor(235, 235, 235))

        slc3_4 = QPieSlice(str(value), value)
        slc3_4.setBorderWidth(2)
        slc3_4.setColor(QColor(168, 50, 50))
        slc3_4.setBorderColor(QColor(235, 235, 235))

        slc3_5 = QPieSlice(str(value), value)
        slc3_5.setBorderWidth(2)
        slc3_5.setColor(QColor(85, 163, 57))
        slc3_5.setBorderColor(QColor(235, 235, 235))

        slc3_6 = QPieSlice(str(value), value)
        slc3_6.setBorderWidth(2)
        slc3_6.setColor(QColor(168, 50, 50))
        slc3_6.setBorderColor(QColor(235, 235, 235))

        slc3_7 = QPieSlice(str(value), value)
        slc3_7.setBorderWidth(2)
        slc3_7.setColor(QColor(85, 163, 57))
        slc3_7.setBorderColor(QColor(235, 235, 235))

        slc3_8 = QPieSlice(str(value), value)
        slc3_8.setBorderWidth(2)
        slc3_8.setColor(QColor(168, 50, 50))
        slc3_8.setBorderColor(QColor(235, 235, 235))

        slc3_9 = QPieSlice(str(value), value)
        slc3_9.setBorderWidth(2)
        slc3_9.setColor(QColor(85, 163, 57))
        slc3_9.setBorderColor(QColor(235, 235, 235))

        slc3_10 = QPieSlice(str(value), value)
        slc3_10.setBorderWidth(2)
        slc3_10.setColor(QColor(168, 50, 50))
        slc3_10.setBorderColor(QColor(235, 235, 235))

        slc3_11 = QPieSlice(str(value), value)
        slc3_11.setBorderWidth(2)
        slc3_11.setColor(QColor(85, 163, 57))
        slc3_11.setBorderColor(QColor(235, 235, 235))

        slc3_12 = QPieSlice(str(value), value)
        slc3_12.setBorderWidth(2)
        slc3_12.setColor(QColor(168, 50, 50))
        slc3_12.setBorderColor(QColor(235, 235, 235))

        slc3_13 = QPieSlice(str(value), value)
        slc3_13.setBorderWidth(2)
        slc3_13.setColor(QColor(85, 163, 57))
        slc3_13.setBorderColor(QColor(235, 235, 235))

        slc3_14 = QPieSlice(str(value), value)
        slc3_14.setBorderWidth(2)
        slc3_14.setColor(QColor(168, 50, 50))
        slc3_14.setBorderColor(QColor(235, 235, 235))

        slc3_15 = QPieSlice(str(value), value)
        slc3_15.setBorderWidth(2)
        slc3_15.setColor(QColor(85, 163, 57))
        slc3_15.setBorderColor(QColor(235, 235, 235))

        slc3_16 = QPieSlice(str(value), value)
        slc3_16.setBorderWidth(2)
        slc3_16.setColor(QColor(168, 50, 50))
        slc3_16.setBorderColor(QColor(235, 235, 235))

        slc3_17 = QPieSlice(str(value), value)
        slc3_17.setBorderWidth(2)
        slc3_17.setColor(QColor(85, 163, 57))
        slc3_17.setBorderColor(QColor(235, 235, 235))

        slc3_18 = QPieSlice(str(value), value)
        slc3_18.setBorderWidth(2)
        slc3_18.setColor(QColor(168, 50, 50))
        slc3_18.setBorderColor(QColor(235, 235, 235))

        slc3_19 = QPieSlice(str(value), value)
        slc3_19.setBorderWidth(2)
        slc3_19.setColor(QColor(85, 163, 57))
        slc3_19.setBorderColor(QColor(235, 235, 235))

        slc3_20 = QPieSlice(str(value), value)
        slc3_20.setBorderWidth(2)
        slc3_20.setColor(QColor(168, 50, 50))
        slc3_20.setBorderColor(QColor(235, 235, 235))


        slc3_1.clicked.connect(lambda: self.handle_slice_click3_1(slc3_1))
        slc3_2.clicked.connect(lambda: self.handle_slice_click3_2(slc3_2))
        slc3_3.clicked.connect(lambda: self.handle_slice_click3_3(slc3_3))
        slc3_4.clicked.connect(lambda: self.handle_slice_click3_4(slc3_4))
        slc3_5.clicked.connect(lambda: self.handle_slice_click3_5(slc3_5))
        slc3_6.clicked.connect(lambda: self.handle_slice_click3_6(slc3_6))
        slc3_7.clicked.connect(lambda: self.handle_slice_click3_7(slc3_7))
        slc3_8.clicked.connect(lambda: self.handle_slice_click3_8(slc3_8))
        slc3_9.clicked.connect(lambda: self.handle_slice_click3_9(slc3_9))
        slc3_10.clicked.connect(lambda: self.handle_slice_click3_10(slc3_10))
        slc3_11.clicked.connect(lambda: self.handle_slice_click3_11(slc3_11))
        slc3_12.clicked.connect(lambda: self.handle_slice_click3_12(slc3_12))
        slc3_13.clicked.connect(lambda: self.handle_slice_click3_13(slc3_13))
        slc3_14.clicked.connect(lambda: self.handle_slice_click3_14(slc3_14))
        slc3_15.clicked.connect(lambda: self.handle_slice_click3_15(slc3_15))
        slc3_16.clicked.connect(lambda: self.handle_slice_click3_16(slc3_16))
        slc3_17.clicked.connect(lambda: self.handle_slice_click3_17(slc3_17))
        slc3_18.clicked.connect(lambda: self.handle_slice_click3_18(slc3_18))
        slc3_19.clicked.connect(lambda: self.handle_slice_click3_19(slc3_19))
        slc3_20.clicked.connect(lambda: self.handle_slice_click3_20(slc3_10))

        donut3.append(slc3_1)
        donut3.append(slc3_2)
        donut3.append(slc3_3)
        donut3.append(slc3_4)
        donut3.append(slc3_5)
        donut3.append(slc3_6)
        donut3.append(slc3_7)
        donut3.append(slc3_8)
        donut3.append(slc3_9)
        donut3.append(slc3_10)
        donut3.append(slc3_11)
        donut3.append(slc3_12)
        donut3.append(slc3_13)
        donut3.append(slc3_14)
        donut3.append(slc3_15)
        donut3.append(slc3_16)
        donut3.append(slc3_17)
        donut3.append(slc3_18)
        donut3.append(slc3_19)
        donut3.append(slc3_20)
        donut3.setHoleSize(0.5)
        donut3.setPieSize(1)
        self.donuts.append(donut3)
        self.chart_view.chart().addSeries(donut3)


    def handle_slice_click3_1(self, slice):
        print(f"Clicked on 3 x 1")
        self.scorersInterfaceController.update_game_state(multiplier=3, value=1, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        self.scorer_interface.update_all()

    def handle_slice_click3_2(self, slice):
        print(f"Clicked on 3 x 18")
        self.scorersInterfaceController.update_game_state(multiplier=3, value=18, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        self.scorer_interface.update_all()

    def handle_slice_click3_3(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=3, value=4, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 3 x 4")
        self.scorer_interface.update_all()

    def handle_slice_click3_4(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=3, value=13, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 3 x 13")
        self.scorer_interface.update_all()

    def handle_slice_click3_5(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=3, value=6, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 3 x 6")
        self.scorer_interface.update_all()

    def handle_slice_click3_6(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=3, value=10, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 3 x 10")
        self.scorer_interface.update_all()

    def handle_slice_click3_7(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=3, value=15, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 3 x 15")
        self.scorer_interface.update_all()

    def handle_slice_click3_8(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=3, value=2, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 3 x 2")
        self.scorer_interface.update_all()

    def handle_slice_click3_9(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=3, value=17, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 3 x 17")
        self.scorer_interface.update_all()

    def handle_slice_click3_10(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=3, value=3, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 3 x 3")
        self.scorer_interface.update_all()

    def handle_slice_click3_11(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=3, value=19, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 3 x 19")
        self.scorer_interface.update_all()
    def handle_slice_click3_12(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=3, value=7, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 3 x 7")
        self.scorer_interface.update_all()

    def handle_slice_click3_13(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=3, value=16, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 3 x 16")
        self.scorer_interface.update_all()

    def handle_slice_click3_14(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=3, value=8, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 3 x 8")
        self.scorer_interface.update_all()

    def handle_slice_click3_15(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=3, value=11, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 3 x 11")
        self.scorer_interface.update_all()

    def handle_slice_click3_16(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=3, value=14, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 3 x 14")
        self.scorer_interface.update_all()


    def handle_slice_click3_17(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=3, value=9, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 3 x 9")
        self.scorer_interface.update_all()

    def handle_slice_click3_18(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=3, value=12, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 3 x 12")
        self.scorer_interface.update_all()

    def handle_slice_click3_19(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=3, value=5, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 3 x 5")
        self.scorer_interface.update_all()

    def handle_slice_click3_20(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=3, value=20, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 3 x 20")
        self.scorer_interface.update_all()


    def setup_donuts4(self):
        donut4 = QPieSeries()
        value = randrange(1, 2)

        donut4.setPieStartAngle(10)
        donut4.setPieEndAngle(370)

        slc4_1 = QPieSlice(str(value), value)
        slc4_1.setBorderWidth(2)
        slc4_1.setColor(QColor(240, 238, 228))
        slc4_1.setBorderColor(QColor(235, 235, 235))

        slc4_2 = QPieSlice(str(value), value)
        slc4_2.setBorderWidth(2)
        slc4_2.setColor(QColor(0, 0, 0))
        slc4_2.setBorderColor(QColor(235, 235, 235))

        slc4_3 = QPieSlice(str(value), value)
        slc4_3.setBorderWidth(2)
        slc4_3.setColor(QColor(240, 238, 228))
        slc4_3.setBorderColor(QColor(235, 235, 235))

        slc4_4 = QPieSlice(str(value), value)
        slc4_4.setBorderWidth(2)
        slc4_4.setColor(QColor(0, 0, 0))
        slc4_4.setBorderColor(QColor(235, 235, 235))

        slc4_5 = QPieSlice(str(value), value)
        slc4_5.setBorderWidth(2)
        slc4_5.setColor(QColor(240, 238, 228))
        slc4_5.setBorderColor(QColor(235, 235, 235))

        slc4_6 = QPieSlice(str(value), value)
        slc4_6.setBorderWidth(2)
        slc4_6.setColor(QColor(0, 0, 0))
        slc4_6.setBorderColor(QColor(235, 235, 235))

        slc4_7 = QPieSlice(str(value), value)
        slc4_7.setBorderWidth(2)
        slc4_7.setColor(QColor(240, 238, 228))
        slc4_7.setBorderColor(QColor(235, 235, 235))

        slc4_8 = QPieSlice(str(value), value)
        slc4_8.setBorderWidth(2)
        slc4_8.setColor(QColor(0, 0, 0))
        slc4_8.setBorderColor(QColor(235, 235, 235))

        slc4_9 = QPieSlice(str(value), value)
        slc4_9.setBorderWidth(2)
        slc4_9.setColor(QColor(240, 238, 228))
        slc4_9.setBorderColor(QColor(235, 235, 235))

        slc4_10 = QPieSlice(str(value), value)
        slc4_10.setBorderWidth(2)
        slc4_10.setColor(QColor(0, 0, 0))
        slc4_10.setBorderColor(QColor(235, 235, 235))

        slc4_11 = QPieSlice(str(value), value)
        slc4_11.setBorderWidth(2)
        slc4_11.setColor(QColor(240, 238, 228))
        slc4_11.setBorderColor(QColor(235, 235, 235))

        slc4_12 = QPieSlice(str(value), value)
        slc4_12.setBorderWidth(2)
        slc4_12.setColor(QColor(0, 0, 0))
        slc4_12.setBorderColor(QColor(235, 235, 235))

        slc4_13 = QPieSlice(str(value), value)
        slc4_13.setBorderWidth(2)
        slc4_13.setColor(QColor(240, 238, 228))
        slc4_13.setBorderColor(QColor(235, 235, 235))

        slc4_14 = QPieSlice(str(value), value)
        slc4_14.setBorderWidth(2)
        slc4_14.setColor(QColor(0, 0, 0))
        slc4_14.setBorderColor(QColor(235, 235, 235))

        slc4_15 = QPieSlice(str(value), value)
        slc4_15.setBorderWidth(2)
        slc4_15.setColor(QColor(240, 238, 228))
        slc4_15.setBorderColor(QColor(235, 235, 235))

        slc4_16 = QPieSlice(str(value), value)
        slc4_16.setBorderWidth(2)
        slc4_16.setColor(QColor(0, 0, 0))
        slc4_16.setBorderColor(QColor(235, 235, 235))

        slc4_17 = QPieSlice(str(value), value)
        slc4_17.setBorderWidth(2)
        slc4_17.setColor(QColor(240, 238, 228))
        slc4_17.setBorderColor(QColor(235, 235, 235))

        slc4_18 = QPieSlice(str(value), value)
        slc4_18.setBorderWidth(2)
        slc4_18.setColor(QColor(0, 0, 0))
        slc4_18.setBorderColor(QColor(235, 235, 235))

        slc4_19 = QPieSlice(str(value), value)
        slc4_19.setBorderWidth(2)
        slc4_19.setColor(QColor(240, 238, 228))
        slc4_19.setBorderColor(QColor(235, 235, 235))

        slc4_20 = QPieSlice(str(value), value)
        slc4_20.setBorderWidth(2)
        slc4_20.setColor(QColor(0, 0, 0))
        slc4_20.setBorderColor(QColor(235, 235, 235))

        slc4_1.clicked.connect(lambda: self.handle_slice_click4_1(slc4_1))
        slc4_2.clicked.connect(lambda: self.handle_slice_click4_2(slc4_2))
        slc4_3.clicked.connect(lambda: self.handle_slice_click4_3(slc4_3))
        slc4_4.clicked.connect(lambda: self.handle_slice_click4_4(slc4_4))
        slc4_5.clicked.connect(lambda: self.handle_slice_click4_5(slc4_5))
        slc4_6.clicked.connect(lambda: self.handle_slice_click4_6(slc4_6))
        slc4_7.clicked.connect(lambda: self.handle_slice_click4_7(slc4_7))
        slc4_8.clicked.connect(lambda: self.handle_slice_click4_8(slc4_8))
        slc4_9.clicked.connect(lambda: self.handle_slice_click4_9(slc4_9))
        slc4_10.clicked.connect(lambda: self.handle_slice_click4_10(slc4_10))
        slc4_11.clicked.connect(lambda: self.handle_slice_click4_11(slc4_11))
        slc4_12.clicked.connect(lambda: self.handle_slice_click4_12(slc4_12))
        slc4_13.clicked.connect(lambda: self.handle_slice_click4_13(slc4_13))
        slc4_14.clicked.connect(lambda: self.handle_slice_click4_14(slc4_14))
        slc4_15.clicked.connect(lambda: self.handle_slice_click4_15(slc4_15))
        slc4_16.clicked.connect(lambda: self.handle_slice_click4_16(slc4_16))
        slc4_17.clicked.connect(lambda: self.handle_slice_click4_17(slc4_17))
        slc4_18.clicked.connect(lambda: self.handle_slice_click4_18(slc4_18))
        slc4_19.clicked.connect(lambda: self.handle_slice_click4_19(slc4_19))
        slc4_20.clicked.connect(lambda: self.handle_slice_click4_20(slc4_10))

        donut4.append(slc4_1)
        donut4.append(slc4_2)
        donut4.append(slc4_3)
        donut4.append(slc4_4)
        donut4.append(slc4_5)
        donut4.append(slc4_6)
        donut4.append(slc4_7)
        donut4.append(slc4_8)
        donut4.append(slc4_9)
        donut4.append(slc4_10)
        donut4.append(slc4_11)
        donut4.append(slc4_12)
        donut4.append(slc4_13)
        donut4.append(slc4_14)
        donut4.append(slc4_15)
        donut4.append(slc4_16)
        donut4.append(slc4_17)
        donut4.append(slc4_18)
        donut4.append(slc4_19)
        donut4.append(slc4_20)
        donut4.setHoleSize(0.1)
        donut4.setPieSize(1)
        donut4.setLabelsVisible(False)
        self.donuts.append(donut4)
        self.chart_view.chart().addSeries(donut4)


    def handle_slice_click4_1(self, slice):
        print(f"Clicked on 1 x 1 (inner)")
        self.scorersInterfaceController.update_game_state(multiplier=1, value=1, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        self.scorer_interface.update_all()

    def handle_slice_click4_2(self, slice):
        print(f"Clicked on 1 x 18 (inner)")
        self.scorersInterfaceController.update_game_state(multiplier=1, value=18, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        self.scorer_interface.update_all()

    def handle_slice_click4_3(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=4, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 4 (inner)")
        self.scorer_interface.update_all()

    def handle_slice_click4_4(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=13, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 13 (inner)")
        self.scorer_interface.update_all()

    def handle_slice_click4_5(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=6, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 6 (inner)")
        self.scorer_interface.update_all()

    def handle_slice_click4_6(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=10, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 10 (inner)")
        self.scorer_interface.update_all()

    def handle_slice_click4_7(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=15, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 15 (inner)")
        self.scorer_interface.update_all()

    def handle_slice_click4_8(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=2, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 2 (inner)")
        self.scorer_interface.update_all()

    def handle_slice_click4_9(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=17, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 17 (inner)")
        self.scorer_interface.update_all()

    def handle_slice_click4_10(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=3, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 3 (inner)")
        self.scorer_interface.update_all()

    def handle_slice_click4_11(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=19, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 19 (inner)")
        self.scorer_interface.update_all()

    def handle_slice_click4_12(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=7, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 7 (inner)")
        self.scorer_interface.update_all()

    def handle_slice_click4_13(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=16, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 16 (inner)")
        self.scorer_interface.update_all()

    def handle_slice_click4_14(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=8, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 8 (inner)")
        self.scorer_interface.update_all()

    def handle_slice_click4_15(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=11, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 11 (inner)")
        self.scorer_interface.update_all()
    def handle_slice_click4_16(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=14, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 14 (inner)")
        self.scorer_interface.update_all()
    def handle_slice_click4_17(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=9, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 9 (inner)")
        self.scorer_interface.update_all()
    def handle_slice_click4_18(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=12, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 12 (inner)")
        self.scorer_interface.update_all()
    def handle_slice_click4_19(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=5, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 5 (inner)")
        self.scorer_interface.update_all()
    def handle_slice_click4_20(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=20, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 20 (inner)")
        self.scorer_interface.update_all()
#********************************************************************************************************************************


    def setup_donuts5(self):
        donut5 = QPieSeries()
        value = randrange(1, 2)

        slc5_1 = QPieSlice(str(value), value)
        slc5_1.setBorderWidth(2)
        slc5_1.setColor(QColor(85, 163, 57))
        slc5_1.setBorderColor(QColor(85, 163, 57))


        slc5_1.clicked.connect(lambda: self.handle_slice_click5_1(slc5_1))

        donut5.append(slc5_1)

        donut5.setHoleSize(0.05)
        donut5.setPieSize(1)
        self.donuts.append(donut5)
        self.chart_view.chart().addSeries(donut5)


    def handle_slice_click5_1(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=1, value=25, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 1 x 25 (bull)")
        self.scorer_interface.update_all()


    def setup_donuts6(self):
        donut6 = QPieSeries()
        value = randrange(1, 2)

        slc6_1 = QPieSlice(str(value), value)
        slc6_1.setBorderWidth(2)
        slc6_1.setColor(QColor(168, 50, 50))
        slc6_1.setBorderColor(QColor(168, 50, 50))


        slc6_1.clicked.connect(lambda: self.handle_slice_click6_1(slc6_1))

        donut6.append(slc6_1)

        donut6.setHoleSize(0)
        donut6.setPieSize(0.035)
        self.donuts.append(donut6)
        self.chart_view.chart().addSeries(donut6)


    def handle_slice_click6_1(self, slice):
        self.scorersInterfaceController.update_game_state(multiplier=2, value=25, is_bounce_out=False, is_foul_out=False, is_knock_out=False)
        print(f"Clicked on 2 x 25 (bullseye)")
        self.scorer_interface.update_all()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec())
