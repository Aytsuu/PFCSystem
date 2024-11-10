# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUIJMXUZg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(1360, 895)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamily(u"Yu Gothic UI")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background-color: #5F8B6D;\n"
"}\n"
"\n"
"#menubar{\n"
"background-color: #003910;\n"
"}\n"
"\n"
"#cl1{\n"
"border-radius: 7px;\n"
"background-color: #D60000;\n"
"}\n"
"\n"
"#cl2{\n"
"border-radius: 7px;\n"
"background-color: #00E217;\n"
"}\n"
"\n"
"#cl3{\n"
"border-radius: 7px;\n"
"background-color: #FAD30A;\n"
"}\n"
"\n"
"#gym_name{\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #003910;\n"
"border: none;\n"
"color: #FFFFFF;\n"
"font-size: 14px;\n"
"font-family: Yu Gothic UI;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,50);\n"
"}")
        self.menubar = QWidget(self.centralwidget)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(90, -10, 331, 911))
        self.logo = QLabel(self.menubar)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(120, 60, 85, 81))
        self.logo.setStyleSheet(u"border-image: url(:/loginRES/logo.png);\n"
"border-radius:40px;")
        self.line = QWidget(self.menubar)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 215, 331, 2))
        font1 = QFont()
        font1.setFamily(u"MS Gothic")
        self.line.setFont(font1)
        self.line.setStyleSheet(u"background-color: #FFFFFF;")
        self.gym_name = QLabel(self.menubar)
        self.gym_name.setObjectName(u"gym_name")
        self.gym_name.setGeometry(QRect(50, 160, 221, 16))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setLegacyWeight(75)
        self.gym_name.setFont(font2)
        self.home = QPushButton(self.menubar)
        self.home.setObjectName(u"home")
        self.home.setGeometry(QRect(0, 220, 331, 71))
        font3 = QFont()
        font3.setFamily(u"Yu Gothic UI")
        font3.setBold(True)
        font3.setLegacyWeight(75)
        self.home.setFont(font3)
        self.home.setCursor(QCursor(Qt.PointingHandCursor))
        self.mem_list = QPushButton(self.menubar)
        self.mem_list.setObjectName(u"mem_list")
        self.mem_list.setGeometry(QRect(0, 290, 331, 71))
        self.mem_list.setFont(font3)
        self.mem_list.setCursor(QCursor(Qt.PointingHandCursor))
        self.mon_serv_log = QPushButton(self.menubar)
        self.mon_serv_log.setObjectName(u"mon_serv_log")
        self.mon_serv_log.setGeometry(QRect(0, 360, 331, 71))
        self.mon_serv_log.setFont(font3)
        self.mon_serv_log.setCursor(QCursor(Qt.PointingHandCursor))
        self.transaction = QPushButton(self.menubar)
        self.transaction.setObjectName(u"transaction")
        self.transaction.setGeometry(QRect(0, 500, 331, 71))
        self.transaction.setFont(font3)
        self.transaction.setCursor(QCursor(Qt.PointingHandCursor))
        self.services = QPushButton(self.menubar)
        self.services.setObjectName(u"services")
        self.services.setGeometry(QRect(0, 570, 331, 71))
        self.services.setFont(font3)
        self.services.setCursor(QCursor(Qt.PointingHandCursor))
        self.employees = QPushButton(self.menubar)
        self.employees.setObjectName(u"employees")
        self.employees.setGeometry(QRect(0, 640, 331, 71))
        self.employees.setFont(font3)
        self.employees.setCursor(QCursor(Qt.PointingHandCursor))
        self.logout = QPushButton(self.menubar)
        self.logout.setObjectName(u"logout")
        self.logout.setGeometry(QRect(0, 833, 331, 71))
        self.logout.setFont(font3)
        self.logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.mem_status = QPushButton(self.menubar)
        self.mem_status.setObjectName(u"mem_status")
        self.mem_status.setGeometry(QRect(0, 430, 331, 71))
        self.mem_status.setFont(font3)
        self.mem_status.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_container = QStackedWidget(self.centralwidget)
        self.menu_container.setObjectName(u"menu_container")
        self.menu_container.setGeometry(QRect(421, 50, 921, 851))
        self.menu_container.setStyleSheet(u"background-color: #5F8B6D;")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.notif_table = QTableWidget(self.home_page)
        if (self.notif_table.columnCount() < 2):
            self.notif_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.notif_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.notif_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.notif_table.setObjectName(u"notif_table")
        self.notif_table.setGeometry(QRect(80, 60, 771, 41))
        font4 = QFont()
        font4.setPointSize(11)
        self.notif_table.setFont(font4)
        self.notif_table.setStyleSheet(u"QTableWidget{\n"
"background-color: rgba(0,0,0,10%);\n"
"gridline-color: transparent;\n"
"color:  rgba(0,0,0,60%);\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"QHeaderView::Section{\n"
"background-color: rgba(0,0,0,7%);\n"
"height: 0;\n"
"margin-bottom: 5px;\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"padding: 15px 10px 15px 10px;\n"
"border-bottom: rgba(0,0,0,10%);\n"
"font-size: 10px;\n"
"outline: none;\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"border: none;\n"
"}\n"
"")
        self.notif_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.notif_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.notif_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.notif_table.horizontalHeader().setHighlightSections(False)
        self.notif_table.verticalHeader().setHighlightSections(False)
        self.notifBtn = QPushButton(self.home_page)
        self.notifBtn.setObjectName(u"notifBtn")
        self.notifBtn.setGeometry(QRect(70, 0, 171, 41))
        self.notifBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.notifBtn.setStyleSheet(u"background: none;\n"
"text-align: right;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/icons8-bell-100 (1) 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.notifBtn.setIcon(icon)
        self.notifBtn.setIconSize(QSize(40, 40))
        self.notiflabel = QLabel(self.home_page)
        self.notiflabel.setObjectName(u"notiflabel")
        self.notiflabel.setGeometry(QRect(80, 10, 141, 20))
        font5 = QFont()
        font5.setFamily(u"Noto Sans")
        font5.setPointSize(14)
        font5.setBold(False)
        font5.setLegacyWeight(50)
        self.notiflabel.setFont(font5)
        self.notiflabel.setStyleSheet(u"font-family: \"Noto Sans\", sans-serif;\n"
"letter-spacing: 1px;\n"
"color: #fff;")
        self.expand_notif = QPushButton(self.home_page)
        self.expand_notif.setObjectName(u"expand_notif")
        self.expand_notif.setGeometry(QRect(450, 90, 30, 30))
        self.expand_notif.setCursor(QCursor(Qt.PointingHandCursor))
        self.expand_notif.setStyleSheet(u"background-color: rgba(0,0,0,20%);\n"
"border-radius:15px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/Double Down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.expand_notif.setIcon(icon1)
        self.expand_notif.setIconSize(QSize(19, 19))
        self.minimize_notif = QPushButton(self.home_page)
        self.minimize_notif.setObjectName(u"minimize_notif")
        self.minimize_notif.setGeometry(QRect(450, 700, 0, 30))
        self.minimize_notif.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_notif.setStyleSheet(u"background-color: rgba(0,0,0,20%);\n"
"border-radius:15px;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/Double Up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_notif.setIcon(icon2)
        self.minimize_notif.setIconSize(QSize(19, 19))
        self.widget = QWidget(self.home_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 50, 771, 2))
        self.widget.setStyleSheet(u"background-color: rgba(0,0,0,30%);")
        self.menu_container.addWidget(self.home_page)
        self.notif_table.raise_()
        self.notiflabel.raise_()
        self.notifBtn.raise_()
        self.expand_notif.raise_()
        self.minimize_notif.raise_()
        self.widget.raise_()
        self.member_list_page = QWidget()
        self.member_list_page.setObjectName(u"member_list_page")
        self.mem_search = QLineEdit(self.member_list_page)
        self.mem_search.setObjectName(u"mem_search")
        self.mem_search.setGeometry(QRect(50, 30, 361, 40))
        self.mem_search.setFont(font4)
        self.mem_search.setStyleSheet(u"background-color: #467855;\n"
"border-radius: 20px;\n"
"padding: 0 40px 0 15px;")
        self.mem_search.setCursorPosition(0)
        self.mem_search_icon = QLabel(self.member_list_page)
        self.mem_search_icon.setObjectName(u"mem_search_icon")
        self.mem_search_icon.setGeometry(QRect(375, 38, 23, 23))
        self.mem_search_icon.setStyleSheet(u"background: none;")
        self.mem_search_icon.setPixmap(QPixmap(u"icons/icons8-search-50 1.png"))
        self.mem_search_icon.setScaledContents(True)
        self.delete_member = QPushButton(self.member_list_page)
        self.delete_member.setObjectName(u"delete_member")
        self.delete_member.setGeometry(QRect(480, 28, 41, 41))
        self.delete_member.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_member.setStyleSheet(u"background: none;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/icons8-remove-100 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_member.setIcon(icon3)
        self.delete_member.setIconSize(QSize(40, 40))
        self.edit_member = QPushButton(self.member_list_page)
        self.edit_member.setObjectName(u"edit_member")
        self.edit_member.setGeometry(QRect(850, 30, 41, 41))
        self.edit_member.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit_member.setStyleSheet(u"background: none;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_member.setIcon(icon4)
        self.edit_member.setIconSize(QSize(40, 40))
        self.widget_2 = QWidget(self.member_list_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(440, 40, 21, 21))
        self.widget_2.setStyleSheet(u"background-color: #ffffff;")
        self.widget_3 = QWidget(self.member_list_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(490, 40, 21, 21))
        self.widget_3.setStyleSheet(u"background-color: #ffffff;")
        self.add_member = QPushButton(self.member_list_page)
        self.add_member.setObjectName(u"add_member")
        self.add_member.setGeometry(QRect(430, 30, 41, 41))
        self.add_member.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_member.setStyleSheet(u"background: none;")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/icons8-add-100 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_member.setIcon(icon5)
        self.add_member.setIconSize(QSize(40, 40))
        self.mem_table = QTableWidget(self.member_list_page)
        if (self.mem_table.columnCount() < 6):
            self.mem_table.setColumnCount(6)
        font6 = QFont()
        font6.setPointSize(12)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font6);
        self.mem_table.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font6);
        self.mem_table.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font6);
        self.mem_table.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font6);
        self.mem_table.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font6);
        self.mem_table.setHorizontalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font6);
        self.mem_table.setHorizontalHeaderItem(5, __qtablewidgetitem7)
        self.mem_table.setObjectName(u"mem_table")
        self.mem_table.setGeometry(QRect(50, 110, 841, 651))
        font7 = QFont()
        font7.setPointSize(10)
        self.mem_table.setFont(font7)
        self.mem_table.setStyleSheet(u"QTableWidget {\n"
"    background-color: #4B805A;\n"
"    color: #000;\n"
"    gridline-color: transparent; \n"
"	border-spacing: 0 1px;\n"
"	border: none;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #437A54;\n"
"   	color: #fff;\n"
"	padding: 3px;\n"
"	border: none; 	\n"
"	border-bottom: 1px solid #467855;\n"
"	font-weight: 600;\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: #4B805A;\n"
"    color: #fff;\n"
"    border-bottom: 1px solid #467855;\n"
"	padding: 3px;\n"
"	font-size: 10px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgba(255,255,255,20%);\n"
"    color: #fff;\n"
"	gridline-color: rgba(255,255,255,20%); \n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"border: none;\n"
"background-color: #075E20;\n"
"height: 16px;\n"
"margin: 0 0 0 15px;\n"
"border-radius: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"background-color: #437A54;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"background-col"
                        "or: #075E20;\n"
"}")
        self.mem_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.mem_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.mem_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.mem_table.setTextElideMode(Qt.ElideMiddle)
        self.mem_table.setShowGrid(True)
        self.mem_table.setGridStyle(Qt.SolidLine)
        self.mem_table.setSortingEnabled(True)
        self.mem_table.setCornerButtonEnabled(True)
        self.mem_table.horizontalHeader().setHighlightSections(False)
        self.mem_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.mem_table.horizontalHeader().setStretchLastSection(False)
        self.mem_table.verticalHeader().setCascadingSectionResizes(False)
        self.mem_table.verticalHeader().setHighlightSections(False)
        self.mem_table.verticalHeader().setProperty("showSortIndicator", False)
        self.menu_container.addWidget(self.member_list_page)
        self.widget_3.raise_()
        self.widget_2.raise_()
        self.mem_search.raise_()
        self.delete_member.raise_()
        self.edit_member.raise_()
        self.add_member.raise_()
        self.mem_table.raise_()
        self.mem_search_icon.raise_()
        self.memship_status_page = QWidget()
        self.memship_status_page.setObjectName(u"memship_status_page")
        self.mshipStat_table = QTableWidget(self.memship_status_page)
        if (self.mshipStat_table.columnCount() < 5):
            self.mshipStat_table.setColumnCount(5)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font6);
        __qtablewidgetitem8.setBackground(QColor(70, 120, 85));
        self.mshipStat_table.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font6);
        __qtablewidgetitem9.setBackground(QColor(70, 120, 85));
        self.mshipStat_table.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font6);
        self.mshipStat_table.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font6);
        self.mshipStat_table.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font6);
        self.mshipStat_table.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        self.mshipStat_table.setObjectName(u"mshipStat_table")
        self.mshipStat_table.setGeometry(QRect(50, 110, 841, 651))
        self.mshipStat_table.setFont(font7)
        self.mshipStat_table.setStyleSheet(u"QTableWidget {\n"
"    background-color: #4B805A;\n"
"    color: #000;\n"
"    gridline-color: transparent; \n"
"	border-spacing: 0 1px;\n"
"	border: none;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #437A54;\n"
"   	color: #fff;\n"
"	padding: 3px;\n"
"	border: none; 	\n"
"	border-bottom: 1px solid #467855;\n"
"	font-weight: 600;\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: #4B805A;\n"
"    color: #fff;\n"
"    border-bottom: 1px solid #467855;\n"
"	padding: 3px;\n"
"	font-size: 10px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgba(255,255,255,20%);\n"
"    color: #fff;\n"
"	gridline-color: rgba(255,255,255,20%);\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"border: none;\n"
"background-color: #075E20;\n"
"height: 16px;\n"
"margin: 0 0 0 15px;\n"
"border-radius: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"background-color: #437A54;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"background-colo"
                        "r: #075E20;\n"
"}")
        self.mshipStat_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.mshipStat_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.mshipStat_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.mshipStat_table.setTextElideMode(Qt.ElideMiddle)
        self.mshipStat_table.setShowGrid(True)
        self.mshipStat_table.setGridStyle(Qt.SolidLine)
        self.mshipStat_table.setSortingEnabled(True)
        self.mshipStat_table.setCornerButtonEnabled(True)
        self.mshipStat_table.horizontalHeader().setDefaultSectionSize(100)
        self.mshipStat_table.horizontalHeader().setHighlightSections(False)
        self.mshipStat_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.mshipStat_table.verticalHeader().setHighlightSections(False)
        self.mshipStat_table.verticalHeader().setProperty("showSortIndicator", False)
        self.mshipStat_search_icon = QLabel(self.memship_status_page)
        self.mshipStat_search_icon.setObjectName(u"mshipStat_search_icon")
        self.mshipStat_search_icon.setGeometry(QRect(375, 38, 23, 23))
        self.mshipStat_search_icon.setStyleSheet(u"background: none;")
        self.mshipStat_search_icon.setPixmap(QPixmap(u"icons/icons8-search-50 1.png"))
        self.mshipStat_search_icon.setScaledContents(True)
        self.mshipStat_search = QLineEdit(self.memship_status_page)
        self.mshipStat_search.setObjectName(u"mshipStat_search")
        self.mshipStat_search.setGeometry(QRect(50, 30, 361, 40))
        self.mshipStat_search.setFont(font4)
        self.mshipStat_search.setStyleSheet(u"background-color: #467855;\n"
"border-radius: 20px;\n"
"padding: 0 40px 0 15px;")
        self.mshipStat_search.setCursorPosition(0)
        self.menu_container.addWidget(self.memship_status_page)
        self.mshipStat_table.raise_()
        self.mshipStat_search.raise_()
        self.mshipStat_search_icon.raise_()
        self.mon_serviceLog_page = QWidget()
        self.mon_serviceLog_page.setObjectName(u"mon_serviceLog_page")
        self.mon_serviceLog_searchIcon = QLabel(self.mon_serviceLog_page)
        self.mon_serviceLog_searchIcon.setObjectName(u"mon_serviceLog_searchIcon")
        self.mon_serviceLog_searchIcon.setGeometry(QRect(375, 38, 23, 23))
        self.mon_serviceLog_searchIcon.setStyleSheet(u"background: none;")
        self.mon_serviceLog_searchIcon.setPixmap(QPixmap(u"icons/icons8-search-50 1.png"))
        self.mon_serviceLog_searchIcon.setScaledContents(True)
        self.mon_serviceLog_search = QLineEdit(self.mon_serviceLog_page)
        self.mon_serviceLog_search.setObjectName(u"mon_serviceLog_search")
        self.mon_serviceLog_search.setGeometry(QRect(50, 30, 361, 40))
        self.mon_serviceLog_search.setFont(font4)
        self.mon_serviceLog_search.setStyleSheet(u"background-color: #467855;\n"
"border-radius: 20px;\n"
"padding: 0 40px 0 15px;")
        self.mon_serviceLog_search.setCursorPosition(0)
        self.mon_serviceLog_table = QTableWidget(self.mon_serviceLog_page)
        if (self.mon_serviceLog_table.columnCount() < 8):
            self.mon_serviceLog_table.setColumnCount(8)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font6);
        __qtablewidgetitem13.setBackground(QColor(70, 120, 85));
        self.mon_serviceLog_table.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font6);
        __qtablewidgetitem14.setBackground(QColor(70, 120, 85));
        self.mon_serviceLog_table.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font6);
        self.mon_serviceLog_table.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font6);
        self.mon_serviceLog_table.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font6);
        self.mon_serviceLog_table.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font6);
        self.mon_serviceLog_table.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font6);
        self.mon_serviceLog_table.setHorizontalHeaderItem(6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font6);
        __qtablewidgetitem20.setBackground(QColor(70, 120, 85));
        self.mon_serviceLog_table.setHorizontalHeaderItem(7, __qtablewidgetitem20)
        self.mon_serviceLog_table.setObjectName(u"mon_serviceLog_table")
        self.mon_serviceLog_table.setGeometry(QRect(50, 110, 841, 651))
        self.mon_serviceLog_table.setFont(font7)
        self.mon_serviceLog_table.setStyleSheet(u"QTableWidget {\n"
"    background-color: #4B805A;\n"
"    color: #000;\n"
"    gridline-color: transparent; \n"
"	border-spacing: 0 1px;\n"
"	border: none;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #437A54;\n"
"   	color: #fff;\n"
"	padding: 3px;\n"
"	border: none; 	\n"
"	border-bottom: 1px solid #467855;\n"
"	font-weight: 600;\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: #4B805A;\n"
"    color: #fff;\n"
"    border-bottom: 1px solid #467855;\n"
"	padding: 3px;\n"
"	font-size: 10px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgba(255,255,255,20%);\n"
"    color: #fff;\n"
"	gridline-color: rgba(255,255,255,20%);\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"border: none;\n"
"background-color: #075E20;\n"
"height: 16px;\n"
"margin: 0 0 0 15px;\n"
"border-radius: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"background-color: #437A54;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"background-colo"
                        "r: #075E20;\n"
"}")
        self.mon_serviceLog_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.mon_serviceLog_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.mon_serviceLog_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.mon_serviceLog_table.setTextElideMode(Qt.ElideMiddle)
        self.mon_serviceLog_table.setShowGrid(True)
        self.mon_serviceLog_table.setGridStyle(Qt.SolidLine)
        self.mon_serviceLog_table.setSortingEnabled(True)
        self.mon_serviceLog_table.setCornerButtonEnabled(True)
        self.mon_serviceLog_table.horizontalHeader().setDefaultSectionSize(100)
        self.mon_serviceLog_table.horizontalHeader().setHighlightSections(False)
        self.mon_serviceLog_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.mon_serviceLog_table.verticalHeader().setHighlightSections(False)
        self.mon_serviceLog_table.verticalHeader().setProperty("showSortIndicator", False)
        self.renew_btn = QPushButton(self.mon_serviceLog_page)
        self.renew_btn.setObjectName(u"renew_btn")
        self.renew_btn.setGeometry(QRect(780, 40, 111, 31))
        self.renew_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.renew_btn.setStyleSheet(u"background-color: #30BD58;\n"
"border-radius: 7px;")
        self.menu_container.addWidget(self.mon_serviceLog_page)
        self.mon_serviceLog_search.raise_()
        self.mon_serviceLog_table.raise_()
        self.renew_btn.raise_()
        self.mon_serviceLog_searchIcon.raise_()
        self.transaction_page = QWidget()
        self.transaction_page.setObjectName(u"transaction_page")
        self.transac_table = QTableWidget(self.transaction_page)
        if (self.transac_table.columnCount() < 8):
            self.transac_table.setColumnCount(8)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font6);
        self.transac_table.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font6);
        self.transac_table.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font6);
        self.transac_table.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font6);
        self.transac_table.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font6);
        self.transac_table.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font6);
        self.transac_table.setHorizontalHeaderItem(5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font6);
        self.transac_table.setHorizontalHeaderItem(6, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font6);
        self.transac_table.setHorizontalHeaderItem(7, __qtablewidgetitem28)
        self.transac_table.setObjectName(u"transac_table")
        self.transac_table.setGeometry(QRect(40, 110, 861, 651))
        self.transac_table.setFont(font7)
        self.transac_table.setStyleSheet(u"QTableWidget {\n"
"    background-color: #4B805A;\n"
"    color: #000;\n"
"    gridline-color: transparent; \n"
"	border-spacing: 0 1px;\n"
"	border: none;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #437A54;\n"
"   	color: #fff;\n"
"	padding: 3px;\n"
"	border: none; 	\n"
"	border-bottom: 1px solid #467855;\n"
"	font-weight: 600;\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: #4B805A;\n"
"    color: #fff;\n"
"    border-bottom: 1px solid #467855;\n"
"	padding: 3px;\n"
"	font-size: 10px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgba(255,255,255,20%);\n"
"    color: #fff;\n"
"	gridline-color: rgba(255,255,255,20%);\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"border: none;\n"
"background-color: #075E20;\n"
"height: 16px;\n"
"margin: 0 0 0 15px;\n"
"border-radius: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"background-color: #437A54;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"background-colo"
                        "r: #075E20;\n"
"}")
        self.transac_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.transac_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.transac_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.transac_table.setTextElideMode(Qt.ElideMiddle)
        self.transac_table.setGridStyle(Qt.SolidLine)
        self.transac_table.setSortingEnabled(True)
        self.transac_table.setCornerButtonEnabled(True)
        self.transac_table.horizontalHeader().setHighlightSections(False)
        self.transac_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.transac_table.verticalHeader().setHighlightSections(False)
        self.transac_table.verticalHeader().setProperty("showSortIndicator", False)
        self.transac_search = QLineEdit(self.transaction_page)
        self.transac_search.setObjectName(u"transac_search")
        self.transac_search.setGeometry(QRect(40, 30, 371, 40))
        self.transac_search.setFont(font4)
        self.transac_search.setStyleSheet(u"background-color: #467855;\n"
"border-radius: 20px;\n"
"padding: 0 40px 0 15px;")
        self.transac_search.setCursorPosition(0)
        self.transac_search_icon = QLabel(self.transaction_page)
        self.transac_search_icon.setObjectName(u"transac_search_icon")
        self.transac_search_icon.setGeometry(QRect(375, 38, 23, 23))
        self.transac_search_icon.setStyleSheet(u"background: none;")
        self.transac_search_icon.setPixmap(QPixmap(u"icons/icons8-search-50 1.png"))
        self.transac_search_icon.setScaledContents(True)
        self.menu_container.addWidget(self.transaction_page)
        self.employees_page = QWidget()
        self.employees_page.setObjectName(u"employees_page")
        self.emp_search = QLineEdit(self.employees_page)
        self.emp_search.setObjectName(u"emp_search")
        self.emp_search.setGeometry(QRect(50, 30, 361, 40))
        self.emp_search.setFont(font4)
        self.emp_search.setStyleSheet(u"background-color: #467855;\n"
"border-radius: 20px;\n"
"padding: 0 40px 0 15px;")
        self.emp_search.setCursorPosition(0)
        self.widget_7 = QWidget(self.employees_page)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(490, 40, 21, 21))
        self.widget_7.setStyleSheet(u"background-color: #ffffff;")
        self.widget_8 = QWidget(self.employees_page)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(440, 40, 21, 21))
        self.widget_8.setStyleSheet(u"background-color: #ffffff;")
        self.emp_table = QTableWidget(self.employees_page)
        if (self.emp_table.columnCount() < 6):
            self.emp_table.setColumnCount(6)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font6);
        self.emp_table.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font6);
        self.emp_table.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font6);
        self.emp_table.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font6);
        self.emp_table.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font6);
        self.emp_table.setHorizontalHeaderItem(4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font6);
        self.emp_table.setHorizontalHeaderItem(5, __qtablewidgetitem34)
        self.emp_table.setObjectName(u"emp_table")
        self.emp_table.setGeometry(QRect(50, 110, 841, 651))
        self.emp_table.setFont(font7)
        self.emp_table.setStyleSheet(u"QTableWidget {\n"
"    background-color: #4B805A;\n"
"    color: #000;\n"
"    gridline-color: transparent; \n"
"	border-spacing: 0 1px;\n"
"	border: none;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #437A54;\n"
"   	color: #fff;\n"
"	padding: 3px;\n"
"	border: none; 	\n"
"	border-bottom: 1px solid #467855;\n"
"	font-weight: 600;\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: #4B805A;\n"
"    color: #fff;\n"
"    border-bottom: 1px solid #467855;\n"
"	padding: 3px;\n"
"	font-size: 10px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgba(255,255,255,20%);\n"
"    color: #fff;\n"
"	gridline-color: rgba(255,255,255,20%);\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"border: none;\n"
"background-color: #075E20;\n"
"height: 16px;\n"
"margin: 0 0 0 15px;\n"
"border-radius: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"background-color: #437A54;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"background-colo"
                        "r: #075E20;\n"
"}")
        self.emp_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.emp_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.emp_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.emp_table.setTextElideMode(Qt.ElideMiddle)
        self.emp_table.setShowGrid(True)
        self.emp_table.setGridStyle(Qt.SolidLine)
        self.emp_table.setSortingEnabled(True)
        self.emp_table.setCornerButtonEnabled(True)
        self.emp_table.horizontalHeader().setHighlightSections(False)
        self.emp_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.emp_table.verticalHeader().setHighlightSections(False)
        self.emp_table.verticalHeader().setProperty("showSortIndicator", False)
        self.add_employee = QPushButton(self.employees_page)
        self.add_employee.setObjectName(u"add_employee")
        self.add_employee.setGeometry(QRect(430, 30, 41, 41))
        self.add_employee.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_employee.setStyleSheet(u"background: none;")
        self.add_employee.setIcon(icon5)
        self.add_employee.setIconSize(QSize(40, 40))
        self.pushButton_9 = QPushButton(self.employees_page)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(850, 30, 51, 41))
        self.pushButton_9.setStyleSheet(u"background: none;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/icons8-edit-25 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon6)
        self.pushButton_9.setIconSize(QSize(40, 40))
        self.delete_employee = QPushButton(self.employees_page)
        self.delete_employee.setObjectName(u"delete_employee")
        self.delete_employee.setGeometry(QRect(480, 28, 41, 41))
        self.delete_employee.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_employee.setStyleSheet(u"background: none;")
        self.delete_employee.setIcon(icon3)
        self.delete_employee.setIconSize(QSize(40, 40))
        self.emp_search_icon = QLabel(self.employees_page)
        self.emp_search_icon.setObjectName(u"emp_search_icon")
        self.emp_search_icon.setGeometry(QRect(375, 38, 23, 23))
        self.emp_search_icon.setStyleSheet(u"background: none;")
        self.emp_search_icon.setPixmap(QPixmap(u"icons/icons8-search-50 1.png"))
        self.emp_search_icon.setScaledContents(True)
        self.edit_employee = QPushButton(self.employees_page)
        self.edit_employee.setObjectName(u"edit_employee")
        self.edit_employee.setGeometry(QRect(850, 30, 41, 41))
        self.edit_employee.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit_employee.setStyleSheet(u"background: none;")
        self.edit_employee.setIcon(icon4)
        self.edit_employee.setIconSize(QSize(40, 40))
        self.menu_container.addWidget(self.employees_page)
        self.emp_search.raise_()
        self.widget_7.raise_()
        self.widget_8.raise_()
        self.emp_table.raise_()
        self.add_employee.raise_()
        self.pushButton_9.raise_()
        self.delete_employee.raise_()
        self.edit_employee.raise_()
        self.emp_search_icon.raise_()
        self.view_details_popup = QWidget(self.centralwidget)
        self.view_details_popup.setObjectName(u"view_details_popup")
        self.view_details_popup.setGeometry(QRect(-10, 0, 0, 902))
        self.view_details_popup.setStyleSheet(u"background-color: rgba(0,0,0,160);")
        self.view_details_widget = QWidget(self.view_details_popup)
        self.view_details_widget.setObjectName(u"view_details_widget")
        self.view_details_widget.setGeometry(QRect(260, 160, 851, 571))
        self.view_details_widget.setStyleSheet(u"#view_details_widget{\n"
"background-color: #FFFFFF;\n"
"border-radius:  15px;\n"
"\n"
"}")
        self.widget_6 = QWidget(self.view_details_widget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(60, 110, 131, 31))
        self.widget_6.setStyleSheet(u"background-color: #346F45;\n"
"border-top-rigth-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_24 = QLabel(self.widget_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(0, 0, 131, 31))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(52, 111, 69, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.label_24.setPalette(palette)
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(10)
        font8.setBold(True)
        font8.setLegacyWeight(75)
        self.label_24.setFont(font8)
        self.label_24.setAlignment(Qt.AlignCenter)
        self.widget_9 = QWidget(self.view_details_widget)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(180, 110, 211, 31))
        self.widget_9.setStyleSheet(u"background-color: #D9D9D9;")
        self.viewmem_Id = QLabel(self.widget_9)
        self.viewmem_Id.setObjectName(u"viewmem_Id")
        self.viewmem_Id.setGeometry(QRect(10, 0, 201, 31))
        font9 = QFont()
        font9.setFamily(u"MS Shell Dlg 2")
        font9.setPointSize(10)
        self.viewmem_Id.setFont(font9)
        self.viewmem_Id.setStyleSheet(u"padding: 5px;\n"
"color: #003910;")
        self.widget_24 = QWidget(self.view_details_widget)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setGeometry(QRect(180, 160, 211, 31))
        self.widget_24.setStyleSheet(u"background-color: #D9D9D9;")
        self.viewmem_name = QLabel(self.widget_24)
        self.viewmem_name.setObjectName(u"viewmem_name")
        self.viewmem_name.setGeometry(QRect(10, 0, 201, 31))
        self.viewmem_name.setFont(font9)
        self.viewmem_name.setStyleSheet(u"padding: 5px; color: #003910;")
        self.widget_40 = QWidget(self.view_details_widget)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setGeometry(QRect(60, 210, 131, 31))
        self.widget_40.setStyleSheet(u"background-color: #346F45;\n"
"border-top-rigth-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_25 = QLabel(self.widget_40)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(0, 0, 131, 31))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_25.setPalette(palette1)
        self.label_25.setFont(font8)
        self.label_25.setAlignment(Qt.AlignCenter)
        self.widget_39 = QWidget(self.view_details_widget)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setGeometry(QRect(180, 210, 211, 31))
        self.widget_39.setStyleSheet(u"background-color: #D9D9D9;")
        self.viewmem_DOB = QLabel(self.widget_39)
        self.viewmem_DOB.setObjectName(u"viewmem_DOB")
        self.viewmem_DOB.setGeometry(QRect(10, 0, 201, 31))
        self.viewmem_DOB.setFont(font9)
        self.viewmem_DOB.setStyleSheet(u"padding: 5px; color: #003910;")
        self.widget_42 = QWidget(self.view_details_widget)
        self.widget_42.setObjectName(u"widget_42")
        self.widget_42.setGeometry(QRect(60, 260, 131, 31))
        self.widget_42.setStyleSheet(u"background-color: #346F45;\n"
"border-top-rigth-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_26 = QLabel(self.widget_42)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(0, 0, 131, 31))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_26.setPalette(palette2)
        self.label_26.setFont(font8)
        self.label_26.setAlignment(Qt.AlignCenter)
        self.widget_41 = QWidget(self.view_details_widget)
        self.widget_41.setObjectName(u"widget_41")
        self.widget_41.setGeometry(QRect(180, 260, 211, 31))
        self.widget_41.setStyleSheet(u"background-color: #D9D9D9;")
        self.viewmem_address = QLabel(self.widget_41)
        self.viewmem_address.setObjectName(u"viewmem_address")
        self.viewmem_address.setGeometry(QRect(10, 0, 201, 31))
        self.viewmem_address.setFont(font9)
        self.viewmem_address.setStyleSheet(u"padding: 5px; color: #003910;")
        self.widget_44 = QWidget(self.view_details_widget)
        self.widget_44.setObjectName(u"widget_44")
        self.widget_44.setGeometry(QRect(60, 310, 131, 31))
        self.widget_44.setStyleSheet(u"background-color: #346F45;\n"
"border-top-rigth-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_27 = QLabel(self.widget_44)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(0, 0, 131, 31))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_27.setPalette(palette3)
        self.label_27.setFont(font8)
        self.label_27.setAlignment(Qt.AlignCenter)
        self.widget_43 = QWidget(self.view_details_widget)
        self.widget_43.setObjectName(u"widget_43")
        self.widget_43.setGeometry(QRect(180, 310, 211, 31))
        self.widget_43.setStyleSheet(u"background-color: #D9D9D9;")
        self.viewmem_telnum = QLabel(self.widget_43)
        self.viewmem_telnum.setObjectName(u"viewmem_telnum")
        self.viewmem_telnum.setGeometry(QRect(10, 0, 201, 31))
        self.viewmem_telnum.setFont(font9)
        self.viewmem_telnum.setStyleSheet(u"padding: 5px; color: #003910;")
        self.widget_46 = QWidget(self.view_details_widget)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setGeometry(QRect(60, 360, 131, 31))
        self.widget_46.setStyleSheet(u"background-color: #346F45;\n"
"border-top-rigth-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_28 = QLabel(self.widget_46)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(0, 0, 131, 31))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_28.setPalette(palette4)
        self.label_28.setFont(font8)
        self.label_28.setAlignment(Qt.AlignCenter)
        self.widget_45 = QWidget(self.view_details_widget)
        self.widget_45.setObjectName(u"widget_45")
        self.widget_45.setGeometry(QRect(180, 360, 211, 31))
        self.widget_45.setStyleSheet(u"background-color: #D9D9D9;")
        self.viewmem_physicalAct = QLabel(self.widget_45)
        self.viewmem_physicalAct.setObjectName(u"viewmem_physicalAct")
        self.viewmem_physicalAct.setGeometry(QRect(10, 0, 201, 31))
        self.viewmem_physicalAct.setFont(font9)
        self.viewmem_physicalAct.setStyleSheet(u"padding: 5px; color: #003910;")
        self.widget_48 = QWidget(self.view_details_widget)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setGeometry(QRect(60, 410, 131, 31))
        self.widget_48.setStyleSheet(u"background-color: #346F45;\n"
"border-top-rigth-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_29 = QLabel(self.widget_48)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(0, 0, 131, 22))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_29.setPalette(palette5)
        self.label_29.setFont(font8)
        self.label_29.setAlignment(Qt.AlignCenter)
        self.widget_47 = QWidget(self.view_details_widget)
        self.widget_47.setObjectName(u"widget_47")
        self.widget_47.setGeometry(QRect(180, 410, 211, 31))
        self.widget_47.setStyleSheet(u"background-color: #D9D9D9;")
        self.viewmem_medicalAilments = QLabel(self.widget_47)
        self.viewmem_medicalAilments.setObjectName(u"viewmem_medicalAilments")
        self.viewmem_medicalAilments.setGeometry(QRect(10, 0, 201, 31))
        self.viewmem_medicalAilments.setFont(font9)
        self.viewmem_medicalAilments.setStyleSheet(u"padding: 5px; color: #003910;")
        self.widget_50 = QWidget(self.view_details_widget)
        self.widget_50.setObjectName(u"widget_50")
        self.widget_50.setGeometry(QRect(460, 410, 131, 31))
        self.widget_50.setStyleSheet(u"background-color: #346F45;\n"
"border-top-rigth-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_30 = QLabel(self.widget_50)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(0, 0, 131, 31))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_30.setPalette(palette6)
        self.label_30.setFont(font8)
        self.label_30.setAlignment(Qt.AlignCenter)
        self.widget_49 = QWidget(self.view_details_widget)
        self.widget_49.setObjectName(u"widget_49")
        self.widget_49.setGeometry(QRect(580, 410, 211, 31))
        self.widget_49.setStyleSheet(u"background-color: #D9D9D9;")
        self.viewmem_prevGym = QLabel(self.widget_49)
        self.viewmem_prevGym.setObjectName(u"viewmem_prevGym")
        self.viewmem_prevGym.setGeometry(QRect(10, 0, 201, 31))
        self.viewmem_prevGym.setFont(font9)
        self.viewmem_prevGym.setStyleSheet(u"padding: 5px; color: #003910;")
        self.widget_38 = QWidget(self.view_details_widget)
        self.widget_38.setObjectName(u"widget_38")
        self.widget_38.setGeometry(QRect(60, 160, 131, 31))
        self.widget_38.setStyleSheet(u"background-color: #346F45;\n"
"border-top-rigth-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_23 = QLabel(self.widget_38)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(-2, 0, 131, 31))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_23.setPalette(palette7)
        self.label_23.setFont(font8)
        self.label_23.setAlignment(Qt.AlignCenter)
        self.widget_54 = QWidget(self.view_details_widget)
        self.widget_54.setObjectName(u"widget_54")
        self.widget_54.setGeometry(QRect(580, 360, 211, 31))
        self.widget_54.setStyleSheet(u"background-color: #D9D9D9;")
        self.viewmem_type = QLabel(self.widget_54)
        self.viewmem_type.setObjectName(u"viewmem_type")
        self.viewmem_type.setGeometry(QRect(10, 0, 201, 31))
        self.viewmem_type.setStyleSheet(u"padding: 5px; color: #003910;")
        self.widget_53 = QWidget(self.view_details_widget)
        self.widget_53.setObjectName(u"widget_53")
        self.widget_53.setGeometry(QRect(460, 360, 131, 31))
        self.widget_53.setStyleSheet(u"background-color: #346F45;\n"
"border-top-rigth-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_36 = QLabel(self.widget_53)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(0, 0, 131, 31))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_36.setPalette(palette8)
        self.label_36.setFont(font8)
        self.label_36.setAlignment(Qt.AlignCenter)
        self.widget_56 = QWidget(self.view_details_widget)
        self.widget_56.setObjectName(u"widget_56")
        self.widget_56.setGeometry(QRect(580, 310, 211, 31))
        self.widget_56.setStyleSheet(u"background-color: #D9D9D9;")
        self.viewmem_status = QLabel(self.widget_56)
        self.viewmem_status.setObjectName(u"viewmem_status")
        self.viewmem_status.setGeometry(QRect(10, 0, 201, 31))
        self.viewmem_status.setFont(font9)
        self.viewmem_status.setStyleSheet(u"padding: 5px; color: #003910;")
        self.widget_55 = QWidget(self.view_details_widget)
        self.widget_55.setObjectName(u"widget_55")
        self.widget_55.setGeometry(QRect(460, 310, 131, 31))
        self.widget_55.setStyleSheet(u"background-color: #346F45;\n"
"border-top-rigth-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_35 = QLabel(self.widget_55)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(0, 0, 131, 31))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_35.setPalette(palette9)
        self.label_35.setFont(font8)
        self.label_35.setAlignment(Qt.AlignCenter)
        self.widget_58 = QWidget(self.view_details_widget)
        self.widget_58.setObjectName(u"widget_58")
        self.widget_58.setGeometry(QRect(580, 260, 211, 31))
        self.widget_58.setStyleSheet(u"background-color: #D9D9D9;")
        self.viewmem_BP = QLabel(self.widget_58)
        self.viewmem_BP.setObjectName(u"viewmem_BP")
        self.viewmem_BP.setGeometry(QRect(10, 0, 201, 31))
        self.viewmem_BP.setFont(font9)
        self.viewmem_BP.setStyleSheet(u"padding: 5px; color: #003910;")
        self.widget_57 = QWidget(self.view_details_widget)
        self.widget_57.setObjectName(u"widget_57")
        self.widget_57.setGeometry(QRect(460, 260, 131, 31))
        self.widget_57.setStyleSheet(u"background-color: #346F45;\n"
"border-top-rigth-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_34 = QLabel(self.widget_57)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(0, 0, 131, 31))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_34.setPalette(palette10)
        self.label_34.setFont(font8)
        self.label_34.setAlignment(Qt.AlignCenter)
        self.widget_60 = QWidget(self.view_details_widget)
        self.widget_60.setObjectName(u"widget_60")
        self.widget_60.setGeometry(QRect(460, 110, 131, 31))
        self.widget_60.setStyleSheet(u"background-color: #346F45;\n"
"border-top-rigth-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_33 = QLabel(self.widget_60)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(0, 0, 131, 31))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_33.setPalette(palette11)
        self.label_33.setFont(font8)
        self.label_33.setAlignment(Qt.AlignCenter)
        self.widget_59 = QWidget(self.view_details_widget)
        self.widget_59.setObjectName(u"widget_59")
        self.widget_59.setGeometry(QRect(580, 110, 211, 31))
        self.widget_59.setStyleSheet(u"background-color: #D9D9D9;")
        self.viewmem_Gender = QLabel(self.widget_59)
        self.viewmem_Gender.setObjectName(u"viewmem_Gender")
        self.viewmem_Gender.setGeometry(QRect(10, 0, 201, 31))
        self.viewmem_Gender.setFont(font9)
        self.viewmem_Gender.setStyleSheet(u"padding: 5px; color: #003910;")
        self.widget_62 = QWidget(self.view_details_widget)
        self.widget_62.setObjectName(u"widget_62")
        self.widget_62.setGeometry(QRect(460, 160, 131, 31))
        self.widget_62.setStyleSheet(u"background-color: #346F45;\n"
"border-top-rigth-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_31 = QLabel(self.widget_62)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(0, 0, 131, 31))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_31.setPalette(palette12)
        self.label_31.setFont(font8)
        self.label_31.setAlignment(Qt.AlignCenter)
        self.widget_61 = QWidget(self.view_details_widget)
        self.widget_61.setObjectName(u"widget_61")
        self.widget_61.setGeometry(QRect(580, 160, 211, 31))
        self.widget_61.setStyleSheet(u"background-color: #D9D9D9;")
        self.viewmem_weight = QLabel(self.widget_61)
        self.viewmem_weight.setObjectName(u"viewmem_weight")
        self.viewmem_weight.setGeometry(QRect(10, 0, 201, 31))
        self.viewmem_weight.setFont(font9)
        self.viewmem_weight.setStyleSheet(u"padding: 5px; color: #003910;")
        self.widget_64 = QWidget(self.view_details_widget)
        self.widget_64.setObjectName(u"widget_64")
        self.widget_64.setGeometry(QRect(580, 210, 211, 31))
        self.widget_64.setStyleSheet(u"background-color: #D9D9D9;")
        self.viewmem_height = QLabel(self.widget_64)
        self.viewmem_height.setObjectName(u"viewmem_height")
        self.viewmem_height.setGeometry(QRect(10, 0, 201, 31))
        self.viewmem_height.setFont(font9)
        self.viewmem_height.setStyleSheet(u"padding: 5px; color: #003910;")
        self.widget_63 = QWidget(self.view_details_widget)
        self.widget_63.setObjectName(u"widget_63")
        self.widget_63.setGeometry(QRect(460, 210, 131, 31))
        self.widget_63.setStyleSheet(u"background-color: #346F45;\n"
"border-top-rigth-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_32 = QLabel(self.widget_63)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(0, 0, 131, 31))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_32.setPalette(palette13)
        self.label_32.setFont(font8)
        self.label_32.setAlignment(Qt.AlignCenter)
        self.viewmem_backbtn = QPushButton(self.view_details_widget)
        self.viewmem_backbtn.setObjectName(u"viewmem_backbtn")
        self.viewmem_backbtn.setGeometry(QRect(690, 500, 101, 35))
        self.viewmem_backbtn.setFont(font3)
        self.viewmem_backbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.viewmem_backbtn.setStyleSheet(u"background-color: #167432;\n"
"border-radius: 15px;")
        self.widget_65 = QWidget(self.view_details_widget)
        self.widget_65.setObjectName(u"widget_65")
        self.widget_65.setGeometry(QRect(0, 0, 851, 61))
        self.widget_65.setStyleSheet(u"background-color: #346F45;\n"
"border-top-right-radius: 15px;\n"
"border-top-left-radius: 15px;")
        self.label_3 = QLabel(self.widget_65)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 20, 851, 20))
        font10 = QFont()
        font10.setFamily(u"Jaldi")
        font10.setPointSize(13)
        font10.setBold(True)
        font10.setLegacyWeight(75)
        self.label_3.setFont(font10)
        self.label_3.setStyleSheet(u"color: #FFFFFF;\n"
"font-family: \"Jaldi\", sans-serif;\n"
"background: none;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.widget_65.raise_()
        self.widget_24.raise_()
        self.widget_61.raise_()
        self.widget_59.raise_()
        self.widget_49.raise_()
        self.widget_47.raise_()
        self.widget_45.raise_()
        self.widget_43.raise_()
        self.widget_41.raise_()
        self.widget_39.raise_()
        self.widget_9.raise_()
        self.widget_6.raise_()
        self.widget_40.raise_()
        self.widget_42.raise_()
        self.widget_44.raise_()
        self.widget_46.raise_()
        self.widget_48.raise_()
        self.widget_50.raise_()
        self.widget_38.raise_()
        self.widget_54.raise_()
        self.widget_53.raise_()
        self.widget_56.raise_()
        self.widget_55.raise_()
        self.widget_58.raise_()
        self.widget_57.raise_()
        self.widget_60.raise_()
        self.widget_62.raise_()
        self.widget_64.raise_()
        self.widget_63.raise_()
        self.viewmem_backbtn.raise_()
        self.register_popup = QWidget(self.centralwidget)
        self.register_popup.setObjectName(u"register_popup")
        self.register_popup.setGeometry(QRect(0, 0, 0, 902))
        self.register_popup.setStyleSheet(u"background-color: rgba(0,0,0,160);")
        self.register_widget = QWidget(self.register_popup)
        self.register_widget.setObjectName(u"register_widget")
        self.register_widget.setEnabled(True)
        self.register_widget.setGeometry(QRect(260, 150, 851, 611))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.Button, brush)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.register_widget.setPalette(palette14)
        self.register_widget.setStyleSheet(u"#register_widget{\n"
"background-color: #FFFFFF;\n"
"border-radius:  15px;\n"
"}")
        self.widget_4 = QWidget(self.register_widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(0, 0, 851, 61))
        self.widget_4.setStyleSheet(u"background-color: #346F45;\n"
"border-top-right-radius: 15px;\n"
"border-top-left-radius: 15px;")
        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, -1, 851, 61))
        self.label_8.setFont(font10)
        self.label_8.setStyleSheet(u"#label_8{\n"
"color: #FFFFFF;\n"
"font-family: \"Jaldi\", sans-serif;\n"
"background: none;\n"
"}")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.regismem_fname = QLineEdit(self.register_widget)
        self.regismem_fname.setObjectName(u"regismem_fname")
        self.regismem_fname.setGeometry(QRect(60, 120, 251, 45))
        palette15 = QPalette()
        brush5 = QBrush(QColor(97, 146, 112, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.regismem_fname.setPalette(palette15)
        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(11)
        font11.setBold(True)
        font11.setLegacyWeight(75)
        self.regismem_fname.setFont(font11)
        self.regismem_fname.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.regismem_contact = QLineEdit(self.register_widget)
        self.regismem_contact.setObjectName(u"regismem_contact")
        self.regismem_contact.setGeometry(QRect(60, 200, 291, 45))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.regismem_contact.setPalette(palette16)
        self.regismem_contact.setFont(font11)
        self.regismem_contact.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.regismem_address = QLineEdit(self.register_widget)
        self.regismem_address.setObjectName(u"regismem_address")
        self.regismem_address.setGeometry(QRect(380, 200, 401, 45))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.regismem_address.setPalette(palette17)
        self.regismem_address.setFont(font11)
        self.regismem_address.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.regismem_medicAilment = QLineEdit(self.register_widget)
        self.regismem_medicAilment.setObjectName(u"regismem_medicAilment")
        self.regismem_medicAilment.setGeometry(QRect(60, 280, 391, 45))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.regismem_medicAilment.setPalette(palette18)
        self.regismem_medicAilment.setFont(font11)
        self.regismem_medicAilment.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.regismem_prevGym = QLineEdit(self.register_widget)
        self.regismem_prevGym.setObjectName(u"regismem_prevGym")
        self.regismem_prevGym.setGeometry(QRect(60, 370, 411, 45))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.regismem_prevGym.setPalette(palette19)
        self.regismem_prevGym.setFont(font11)
        self.regismem_prevGym.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.regismem_BP = QLineEdit(self.register_widget)
        self.regismem_BP.setObjectName(u"regismem_BP")
        self.regismem_BP.setGeometry(QRect(500, 370, 101, 45))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.regismem_BP.setPalette(palette20)
        self.regismem_BP.setFont(font11)
        self.regismem_BP.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.regismem_physicalAct = QLineEdit(self.register_widget)
        self.regismem_physicalAct.setObjectName(u"regismem_physicalAct")
        self.regismem_physicalAct.setGeometry(QRect(60, 450, 321, 45))
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.regismem_physicalAct.setPalette(palette21)
        self.regismem_physicalAct.setFont(font11)
        self.regismem_physicalAct.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.regismem_weight = QLineEdit(self.register_widget)
        self.regismem_weight.setObjectName(u"regismem_weight")
        self.regismem_weight.setGeometry(QRect(405, 450, 101, 45))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.regismem_weight.setPalette(palette22)
        self.regismem_weight.setFont(font11)
        self.regismem_weight.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.regismem_height = QLineEdit(self.register_widget)
        self.regismem_height.setObjectName(u"regismem_height")
        self.regismem_height.setGeometry(QRect(530, 450, 101, 45))
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.regismem_height.setPalette(palette23)
        self.regismem_height.setFont(font11)
        self.regismem_height.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.regismem_cancelbtn = QPushButton(self.register_widget)
        self.regismem_cancelbtn.setObjectName(u"regismem_cancelbtn")
        self.regismem_cancelbtn.setGeometry(QRect(550, 534, 101, 41))
        self.regismem_cancelbtn.setFont(font3)
        self.regismem_cancelbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.regismem_cancelbtn.setStyleSheet(u"background-color: #AE2626;\n"
"border-radius: 20px;")
        self.regismem_savebtn = QPushButton(self.register_widget)
        self.regismem_savebtn.setObjectName(u"regismem_savebtn")
        self.regismem_savebtn.setGeometry(QRect(680, 534, 101, 41))
        self.regismem_savebtn.setFont(font3)
        self.regismem_savebtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.regismem_savebtn.setStyleSheet(u"background-color: #167432;\n"
"border-radius: 20px;")
        self.regismemStud_radio = QRadioButton(self.register_widget)
        self.regismemStud_radio.setObjectName(u"regismemStud_radio")
        self.regismemStud_radio.setGeometry(QRect(500, 280, 111, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.regismemStud_radio.sizePolicy().hasHeightForWidth())
        self.regismemStud_radio.setSizePolicy(sizePolicy)
        palette24 = QPalette()
        brush6 = QBrush(QColor(88, 80, 80, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        brush7 = QBrush(QColor(88, 80, 80, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.regismemStud_radio.setPalette(palette24)
        self.regismemStud_radio.setFont(font11)
        self.regismemStud_radio.setStyleSheet(u"background: none;\n"
"color: #585050;")
        self.regismemStud_radio.setIconSize(QSize(20, 20))
        self.regismemProf_radio = QRadioButton(self.register_widget)
        self.regismemProf_radio.setObjectName(u"regismemProf_radio")
        self.regismemProf_radio.setGeometry(QRect(640, 280, 111, 41))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.regismemProf_radio.setPalette(palette25)
        self.regismemProf_radio.setFont(font11)
        self.regismemProf_radio.setStyleSheet(u"background: none;\n"
"color: #585050;")
        self.regismemProf_radio.setIconSize(QSize(20, 20))
        self.regismem_Status = QComboBox(self.register_widget)
        self.regismem_Status.addItem("")
        self.regismem_Status.addItem("")
        self.regismem_Status.addItem("")
        self.regismem_Status.setObjectName(u"regismem_Status")
        self.regismem_Status.setGeometry(QRect(630, 370, 151, 45))
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette26.setBrush(QPalette.Active, QPalette.Text, brush)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette26.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette26.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.regismem_Status.setPalette(palette26)
        self.regismem_Status.setFont(font11)
        self.regismem_Status.setStyleSheet(u"#regismem_Status{\n"
"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"color: #FFFFF;\n"
"}\n"
"\n"
"#regismem_Status::drop-down{\n"
"border: 0px;\n"
"width: 30px;\n"
"}\n"
"\n"
"#regismem_Status::down-arrow{\n"
"image: url(:/icons/icons/Drop Down.png);\n"
"width: 20px;\n"
"height: 20px;\n"
"margin-right: 17px;\n"
"}\n"
"\n"
"#regismem_Status QListView{\n"
"font-size: 11px;\n"
"padding: 5px;\n"
"border: 1px solid rgba(0,0,0,10%);\n"
"background-color: #fff;\n"
"color: #346F45;\n"
"outline: 0px;\n"
"}\n"
"\n"
"\n"
"#regismem_Status QListView:item{\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"#regismem_Status QListView:item:hover{\n"
"background-color: #619270;\n"
"color: #fff;\n"
"}\n"
"\n"
"")
        self.regismem_Status.setEditable(True)
        self.registermem_Gender = QComboBox(self.register_widget)
        self.registermem_Gender.addItem("")
        self.registermem_Gender.addItem("")
        self.registermem_Gender.addItem("")
        self.registermem_Gender.setObjectName(u"registermem_Gender")
        self.registermem_Gender.setGeometry(QRect(650, 450, 131, 45))
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette27.setBrush(QPalette.Active, QPalette.Text, brush)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette27.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette27.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.registermem_Gender.setPalette(palette27)
        self.registermem_Gender.setFont(font11)
        self.registermem_Gender.setStyleSheet(u"#registermem_Gender{\n"
"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"color: #FFFFF;\n"
"}\n"
"\n"
"#registermem_Gender::drop-down{\n"
"border: 0px;\n"
"width: 30px;\n"
"}\n"
"\n"
"#registermem_Gender::down-arrow{\n"
"image: url(:/icons/icons/Drop Down.png);\n"
"width: 20px;\n"
"height: 20px;\n"
"margin-right: 17px;\n"
"}\n"
"\n"
"#registermem_Gender QListView{\n"
"font-size: 11px;\n"
"padding: 5px;\n"
"border: 1px solid rgba(0,0,0,10%);\n"
"background-color: #fff;\n"
"color: #346F45;\n"
"outline: 0px;\n"
"}\n"
"\n"
"\n"
"#registermem_Gender QListView:item{\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"#registermem_Gender QListView:item:hover{\n"
"background-color: #619270;\n"
"color: #fff;\n"
"}\n"
"\n"
"")
        self.registermem_Gender.setEditable(True)
        self.regismem_DOB = QDateEdit(self.register_widget)
        self.regismem_DOB.setObjectName(u"regismem_DOB")
        self.regismem_DOB.setGeometry(QRect(620, 120, 161, 45))
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette28.setBrush(QPalette.Active, QPalette.Text, brush)
        palette28.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette28.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette28.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.regismem_DOB.setPalette(palette28)
        font12 = QFont()
        font12.setFamily(u"MS Shell Dlg 2")
        font12.setPointSize(11)
        self.regismem_DOB.setFont(font12)
        self.regismem_DOB.setStyleSheet(u"#regismem_DOB{\n"
"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"color: #fff;\n"
"}\n"
"\n"
"#regismem_DOB::drop-down{\n"
"border: 0px;\n"
"width: 30px;\n"
"}\n"
"\n"
"#regismem_DOB::down-arrow{\n"
"image: url(:/icons/icons/Calendar.png);\n"
"width: 20px;\n"
"height: 20px;\n"
"margin-right: 17px;\n"
"}\n"
"\n"
"#regismem_DOB QWidget{\n"
"background-color: #fff;\n"
"alternate-background-color: #fff;\n"
"color: #003910;\n"
"}\n"
"\n"
"#qt_calendar_calendarview{\n"
"border: 1px solid #D6D6D6;\n"
"min-width: 200px;\n"
"min-height: 170px;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth, #qt_calendar_nextmonth{\n"
"qproperty-icon: none;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth{\n"
"image: url(:/icons/icons/ArrowPrev.png);\n"
"padding: 5px 0 5px 0;\n"
"}\n"
"\n"
"#qt_calendar_nextmonth{\n"
"image: url(:/icons/icons/ArrowNext.png);\n"
"padding: 5px 0 5px 0;\n"
"}\n"
"\n"
"#qt_calendar_monthbutton{\n"
"padding: 0 15px 0 0;\n"
"border-radius: 5px;\n"
"margin: 0 5px;\n"
"font"
                        "-size: 13px;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton{\n"
"padding: 0 30px 0 10px;\n"
"border-radius: 5px;\n"
"font-size: 13px;\n"
"}\n"
"\n"
"#qt_calendar_yearedit{\n"
"font-size: 13px;\n"
"background: transparent;\n"
"color: #fff;\n"
"font-size: 13px;\n"
"min-width: 55px;\n"
"padding: 0 15px;\n"
"}\n"
"\n"
"#qt_calendar_navigationbar{\n"
"border: 1px solid #D6D6D6;\n"
"}\n"
"\n"
"#regismem_DOB QToolButton {\n"
"    background-color: #fff;\n"
"    border: none; \n"
"    margin: 0px;  \n"
"}\n"
"\n"
"#regismem_DOB QToolButton QMenu{\n"
"background-color: #FFFFFF;\n"
"border: 1px solid #D6D6D6;\n"
"}\n"
"\n"
"#regismem_DOB QToolButton QMenu::item{\n"
"padding: 5px;\n"
"min-width: 70px;\n"
"color: #000;\n"
"}\n"
"\n"
"#regismem_DOB QToolButton QMenu::item:selected:enabled{\n"
"background-color: #346F45;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:hover{\n"
"border-radius: 5px;\n"
"background-color: #619270;\n"
"color: #fff;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:selected{\n"
"border-radius: 5px;\n"
"bac"
                        "kground-color: #346F45;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item{\n"
"padding: 3px;\n"
"}")
        self.regismem_DOB.setReadOnly(False)
        self.regismem_DOB.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.regismem_DOB.setCalendarPopup(True)
        self.regismem_lname = QLineEdit(self.register_widget)
        self.regismem_lname.setObjectName(u"regismem_lname")
        self.regismem_lname.setGeometry(QRect(340, 120, 251, 45))
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.regismem_lname.setPalette(palette29)
        self.regismem_lname.setFont(font11)
        self.regismem_lname.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.edit_details_popup = QWidget(self.centralwidget)
        self.edit_details_popup.setObjectName(u"edit_details_popup")
        self.edit_details_popup.setGeometry(QRect(0, 0, 0, 902))
        self.edit_details_popup.setStyleSheet(u"background-color: rgba(0,0,0,160);")
        self.edit_widget = QWidget(self.edit_details_popup)
        self.edit_widget.setObjectName(u"edit_widget")
        self.edit_widget.setEnabled(True)
        self.edit_widget.setGeometry(QRect(260, 150, 851, 611))
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.Button, brush)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush)
        brush8 = QBrush(QColor(0, 57, 16, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette30.setBrush(QPalette.Active, QPalette.HighlightedText, brush8)
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush8)
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush8)
        self.edit_widget.setPalette(palette30)
        self.edit_widget.setStyleSheet(u"#edit_widget{\n"
"background-color: #FFFFFF;\n"
"border-radius:  15px;\n"
"}")
        self.widget_12 = QWidget(self.edit_widget)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(0, 0, 851, 61))
        self.widget_12.setStyleSheet(u"background-color: #346F45;\n"
"border-top-right-radius: 15px;\n"
"border-top-left-radius: 15px;")
        self.label_2 = QLabel(self.widget_12)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, -1, 851, 61))
        self.label_2.setFont(font10)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"#label_2{\n"
"color: #FFFFFF;\n"
"font-family: \"Jaldi\", sans-serif;\n"
"background: none;\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.mem_fname = QLineEdit(self.edit_widget)
        self.mem_fname.setObjectName(u"mem_fname")
        self.mem_fname.setGeometry(QRect(60, 120, 251, 45))
        palette31 = QPalette()
        palette31.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette31.setBrush(QPalette.Active, QPalette.Text, brush)
        palette31.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette31.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette31.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette31.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette31.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette31.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette31.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette31.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette31.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.mem_fname.setPalette(palette31)
        self.mem_fname.setFont(font11)
        self.mem_fname.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.mem_contact = QLineEdit(self.edit_widget)
        self.mem_contact.setObjectName(u"mem_contact")
        self.mem_contact.setGeometry(QRect(60, 200, 291, 45))
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette32.setBrush(QPalette.Active, QPalette.Text, brush)
        palette32.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette32.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette32.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette32.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette32.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette32.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette32.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette32.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette32.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.mem_contact.setPalette(palette32)
        self.mem_contact.setFont(font11)
        self.mem_contact.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.mem_address = QLineEdit(self.edit_widget)
        self.mem_address.setObjectName(u"mem_address")
        self.mem_address.setGeometry(QRect(380, 200, 401, 45))
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette33.setBrush(QPalette.Active, QPalette.Text, brush)
        palette33.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette33.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette33.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette33.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette33.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette33.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette33.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette33.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette33.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.mem_address.setPalette(palette33)
        self.mem_address.setFont(font11)
        self.mem_address.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.mem_medic_ailments = QLineEdit(self.edit_widget)
        self.mem_medic_ailments.setObjectName(u"mem_medic_ailments")
        self.mem_medic_ailments.setGeometry(QRect(60, 280, 391, 45))
        palette34 = QPalette()
        palette34.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette34.setBrush(QPalette.Active, QPalette.Text, brush)
        palette34.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette34.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette34.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette34.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette34.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette34.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette34.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette34.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette34.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.mem_medic_ailments.setPalette(palette34)
        self.mem_medic_ailments.setFont(font11)
        self.mem_medic_ailments.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.mem_prevGym = QLineEdit(self.edit_widget)
        self.mem_prevGym.setObjectName(u"mem_prevGym")
        self.mem_prevGym.setGeometry(QRect(60, 370, 411, 45))
        palette35 = QPalette()
        palette35.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette35.setBrush(QPalette.Active, QPalette.Text, brush)
        palette35.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette35.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette35.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette35.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette35.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette35.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette35.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette35.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette35.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.mem_prevGym.setPalette(palette35)
        self.mem_prevGym.setFont(font11)
        self.mem_prevGym.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.mem_BP = QLineEdit(self.edit_widget)
        self.mem_BP.setObjectName(u"mem_BP")
        self.mem_BP.setGeometry(QRect(500, 370, 101, 45))
        palette36 = QPalette()
        palette36.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette36.setBrush(QPalette.Active, QPalette.Text, brush)
        palette36.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette36.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette36.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette36.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette36.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette36.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette36.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette36.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette36.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette36.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.mem_BP.setPalette(palette36)
        self.mem_BP.setFont(font11)
        self.mem_BP.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.mem_physicalAct = QLineEdit(self.edit_widget)
        self.mem_physicalAct.setObjectName(u"mem_physicalAct")
        self.mem_physicalAct.setGeometry(QRect(60, 450, 321, 45))
        palette37 = QPalette()
        palette37.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette37.setBrush(QPalette.Active, QPalette.Text, brush)
        palette37.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette37.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette37.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette37.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette37.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette37.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette37.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette37.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette37.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.mem_physicalAct.setPalette(palette37)
        self.mem_physicalAct.setFont(font11)
        self.mem_physicalAct.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.mem_weight = QLineEdit(self.edit_widget)
        self.mem_weight.setObjectName(u"mem_weight")
        self.mem_weight.setGeometry(QRect(405, 450, 101, 45))
        palette38 = QPalette()
        palette38.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette38.setBrush(QPalette.Active, QPalette.Text, brush)
        palette38.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette38.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette38.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette38.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette38.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette38.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette38.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette38.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette38.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.mem_weight.setPalette(palette38)
        self.mem_weight.setFont(font11)
        self.mem_weight.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.mem_height = QLineEdit(self.edit_widget)
        self.mem_height.setObjectName(u"mem_height")
        self.mem_height.setGeometry(QRect(530, 450, 101, 45))
        palette39 = QPalette()
        palette39.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette39.setBrush(QPalette.Active, QPalette.Text, brush)
        palette39.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette39.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette39.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette39.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette39.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette39.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette39.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette39.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette39.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.mem_height.setPalette(palette39)
        self.mem_height.setFont(font11)
        self.mem_height.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.mem_cancelbtn = QPushButton(self.edit_widget)
        self.mem_cancelbtn.setObjectName(u"mem_cancelbtn")
        self.mem_cancelbtn.setGeometry(QRect(550, 534, 101, 41))
        self.mem_cancelbtn.setFont(font3)
        self.mem_cancelbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.mem_cancelbtn.setStyleSheet(u"background-color: #AE2626;\n"
"border-radius: 20px;")
        self.mem_savebtn = QPushButton(self.edit_widget)
        self.mem_savebtn.setObjectName(u"mem_savebtn")
        self.mem_savebtn.setGeometry(QRect(680, 534, 101, 41))
        self.mem_savebtn.setFont(font3)
        self.mem_savebtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.mem_savebtn.setStyleSheet(u"background-color: #167432;\n"
"border-radius: 20px;")
        self.memStud_radiobtn = QRadioButton(self.edit_widget)
        self.memStud_radiobtn.setObjectName(u"memStud_radiobtn")
        self.memStud_radiobtn.setGeometry(QRect(500, 280, 111, 41))
        sizePolicy.setHeightForWidth(self.memStud_radiobtn.sizePolicy().hasHeightForWidth())
        self.memStud_radiobtn.setSizePolicy(sizePolicy)
        palette40 = QPalette()
        palette40.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette40.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette40.setBrush(QPalette.Active, QPalette.Midlight, brush8)
        palette40.setBrush(QPalette.Active, QPalette.Dark, brush8)
        palette40.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette40.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette40.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette40.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette40.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette40.setBrush(QPalette.Active, QPalette.Shadow, brush8)
        palette40.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette40.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
        palette40.setBrush(QPalette.Active, QPalette.Link, brush8)
        palette40.setBrush(QPalette.Active, QPalette.LinkVisited, brush8)
        palette40.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette40.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette40.setBrush(QPalette.Active, QPalette.ToolTipText, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette40.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette40.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette40.setBrush(QPalette.Inactive, QPalette.Midlight, brush8)
        palette40.setBrush(QPalette.Inactive, QPalette.Dark, brush8)
        palette40.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette40.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette40.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette40.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette40.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette40.setBrush(QPalette.Inactive, QPalette.Shadow, brush8)
        palette40.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette40.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush8)
        palette40.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette40.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette40.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette40.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette40.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette40.setBrush(QPalette.Disabled, QPalette.Midlight, brush8)
        palette40.setBrush(QPalette.Disabled, QPalette.Dark, brush8)
        palette40.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette40.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette40.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette40.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette40.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette40.setBrush(QPalette.Disabled, QPalette.Shadow, brush8)
        brush9 = QBrush(QColor(0, 120, 215, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette40.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette40.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush)
        palette40.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette40.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush8)
        palette40.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette40.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette40.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.memStud_radiobtn.setPalette(palette40)
        self.memStud_radiobtn.setFont(font11)
        self.memStud_radiobtn.setStyleSheet(u"background: none;\n"
"color: #585050;")
        self.memStud_radiobtn.setIconSize(QSize(20, 20))
        self.memProf_radiobtn = QRadioButton(self.edit_widget)
        self.memProf_radiobtn.setObjectName(u"memProf_radiobtn")
        self.memProf_radiobtn.setGeometry(QRect(640, 280, 111, 41))
        palette41 = QPalette()
        palette41.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette41.setBrush(QPalette.Active, QPalette.Dark, brush8)
        palette41.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette41.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette41.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette41.setBrush(QPalette.Active, QPalette.Base, brush)
        palette41.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette41.setBrush(QPalette.Active, QPalette.Shadow, brush8)
        palette41.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette41.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
        palette41.setBrush(QPalette.Active, QPalette.Link, brush8)
        palette41.setBrush(QPalette.Active, QPalette.LinkVisited, brush8)
        palette41.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette41.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette41.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette41.setBrush(QPalette.Inactive, QPalette.Dark, brush8)
        palette41.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette41.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette41.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette41.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette41.setBrush(QPalette.Inactive, QPalette.Shadow, brush8)
        palette41.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette41.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush8)
        palette41.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette41.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette41.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette41.setBrush(QPalette.Disabled, QPalette.Dark, brush8)
        palette41.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette41.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette41.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette41.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette41.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette41.setBrush(QPalette.Disabled, QPalette.Shadow, brush8)
        palette41.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette41.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush)
        palette41.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette41.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush8)
        palette41.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette41.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.memProf_radiobtn.setPalette(palette41)
        self.memProf_radiobtn.setFont(font11)
        self.memProf_radiobtn.setStyleSheet(u"background: none;\n"
"color: #585050;")
        self.memProf_radiobtn.setIconSize(QSize(20, 20))
        self.memStat_comboBox = QComboBox(self.edit_widget)
        self.memStat_comboBox.addItem("")
        self.memStat_comboBox.addItem("")
        self.memStat_comboBox.addItem("")
        self.memStat_comboBox.setObjectName(u"memStat_comboBox")
        self.memStat_comboBox.setGeometry(QRect(630, 370, 141, 45))
        palette42 = QPalette()
        palette42.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette42.setBrush(QPalette.Active, QPalette.Text, brush)
        palette42.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette42.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette42.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette42.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette42.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette42.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette42.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette42.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette42.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.memStat_comboBox.setPalette(palette42)
        self.memStat_comboBox.setFont(font11)
        self.memStat_comboBox.setStyleSheet(u"#memStat_comboBox{\n"
"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"color: #FFFFF;\n"
"}\n"
"\n"
"#memStat_comboBox::drop-down{\n"
"border: 0px;\n"
"width: 30px;\n"
"}\n"
"\n"
"#memStat_comboBox::down-arrow{\n"
"image: url(:/icons/icons/Drop Down.png);\n"
"width: 20px;\n"
"height: 20px;\n"
"margin-right: 17px;\n"
"}\n"
"\n"
"#memStat_comboBox QListView{\n"
"font-size: 11px;\n"
"padding: 5px;\n"
"border: 1px solid rgba(0,0,0,10%);\n"
"background-color: #fff;\n"
"color: #346F45;\n"
"outline: 0px;\n"
"}\n"
"\n"
"\n"
"#memStat_comboBox QListView:item{\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"#memStat_comboBox QListView:item:hover{\n"
"background-color: #619270;\n"
"color: #fff;\n"
"}\n"
"\n"
"")
        self.memStat_comboBox.setEditable(True)
        self.memGender_comboBox = QComboBox(self.edit_widget)
        self.memGender_comboBox.addItem("")
        self.memGender_comboBox.addItem("")
        self.memGender_comboBox.addItem("")
        self.memGender_comboBox.setObjectName(u"memGender_comboBox")
        self.memGender_comboBox.setGeometry(QRect(650, 450, 121, 45))
        palette43 = QPalette()
        palette43.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette43.setBrush(QPalette.Active, QPalette.Text, brush)
        palette43.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette43.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette43.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette43.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette43.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette43.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette43.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette43.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette43.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.memGender_comboBox.setPalette(palette43)
        self.memGender_comboBox.setFont(font11)
        self.memGender_comboBox.setStyleSheet(u"#memGender_comboBox{\n"
"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"color: #FFFFF;\n"
"}\n"
"\n"
"#memGender_comboBox::drop-down{\n"
"border: 0px;\n"
"width: 30px;\n"
"}\n"
"\n"
"#memGender_comboBox::down-arrow{\n"
"image: url(:/icons/icons/Drop Down.png);\n"
"width: 20px;\n"
"height: 20px;\n"
"margin-right: 17px;\n"
"}\n"
"\n"
"#memGender_comboBox QListView{\n"
"font-size: 11px;\n"
"padding: 5px;\n"
"border: 1px solid rgba(0,0,0,10%);\n"
"background-color: #fff;\n"
"color: #346F45;\n"
"outline: 0px;\n"
"}\n"
"\n"
"\n"
"#memGender_comboBox QListView:item{\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"#memGender_comboBox QListView:item:hover{\n"
"background-color: #619270;\n"
"color: #fff;\n"
"}\n"
"\n"
"")
        self.memGender_comboBox.setEditable(True)
        self.mem_DOB = QDateEdit(self.edit_widget)
        self.mem_DOB.setObjectName(u"mem_DOB")
        self.mem_DOB.setGeometry(QRect(620, 120, 161, 45))
        palette44 = QPalette()
        palette44.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette44.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette44.setBrush(QPalette.Active, QPalette.Text, brush)
        palette44.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette44.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette44.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette44.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette44.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette44.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette44.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette44.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette44.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.mem_DOB.setPalette(palette44)
        self.mem_DOB.setFont(font12)
        self.mem_DOB.setStyleSheet(u"#mem_DOB{\n"
"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"color: #fff;\n"
"}\n"
"\n"
"#mem_DOB::drop-down{\n"
"border: 0px;\n"
"width: 30px;\n"
"}\n"
"\n"
"#mem_DOB::down-arrow{\n"
"image: url(:/icons/icons/Calendar.png);\n"
"width: 20px;\n"
"height: 20px;\n"
"margin-right: 17px;\n"
"}\n"
"\n"
"#mem_DOB QWidget{\n"
"background-color: #fff;\n"
"alternate-background-color: #fff;\n"
"color: #003910;\n"
"}\n"
"\n"
"#qt_calendar_calendarview{\n"
"border: 1px solid #D6D6D6;\n"
"min-width: 200px;\n"
"min-height: 170px;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth, #qt_calendar_nextmonth{\n"
"qproperty-icon: none;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth{\n"
"image: url(:/icons/icons/ArrowPrev.png);\n"
"padding: 5px 0 5px 0;\n"
"}\n"
"\n"
"#qt_calendar_nextmonth{\n"
"image: url(:/icons/icons/ArrowNext.png);\n"
"padding: 5px 0 5px 0;\n"
"}\n"
"\n"
"#qt_calendar_monthbutton{\n"
"padding: 0 15px 0 0;\n"
"border-radius: 5px;\n"
"margin: 0 5px;\n"
"font-size: 13px;\n"
"}\n"
""
                        "\n"
"#qt_calendar_yearbutton{\n"
"padding: 0 30px 0 10px;\n"
"border-radius: 5px;\n"
"font-size: 13px;\n"
"}\n"
"\n"
"#qt_calendar_yearedit{\n"
"font-size: 13px;\n"
"background: transparent;\n"
"color: #fff;\n"
"font-size: 13px;\n"
"min-width: 55px;\n"
"padding: 0 15px;\n"
"}\n"
"\n"
"#qt_calendar_navigationbar{\n"
"border: 1px solid #D6D6D6;\n"
"}\n"
"\n"
"#mem_DOB QToolButton {\n"
"    background-color: #fff;\n"
"    border: none; \n"
"    margin: 0px;  \n"
"}\n"
"\n"
"#mem_DOB QToolButton QMenu{\n"
"background-color: #FFFFFF;\n"
"border: 1px solid #D6D6D6;\n"
"}\n"
"\n"
"#mem_DOB QToolButton QMenu::item{\n"
"padding: 5px;\n"
"min-width: 70px;\n"
"color: #000;\n"
"}\n"
"\n"
"#mem_DOB QToolButton QMenu::item:selected:enabled{\n"
"background-color: #346F45;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:hover{\n"
"border-radius: 5px;\n"
"background-color: #619270;\n"
"color: #fff;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:selected{\n"
"border-radius: 5px;\n"
"background-color: #346F45;\n"
"}\n"
"\n"
"#qt_"
                        "calendar_calendarview::item{\n"
"padding: 3px;\n"
"}")
        self.mem_DOB.setReadOnly(False)
        self.mem_DOB.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.mem_DOB.setCalendarPopup(True)
        self.mem_lname = QLineEdit(self.edit_widget)
        self.mem_lname.setObjectName(u"mem_lname")
        self.mem_lname.setGeometry(QRect(340, 120, 251, 45))
        palette45 = QPalette()
        palette45.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette45.setBrush(QPalette.Active, QPalette.Text, brush)
        palette45.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette45.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette45.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette45.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette45.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette45.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette45.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette45.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette45.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.mem_lname.setPalette(palette45)
        self.mem_lname.setFont(font11)
        self.mem_lname.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.payment_popup = QWidget(self.centralwidget)
        self.payment_popup.setObjectName(u"payment_popup")
        self.payment_popup.setGeometry(QRect(0, 0, 0, 902))
        self.payment_popup.setStyleSheet(u"background-color: rgba(0,0,0,160);")
        self.payment_widget = QWidget(self.payment_popup)
        self.payment_widget.setObjectName(u"payment_widget")
        self.payment_widget.setEnabled(True)
        self.payment_widget.setGeometry(QRect(300, 150, 751, 571))
        palette46 = QPalette()
        palette46.setBrush(QPalette.Active, QPalette.Button, brush)
        palette46.setBrush(QPalette.Active, QPalette.Base, brush)
        palette46.setBrush(QPalette.Active, QPalette.Window, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.payment_widget.setPalette(palette46)
        self.payment_widget.setStyleSheet(u"#payment_widget{\n"
"background-color: #FFFFFF;\n"
"border-radius:  15px;\n"
"}")
        self.widget_14 = QWidget(self.payment_widget)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setGeometry(QRect(0, 0, 751, 61))
        self.widget_14.setStyleSheet(u"background-color: #346F45;\n"
"border-top-right-radius: 15px;\n"
"border-top-left-radius: 15px;")
        self.label_11 = QLabel(self.widget_14)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, -1, 751, 61))
        self.label_11.setFont(font10)
        self.label_11.setStyleSheet(u"#label_11{\n"
"color: #FFFFFF;\n"
"font-family: \"Jaldi\", sans-serif;\n"
"background: none;\n"
"}")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.payment_amt = QLineEdit(self.payment_widget)
        self.payment_amt.setObjectName(u"payment_amt")
        self.payment_amt.setGeometry(QRect(190, 240, 351, 45))
        palette47 = QPalette()
        palette47.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette47.setBrush(QPalette.Active, QPalette.Text, brush)
        palette47.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette47.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette47.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette47.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette47.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette47.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette47.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette47.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette47.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.payment_amt.setPalette(palette47)
        self.payment_amt.setFont(font11)
        self.payment_amt.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.payment_amt.setReadOnly(True)
        self.payment_tenderedAmt = QLineEdit(self.payment_widget)
        self.payment_tenderedAmt.setObjectName(u"payment_tenderedAmt")
        self.payment_tenderedAmt.setGeometry(QRect(190, 380, 351, 45))
        palette48 = QPalette()
        palette48.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette48.setBrush(QPalette.Active, QPalette.Text, brush)
        palette48.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette48.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette48.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette48.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette48.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette48.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette48.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette48.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette48.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette48.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.payment_tenderedAmt.setPalette(palette48)
        self.payment_tenderedAmt.setFont(font11)
        self.payment_tenderedAmt.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.pay_cancelbtn = QPushButton(self.payment_widget)
        self.pay_cancelbtn.setObjectName(u"pay_cancelbtn")
        self.pay_cancelbtn.setGeometry(QRect(440, 470, 101, 41))
        self.pay_cancelbtn.setFont(font3)
        self.pay_cancelbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pay_cancelbtn.setStyleSheet(u"background-color: #AE2626;\n"
"border-radius: 20px;")
        self.pay_btn = QPushButton(self.payment_widget)
        self.pay_btn.setObjectName(u"pay_btn")
        self.pay_btn.setGeometry(QRect(570, 470, 101, 41))
        self.pay_btn.setFont(font3)
        self.pay_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pay_btn.setStyleSheet(u"background-color: #167432;\n"
"border-radius: 20px;")
        self.paymentServices_cmbBox = QComboBox(self.payment_widget)
        self.paymentServices_cmbBox.addItem("")
        self.paymentServices_cmbBox.setObjectName(u"paymentServices_cmbBox")
        self.paymentServices_cmbBox.setGeometry(QRect(190, 170, 351, 45))
        palette49 = QPalette()
        palette49.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette49.setBrush(QPalette.Active, QPalette.Text, brush)
        palette49.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette49.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette49.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette49.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette49.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette49.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette49.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette49.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette49.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette49.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.paymentServices_cmbBox.setPalette(palette49)
        self.paymentServices_cmbBox.setFont(font11)
        self.paymentServices_cmbBox.setStyleSheet(u"#paymentServices_cmbBox{\n"
"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"color: #FFFFF;\n"
"}\n"
"\n"
"#paymentServices_cmbBox::drop-down{\n"
"border: 0px;\n"
"width: 30px;\n"
"}\n"
"\n"
"#paymentServices_cmbBox::down-arrow{\n"
"image: url(:/icons/icons/Drop Down.png);\n"
"width: 20px;\n"
"height: 20px;\n"
"margin-right: 17px;\n"
"}\n"
"\n"
"#paymentServices_cmbBox QListView{\n"
"font-size: 11px;\n"
"padding: 5px;\n"
"border: 1px solid rgba(0,0,0,10%);\n"
"background-color: #fff;\n"
"color: #346F45;\n"
"outline: 0px;\n"
"}\n"
"\n"
"\n"
"#paymentServices_cmbBox QListView:item{\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"#paymentServices_cmbBox QListView:item:hover{\n"
"background-color: #619270;\n"
"color: #fff;\n"
"}\n"
"\n"
"")
        self.paymentServices_cmbBox.setEditable(True)
        self.payment_instructor = QComboBox(self.payment_widget)
        self.payment_instructor.addItem("")
        self.payment_instructor.addItem("")
        self.payment_instructor.setObjectName(u"payment_instructor")
        self.payment_instructor.setGeometry(QRect(190, 100, 351, 45))
        palette50 = QPalette()
        palette50.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette50.setBrush(QPalette.Active, QPalette.Text, brush)
        palette50.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette50.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette50.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette50.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette50.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette50.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette50.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette50.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette50.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.payment_instructor.setPalette(palette50)
        self.payment_instructor.setFont(font11)
        self.payment_instructor.setStyleSheet(u"#payment_instructor{\n"
"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"color: #FFFFF;\n"
"}\n"
"\n"
"#payment_instructor::drop-down{\n"
"border: 0px;\n"
"width: 30px;\n"
"}\n"
"\n"
"#payment_instructor::down-arrow{\n"
"image: url(:/icons/icons/Drop Down.png);\n"
"width: 20px;\n"
"height: 20px;\n"
"margin-right: 17px;\n"
"}\n"
"\n"
"#payment_instructor QListView{\n"
"font-size: 11px;\n"
"padding: 5px;\n"
"border: 1px solid rgba(0,0,0,10%);\n"
"background-color: #fff;\n"
"color: #346F45;\n"
"outline: 0px;\n"
"}\n"
"\n"
"\n"
"#payment_instructor QListView:item{\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"#payment_instructor QListView:item:hover{\n"
"background-color: #619270;\n"
"color: #fff;\n"
"}\n"
"\n"
"")
        self.payment_instructor.setEditable(True)
        self.payment_memFee = QLineEdit(self.payment_widget)
        self.payment_memFee.setObjectName(u"payment_memFee")
        self.payment_memFee.setGeometry(QRect(190, 310, 351, 45))
        palette51 = QPalette()
        palette51.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette51.setBrush(QPalette.Active, QPalette.Text, brush)
        palette51.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette51.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette51.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette51.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette51.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette51.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette51.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette51.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette51.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.payment_memFee.setPalette(palette51)
        self.payment_memFee.setFont(font11)
        self.payment_memFee.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.member_delete_popup = QWidget(self.centralwidget)
        self.member_delete_popup.setObjectName(u"member_delete_popup")
        self.member_delete_popup.setGeometry(QRect(0, 0, 0, 902))
        self.member_delete_popup.setStyleSheet(u"background-color: rgba(0,0,0,160);")
        self.confirm_memdel_widget = QWidget(self.member_delete_popup)
        self.confirm_memdel_widget.setObjectName(u"confirm_memdel_widget")
        self.confirm_memdel_widget.setEnabled(True)
        self.confirm_memdel_widget.setGeometry(QRect(330, 350, 721, 231))
        palette52 = QPalette()
        palette52.setBrush(QPalette.Active, QPalette.Button, brush)
        palette52.setBrush(QPalette.Active, QPalette.Base, brush)
        palette52.setBrush(QPalette.Active, QPalette.Window, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.confirm_memdel_widget.setPalette(palette52)
        self.confirm_memdel_widget.setStyleSheet(u"#confirm_memdel_widget{\n"
"background-color: #FFFFFF;\n"
"border-radius:  15px;\n"
"}")
        self.cancelDelete_mem = QPushButton(self.confirm_memdel_widget)
        self.cancelDelete_mem.setObjectName(u"cancelDelete_mem")
        self.cancelDelete_mem.setGeometry(QRect(570, 160, 101, 41))
        self.cancelDelete_mem.setFont(font3)
        self.cancelDelete_mem.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelDelete_mem.setStyleSheet(u"background-color: #AE2626;\n"
"border-radius: 20px;")
        self.confDelete_mem = QPushButton(self.confirm_memdel_widget)
        self.confDelete_mem.setObjectName(u"confDelete_mem")
        self.confDelete_mem.setGeometry(QRect(440, 160, 101, 41))
        self.confDelete_mem.setFont(font3)
        self.confDelete_mem.setCursor(QCursor(Qt.PointingHandCursor))
        self.confDelete_mem.setStyleSheet(u"background-color: #167432;\n"
"border-radius: 20px;")
        self.label_12 = QLabel(self.confirm_memdel_widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 0, 721, 71))
        self.label_12.setFont(font10)
        self.label_12.setStyleSheet(u"color: #AE2626;\n"
"font-family: \"Jaldi\", sans-serif;\n"
"background: none;\n"
"")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.confirm_memdel_widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(80, 50, 561, 91))
        font13 = QFont()
        font13.setFamily(u"Segoe UI")
        font13.setPointSize(13)
        font13.setBold(True)
        font13.setLegacyWeight(75)
        self.label_13.setFont(font13)
        self.label_13.setStyleSheet(u"background: none;\n"
"color: #222020;")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setWordWrap(True)
        self.renew_popup = QWidget(self.centralwidget)
        self.renew_popup.setObjectName(u"renew_popup")
        self.renew_popup.setGeometry(QRect(0, 0, 0, 902))
        self.renew_popup.setStyleSheet(u"background-color: rgba(0,0,0,160);")
        self.renew_widget = QWidget(self.renew_popup)
        self.renew_widget.setObjectName(u"renew_widget")
        self.renew_widget.setEnabled(True)
        self.renew_widget.setGeometry(QRect(300, 150, 751, 571))
        palette53 = QPalette()
        palette53.setBrush(QPalette.Active, QPalette.Button, brush)
        palette53.setBrush(QPalette.Active, QPalette.Base, brush)
        palette53.setBrush(QPalette.Active, QPalette.Window, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.renew_widget.setPalette(palette53)
        self.renew_widget.setStyleSheet(u"#renew_widget{\n"
"background-color: #FFFFFF;\n"
"border-radius:  15px;\n"
"}")
        self.widget_33 = QWidget(self.renew_widget)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setGeometry(QRect(0, 0, 751, 61))
        self.widget_33.setStyleSheet(u"background-color: #346F45;\n"
"border-top-right-radius: 15px;\n"
"border-top-left-radius: 15px;")
        self.label_7 = QLabel(self.widget_33)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, -1, 751, 61))
        self.label_7.setFont(font10)
        self.label_7.setStyleSheet(u"#label_7{\n"
"color: #FFFFFF;\n"
"font-family: \"Jaldi\", sans-serif;\n"
"background: none;\n"
"}")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.renew_amt = QLineEdit(self.renew_widget)
        self.renew_amt.setObjectName(u"renew_amt")
        self.renew_amt.setGeometry(QRect(190, 270, 351, 45))
        palette54 = QPalette()
        palette54.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette54.setBrush(QPalette.Active, QPalette.Text, brush)
        palette54.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette54.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette54.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette54.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette54.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette54.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette54.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette54.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette54.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.renew_amt.setPalette(palette54)
        self.renew_amt.setFont(font11)
        self.renew_amt.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.renew_amt.setReadOnly(True)
        self.renew_tenderedAmt = QLineEdit(self.renew_widget)
        self.renew_tenderedAmt.setObjectName(u"renew_tenderedAmt")
        self.renew_tenderedAmt.setGeometry(QRect(190, 350, 351, 45))
        palette55 = QPalette()
        palette55.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette55.setBrush(QPalette.Active, QPalette.Text, brush)
        palette55.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette55.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette55.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette55.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette55.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette55.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette55.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette55.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette55.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.renew_tenderedAmt.setPalette(palette55)
        self.renew_tenderedAmt.setFont(font11)
        self.renew_tenderedAmt.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.renewCancel_btn = QPushButton(self.renew_widget)
        self.renewCancel_btn.setObjectName(u"renewCancel_btn")
        self.renewCancel_btn.setGeometry(QRect(440, 470, 101, 41))
        self.renewCancel_btn.setFont(font3)
        self.renewCancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.renewCancel_btn.setStyleSheet(u"background-color: #AE2626;\n"
"border-radius: 20px;")
        self.renewPay_btn = QPushButton(self.renew_widget)
        self.renewPay_btn.setObjectName(u"renewPay_btn")
        self.renewPay_btn.setGeometry(QRect(570, 470, 101, 41))
        self.renewPay_btn.setFont(font3)
        self.renewPay_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.renewPay_btn.setStyleSheet(u"background-color: #167432;\n"
"border-radius: 20px;")
        self.renewService_comboBox = QComboBox(self.renew_widget)
        self.renewService_comboBox.addItem("")
        self.renewService_comboBox.setObjectName(u"renewService_comboBox")
        self.renewService_comboBox.setGeometry(QRect(190, 190, 351, 45))
        palette56 = QPalette()
        palette56.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette56.setBrush(QPalette.Active, QPalette.Text, brush)
        palette56.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette56.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette56.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette56.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette56.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette56.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette56.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette56.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette56.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette56.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette56.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette56.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette56.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.renewService_comboBox.setPalette(palette56)
        self.renewService_comboBox.setFont(font11)
        self.renewService_comboBox.setStyleSheet(u"#renewService_comboBox{\n"
"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"color: #FFFFF;\n"
"}\n"
"\n"
"#renewService_comboBox::drop-down{\n"
"border: 0px;\n"
"width: 30px;\n"
"}\n"
"\n"
"#renewService_comboBox::down-arrow{\n"
"image: url(:/icons/icons/Drop Down.png);\n"
"width: 20px;\n"
"height: 20px;\n"
"margin-right: 17px;\n"
"}\n"
"\n"
"#renewService_comboBox QListView{\n"
"font-size: 11px;\n"
"padding: 5px;\n"
"border: 1px solid rgba(0,0,0,10%);\n"
"background-color: #fff;\n"
"color: #346F45;\n"
"outline: 0px;\n"
"}\n"
"\n"
"\n"
"#renewService_comboBox QListView:item{\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"#renewService_comboBox QListView:item:hover{\n"
"background-color: #619270;\n"
"color: #fff;\n"
"}\n"
"\n"
"\n"
"")
        self.renewService_comboBox.setEditable(True)
        self.renew_instructor = QComboBox(self.renew_widget)
        self.renew_instructor.addItem("")
        self.renew_instructor.addItem("")
        self.renew_instructor.setObjectName(u"renew_instructor")
        self.renew_instructor.setGeometry(QRect(190, 110, 351, 45))
        palette57 = QPalette()
        palette57.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette57.setBrush(QPalette.Active, QPalette.Text, brush)
        palette57.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette57.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette57.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette57.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette57.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette57.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette57.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette57.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette57.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette57.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette57.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette57.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette57.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.renew_instructor.setPalette(palette57)
        self.renew_instructor.setFont(font11)
        self.renew_instructor.setStyleSheet(u"#renew_instructor{\n"
"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"color: #FFFFF;\n"
"}\n"
"\n"
"#renew_instructor::drop-down{\n"
"border: 0px;\n"
"width: 30px;\n"
"}\n"
"\n"
"#renew_instructor::down-arrow{\n"
"image: url(:/icons/icons/Drop Down.png);\n"
"width: 20px;\n"
"height: 20px;\n"
"margin-right: 17px;\n"
"}\n"
"\n"
"#renew_instructor QListView{\n"
"font-size: 11px;\n"
"padding: 5px;\n"
"border: 1px solid rgba(0,0,0,10%);\n"
"background-color: #fff;\n"
"color: #346F45;\n"
"outline: 0px;\n"
"}\n"
"\n"
"\n"
"#renew_instructor QListView:item{\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"#renew_instructor QListView:item:hover{\n"
"background-color: #619270;\n"
"color: #fff;\n"
"}\n"
"\n"
"")
        self.renew_instructor.setEditable(True)
        self.services_popup = QWidget(self.centralwidget)
        self.services_popup.setObjectName(u"services_popup")
        self.services_popup.setGeometry(QRect(0, 0, 0, 902))
        self.services_popup.setStyleSheet(u"background-color: rgba(0,0,0,160);")
        self.services_widget = QWidget(self.services_popup)
        self.services_widget.setObjectName(u"services_widget")
        self.services_widget.setGeometry(QRect(340, 150, 701, 611))
        self.services_widget.setStyleSheet(u"#services_widget{\n"
"background-color: #FFFFFF;\n"
"border-radius:  15px;\n"
"\n"
"}")
        self.widget_10 = QWidget(self.services_widget)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(0, 70, 851, 15))
        self.widget_10.setStyleSheet(u"background-color: #346F45;")
        self.addService_btn = QPushButton(self.services_widget)
        self.addService_btn.setObjectName(u"addService_btn")
        self.addService_btn.setGeometry(QRect(30, 25, 41, 31))
        self.addService_btn.setFont(font3)
        self.addService_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addService_btn.setStyleSheet(u"background: none;\n"
"")
        self.addService_btn.setIcon(icon5)
        self.addService_btn.setIconSize(QSize(35, 35))
        self.label_4 = QLabel(self.services_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 30, 341, 20))
        font14 = QFont()
        font14.setFamily(u"Yu Gothic")
        font14.setPointSize(15)
        font14.setBold(True)
        font14.setLegacyWeight(75)
        self.label_4.setFont(font14)
        self.label_4.setStyleSheet(u"color: #003C11;\n"
"background: none;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.deleteService_btn = QPushButton(self.services_widget)
        self.deleteService_btn.setObjectName(u"deleteService_btn")
        self.deleteService_btn.setGeometry(QRect(110, 23, 41, 31))
        self.deleteService_btn.setFont(font3)
        self.deleteService_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteService_btn.setStyleSheet(u"background: none;\n"
"")
        self.deleteService_btn.setIcon(icon3)
        self.deleteService_btn.setIconSize(QSize(32, 32))
        self.editService_btn = QPushButton(self.services_widget)
        self.editService_btn.setObjectName(u"editService_btn")
        self.editService_btn.setGeometry(QRect(70, 24, 41, 31))
        self.editService_btn.setFont(font3)
        self.editService_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editService_btn.setStyleSheet(u"background: none;\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/editblack.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editService_btn.setIcon(icon7)
        self.editService_btn.setIconSize(QSize(32, 32))
        self.services_table = QTableWidget(self.services_widget)
        if (self.services_table.columnCount() < 3):
            self.services_table.setColumnCount(3)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font6);
        self.services_table.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font6);
        self.services_table.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font6);
        self.services_table.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        self.services_table.setObjectName(u"services_table")
        self.services_table.setGeometry(QRect(0, 83, 701, 511))
        palette58 = QPalette()
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette58.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette58.setBrush(QPalette.Active, QPalette.Button, brush)
        palette58.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette58.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette58.setBrush(QPalette.Active, QPalette.Base, brush)
        palette58.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette58.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette58.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette58.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette58.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette58.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette58.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette58.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette58.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette58.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette58.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette58.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette58.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette58.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette58.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette58.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.services_table.setPalette(palette58)
        font15 = QFont()
        font15.setFamily(u"Segoe UI")
        font15.setPointSize(10)
        self.services_table.setFont(font15)
        self.services_table.setStyleSheet(u"QTableWidget {\n"
"    background-color: #fff;\n"
"    color: #000;\n"
"    gridline-color: transparent; \n"
"	border-spacing: 0 1px;\n"
"	border: none;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #fff;\n"
"   	color: #000;\n"
"	padding: 3px;\n"
"	border: none; 	\n"
"	border-bottom: 1px solid #ddd;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: #ffffff;\n"
"    color: #003910;\n"
"    border-bottom: 1px solid #ddd;\n"
"	padding: 3px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #c4e3f3;\n"
"    color: #003910;\n"
"    gridline-color: #c4e3f3; \n"
"}")
        self.services_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.services_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.services_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.services_table.setTextElideMode(Qt.ElideMiddle)
        self.services_table.setShowGrid(True)
        self.services_table.setGridStyle(Qt.SolidLine)
        self.services_table.setSortingEnabled(True)
        self.services_table.horizontalHeader().setHighlightSections(False)
        self.services_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.services_table.verticalHeader().setHighlightSections(False)
        self.services_table.verticalHeader().setProperty("showSortIndicator", False)
        self.services_exitbtn = QPushButton(self.services_widget)
        self.services_exitbtn.setObjectName(u"services_exitbtn")
        self.services_exitbtn.setGeometry(QRect(660, 10, 31, 31))
        self.services_exitbtn.setFont(font3)
        self.services_exitbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.services_exitbtn.setStyleSheet(u"background: none;\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/loginRES/icons/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.services_exitbtn.setIcon(icon8)
        self.services_exitbtn.setIconSize(QSize(25, 25))
        self.add_service_widget = QWidget(self.services_popup)
        self.add_service_widget.setObjectName(u"add_service_widget")
        self.add_service_widget.setGeometry(QRect(370, 250, 0, 361))
        self.add_service_widget.setStyleSheet(u"#add_service_widget{\n"
"background-color: #FFFFFF;\n"
"border-radius:  15px;\n"
"\n"
"}")
        self.widget_13 = QWidget(self.add_service_widget)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(0, 70, 701, 16))
        self.widget_13.setStyleSheet(u"background-color: #346F45;")
        self.label_14 = QLabel(self.add_service_widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 30, 701, 20))
        self.label_14.setFont(font14)
        self.label_14.setStyleSheet(u"color: #003C11;\n"
"background: none;")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.addService_name = QLineEdit(self.add_service_widget)
        self.addService_name.setObjectName(u"addService_name")
        self.addService_name.setGeometry(QRect(180, 130, 351, 45))
        palette59 = QPalette()
        palette59.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette59.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette59.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette59.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette59.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette59.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette59.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette59.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette59.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.addService_name.setPalette(palette59)
        self.addService_name.setFont(font11)
        self.addService_name.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.addService_amount = QLineEdit(self.add_service_widget)
        self.addService_amount.setObjectName(u"addService_amount")
        self.addService_amount.setGeometry(QRect(180, 200, 351, 45))
        palette60 = QPalette()
        palette60.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette60.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette60.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette60.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette60.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette60.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette60.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette60.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette60.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.addService_amount.setPalette(palette60)
        self.addService_amount.setFont(font11)
        self.addService_amount.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.addService_savebtn = QPushButton(self.add_service_widget)
        self.addService_savebtn.setObjectName(u"addService_savebtn")
        self.addService_savebtn.setGeometry(QRect(550, 290, 101, 41))
        self.addService_savebtn.setFont(font3)
        self.addService_savebtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addService_savebtn.setStyleSheet(u"background-color: #167432;\n"
"border-radius: 20px;")
        self.addService_cancelbtn = QPushButton(self.add_service_widget)
        self.addService_cancelbtn.setObjectName(u"addService_cancelbtn")
        self.addService_cancelbtn.setGeometry(QRect(430, 290, 101, 41))
        self.addService_cancelbtn.setFont(font3)
        self.addService_cancelbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addService_cancelbtn.setStyleSheet(u"background-color: #AE2626;\n"
"border-radius: 20px;")
        self.update_service_widget = QWidget(self.services_popup)
        self.update_service_widget.setObjectName(u"update_service_widget")
        self.update_service_widget.setGeometry(QRect(370, 250, 0, 361))
        self.update_service_widget.setStyleSheet(u"#update_service_widget{\n"
"background-color: #FFFFFF;\n"
"border-radius:  15px;\n"
"\n"
"}")
        self.widget_16 = QWidget(self.update_service_widget)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setGeometry(QRect(0, 70, 701, 16))
        self.widget_16.setStyleSheet(u"background-color: #346F45;")
        self.label_16 = QLabel(self.update_service_widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 30, 701, 20))
        self.label_16.setFont(font14)
        self.label_16.setStyleSheet(u"color: #003C11;\n"
"background: none;")
        self.label_16.setAlignment(Qt.AlignCenter)
        self.service_Update = QLineEdit(self.update_service_widget)
        self.service_Update.setObjectName(u"service_Update")
        self.service_Update.setGeometry(QRect(180, 130, 351, 45))
        palette61 = QPalette()
        palette61.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette61.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette61.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette61.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette61.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette61.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette61.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette61.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette61.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.service_Update.setPalette(palette61)
        self.service_Update.setFont(font11)
        self.service_Update.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.service_Amount = QLineEdit(self.update_service_widget)
        self.service_Amount.setObjectName(u"service_Amount")
        self.service_Amount.setGeometry(QRect(180, 200, 351, 45))
        palette62 = QPalette()
        palette62.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette62.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette62.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette62.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette62.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette62.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette62.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette62.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette62.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.service_Amount.setPalette(palette62)
        self.service_Amount.setFont(font11)
        self.service_Amount.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.serviceUpdate_savebtn = QPushButton(self.update_service_widget)
        self.serviceUpdate_savebtn.setObjectName(u"serviceUpdate_savebtn")
        self.serviceUpdate_savebtn.setGeometry(QRect(550, 290, 101, 41))
        self.serviceUpdate_savebtn.setFont(font3)
        self.serviceUpdate_savebtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.serviceUpdate_savebtn.setStyleSheet(u"background-color: #167432;\n"
"border-radius: 20px;")
        self.serviceUpdate_cancelbtn = QPushButton(self.update_service_widget)
        self.serviceUpdate_cancelbtn.setObjectName(u"serviceUpdate_cancelbtn")
        self.serviceUpdate_cancelbtn.setGeometry(QRect(430, 290, 101, 41))
        self.serviceUpdate_cancelbtn.setFont(font3)
        self.serviceUpdate_cancelbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.serviceUpdate_cancelbtn.setStyleSheet(u"background-color: #AE2626;\n"
"border-radius: 20px;")
        self.add_employee_popup = QWidget(self.centralwidget)
        self.add_employee_popup.setObjectName(u"add_employee_popup")
        self.add_employee_popup.setGeometry(QRect(0, 0, 0, 902))
        self.add_employee_popup.setStyleSheet(u"background-color: rgba(0,0,0,160);")
        self.add_employee_widget = QWidget(self.add_employee_popup)
        self.add_employee_widget.setObjectName(u"add_employee_widget")
        self.add_employee_widget.setEnabled(True)
        self.add_employee_widget.setGeometry(QRect(250, 255, 851, 381))
        palette63 = QPalette()
        palette63.setBrush(QPalette.Active, QPalette.Button, brush)
        palette63.setBrush(QPalette.Active, QPalette.Base, brush)
        palette63.setBrush(QPalette.Active, QPalette.Window, brush)
        palette63.setBrush(QPalette.Active, QPalette.HighlightedText, brush8)
        palette63.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette63.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette63.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette63.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush8)
        palette63.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette63.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette63.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette63.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush8)
        self.add_employee_widget.setPalette(palette63)
        self.add_employee_widget.setStyleSheet(u"#add_employee_widget{\n"
"background-color: #FFFFFF;\n"
"border-radius:  15px;\n"
"}")
        self.widget_17 = QWidget(self.add_employee_widget)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setGeometry(QRect(0, 0, 851, 61))
        self.widget_17.setStyleSheet(u"background-color: #346F45;\n"
"border-top-right-radius: 15px;\n"
"border-top-left-radius: 15px;")
        self.label_17 = QLabel(self.widget_17)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(0, -1, 851, 61))
        self.label_17.setFont(font10)
        self.label_17.setStyleSheet(u"#label_17{\n"
"color: #FFFFFF;\n"
"font-family: \"Jaldi\", sans-serif;\n"
"background: none;\n"
"}")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.AddEmp_fname = QLineEdit(self.add_employee_widget)
        self.AddEmp_fname.setObjectName(u"AddEmp_fname")
        self.AddEmp_fname.setGeometry(QRect(50, 110, 281, 45))
        palette64 = QPalette()
        palette64.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette64.setBrush(QPalette.Active, QPalette.Text, brush)
        palette64.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette64.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette64.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette64.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette64.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette64.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette64.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette64.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette64.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette64.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette64.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette64.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette64.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.AddEmp_fname.setPalette(palette64)
        self.AddEmp_fname.setFont(font11)
        self.AddEmp_fname.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.AddEmp_contact = QLineEdit(self.add_employee_widget)
        self.AddEmp_contact.setObjectName(u"AddEmp_contact")
        self.AddEmp_contact.setGeometry(QRect(50, 190, 231, 45))
        palette65 = QPalette()
        palette65.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette65.setBrush(QPalette.Active, QPalette.Text, brush)
        palette65.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette65.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette65.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette65.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette65.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette65.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette65.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette65.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette65.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette65.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette65.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette65.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette65.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.AddEmp_contact.setPalette(palette65)
        self.AddEmp_contact.setFont(font11)
        self.AddEmp_contact.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.AddEmp_address = QLineEdit(self.add_employee_widget)
        self.AddEmp_address.setObjectName(u"AddEmp_address")
        self.AddEmp_address.setGeometry(QRect(300, 190, 501, 45))
        palette66 = QPalette()
        palette66.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette66.setBrush(QPalette.Active, QPalette.Text, brush)
        palette66.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette66.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette66.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette66.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette66.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette66.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette66.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette66.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette66.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette66.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette66.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette66.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette66.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.AddEmp_address.setPalette(palette66)
        self.AddEmp_address.setFont(font11)
        self.AddEmp_address.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.AddEmp_cancelbtn = QPushButton(self.add_employee_widget)
        self.AddEmp_cancelbtn.setObjectName(u"AddEmp_cancelbtn")
        self.AddEmp_cancelbtn.setGeometry(QRect(570, 300, 101, 41))
        self.AddEmp_cancelbtn.setFont(font3)
        self.AddEmp_cancelbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.AddEmp_cancelbtn.setStyleSheet(u"background-color: #AE2626;\n"
"border-radius: 20px;")
        self.AddEmp_savebtn = QPushButton(self.add_employee_widget)
        self.AddEmp_savebtn.setObjectName(u"AddEmp_savebtn")
        self.AddEmp_savebtn.setGeometry(QRect(700, 300, 101, 41))
        self.AddEmp_savebtn.setFont(font3)
        self.AddEmp_savebtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.AddEmp_savebtn.setStyleSheet(u"background-color: #167432;\n"
"border-radius: 20px;")
        self.pushButton_21 = QPushButton(self.add_employee_widget)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(770, 123, 21, 21))
        self.pushButton_21.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_21.setStyleSheet(u"background: none;")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/Drop Down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_21.setIcon(icon9)
        self.pushButton_21.setIconSize(QSize(20, 20))
        self.AddEmp_DOB = QDateEdit(self.add_employee_widget)
        self.AddEmp_DOB.setObjectName(u"AddEmp_DOB")
        self.AddEmp_DOB.setGeometry(QRect(640, 110, 161, 45))
        palette67 = QPalette()
        palette67.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette67.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette67.setBrush(QPalette.Active, QPalette.Text, brush)
        palette67.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette67.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette67.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette67.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette67.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette67.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette67.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette67.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette67.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette67.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette67.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette67.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette67.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette67.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette67.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette67.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette67.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette67.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.AddEmp_DOB.setPalette(palette67)
        self.AddEmp_DOB.setFont(font12)
        self.AddEmp_DOB.setStyleSheet(u"#AddEmp_DOB{\n"
"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"color: #fff;\n"
"}\n"
"\n"
"#AddEmp_DOB::drop-down{\n"
"border: 0px;\n"
"width: 30px;\n"
"}\n"
"\n"
"#AddEmp_DOB::down-arrow{\n"
"image: url(:/icons/icons/Calendar.png);\n"
"width: 20px;\n"
"height: 20px;\n"
"margin-right: 17px;\n"
"}\n"
"\n"
"#AddEmp_DOB QWidget{\n"
"background-color: #fff;\n"
"alternate-background-color: #fff;\n"
"color: #003910;\n"
"}\n"
"\n"
"#qt_calendar_calendarview{\n"
"border: 1px solid #D6D6D6;\n"
"min-width: 200px;\n"
"min-height: 170px;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth, #qt_calendar_nextmonth{\n"
"qproperty-icon: none;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth{\n"
"image: url(:/icons/icons/ArrowPrev.png);\n"
"padding: 5px 0 5px 0;\n"
"}\n"
"\n"
"#qt_calendar_nextmonth{\n"
"image: url(:/icons/icons/ArrowNext.png);\n"
"padding: 5px 0 5px 0;\n"
"}\n"
"#qt_calendar_monthbutton{\n"
"padding: 0 15px 0 0;\n"
"border-radius: 5px;\n"
"margin: 0 5px;\n"
"font-size: 13px;\n"
""
                        "}\n"
"\n"
"#qt_calendar_yearbutton{\n"
"padding: 0 30px 0 10px;\n"
"border-radius: 5px;\n"
"font-size: 13px;\n"
"}\n"
"\n"
"#qt_calendar_yearedit{\n"
"font-size: 13px;\n"
"background: transparent;\n"
"color: #fff;\n"
"font-size: 13px;\n"
"min-width: 55px;\n"
"padding: 0 15px;\n"
"}\n"
"\n"
"#qt_calendar_navigationbar{\n"
"border: 1px solid #D6D6D6;\n"
"}\n"
"\n"
"#AddEmp_DOB QToolButton {\n"
"    background-color: #fff;\n"
"    border: none; \n"
"    margin: 0px;  \n"
"}\n"
"\n"
"#AddEmp_DOB QToolButton QMenu{\n"
"background-color: #FFFFFF;\n"
"border: 1px solid #D6D6D6;\n"
"}\n"
"\n"
"#AddEmp_DOB QToolButton QMenu::item{\n"
"padding: 5px;\n"
"min-width: 70px;\n"
"color: #000;\n"
"}\n"
"\n"
"#AddEmp_DOB QToolButton QMenu::item:selected:enabled{\n"
"background-color: #346F45;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:hover{\n"
"border-radius: 5px;\n"
"background-color: #619270;\n"
"color: #fff;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:selected{\n"
"border-radius: 5px;\n"
"background-color: #346F45;\n"
""
                        "}\n"
"\n"
"#qt_calendar_calendarview::item{\n"
"padding: 3px;\n"
"}")
        self.AddEmp_DOB.setReadOnly(False)
        self.AddEmp_DOB.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.AddEmp_DOB.setCalendarPopup(True)
        self.AddEmp_lname = QLineEdit(self.add_employee_widget)
        self.AddEmp_lname.setObjectName(u"AddEmp_lname")
        self.AddEmp_lname.setGeometry(QRect(350, 110, 271, 45))
        palette68 = QPalette()
        palette68.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette68.setBrush(QPalette.Active, QPalette.Text, brush)
        palette68.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette68.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette68.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette68.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette68.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette68.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette68.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette68.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette68.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette68.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette68.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette68.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette68.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.AddEmp_lname.setPalette(palette68)
        self.AddEmp_lname.setFont(font11)
        self.AddEmp_lname.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.employee_delete_popup = QWidget(self.centralwidget)
        self.employee_delete_popup.setObjectName(u"employee_delete_popup")
        self.employee_delete_popup.setGeometry(QRect(0, 0, 0, 902))
        self.employee_delete_popup.setStyleSheet(u"background-color: rgba(0,0,0,160);")
        self.confirm_empdel_widget = QWidget(self.employee_delete_popup)
        self.confirm_empdel_widget.setObjectName(u"confirm_empdel_widget")
        self.confirm_empdel_widget.setEnabled(True)
        self.confirm_empdel_widget.setGeometry(QRect(330, 350, 721, 191))
        palette69 = QPalette()
        palette69.setBrush(QPalette.Active, QPalette.Button, brush)
        palette69.setBrush(QPalette.Active, QPalette.Base, brush)
        palette69.setBrush(QPalette.Active, QPalette.Window, brush)
        palette69.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette69.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette69.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette69.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette69.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette69.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.confirm_empdel_widget.setPalette(palette69)
        self.confirm_empdel_widget.setStyleSheet(u"#confirm_empdel_widget{\n"
"background-color: #FFFFFF;\n"
"border-radius:  15px;\n"
"}")
        self.cancelDelete_emp = QPushButton(self.confirm_empdel_widget)
        self.cancelDelete_emp.setObjectName(u"cancelDelete_emp")
        self.cancelDelete_emp.setGeometry(QRect(570, 120, 101, 41))
        self.cancelDelete_emp.setFont(font3)
        self.cancelDelete_emp.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelDelete_emp.setStyleSheet(u"background-color: #AE2626;\n"
"border-radius: 20px;")
        self.confDelete_emp = QPushButton(self.confirm_empdel_widget)
        self.confDelete_emp.setObjectName(u"confDelete_emp")
        self.confDelete_emp.setGeometry(QRect(440, 120, 101, 41))
        self.confDelete_emp.setFont(font3)
        self.confDelete_emp.setCursor(QCursor(Qt.PointingHandCursor))
        self.confDelete_emp.setStyleSheet(u"background-color: #167432;\n"
"border-radius: 20px;")
        self.label_18 = QLabel(self.confirm_empdel_widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 0, 721, 71))
        self.label_18.setFont(font10)
        self.label_18.setStyleSheet(u"color: #AE2626;\n"
"font-family: \"Jaldi\", sans-serif;\n"
"background: none;\n"
"")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_19 = QLabel(self.confirm_empdel_widget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(50, 90, 351, 31))
        self.label_19.setFont(font13)
        self.label_19.setStyleSheet(u"background: none;\n"
"color: #222020;")
        self.logout_popup = QWidget(self.centralwidget)
        self.logout_popup.setObjectName(u"logout_popup")
        self.logout_popup.setGeometry(QRect(0, 0, 0, 902))
        self.logout_popup.setStyleSheet(u"background-color: rgba(0,0,0,160);")
        self.confirm_logout_widget = QWidget(self.logout_popup)
        self.confirm_logout_widget.setObjectName(u"confirm_logout_widget")
        self.confirm_logout_widget.setEnabled(True)
        self.confirm_logout_widget.setGeometry(QRect(330, 350, 721, 191))
        palette70 = QPalette()
        palette70.setBrush(QPalette.Active, QPalette.Button, brush)
        palette70.setBrush(QPalette.Active, QPalette.Base, brush)
        palette70.setBrush(QPalette.Active, QPalette.Window, brush)
        palette70.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette70.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette70.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette70.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette70.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette70.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.confirm_logout_widget.setPalette(palette70)
        self.confirm_logout_widget.setStyleSheet(u"#confirm_logout_widget{\n"
"background-color: #FFFFFF;\n"
"border-radius:  15px;\n"
"}")
        self.cancelLogout_btn = QPushButton(self.confirm_logout_widget)
        self.cancelLogout_btn.setObjectName(u"cancelLogout_btn")
        self.cancelLogout_btn.setGeometry(QRect(570, 120, 101, 41))
        self.cancelLogout_btn.setFont(font3)
        self.cancelLogout_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelLogout_btn.setStyleSheet(u"background-color: #AE2626;\n"
"border-radius: 20px;")
        self.confLogout_btn = QPushButton(self.confirm_logout_widget)
        self.confLogout_btn.setObjectName(u"confLogout_btn")
        self.confLogout_btn.setGeometry(QRect(440, 120, 101, 41))
        self.confLogout_btn.setFont(font3)
        self.confLogout_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.confLogout_btn.setStyleSheet(u"background-color: #167432;\n"
"border-radius: 20px;")
        self.label_21 = QLabel(self.confirm_logout_widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 0, 721, 71))
        self.label_21.setFont(font10)
        self.label_21.setStyleSheet(u"color: #AE2626;\n"
"font-family: \"Jaldi\", sans-serif;\n"
"background: none;\n"
"")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_22 = QLabel(self.confirm_logout_widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(50, 90, 351, 31))
        self.label_22.setFont(font13)
        self.label_22.setStyleSheet(u"background: none;\n"
"color: #222020;")
        self.success_widget = QWidget(self.centralwidget)
        self.success_widget.setObjectName(u"success_widget")
        self.success_widget.setGeometry(QRect(510, 30, 0, 61))
        self.success_widget.setStyleSheet(u"QWidget{\n"
"background-color: #fff;\n"
"border-radius: 20px;\n"
"}")
        self.label_5 = QLabel(self.success_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 10, 42, 42))
        self.label_5.setStyleSheet(u"")
        self.label_5.setPixmap(QPixmap(u":/icons/icons/Checkmark.png"))
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(self.success_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 0, 251, 61))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: #003910;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.savechanges_widget = QWidget(self.centralwidget)
        self.savechanges_widget.setObjectName(u"savechanges_widget")
        self.savechanges_widget.setGeometry(QRect(540, 30, 0, 61))
        self.savechanges_widget.setStyleSheet(u"QWidget{\n"
"background-color: #fff;\n"
"border-radius: 20px;\n"
"}")
        self.label_39 = QLabel(self.savechanges_widget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(235, 10, 42, 42))
        self.label_39.setPixmap(QPixmap(u":/icons/icons/Checkmark.png"))
        self.label_39.setScaledContents(True)
        self.label_40 = QLabel(self.savechanges_widget)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(50, 0, 191, 61))
        self.label_40.setFont(font2)
        self.label_40.setStyleSheet(u"color: #003910;\n"
"background: none;")
        self.label_40.setAlignment(Qt.AlignCenter)
        self.change_popup = QWidget(self.centralwidget)
        self.change_popup.setObjectName(u"change_popup")
        self.change_popup.setGeometry(QRect(-10, 0, 0, 902))
        self.change_popup.setStyleSheet(u"background-color: rgba(0,0,0,160);")
        self.change_widget = QWidget(self.change_popup)
        self.change_widget.setObjectName(u"change_widget")
        self.change_widget.setGeometry(QRect(490, 315, 431, 221))
        self.change_widget.setStyleSheet(u"#change_widget{\n"
"background-color: #fff;\n"
"border-radius: 10px;\n"
"}")
        self.label_42 = QLabel(self.change_widget)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(0, 0, 431, 61))
        font16 = QFont()
        font16.setFamily(u"Segoe UI")
        font16.setPointSize(17)
        font16.setBold(True)
        font16.setLegacyWeight(75)
        self.label_42.setFont(font16)
        self.label_42.setStyleSheet(u"color: #003910;\n"
"background: none;")
        self.label_42.setAlignment(Qt.AlignCenter)
        self.label_43 = QLabel(self.change_widget)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(70, 17, 41, 141))
        font17 = QFont()
        font17.setFamily(u"Segoe UI Semibold")
        font17.setPointSize(11)
        font17.setBold(True)
        font17.setLegacyWeight(75)
        self.label_43.setFont(font17)
        self.label_43.setStyleSheet(u"background: none;\n"
"color: #003910;")
        self.change_field = QLineEdit(self.change_widget)
        self.change_field.setObjectName(u"change_field")
        self.change_field.setGeometry(QRect(110, 62, 321, 51))
        self.change_field.setFont(font17)
        self.change_field.setStyleSheet(u"background-color: #eee;\n"
"color: #000;\n"
"border: none;\n"
"padding: 10px;")
        self.change_field.setReadOnly(True)
        self.change_okBtn = QPushButton(self.change_widget)
        self.change_okBtn.setObjectName(u"change_okBtn")
        self.change_okBtn.setGeometry(QRect(260, 150, 141, 41))
        self.change_okBtn.setFont(font3)
        self.change_okBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.change_okBtn.setStyleSheet(u"background-color: #167432;\n"
"border-radius: 20px;")
        self.rowSelection_notice = QWidget(self.centralwidget)
        self.rowSelection_notice.setObjectName(u"rowSelection_notice")
        self.rowSelection_notice.setGeometry(QRect(540, 10, 0, 51))
        self.rowSelection_notice.setStyleSheet(u"QWidget{\n"
"background-color: #fff;\n"
"border-radius: 20px;\n"
"}")
        self.label_50 = QLabel(self.rowSelection_notice)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(20, 9, 35, 35))
        self.label_50.setStyleSheet(u"")
        self.label_50.setPixmap(QPixmap(u":/icons/icons/notice.png"))
        self.label_50.setScaledContents(True)
        self.label_51 = QLabel(self.rowSelection_notice)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(50, 0, 231, 51))
        self.label_51.setFont(font13)
        self.label_51.setStyleSheet(u"color: #000;\n"
"background:none;")
        self.label_51.setAlignment(Qt.AlignCenter)
        self.service_delete_popup = QWidget(self.centralwidget)
        self.service_delete_popup.setObjectName(u"service_delete_popup")
        self.service_delete_popup.setGeometry(QRect(-10, 0, 0, 902))
        self.service_delete_popup.setStyleSheet(u"background-color: rgba(0,0,0,160);")
        self.confirm_servdel_widget = QWidget(self.service_delete_popup)
        self.confirm_servdel_widget.setObjectName(u"confirm_servdel_widget")
        self.confirm_servdel_widget.setEnabled(True)
        self.confirm_servdel_widget.setGeometry(QRect(330, 350, 721, 191))
        palette71 = QPalette()
        palette71.setBrush(QPalette.Active, QPalette.Button, brush)
        palette71.setBrush(QPalette.Active, QPalette.Base, brush)
        palette71.setBrush(QPalette.Active, QPalette.Window, brush)
        palette71.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette71.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette71.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette71.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette71.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette71.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.confirm_servdel_widget.setPalette(palette71)
        self.confirm_servdel_widget.setStyleSheet(u"#confirm_servdel_widget{\n"
"background-color: #FFFFFF;\n"
"border-radius:  15px;\n"
"}")
        self.cancelDelete_serv = QPushButton(self.confirm_servdel_widget)
        self.cancelDelete_serv.setObjectName(u"cancelDelete_serv")
        self.cancelDelete_serv.setGeometry(QRect(570, 120, 101, 41))
        self.cancelDelete_serv.setFont(font3)
        self.cancelDelete_serv.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelDelete_serv.setStyleSheet(u"background-color: #AE2626;\n"
"border-radius: 20px;")
        self.confDelete_serv = QPushButton(self.confirm_servdel_widget)
        self.confDelete_serv.setObjectName(u"confDelete_serv")
        self.confDelete_serv.setGeometry(QRect(440, 120, 101, 41))
        self.confDelete_serv.setFont(font3)
        self.confDelete_serv.setCursor(QCursor(Qt.PointingHandCursor))
        self.confDelete_serv.setStyleSheet(u"background-color: #167432;\n"
"border-radius: 20px;")
        self.label_15 = QLabel(self.confirm_servdel_widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 0, 721, 71))
        self.label_15.setFont(font10)
        self.label_15.setStyleSheet(u"color: #AE2626;\n"
"font-family: \"Jaldi\", sans-serif;\n"
"background: none;\n"
"")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_38 = QLabel(self.confirm_servdel_widget)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(50, 90, 351, 31))
        self.label_38.setFont(font13)
        self.label_38.setStyleSheet(u"background: none;\n"
"color: #222020;")
        self.confirm_pay_widget = QWidget(self.centralwidget)
        self.confirm_pay_widget.setObjectName(u"confirm_pay_widget")
        self.confirm_pay_widget.setEnabled(True)
        self.confirm_pay_widget.setGeometry(QRect(505, 10, 0, 111))
        palette72 = QPalette()
        palette72.setBrush(QPalette.Active, QPalette.Button, brush)
        palette72.setBrush(QPalette.Active, QPalette.Base, brush)
        palette72.setBrush(QPalette.Active, QPalette.Window, brush)
        palette72.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette72.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette72.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette72.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette72.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette72.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.confirm_pay_widget.setPalette(palette72)
        self.confirm_pay_widget.setStyleSheet(u"#confirm_pay_widget{\n"
"background-color: #FFFFFF;\n"
"border-radius:  15px;\n"
"}")
        self.cancelPay_mem = QPushButton(self.confirm_pay_widget)
        self.cancelPay_mem.setObjectName(u"cancelPay_mem")
        self.cancelPay_mem.setGeometry(QRect(240, 60, 81, 31))
        self.cancelPay_mem.setFont(font3)
        self.cancelPay_mem.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelPay_mem.setStyleSheet(u"background-color: #AE2626;\n"
"border-radius: 15px;")
        self.confPay_mem = QPushButton(self.confirm_pay_widget)
        self.confPay_mem.setObjectName(u"confPay_mem")
        self.confPay_mem.setGeometry(QRect(140, 60, 81, 31))
        self.confPay_mem.setFont(font3)
        self.confPay_mem.setCursor(QCursor(Qt.PointingHandCursor))
        self.confPay_mem.setStyleSheet(u"background-color: #167432;\n"
"border-radius: 15px;")
        self.label_41 = QLabel(self.confirm_pay_widget)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(0, 0, 241, 61))
        self.label_41.setFont(font10)
        self.label_41.setStyleSheet(u"color: #AE2626;\n"
"font-family: \"Jaldi\", sans-serif;\n"
"background: none;\n"
"")
        self.label_41.setAlignment(Qt.AlignCenter)
        self.invalid_notice = QWidget(self.centralwidget)
        self.invalid_notice.setObjectName(u"invalid_notice")
        self.invalid_notice.setGeometry(QRect(480, 10, 0, 51))
        self.invalid_notice.setStyleSheet(u"QWidget{\n"
"background-color: #fff;\n"
"border-radius: 20px;\n"
"}")
        self.label_60 = QLabel(self.invalid_notice)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(20, 9, 35, 35))
        self.label_60.setStyleSheet(u"")
        self.label_60.setPixmap(QPixmap(u":/icons/icons/notice.png"))
        self.label_60.setScaledContents(True)
        self.fieldNotice = QLabel(self.invalid_notice)
        self.fieldNotice.setObjectName(u"fieldNotice")
        self.fieldNotice.setGeometry(QRect(50, 0, 321, 51))
        self.fieldNotice.setFont(font13)
        self.fieldNotice.setStyleSheet(u"color: #000;\n"
"background:none;")
        self.fieldNotice.setAlignment(Qt.AlignCenter)
        self.addAdmin_notice = QWidget(self.centralwidget)
        self.addAdmin_notice.setObjectName(u"addAdmin_notice")
        self.addAdmin_notice.setGeometry(QRect(0, 0, 0, 31))
        self.addAdmin_notice.setStyleSheet(u"background-color: rgba(0,0,0,70);")
        self.label = QLabel(self.addAdmin_notice)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 3, 1361, 31))
        font18 = QFont()
        font18.setFamily(u"Segoe UI Variable Small")
        font18.setPointSize(10)
        self.label.setFont(font18)
        self.label.setStyleSheet(u"background: none;\n"
"color: #fff;")
        self.label.setAlignment(Qt.AlignCenter)
        self.addAdminBtn = QPushButton(self.addAdmin_notice)
        self.addAdminBtn.setObjectName(u"addAdminBtn")
        self.addAdminBtn.setGeometry(QRect(930, 2, 101, 31))
        self.addAdminBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addAdminBtn.setStyleSheet(u"QPushButton{\n"
"background: none;\n"
"font-size: 12.5px;\n"
"color: #FFF455;\n"
"text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: #fff;\n"
"}")
        self.tenderedAmt_notice = QWidget(self.centralwidget)
        self.tenderedAmt_notice.setObjectName(u"tenderedAmt_notice")
        self.tenderedAmt_notice.setGeometry(QRect(480, 10, 0, 51))
        self.tenderedAmt_notice.setStyleSheet(u"QWidget{\n"
"background-color: #fff;\n"
"border-radius: 20px;\n"
"}")
        self.label_61 = QLabel(self.tenderedAmt_notice)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(20, 9, 35, 35))
        self.label_61.setStyleSheet(u"")
        self.label_61.setPixmap(QPixmap(u":/icons/icons/notice.png"))
        self.label_61.setScaledContents(True)
        self.tenderedfieldNotice = QLabel(self.tenderedAmt_notice)
        self.tenderedfieldNotice.setObjectName(u"tenderedfieldNotice")
        self.tenderedfieldNotice.setGeometry(QRect(50, 0, 321, 51))
        self.tenderedfieldNotice.setFont(font13)
        self.tenderedfieldNotice.setStyleSheet(u"color: #000;\n"
"background:none;")
        self.tenderedfieldNotice.setAlignment(Qt.AlignCenter)
        self.new_notifbtn = QPushButton(self.centralwidget)
        self.new_notifbtn.setObjectName(u"new_notifbtn")
        self.new_notifbtn.setGeometry(QRect(540, 10, 0, 51))
        self.new_notifbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_notifbtn.setStyleSheet(u"QPushButton{\n"
"background-color:#fff;\n"
"text-align: left;\n"
"padding: 0 0 0 30px;\n"
"color: #000;\n"
"font-size: 15px;\n"
"font-weight: 500;\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#ddd;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:#fff;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/new_notif.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_notifbtn.setIcon(icon10)
        self.new_notifbtn.setIconSize(QSize(30, 30))
        self.service_delete_notice = QWidget(self.centralwidget)
        self.service_delete_notice.setObjectName(u"service_delete_notice")
        self.service_delete_notice.setGeometry(QRect(420, 10, 0, 51))
        self.service_delete_notice.setStyleSheet(u"QWidget{\n"
"background-color: #fff;\n"
"border-radius: 20px;\n"
"}")
        self.label_62 = QLabel(self.service_delete_notice)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(20, 9, 35, 35))
        self.label_62.setStyleSheet(u"")
        self.label_62.setPixmap(QPixmap(u":/icons/icons/notice.png"))
        self.label_62.setScaledContents(True)
        self.fieldNotice_2 = QLabel(self.service_delete_notice)
        self.fieldNotice_2.setObjectName(u"fieldNotice_2")
        self.fieldNotice_2.setGeometry(QRect(50, 0, 491, 51))
        self.fieldNotice_2.setFont(font13)
        self.fieldNotice_2.setStyleSheet(u"color: #000;\n"
"background:none;")
        self.fieldNotice_2.setAlignment(Qt.AlignCenter)
        self.renewal_reminder_popup = QWidget(self.centralwidget)
        self.renewal_reminder_popup.setObjectName(u"renewal_reminder_popup")
        self.renewal_reminder_popup.setGeometry(QRect(0, 0, 0, 902))
        self.renewal_reminder_popup.setStyleSheet(u"background-color: rgba(0,0,0,160);")
        self.renewal_reminder_widget = QWidget(self.renewal_reminder_popup)
        self.renewal_reminder_widget.setObjectName(u"renewal_reminder_widget")
        self.renewal_reminder_widget.setGeometry(QRect(450, 280, 491, 291))
        self.renewal_reminder_widget.setStyleSheet(u"#renewal_reminder_widget{\n"
"background-color: #fff;\n"
"border-radius: 10px;\n"
"}")
        self.renew_mshipBtn = QPushButton(self.renewal_reminder_widget)
        self.renew_mshipBtn.setObjectName(u"renew_mshipBtn")
        self.renew_mshipBtn.setGeometry(QRect(0, 210, 247, 81))
        self.renew_mshipBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.renew_mshipBtn.setStyleSheet(u"QPushButton{\n"
"background-color: #30BD58;\n"
"border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #22883F;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #04D740;\n"
"}")
        self.renew_monservBtn = QPushButton(self.renewal_reminder_widget)
        self.renew_monservBtn.setObjectName(u"renew_monservBtn")
        self.renew_monservBtn.setGeometry(QRect(250, 210, 241, 81))
        self.renew_monservBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.renew_monservBtn.setStyleSheet(u"QPushButton{\n"
"background-color: #30BD58;\n"
"border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #22883F;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #04D740;\n"
"}")
        self.reminder_text = QLabel(self.renewal_reminder_widget)
        self.reminder_text.setObjectName(u"reminder_text")
        self.reminder_text.setGeometry(QRect(30, 30, 431, 131))
        font19 = QFont()
        font19.setFamily(u"Segoe UI")
        font19.setBold(True)
        font19.setLegacyWeight(62)
        self.reminder_text.setFont(font19)
        self.reminder_text.setStyleSheet(u"font-size: 15px;\n"
"letter-spacing: 1px;\n"
"line-spacing: 3px;\n"
"text-align: center;\n"
"font-weight: 500;\n"
"background:none;\n"
"color: #003910;")
        self.reminder_text.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.reminder_text.setWordWrap(True)
        self.exit_reminder = QPushButton(self.renewal_reminder_popup)
        self.exit_reminder.setObjectName(u"exit_reminder")
        self.exit_reminder.setGeometry(QRect(925, 262, 31, 31))
        self.exit_reminder.setCursor(QCursor(Qt.PointingHandCursor))
        self.exit_reminder.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0,0,0,30%);\n"
"border-radius: 15px\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/w_exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_reminder.setIcon(icon11)
        self.exit_reminder.setIconSize(QSize(20, 20))
        self.membership_renewal_popup = QWidget(self.centralwidget)
        self.membership_renewal_popup.setObjectName(u"membership_renewal_popup")
        self.membership_renewal_popup.setGeometry(QRect(0, 0, 0, 902))
        self.membership_renewal_popup.setStyleSheet(u"background-color: rgba(0,0,0,160);")
        self.membership_renewal_widget = QWidget(self.membership_renewal_popup)
        self.membership_renewal_widget.setObjectName(u"membership_renewal_widget")
        self.membership_renewal_widget.setEnabled(True)
        self.membership_renewal_widget.setGeometry(QRect(350, 210, 671, 411))
        palette73 = QPalette()
        palette73.setBrush(QPalette.Active, QPalette.Button, brush)
        palette73.setBrush(QPalette.Active, QPalette.Base, brush)
        palette73.setBrush(QPalette.Active, QPalette.Window, brush)
        palette73.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette73.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette73.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette73.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette73.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette73.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.membership_renewal_widget.setPalette(palette73)
        self.membership_renewal_widget.setStyleSheet(u"#membership_renewal_widget{\n"
"background-color: #FFFFFF;\n"
"border-radius:  15px;\n"
"}")
        self.widget_34 = QWidget(self.membership_renewal_widget)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setGeometry(QRect(0, 0, 671, 61))
        self.widget_34.setStyleSheet(u"background-color: #346F45;\n"
"border-top-right-radius: 15px;\n"
"border-top-left-radius: 15px;")
        self.label_9 = QLabel(self.widget_34)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, -1, 671, 61))
        self.label_9.setFont(font10)
        self.label_9.setStyleSheet(u"#label_9{\n"
"color: #FFFFFF;\n"
"font-family: \"Jaldi\", sans-serif;\n"
"background: none;\n"
"}")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.mem_fee = QLineEdit(self.membership_renewal_widget)
        self.mem_fee.setObjectName(u"mem_fee")
        self.mem_fee.setGeometry(QRect(150, 130, 351, 45))
        palette74 = QPalette()
        palette74.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette74.setBrush(QPalette.Active, QPalette.Text, brush)
        palette74.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette74.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette74.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette74.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette74.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette74.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette74.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette74.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette74.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette74.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette74.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette74.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette74.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.mem_fee.setPalette(palette74)
        self.mem_fee.setFont(font11)
        self.mem_fee.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.mem_fee.setReadOnly(False)
        self.memRenew_tendered = QLineEdit(self.membership_renewal_widget)
        self.memRenew_tendered.setObjectName(u"memRenew_tendered")
        self.memRenew_tendered.setGeometry(QRect(150, 210, 351, 45))
        palette75 = QPalette()
        palette75.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette75.setBrush(QPalette.Active, QPalette.Text, brush)
        palette75.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette75.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette75.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette75.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette75.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette75.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette75.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette75.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette75.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette75.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette75.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette75.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette75.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.memRenew_tendered.setPalette(palette75)
        self.memRenew_tendered.setFont(font11)
        self.memRenew_tendered.setStyleSheet(u"background-color: #619270;\n"
"border-radius: 20px;\n"
"padding: 0 15px 0 15px;")
        self.memRenew_cancelBtn = QPushButton(self.membership_renewal_widget)
        self.memRenew_cancelBtn.setObjectName(u"memRenew_cancelBtn")
        self.memRenew_cancelBtn.setGeometry(QRect(390, 330, 101, 41))
        self.memRenew_cancelBtn.setFont(font3)
        self.memRenew_cancelBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.memRenew_cancelBtn.setStyleSheet(u"background-color: #AE2626;\n"
"border-radius: 20px;")
        self.memRenew_payBtn = QPushButton(self.membership_renewal_widget)
        self.memRenew_payBtn.setObjectName(u"memRenew_payBtn")
        self.memRenew_payBtn.setGeometry(QRect(510, 330, 101, 41))
        self.memRenew_payBtn.setFont(font3)
        self.memRenew_payBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.memRenew_payBtn.setStyleSheet(u"background-color: #167432;\n"
"border-radius: 20px;")
        self.delete_notif = QWidget(self.centralwidget)
        self.delete_notif.setObjectName(u"delete_notif")
        self.delete_notif.setGeometry(QRect(650, 15, 0, 51))
        self.delete_notif.setStyleSheet(u"background-color: #fff;\n"
"border-radius: 25px")
        self.label_20 = QLabel(self.delete_notif)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(25, 10, 30, 30))
        self.label_20.setPixmap(QPixmap(u":/icons/icons/r_trash.png"))
        self.label_20.setScaledContents(True)
        self.pushButton = QPushButton(self.delete_notif)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 25, 20, 20))
        self.pushButton.setStyleSheet(u"background-color:#fff;\n"
"border:none;\n"
"border-radius: 9px;")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/r_check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon12)
        self.pushButton.setIconSize(QSize(20, 20))
        self.assigned_emp_delete = QWidget(self.centralwidget)
        self.assigned_emp_delete.setObjectName(u"assigned_emp_delete")
        self.assigned_emp_delete.setGeometry(QRect(0, 0, 0, 902))
        self.assigned_emp_delete.setStyleSheet(u"background-color: rgba(0,0,0,160);")
        self.confirm_empdel_widget_2 = QWidget(self.assigned_emp_delete)
        self.confirm_empdel_widget_2.setObjectName(u"confirm_empdel_widget_2")
        self.confirm_empdel_widget_2.setEnabled(True)
        self.confirm_empdel_widget_2.setGeometry(QRect(330, 310, 721, 271))
        palette76 = QPalette()
        palette76.setBrush(QPalette.Active, QPalette.Button, brush)
        palette76.setBrush(QPalette.Active, QPalette.Base, brush)
        palette76.setBrush(QPalette.Active, QPalette.Window, brush)
        palette76.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette76.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette76.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette76.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette76.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette76.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.confirm_empdel_widget_2.setPalette(palette76)
        self.confirm_empdel_widget_2.setStyleSheet(u"#confirm_empdel_widget_2{\n"
"background-color: #FFFFFF;\n"
"border-radius:  15px;\n"
"}")
        self.cancel_assigned_emp_delete = QPushButton(self.confirm_empdel_widget_2)
        self.cancel_assigned_emp_delete.setObjectName(u"cancel_assigned_emp_delete")
        self.cancel_assigned_emp_delete.setGeometry(QRect(540, 190, 101, 41))
        self.cancel_assigned_emp_delete.setFont(font3)
        self.cancel_assigned_emp_delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_assigned_emp_delete.setStyleSheet(u"background-color: #AE2626;\n"
"border-radius: 20px;")
        self.conf_assigned_emp_delete = QPushButton(self.confirm_empdel_widget_2)
        self.conf_assigned_emp_delete.setObjectName(u"conf_assigned_emp_delete")
        self.conf_assigned_emp_delete.setGeometry(QRect(420, 190, 101, 41))
        self.conf_assigned_emp_delete.setFont(font3)
        self.conf_assigned_emp_delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.conf_assigned_emp_delete.setStyleSheet(u"background-color: #167432;\n"
"border-radius: 20px;")
        self.label_37 = QLabel(self.confirm_empdel_widget_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(0, 0, 721, 71))
        self.label_37.setFont(font10)
        self.label_37.setStyleSheet(u"color: #AE2626;\n"
"font-family: \"Jaldi\", sans-serif;\n"
"background: none;\n"
"")
        self.label_37.setAlignment(Qt.AlignCenter)
        self.label_44 = QLabel(self.confirm_empdel_widget_2)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(0, 70, 721, 31))
        self.label_44.setFont(font13)
        self.label_44.setStyleSheet(u"background: none;\n"
"color: #222020;")
        self.label_44.setAlignment(Qt.AlignCenter)
        self.label_45 = QLabel(self.confirm_empdel_widget_2)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(0, 100, 721, 31))
        self.label_45.setFont(font13)
        self.label_45.setStyleSheet(u"background: none;\n"
"color: #222020;")
        self.label_45.setAlignment(Qt.AlignCenter)
        self.label_46 = QLabel(self.confirm_empdel_widget_2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(0, 130, 721, 31))
        self.label_46.setFont(font13)
        self.label_46.setStyleSheet(u"background: none;\n"
"color: #222020;")
        self.label_46.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar.raise_()
        self.menu_container.raise_()
        self.view_details_popup.raise_()
        self.register_popup.raise_()
        self.edit_details_popup.raise_()
        self.payment_popup.raise_()
        self.member_delete_popup.raise_()
        self.renew_popup.raise_()
        self.services_popup.raise_()
        self.add_employee_popup.raise_()
        self.employee_delete_popup.raise_()
        self.logout_popup.raise_()
        self.change_popup.raise_()
        self.success_widget.raise_()
        self.rowSelection_notice.raise_()
        self.service_delete_popup.raise_()
        self.addAdmin_notice.raise_()
        self.new_notifbtn.raise_()
        self.service_delete_notice.raise_()
        self.renewal_reminder_popup.raise_()
        self.membership_renewal_popup.raise_()
        self.delete_notif.raise_()
        self.invalid_notice.raise_()
        self.tenderedAmt_notice.raise_()
        self.savechanges_widget.raise_()
        self.confirm_pay_widget.raise_()
        self.assigned_emp_delete.raise_()

        self.retranslateUi(MainWindow)

        self.menu_container.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.gym_name.setText(QCoreApplication.translate("MainWindow", u"PEOPLE FITNESS CENTER", None))
        self.home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.mem_list.setText(QCoreApplication.translate("MainWindow", u"LIST OF MEMBERS", None))
        self.mon_serv_log.setText(QCoreApplication.translate("MainWindow", u"MONTHLY SERVICE LOG", None))
        self.transaction.setText(QCoreApplication.translate("MainWindow", u"TRANSACTION HISTORY", None))
        self.services.setText(QCoreApplication.translate("MainWindow", u"SERVICES", None))
        self.employees.setText(QCoreApplication.translate("MainWindow", u"EMPLOYEES", None))
        self.logout.setText(QCoreApplication.translate("MainWindow", u"LOG OUT", None))
        self.mem_status.setText(QCoreApplication.translate("MainWindow", u"MEMBERSHIP STATUS", None))
        self.notifBtn.setText("")
        self.notiflabel.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.expand_notif.setText("")
        self.minimize_notif.setText("")
        self.mem_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.mem_search_icon.setText("")
        self.delete_member.setText("")
        self.edit_member.setText("")
        self.add_member.setText("")
        ___qtablewidgetitem = self.mem_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.mem_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"FIRST NAME", None));
        ___qtablewidgetitem2 = self.mem_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LAST NAME", None));
        ___qtablewidgetitem3 = self.mem_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"DATE OF BIRTH", None));
        ___qtablewidgetitem4 = self.mem_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"GENDER", None));
        ___qtablewidgetitem5 = self.mem_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ADDRESS", None));
        ___qtablewidgetitem6 = self.mshipStat_table.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem7 = self.mshipStat_table.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"FIRST NAME", None));
        ___qtablewidgetitem8 = self.mshipStat_table.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"LAST NAME", None));
        ___qtablewidgetitem9 = self.mshipStat_table.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"START DATE", None));
        ___qtablewidgetitem10 = self.mshipStat_table.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"END DATE", None));
        self.mshipStat_search_icon.setText("")
        self.mshipStat_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.mon_serviceLog_searchIcon.setText("")
        self.mon_serviceLog_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem11 = self.mon_serviceLog_table.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem12 = self.mon_serviceLog_table.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"FIRST NAME", None));
        ___qtablewidgetitem13 = self.mon_serviceLog_table.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"LAST NAME", None));
        ___qtablewidgetitem14 = self.mon_serviceLog_table.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"SERVICE TYPE", None));
        ___qtablewidgetitem15 = self.mon_serviceLog_table.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"INSTRUCTOR", None));
        ___qtablewidgetitem16 = self.mon_serviceLog_table.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"START DATE", None));
        ___qtablewidgetitem17 = self.mon_serviceLog_table.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"END DATE", None));
        ___qtablewidgetitem18 = self.mon_serviceLog_table.horizontalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        self.renew_btn.setText(QCoreApplication.translate("MainWindow", u"Renew", None))
        ___qtablewidgetitem19 = self.transac_table.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"TRANSACTION NO.", None));
        ___qtablewidgetitem20 = self.transac_table.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"MEMBER ID", None));
        ___qtablewidgetitem21 = self.transac_table.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem22 = self.transac_table.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"DATE", None));
        ___qtablewidgetitem23 = self.transac_table.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"SERVICE", None));
        ___qtablewidgetitem24 = self.transac_table.horizontalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"TOTAL AMOUNT", None));
        ___qtablewidgetitem25 = self.transac_table.horizontalHeaderItem(6)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"TENDERED", None));
        ___qtablewidgetitem26 = self.transac_table.horizontalHeaderItem(7)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"CHANGE", None));
        self.transac_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.transac_search_icon.setText("")
        self.emp_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem27 = self.emp_table.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem28 = self.emp_table.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"FIRST NAME", None));
        ___qtablewidgetitem29 = self.emp_table.horizontalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"LAST NAME", None));
        ___qtablewidgetitem30 = self.emp_table.horizontalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"CONTACT", None));
        ___qtablewidgetitem31 = self.emp_table.horizontalHeaderItem(4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"ADDRESS", None));
        ___qtablewidgetitem32 = self.emp_table.horizontalHeaderItem(5)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"POSITION", None));
        self.add_employee.setText("")
        self.pushButton_9.setText("")
        self.delete_employee.setText("")
        self.emp_search_icon.setText("")
        self.edit_employee.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.viewmem_Id.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.viewmem_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Birthdate", None))
        self.viewmem_DOB.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.viewmem_address.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Tel. Number", None))
        self.viewmem_telnum.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Physical Activities", None))
        self.viewmem_physicalAct.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Medical Ailments", None))
        self.viewmem_medicalAilments.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Previous Gym", None))
        self.viewmem_prevGym.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.viewmem_type.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.viewmem_status.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.viewmem_BP.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Blood Pressure", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.viewmem_Gender.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Weight", None))
        self.viewmem_weight.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.viewmem_height.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.viewmem_backbtn.setText(QCoreApplication.translate("MainWindow", u"Go back", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"VIEW MEMBER DETAILS", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"REGISTER A MEMBER", None))
        self.regismem_fname.setText("")
        self.regismem_fname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name  *", None))
        self.regismem_contact.setText("")
        self.regismem_contact.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contact No.  *", None))
        self.regismem_address.setText("")
        self.regismem_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address  *", None))
        self.regismem_medicAilment.setText("")
        self.regismem_medicAilment.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Medical Ailments", None))
        self.regismem_prevGym.setText("")
        self.regismem_prevGym.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Previous Gym", None))
        self.regismem_BP.setText("")
        self.regismem_BP.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BP *", None))
        self.regismem_physicalAct.setText("")
        self.regismem_physicalAct.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Physical Activities", None))
        self.regismem_weight.setText("")
        self.regismem_weight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Weight  *", None))
        self.regismem_height.setText("")
        self.regismem_height.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Height  *", None))
        self.regismem_cancelbtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.regismem_savebtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.regismemStud_radio.setText(QCoreApplication.translate("MainWindow", u"Student", None))
        self.regismemProf_radio.setText(QCoreApplication.translate("MainWindow", u"Professional", None))
        self.regismem_Status.setItemText(0, QCoreApplication.translate("MainWindow", u"Status", None))
        self.regismem_Status.setItemText(1, QCoreApplication.translate("MainWindow", u"Single", None))
        self.regismem_Status.setItemText(2, QCoreApplication.translate("MainWindow", u"Married", None))

        self.regismem_Status.setCurrentText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.regismem_Status.setPlaceholderText("")
        self.registermem_Gender.setItemText(0, QCoreApplication.translate("MainWindow", u"Gender", None))
        self.registermem_Gender.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.registermem_Gender.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.registermem_Gender.setCurrentText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.registermem_Gender.setPlaceholderText("")
        self.regismem_DOB.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.regismem_lname.setText("")
        self.regismem_lname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Name  *", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"EDIT MEMBER DETAILS", None))
        self.mem_fname.setText("")
        self.mem_fname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name  *", None))
        self.mem_contact.setText("")
        self.mem_contact.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contact No.  *", None))
        self.mem_address.setText("")
        self.mem_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address  *", None))
        self.mem_medic_ailments.setText("")
        self.mem_medic_ailments.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Medical Ailments", None))
        self.mem_prevGym.setText("")
        self.mem_prevGym.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Previous Gym", None))
        self.mem_BP.setText("")
        self.mem_BP.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BP  *", None))
        self.mem_physicalAct.setText("")
        self.mem_physicalAct.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Physical Activities", None))
        self.mem_weight.setText("")
        self.mem_weight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Weight  *", None))
        self.mem_height.setText("")
        self.mem_height.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Height  *", None))
        self.mem_cancelbtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.mem_savebtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.memStud_radiobtn.setText(QCoreApplication.translate("MainWindow", u"Student", None))
        self.memProf_radiobtn.setText(QCoreApplication.translate("MainWindow", u"Professional", None))
        self.memStat_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Status", None))
        self.memStat_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Single", None))
        self.memStat_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Married", None))

        self.memStat_comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.memStat_comboBox.setPlaceholderText("")
        self.memGender_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Gender", None))
        self.memGender_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.memGender_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.memGender_comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.memGender_comboBox.setPlaceholderText("")
        self.mem_DOB.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.mem_lname.setText("")
        self.mem_lname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Name  *", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"PAYMENT", None))
        self.payment_amt.setText("")
        self.payment_amt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.payment_tenderedAmt.setText("")
        self.payment_tenderedAmt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tendered Amount", None))
        self.pay_cancelbtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pay_btn.setText(QCoreApplication.translate("MainWindow", u"Pay", None))
        self.paymentServices_cmbBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Service", None))

        self.paymentServices_cmbBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Service", None))
        self.paymentServices_cmbBox.setPlaceholderText("")
        self.payment_instructor.setItemText(0, QCoreApplication.translate("MainWindow", u"Instructor", None))
        self.payment_instructor.setItemText(1, QCoreApplication.translate("MainWindow", u"None", None))

        self.payment_instructor.setCurrentText(QCoreApplication.translate("MainWindow", u"Instructor", None))
        self.payment_instructor.setPlaceholderText("")
        self.payment_memFee.setText("")
        self.payment_memFee.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Yearly Membership Fee", None))
        self.cancelDelete_mem.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.confDelete_mem.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CONFIRM DELETE", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Deleting this member will also remove all transactions associated with this member. Do you wish to proceed?", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"MONTHLY SERVICE ACCESS RENEWAL", None))
        self.renew_amt.setText("")
        self.renew_amt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.renew_tenderedAmt.setText("")
        self.renew_tenderedAmt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tendered Amount", None))
        self.renewCancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.renewPay_btn.setText(QCoreApplication.translate("MainWindow", u"Pay", None))
        self.renewService_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Service", None))

        self.renewService_comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Service", None))
        self.renewService_comboBox.setPlaceholderText("")
        self.renew_instructor.setItemText(0, QCoreApplication.translate("MainWindow", u"Instructor", None))
        self.renew_instructor.setItemText(1, QCoreApplication.translate("MainWindow", u"None", None))

        self.renew_instructor.setCurrentText(QCoreApplication.translate("MainWindow", u"Instructor", None))
        self.renew_instructor.setPlaceholderText("")
        self.addService_btn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"SERVICES", None))
        self.deleteService_btn.setText("")
        self.editService_btn.setText("")
        ___qtablewidgetitem33 = self.services_table.horizontalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem34 = self.services_table.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"TYPE", None));
        ___qtablewidgetitem35 = self.services_table.horizontalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"AMOUNT", None));
        self.services_exitbtn.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"ADD A SERVICE", None))
        self.addService_name.setText("")
        self.addService_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Service", None))
        self.addService_amount.setText("")
        self.addService_amount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.addService_savebtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.addService_cancelbtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"UPDATE A SERVICE", None))
        self.service_Update.setText("")
        self.service_Update.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Service", None))
        self.service_Amount.setText("")
        self.service_Amount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.serviceUpdate_savebtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.serviceUpdate_cancelbtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"ADD AN EMPLOYEE", None))
        self.AddEmp_fname.setText("")
        self.AddEmp_fname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name  *", None))
        self.AddEmp_contact.setText("")
        self.AddEmp_contact.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contact No.  *", None))
        self.AddEmp_address.setText("")
        self.AddEmp_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address  *", None))
        self.AddEmp_cancelbtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.AddEmp_savebtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_21.setText("")
        self.AddEmp_DOB.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.AddEmp_lname.setText("")
        self.AddEmp_lname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Name  *", None))
        self.cancelDelete_emp.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.confDelete_emp.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"CONFIRM DELETE", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Do you wish to delete this employee?", None))
        self.cancelLogout_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.confLogout_btn.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"CONFIRM LOGOUT", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Do you wish to log out?", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Successfully Recorded!", None))
        self.label_39.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Changes Saved!", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Php", None))
        self.change_field.setText("")
        self.change_okBtn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_50.setText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Must select a row.", None))
        self.cancelDelete_serv.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.confDelete_serv.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"CONFIRM DELETE", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Do you wish to delete this service?", None))
        self.cancelPay_mem.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.confPay_mem.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"CONFIRM PAYMENT", None))
        self.label_60.setText("")
        self.fieldNotice.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Please consider designating an administrator to facilitate the ongoing operations.", None))
        self.addAdminBtn.setText(QCoreApplication.translate("MainWindow", u"Add an admin", None))
        self.label_61.setText("")
        self.tenderedfieldNotice.setText(QCoreApplication.translate("MainWindow", u"Insufficient tendered amount.", None))
        self.new_notifbtn.setText(QCoreApplication.translate("MainWindow", u"    New Notifications", None))
        self.label_62.setText("")
        self.fieldNotice_2.setText(QCoreApplication.translate("MainWindow", u"Cannot delete a service associated with a membership", None))
        self.renew_mshipBtn.setText(QCoreApplication.translate("MainWindow", u"RENEW MEMBERSHIP", None))
        self.renew_monservBtn.setText(QCoreApplication.translate("MainWindow", u"RENEW MONTHLY SERVICE", None))
        self.reminder_text.setText(QCoreApplication.translate("MainWindow", u"This member's membership will expire within 7 day/s. Would you like to proceed with the monthly service access renewal or renew  membership first? ", None))
        self.exit_reminder.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"MEMBERSHIP RENEWAL", None))
        self.mem_fee.setText("")
        self.mem_fee.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Membership Fee", None))
        self.memRenew_tendered.setText("")
        self.memRenew_tendered.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tendered Amount", None))
        self.memRenew_cancelBtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.memRenew_payBtn.setText(QCoreApplication.translate("MainWindow", u"Pay", None))
        self.label_20.setText("")
        self.pushButton.setText("")
        self.cancel_assigned_emp_delete.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.conf_assigned_emp_delete.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"CONFIRM DELETE", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Deleting this employee will remove their record from the system.", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"All related entries in the service log will be set to NULL.", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Are you sure you want to proceed?", None))
    # retranslateUi

