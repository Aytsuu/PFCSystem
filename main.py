from pymongo import MongoClient
from PySide6 import QtWidgets, QtCore
from ui_loginUI import *
from ui_mainUI import *
from PySide6.QtGui import *
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading
import time


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.show()

        #LOGIN 
        # ===========================================================================================================================================================================
        
        self.ui.signInBtn.clicked.connect(self.handle_login)
        self.ui.usernameField.installEventFilter(self)
        self.ui.passwordField.installEventFilter(self)

    #Enter key clicked
    # ===========================================================================================================================================================================

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if source == self.ui.usernameField or source == self.ui.passwordField:
                key = event.key()
                if key == QtCore.Qt.Key_Return or key == QtCore.Qt.Key_Enter:
                    self.handle_login()   
                else:
                    self.ui.usernameField.setStyleSheet("border: none;")
                    self.ui.passwordField.setStyleSheet("border: none;")
        
        return False
    #Login button key clicked
    # ===========================================================================================================================================================================
    
    def handle_login(self):
        if self.ui.usernameField.text() == 'admin' and self.ui.passwordField.text() == 'adminpass':   
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
     
        else:
            self.ui.usernameField.setStyleSheet("border: 1px solid red;")
            self.ui.passwordField.setStyleSheet("border: 1px solid red;")
            

class AutoResizeTableWidget(QTableWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.verticalHeader().setDefaultSectionSize(50)  # Set a default height for the rows
        
    def resizeEvent(self, event):
        for row in range(self.rowCount()):
            self.resizeRowToContents(row)
        super().resizeEvent(event)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.database = None
        self.prev_page = 1
        self.editEmployee = False
        self.AllowOperations = False
        self.IsRenew = False
        self.IsMembership = False
        self.employeeIDList = []
        self.emp_id = None
        double_validator = QDoubleValidator(0.0, 9999.99, 2)
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        # ===========================================================================================================================================================================
        # Initialize database connection and collections
        # ===========================================================================================================================================================================
        
        self.db_connect()

        self.servicesdb = self.database.services
        self.membersdb = self.database.members
        self.employeedb = self.database.employee
        self.mon_servicelogdb = self.database.monthly_service_log
        self.transactiondb = self.database.transaction_history
        self.notificationdb = self.database.notification

        # ===========================================================================================================================================================================
        # Adding admin and check if admin exists in employees record
        # ====== =====================================================================================================================================================================

        self.adminIsExist()
        self.view_Dashboard()
        self.ui.addAdminBtn.clicked.connect(self.add_admin)

        # ===========================================================================================================================================================================
        # Threading, to execute different codes at the same time
        # ===========================================================================================================================================================================

        # Monitors the remaining days of members' monthly service access
        infinite_execution1 = threading.Thread(target=self.monitor_monServiceAccess, daemon=True)
        infinite_execution1.start()

        # Monitors the remaining days of members' membership
        infinite_execution2 = threading.Thread(target=self.monitor_membership, daemon=True)
        infinite_execution2.start()

        # Monitor if membership has expired
        infinite_execution3 = threading.Thread(target=self.delete_expiredMship, daemon=True)
        infinite_execution3.start()

        # ===========================================================================================================================================================================
        # Validor for input fields that ask for digits and/or fraction
        # ===========================================================================================================================================================================

        decimal_validator = QRegularExpressionValidator(QRegularExpression("\\d*\\.?\\d*"))
        int_validator = QRegularExpressionValidator(QRegularExpression("\\d*"))

        self.customerBPValidator = QRegularExpression("^\s*(\d{1,3})\s*[-/]\s*(\d{1,3})\s*$")
        self.emailValidator = QRegularExpression("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

        validBP = QRegularExpressionValidator(self.customerBPValidator, self.ui.regismem_BP)
        validBPUpdate = QRegularExpressionValidator(self.customerBPValidator, self.ui.mem_BP)
        
        self.ui.regismem_contact.setValidator(int_validator)
        self.ui.regismem_height.setValidator(decimal_validator)
        self.ui.regismem_weight.setValidator(decimal_validator)
        self.ui.regismem_BP.setValidator(validBP)
        self.ui.renew_tenderedAmt.setValidator(decimal_validator)
        self.ui.mem_contact.setValidator(int_validator)
        self.ui.mem_height.setValidator(decimal_validator)
        self.ui.mem_weight.setValidator(decimal_validator)
        self.ui.mem_BP.setValidator(validBPUpdate)
        self.ui.AddEmp_contact.setValidator(int_validator)
        self.ui.payment_memFee.setValidator(decimal_validator)
        self.ui.payment_tenderedAmt.setValidator(decimal_validator)
        self.ui.renew_tenderedAmt.setValidator(decimal_validator)
        self.ui.memRenew_tendered.setValidator(decimal_validator)
        self.ui.mem_fee.setValidator(decimal_validator)
        self.ui.service_Amount.setValidator(decimal_validator)
        self.ui.addService_amount.setValidator(decimal_validator)   
    
        # ===========================================================================================================================================================================
        # NOTIFICATIONS
        # ===========================================================================================================================================================================

        self.ui.notifBtn.clicked.connect(self.show_notif)
        self.ui.notif_close.clicked.connect(self.close_notif)
        
        # ===========================================================================================================================================================================
        # TABLE WIDGETS MODIFICATIONS
        # ===========================================================================================================================================================================

        #Resizing the columns to fit the table width
        self.ui.mem_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.mon_serviceLog_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.mshipStat_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.transac_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.services_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.emp_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.notif_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.newMem_dashboard.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.notif_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.ui.notif_table.setColumnWidth(0, 450)


        #Remove outline on selecting a row/item
        self.ui.mem_table.setFocusPolicy(Qt.NoFocus)
        self.ui.mon_serviceLog_table.setFocusPolicy(Qt.NoFocus)
        self.ui.mshipStat_table.setFocusPolicy(Qt.NoFocus)
        self.ui.transac_table.setFocusPolicy(Qt.NoFocus)
        self.ui.services_table.setFocusPolicy(Qt.NoFocus)
        self.ui.emp_table.setFocusPolicy(Qt.NoFocus)
        self.ui.notif_table.setFocusPolicy(Qt.NoFocus)
        self.ui.newMem_dashboard.setFocusPolicy(Qt.NoFocus)

        #remove vertical headers
        self.ui.emp_table.verticalHeader().setVisible(False)
        self.ui.transac_table.verticalHeader().setVisible(False)
        self.ui.mon_serviceLog_table.verticalHeader().setVisible(False)
        self.ui.mshipStat_table.verticalHeader().setVisible(False)
        self.ui.mem_table.verticalHeader().setVisible(False)
        self.ui.services_table.verticalHeader().setVisible(False)
        self.ui.notif_table.verticalHeader().setVisible(False)
        self.ui.newMem_dashboard.verticalHeader().setVisible(False)

        self.ui.notif_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.notif_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # ===========================================================================================================================================================================
        # MENU method calling
        # ===========================================================================================================================================================================

        self.ui.menu_container.setCurrentWidget(self.ui.home_page)
        self.ui.home.setStyleSheet("background-color: rgba(255,255,255,50)")
        self.ui.home.clicked.connect(self.select_home)
        self.ui.mem_list.clicked.connect(self.select_memlist)
        self.ui.mon_serv_log.clicked.connect(self.select_monServiceLog)
        self.ui.mem_status.clicked.connect(self.select_mshipStat)
        self.ui.transaction.clicked.connect(self.select_transact)
        self.ui.employees.clicked.connect(self.select_employees)
        self.ui.services.clicked.connect(self.service_popup)

        # ===========================================================================================================================================================================
        # LOGOUT method calling
        # ===========================================================================================================================================================================

        self.ui.services_exitbtn.clicked.connect(self.close_service_popup)
        self.ui.logout.clicked.connect(self.logoutpopup)
        self.ui.confLogout_btn.clicked.connect(self.confirm_logout)
        self.ui.cancelLogout_btn.clicked.connect(self.cancel_logout)

        # ===========================================================================================================================================================================
        # Dashboard method calling
        # ===========================================================================================================================================================================
            
        self.show_dashboard_data()

        # ===========================================================================================================================================================================
        # SERVICES method calling
        # ===========================================================================================================================================================================

        self.ui.addService_btn.clicked.connect(self.add_service)
        self.ui.addService_cancelbtn.clicked.connect(self.cancel_add_service)
        self.ui.editService_btn.clicked.connect(self.edit_service)
        self.ui.serviceUpdate_cancelbtn.clicked.connect(self.cancel_edit_service)
        self.ui.addService_savebtn.clicked.connect(self.check_add_service_fields)
        self.ui.serviceUpdate_savebtn.clicked.connect(self.check_update_service_fields)
        self.ui.deleteService_btn.clicked.connect(self.delete_service)
        self.ui.confDelete_serv.clicked.connect(self.confirm_delete_service)
        self.ui.cancelDelete_serv.clicked.connect(self.cancel_delete_service)
        self.ui.addService_amount.setValidator(double_validator)

        # ===========================================================================================================================================================================
        # RENEW MONTHLY SERVICE ACCESS method calling
        # ===========================================================================================================================================================================

        self.ui.renew_btn.clicked.connect(self.renew_popup)
        self.retrieve_employee_from_DB()
        self.retrieve_employee_from_DB_renew()
        self.ui.renewCancel_btn.clicked.connect(self.cancel_renew)
        self.ui.renewPay_btn.clicked.connect(self.check_renew_fields)
        self.ui.renewService_comboBox.currentTextChanged.connect(self.update_renewPay_amount)
        self.ui.renew_instructor.activated.connect(self.get_EmployeeIndex)
        self.ui.renew_monservBtn.clicked.connect(lambda: (self.ui.renew_popup.setFixedWidth(1381),self.ui.renewal_reminder_popup.setFixedWidth(0)))
        self.ui.renew_mshipBtn.clicked.connect(lambda: (self.ui.membership_renewal_popup.setFixedWidth(1381), self.ui.renewal_reminder_popup.setFixedWidth(0), self.ui.mem_fee.setEnabled(True), self.ui.memRenew_tendered.setEnabled(True)))
        self.ui.memRenew_cancelBtn.clicked.connect(lambda: (self.ui.membership_renewal_popup.setFixedWidth(0), self.ui.mem_fee.setText(''), self.ui.memRenew_tendered.setText('')))
        self.ui.memRenew_payBtn.clicked.connect(self.check_memRenew_fields)
        self.ui.exit_reminder.clicked.connect(lambda: self.ui.renewal_reminder_popup.setFixedWidth(0))
        
        # ===========================================================================================================================================================================
        # REGISTER MEMBER method calling
        # ===========================================================================================================================================================================

        self.ui.add_member.clicked.connect(self.add_member)
        self.ui.regismem_cancelbtn.clicked.connect(self.regis_cancel)
        self.ui.regismem_savebtn.clicked.connect(self.check_add_member_fields)
        self.ui.pay_cancelbtn.clicked.connect(self.cancel_payment)
        self.ui.pay_btn.clicked.connect(self.check_payment_fields)
        self.ui.confPay_mem.clicked.connect(self.confirm_RegisterOrRenew)
        self.ui.cancelPay_mem.clicked.connect(self.cancel_payment_conf)
        self.retrieve_services_from_DB()
        self.ui.paymentServices_cmbBox.currentTextChanged.connect(self.update_payment_amount)
        self.ui.payment_instructor.activated.connect(self.get_EmployeeIndex)
        self.ui.change_okBtn.clicked.connect(lambda: self.ui.change_popup.setFixedWidth(0))

        # ===========================================================================================================================================================================
        # DELETE MEMBER method calling
        # ===========================================================================================================================================================================

        self.ui.delete_member.clicked.connect(self.delete_member)
        self.ui.cancelDelete_mem.clicked.connect(self.cancel_delete_mem)
        self.ui.confDelete_mem.clicked.connect(self.confirm_delete_mem)

        # ===========================================================================================================================================================================
        # EDIT MEMBER DETAILS method calling
        # ===========================================================================================================================================================================
        
        self.ui.edit_member.clicked.connect(self.edit_member)
        self.ui.mem_cancelbtn.clicked.connect(self.cancel_edit_mem)
        self.ui.mem_savebtn.clicked.connect(self.check_edit_member_fields)
        
        # ===========================================================================================================================================================================
        # VIEW MEMBER DETAILS method calling
        #===========================================================================================================================================================================
        self.ui.mem_table.cellDoubleClicked.connect(self.select_row_to_view)
        self.ui.viewmem_backbtn.clicked.connect(self.close_view)

        # ===========================================================================================================================================================================
        # TRANSACTION HISTORY method calling
        # ===========================================================================================================================================================================

        self.populate_transact_table()
        self.ui.transac_search.textChanged.connect(self.transaction_search)

        # ===========================================================================================================================================================================
        # EMPLOYEE method calling
        # ===========================================================================================================================================================================
  
        self.ui.add_employee.clicked.connect(self.add_employee)
        self.ui.AddEmp_cancelbtn.clicked.connect(self.cancel_add_employee)
        self.ui.edit_employee.clicked.connect(self.edit_employee)
        self.ui.AddEmp_savebtn.clicked.connect(self.check_add_employee_fields)   
        self.ui.delete_employee.clicked.connect(self.delete_emp)
        self.ui.conf_assigned_emp_delete.clicked.connect(self.confirm_delete_employee)
        self.ui.cancel_assigned_emp_delete.clicked.connect(self.cancel_assigned_emp_delete)
        self.ui.confDelete_emp.clicked.connect(self.confirm_delete_employee)
        self.ui.cancelDelete_emp.clicked.connect(self.cancel_delete_employee)
        self.ui.emp_search.textChanged.connect(self.employee_search)

    # ===========================================================================================================================================================================
    # MongoDB Connection 
    # ===========================================================================================================================================================================

    def db_connect(self):
        client = MongoClient("localhost", 27017)
        self.database = client.PFCsystemDB

    # ===========================================================================================================================================================================
    # Table selection 
    # ===========================================================================================================================================================================

    def mousePressEvent(self, event):

        pos = event.position().toPoint() 

        # Convert the global position to the widget's coordinate system
        widget_pos = self.mapFromGlobal(self.mapToGlobal(pos))

        # Check if the click is outside the table
        if (
            not self.ui.mem_table.geometry().contains(widget_pos) or
            not self.ui.mon_serviceLog_table.geometry().contains(widget_pos) or
            not self.ui.mshipStat_table.geometry().contains(widget_pos) or
            not self.ui.transac_table.geometry().contains(widget_pos) or
            not self.ui.services_table.geometry().contains(widget_pos) or
            not self.ui.emp_table.geometry().contains(widget_pos) or
            not self.ui.notif_table.geometry().contains(widget_pos)
        ):            
            self.ui.mem_table.clearSelection()
            self.ui.mon_serviceLog_table.clearSelection()
            self.ui.mshipStat_table.clearSelection()
            self.ui.transac_table.clearSelection()
            self.ui.services_table.clearSelection()
            self.ui.emp_table.clearSelection()
            self.ui.notif_table.clearSelection()

        # Call the base class implementation
        super().mousePressEvent(event)

    # ===========================================================================================================================================================================
    # Menu bar selection
    # ===========================================================================================================================================================================
    
    def select_home(self):
        self.ui.menu_container.setCurrentWidget(self.ui.home_page)
        self.ui.home.setStyleSheet("QPushButton{background-color: rgba(255,255,255,50)}")
        self.ui.mem_list.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.mon_serv_log.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.mem_status.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.transaction.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.services.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.employees.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.previous(1)
        self.show_dashboard_data()
        self.view_Dashboard()
        
    def select_memlist(self):
        self.ui.menu_container.setCurrentWidget(self.ui.member_list_page)
        self.ui.home.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.mem_list.setStyleSheet("QPushButton{background-color: rgba(255,255,255,50)}")
        self.ui.mem_status.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.mon_serv_log.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.transaction.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.services.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.employees.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.previous(2)
        self.populate_mem_table()
        self.ui.mem_search.textChanged.connect(self.member_search)
        
    def select_monServiceLog(self):
        self.ui.menu_container.setCurrentWidget(self.ui.mon_serviceLog_page)
        self.ui.home.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.mem_list.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.mon_serv_log.setStyleSheet("QPushButton{background-color: rgba(255,255,255,50)}")
        self.ui.mem_status.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.transaction.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.services.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.employees.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.previous(3)
        self.populate_monServiceLog()
        self.ui.mon_serviceLog_search.textChanged.connect(self.monServiceLog_search)

    def select_mshipStat(self):
        self.ui.menu_container.setCurrentWidget(self.ui.memship_status_page)
        self.ui.home.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.mem_list.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.mon_serv_log.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.mem_status.setStyleSheet("QPushButton{background-color: rgba(255,255,255,50)}")
        self.ui.transaction.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.services.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.employees.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.previous(4)
        self.populate_mshipStat()
        self.ui.mshipStat_search.textChanged.connect(self.mshipStat_search)
    
    def select_transact(self):
        self.ui.menu_container.setCurrentWidget(self.ui.transaction_page)
        self.populate_transact_table()
        self.ui.home.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.mem_list.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.mon_serv_log.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.mem_status.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.transaction.setStyleSheet("QPushButton{background-color: rgba(255,255,255,50)}")
        self.ui.services.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.employees.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.previous(5)
    
    def select_employees(self):
        self.ui.menu_container.setCurrentWidget(self.ui.employees_page)
        self.ui.home.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.mem_list.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.mon_serv_log.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.mem_status.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.transaction.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.services.setStyleSheet("QPushButton{background-color: none} QPushButton:hover{background-color: rgba(255,255,255,50);}")
        self.ui.employees.setStyleSheet("QPushButton{background-color: rgba(255,255,255,50)}")
        self.previous(6)
        self.populate_employee_table()

    # ===========================================================================================================================================================================
    # Check if employee record has admin 
    # ===========================================================================================================================================================================
    
    def adminIsExist(self):
        check_admin = {"position": "ADMINISTRATOR"}
        admin_data = self.employeedb.count_documents(check_admin)
    
        if admin_data != 0:
            self.AllowOperations = True
        else:
            self.ui.addAdmin_notice.setFixedWidth(1361)

    # ===========================================================================================================================================================================
    # Previous Page
    # ===========================================================================================================================================================================

    def previous(self,page):
        self.prev_page = page


    # ===========================================================================================================================================================================
    # Dashboard menu functions
    # ===========================================================================================================================================================================

    def show_dashboard_data(self):
        self.total_members()

    def total_members(self):

        pipeline = [
            {
                "$project" : {
                    "_id" : 1,
                    "first name": 1,
                    "last name" : 1,
                    "start date" : {
                        "$dateToString" : {
                            "format" : "%Y-%m-%d",
                            "date" : {
                                "$toDate": {
                                    "$substr": [ "$start date", 0, 10 ] # Extracting the first 19 characters (yyyy-MM-dd)
                                }
                            }
                        }
                    }
                }
            },
            {
                "$match" : {
                    "start date" : {"$eq" : str(datetime.date.today())}
                }
            }   
        ]

        new_members = list(self.membersdb.aggregate(pipeline))

        self.ui.total_newMem.setText(str(len(new_members)))

        self.ui.newMem_dashboard.setRowCount(0)
        for row_number, new_member in enumerate(new_members):
            self.ui.newMem_dashboard.insertRow(row_number)
            for column_number, data in enumerate(new_member):
                item = QtWidgets.QTableWidgetItem(str(new_member[data]))
                item.setTextAlignment(Qt.AlignHCenter)
                self.ui.newMem_dashboard.setItem(row_number, column_number, item)

    # ===========================================================================================================================================================================
    # Services menu functions
    # ===========================================================================================================================================================================

    #Validate add service fields
    def check_add_service_fields(self):
        if not self.ui.addService_name.text() or not self.ui.addService_amount.text():
            self.ui.fieldNotice.setText('Please add data in all fields.')
            self.ui.invalid_notice.setFixedWidth(391)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 
        else:
            if float(self.ui.addService_amount.text()) < 1.00:
                self.ui.fieldNotice.setText('Invalid service amount.')
                self.ui.invalid_notice.setFixedWidth(391)
                QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 
            else:
                self.add_service_into_DB()

    #Validate update service fields
    def check_update_service_fields(self):
        if not self.ui.service_Update.text() or not self.ui.service_Amount.text():
            self.ui.fieldNotice.setText('Please add data in all fields.')
            self.ui.invalid_notice.setFixedWidth(391)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 
        else:
            if float(self.ui.service_Amount.text()) < 1.00:
                self.ui.fieldNotice.setText('Invalid service amount.')
                self.ui.invalid_notice.setFixedWidth(391)
                QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 
            else:
                self.update_service()

    #Service menu selection
    def service_popup(self):

        #Highlights the service in menu bar 
        self.ui.services_popup.setFixedWidth(1381)  
        self.ui.home.setStyleSheet("background-color: none") 
        self.ui.mem_list.setStyleSheet("background-color: none")
        self.ui.mon_serv_log.setStyleSheet("background-color: none")
        self.ui.mem_status.setStyleSheet("background-color: none")
        self.ui.transaction.setStyleSheet("background-color: none")
        self.ui.services.setStyleSheet("background-color: rgba(255,255,255,50)")
        self.ui.employees.setStyleSheet("background-color: none")
        self.populate_services_table()
        
    #Closing services
    def close_service_popup(self):
        self.ui.services_popup.setFixedWidth(0)   
        self.ui.services.setStyleSheet("background-color: none")
        if self.prev_page == 1: self.select_home()
        elif self.prev_page == 2: self.select_memlist()
        elif self.prev_page == 3: self.select_monServiceLog()
        elif self.prev_page == 4: self.select_mshipStat()
        elif self.prev_page == 5: self.select_transact()
        elif self.prev_page == 6: self.select_employees()

    #Add service popup
    def add_service(self):
        if self.AllowOperations == True:
            self.ui.services_widget.setFixedWidth(0)  
            self.ui.add_service_widget.setFixedWidth(701) 
        else:
            self.ui.addAdmin_notice.setFixedWidth(0)
            QtCore.QTimer.singleShot(40, lambda: self.ui.addAdmin_notice.setFixedWidth(1361))        

    #Cancel add service
    def cancel_add_service(self):
        self.ui.services_widget.setFixedWidth(701)  
        self.ui.add_service_widget.setFixedWidth(0)  
        self.ui.addService_name.setText('')
        self.ui.addService_amount.setText('')

    #Edit service popup
    def edit_service(self):
        selected_row = -1
        if len(self.ui.services_table.selectedItems()) > 0:
            selected_row = self.ui.services_table.currentRow()

        if selected_row != -1:
            self.ui.services_widget.setFixedWidth(0)  
            self.ui.update_service_widget.setFixedWidth(701)  
            service_type = self.ui.services_table.item(selected_row, 1).text()
            service_price = self.ui.services_table.item(selected_row,2).text()

            self.ui.service_Update.setText(str(service_type))
            self.ui.service_Amount.setText(str(service_price))
        else:
            self.ui.rowSelection_notice.setFixedWidth(301)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.rowSelection_notice.setFixedWidth(0))  

    #Update service in DB
    def update_service(self):
        serv_id = self.ui.services_table.item(self.ui.services_table.currentRow(), 0).text()
        serv_type = self.ui.service_Update.text().upper()
        serv_price = float(self.ui.service_Amount.text())

        is_service_exist = self.servicesdb.find_one({"type" : serv_type})

        if is_service_exist is None or (is_service_exist is not None and is_service_exist['_id'] == int(serv_id)):
            update_service = {
                "$set" : {
                    "type" : serv_type,
                    "price" : serv_price
                }
            }

            result = self.servicesdb.update_one({"_id" : int(serv_id)}, update_service)

            if result:
                self.ui.services_widget.setFixedWidth(701)
                self.ui.update_service_widget.setFixedWidth(0) 
                self.ui.service_Update.setText('')
                self.ui.service_Amount.setText('')
                self.retrieve_services_from_DB()
                self.populate_services_table()
        else:
            self.ui.fieldNotice.setText('Service already exists.')
            self.ui.invalid_notice.setFixedWidth(391)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 

    #Cancel deleting a service
    def cancel_delete_service(self):
        self.ui.service_delete_popup.setFixedWidth(0)
        self.ui.services_popup.setFixedWidth(1381)

    #Delete confirmation for service deletion
    def delete_service(self):

        if len(self.ui.services_table.selectedItems()) > 0:
            self.ui.service_delete_popup.setFixedWidth(1381)
            self.ui.services_popup.setFixedWidth(0)
        else:
            self.ui.rowSelection_notice.setFixedWidth(301)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.rowSelection_notice.setFixedWidth(0))  
    
    #Confirm deletion of a service
    def confirm_delete_service(self):
        selected_row = -1

        if len(self.ui.services_table.selectedItems()) > 0:
            selected_row = self.ui.services_table.currentRow()

        if selected_row != -1:
            serv_id = self.ui.services_table.item(selected_row, 0)
            serv_type = self.ui.services_table.item(selected_row, 1).text()
            is_service_used = self.mon_servicelogdb.count_documents({'service type': serv_type})
            
            if is_service_used == 0:
                result = self.servicesdb.delete_one({"_id" : int(serv_id.text())})

                if result:
                    self.ui.services_table.removeRow(selected_row)
                    self.retrieve_services_from_DB()
                    self.populate_services_table()
                    self.ui.delete_notif.setFixedWidth(81)
                    QtCore.QTimer.singleShot(1300, lambda: self.ui.delete_notif.setFixedWidth(0)) 
                
            else:
                self.ui.fieldNotice.setText('Unable to delete: Service in use.')
                self.ui.invalid_notice.setFixedWidth(391)
                QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 

        self.ui.service_delete_popup.setFixedWidth(0)
        self.ui.services_popup.setFixedWidth(1381)
        
    #Cancel edit service
    def cancel_edit_service(self):
        self.ui.services_widget.setFixedWidth(701)  
        self.ui.update_service_widget.setFixedWidth(0)  
      

    def add_service_into_DB(self):
        serv_type = self.ui.addService_name.text().upper()
        serv_price = float(self.ui.addService_amount.text())

        is_service_exist = self.servicesdb.count_documents({"type" : serv_type})

        if is_service_exist == 0:
            last_serviceid = next(self.servicesdb.find().sort("_id", -1).limit(1),{}).get('_id',None)
            serv_id = int(last_serviceid) + 1 if last_serviceid is not None else 0

            service = {
                "_id" : serv_id,
                "type" : serv_type,
                "price" : serv_price
            }
            
            result = self.servicesdb.insert_one(service)
            
            if result:
                self.ui.success_widget.setFixedWidth(371)
                QtCore.QTimer.singleShot(1300, lambda: self.ui.success_widget.setFixedWidth(0))   

                #clears text fields
                self.ui.services_widget.setFixedWidth(701)  
                self.ui.add_service_widget.setFixedWidth(0)
                self.ui.addService_name.setText('')
                self.ui.addService_amount.setText('')
                self.retrieve_services_from_DB()
                self.populate_services_table()
        else: 

            self.ui.fieldNotice.setText('Service already exists.')
            self.ui.invalid_notice.setFixedWidth(391)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 
                
    #Display all services in the table
    def populate_services_table(self):    
        self.ui.services_table.setRowCount(0)
        result = self.servicesdb.find()

        for row_number, service in enumerate(result):
            self.ui.services_table.insertRow(row_number)
            for column_number, data in enumerate(service):
                item = QtWidgets.QTableWidgetItem(str(service[data]))
                item.setTextAlignment(Qt.AlignHCenter)
                self.ui.services_table.setItem(row_number, column_number, item)
    
    #Displaying services in the combo box, for registration and renewal of monthly service access
    def retrieve_services_from_DB(self):
        
        services = self.servicesdb.find()
        self.ui.paymentServices_cmbBox.clear()
        self.ui.paymentServices_cmbBox.addItem('Service')
        for service in services:
            service_type = service['type']
            self.ui.paymentServices_cmbBox.addItem(service_type)
            self.ui.renewService_comboBox.addItem(service_type)

    # =========================================================================================================================================================================== 
    # Monthly Service Log menu functions 
    # ===========================================================================================================================================================================

    #Automatically displays the cost of a service during payment
    def update_renewPay_amount(self):
        servicename = self.ui.renewService_comboBox.currentText()
        service_id, serv_price = self.get_service_id(servicename)

        if serv_price is not None:
            self.ui.renew_amt.setText(str(serv_price))
        else:
            self.ui.renew_amt.setText('')
    
    #Functional search bar
    def monServiceLog_search(self):
        text = self.ui.mon_serviceLog_search.text().lower()  
        for row in range(self.ui.mon_serviceLog_table.rowCount()):
            row_hidden = True
            for col in range(self.ui.mon_serviceLog_table.columnCount()):
                item = self.ui.mon_serviceLog_table.item(row, col)
                if item and text in item.text().lower():  
                    row_hidden = False
                    break
            self.ui.mon_serviceLog_table.setRowHidden(row, row_hidden) 

    #Functional search bar
    def mshipStat_search(self):
        text = self.ui.mshipStat_search.text().lower()  
        for row in range(self.ui.mshipStat_table.rowCount()):
            row_hidden = True
            for col in range(self.ui.mshipStat_table.columnCount()):
                item = self.ui.mshipStat_table.item(row, col)
                if item and text in item.text().lower():  
                    row_hidden = False
                    break
            self.ui.mshipStat_table.setRowHidden(row, row_hidden) 
    
    #Validating renew input fields
    def check_renew_fields(self):
        if(self.ui.renew_instructor.currentText() == 'Instructor' or
            self.ui.renewService_comboBox.currentText() == 'Service' or
            not self.ui.renew_amt.text() or
            not self.ui.renew_tenderedAmt.text()):

            self.ui.fieldNotice.setText('All fields must be filled.')
            self.ui.invalid_notice.setFixedWidth(391)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0))  

        else:
            tenderedAmt =  float(self.ui.renew_tenderedAmt.text())
            if tenderedAmt < (float(self.ui.renew_amt.text())):
                self.ui.tenderedAmt_notice.setFixedWidth(391)
                QtCore.QTimer.singleShot(1300, lambda: self.ui.tenderedAmt_notice.setFixedWidth(0))  
            else:
                self.confirm_payment_conf()
    
    #Displaying instructors in the combo box
    def retrieve_employee_from_DB_renew(self):
        self.employeeIDList = []
       
        employees = self.employeedb.find({"position" : "INSTRUCTOR"})

        if employees:
            self.ui.renew_instructor.clear()
            self.ui.renew_instructor.addItem('Instructor')
            self.employeeIDList.append(None)
            for employee in employees:
                emp_id = employee['_id']
                emp_name = employee['fname'] + " " + employee['lname']
                self.ui.renew_instructor.addItem(emp_name)
                self.employeeIDList.append(emp_id)
            self.ui.renew_instructor.addItem('None')
            self.employeeIDList.append(None)

    #Shows renew page
    def renew_popup(self):
        selected_row = -1

        if len(self.ui.mon_serviceLog_table.selectedItems()) > 0:
            selected_row = self.ui.mon_serviceLog_table.currentRow()

        if selected_row != -1:
            if self.ui.mon_serviceLog_table.item(selected_row, 7).text() == 'EXPIRED': 
                self.IsRenew = True
                self.check_before_monthly_renewal()
            else:
                self.ui.fieldNotice.setText('Cannot renew if status is active.')
                self.ui.invalid_notice.setFixedWidth(391)
                QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 

        else:
            self.ui.rowSelection_notice.setFixedWidth(301)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.rowSelection_notice.setFixedWidth(0))  
            

    def check_before_monthly_renewal(self):
        selected_row = self.ui.mon_serviceLog_table.currentRow()
        if selected_row != -1:
            monserv_id = self.ui.mon_serviceLog_table.item(selected_row, 0).text()
            expiry = self.mon_servicelogdb.find_one({"_id": int(monserv_id)})
            membership_exp = datetime.datetime.strptime((str(expiry['end date']).split(" ")[0]), "%Y-%m-%d").date()

            if membership_exp:
                today = datetime.datetime.today().date()
                remaining_days = (membership_exp - today).days
                if remaining_days < 30 and remaining_days > 0:
                    self.ui.reminder_text.setText(f"This member's membership will expire within {remaining_days} day/s. Would you like to proceed with the monthly service access renewal or renew membership first?")
                    self.ui.renewal_reminder_popup.setFixedWidth(1381)   
                else:
                    self.ui.renew_popup.setFixedWidth(1381)  

                

    #Cancel renew
    def cancel_renew(self):
        self.ui.renew_popup.setFixedWidth(0)

    #Confirm renew of monthly service access
    def pay_renew(self):
        servicename = self.ui.renewService_comboBox.currentText()
        service_id ,serv_price= self.get_service_id(servicename)
        renew_amt = self.ui.renew_amt.text()
        renew_tendered = self.ui.renew_tenderedAmt.text()
        selected_row = self.ui.mon_serviceLog_table.currentRow()
        monserv_id = self.ui.mon_serviceLog_table.item(selected_row, 0).text()
        mon_id = monserv_id

        
        service_type = self.servicesdb.find_one({"_id" : service_id})['type']

        renew_monthly = {
            "$set" : {
                "service type": service_type,
                "employee id": self.emp_id,
                "start date": str(datetime.datetime.today()),
                "end date": str(datetime.datetime.today() + datetime.timedelta(days=30))
            }
        }

        result = self.mon_servicelogdb.update_one({'_id' : int(mon_id)}, renew_monthly)

        if result.modified_count > 0:
            self.ui.savechanges_widget.setFixedWidth(341)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.savechanges_widget.setFixedWidth(0)) 
            self.ui.renew_popup.setFixedWidth(0)
            self.populate_monServiceLog()

            mem_contact = self.membersdb.find_one({"_id" : int(mon_id)})['contact']

            self.add_transaction_DB(service_id, renew_amt, renew_tendered, mem_contact)

            if float(renew_tendered) >= float(renew_amt):
                self.ui.change_popup.setFixedWidth(1381)
                change = float(renew_tendered) - float(renew_amt)
                self.ui.change_field.setText(f"{change:.2f}")
                self.populate_monServiceLog()
                member = self.membersdb.find_one({"_id": int(monserv_id)})
                #--------------Email for Member------------------
                email_text = f"""
                <html>
                <body style="font-family: Arial, sans-serif; color: #333; background-color: #f4f4f4; margin: 0; padding: 0;">
                <div style="background-color: #ffffff; margin: 20px auto; width: 90%; max-width: 600px; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                    <h2 style="color: #1E90FF; text-align: left; margin-bottom: 20px;">Hi {member['first name']},</h2>
                    <p style="line-height: 1.6; font-size: 16px; text-align: center;">Thank you for renewing your membership with <strong>People Fitness Center</strong>!</p>
                    <p style="line-height: 1.6; font-size: 16px;">We're excited to let you know that your monthly service access has been successfully renewed. We're thrilled to continue supporting you in achieving your fitness goals!</p>
                    <p style="line-height: 1.6; font-size: 16px;">If you have any questions or need assistance, feel free to reach out. We're here to help and ensure you have the best experience possible.</p>
                    <p style="line-height: 1.6; font-size: 16px;">Thanks again for being a valued member of People Fitness Center. We look forward to seeing you in the gym soon!</p>
                    <br>
                    <div style="text-align: center;"> 
                    <img src="https://drive.google.com/uc?export=view&id=1Am6E_LO5laC9XbiEQOoDtmZD_F4aOlU5" alt="Welcome Image" width="150" height="150"/>
                    </div>
                    <h3 style="text-align: center; font-size: 18px; color: #333; margin-top: 20px;">People Fitness Center</h3>
                </div>
                </body>
                </html>
                """
                email_subject = 'Your Monthly Service Access Has Been Renewed!'
                self.send_email(member['email'].lower(), email_text, email_subject)

                if self.emp_id is not None:
                    instructor_members = list(self. mon_servicelogdb.find({'employee id': self.emp_id}))
                    instructor = self.employeedb.find_one({'_id': self.emp_id})
                    member_list = ''.join([f'<li>{member["member_fname"]} {member["member_lname"] }</li>' for member in instructor_members])
                
                    #----------Email for Instructor-------------------
                    instructor_text = f"""
                    <html>
                    <body style="font-family: Arial, sans-serif; color: #333; background-color: #f4f4f4; margin: 0; padding: 0;">
                    <div style="background-color: #ffffff; margin: 20px auto; width: 90%; max-width: 600px; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                    <h2 style="color: #1E90FF; text-align: left; margin-bottom: 20px;">Hi {instructor['fname']},</h2>
                        <p style="line-height: 1.6; font-size: 16px; text-align: center;">We hope you're doing well!</p>
                        <p style="line-height: 1.6; font-size: 16px;">We are excited to inform you that a new member has been assigned to you. Below is the updated list of members you will be working with:</p>
                        <ul style="font-size: 16px; line-height: 1.6;">
                        {member_list} 
                        </ul>
                    <p style="line-height: 1.6; font-size: 16px;">Please make sure to provide them with the necessary guidance and support. If you have any questions or need assistance, feel free to reach out.</p>
                    <p style="line-height: 1.6; font-size: 16px;">We look forward to a productive session together. Thanks for your continued dedication and support!</p>
                    <br>
                    <div style="text-align: center;">
                    <img src="https://drive.google.com/uc?export=view&id=1Am6E_LO5laC9XbiEQOoDtmZD_F4aOlU5" alt="Welcome Image" width="150" height="150"/>
                    </div>
                    <h3 style="text-align: center; font-size: 18px; color: #333; margin-top: 20px;">People Fitness Center</h3>
                    </div>
                    </body>
                    </html>
                    """
                    instructor_subject = "A New Member Is Assigned To You"  
                    self.send_email(instructor['email'].lower(), instructor_text, instructor_subject)

            self.ui.renew_popup.setFixedWidth(0) 

    #Displaying all members with monthly service access
    def populate_monServiceLog(self):

        now = datetime.datetime.today()
        result = self.mon_servicelogdb.find()
        self.ui.mon_serviceLog_table.setRowCount(0)


        if result:
            for row_number, log in enumerate(result):
                    self.ui.mon_serviceLog_table.insertRow(row_number)
                    for column_number, (key, data) in enumerate(log.items()):
                        if key == 'end date':
                            if str(now) < data: 
                                item = QtWidgets.QTableWidgetItem('ACTIVE')
                                item.setTextAlignment(Qt.AlignHCenter)
                                self.ui.mon_serviceLog_table.setItem(row_number, 7, item)
                            else:
                                item = QtWidgets.QTableWidgetItem('EXPIRED')
                                item.setTextAlignment(Qt.AlignHCenter)
                                self.ui.mon_serviceLog_table.setItem(row_number, 7, item)
                        
                        if column_number in [5, 6]:
                            data = str(log[key]).split(" ")[0]

                        if column_number == 4:
                            if log[key] is not None:
                                result = self.employeedb.find_one({"_id" : log[key]})
                                data = result['fname'] + ' ' + result['lname']
                            else: data = 'NONE'

                        item = QtWidgets.QTableWidgetItem(data if column_number in [4, 5, 6] else str(log[key]))
                        item.setTextAlignment(Qt.AlignHCenter)
                        self.ui.mon_serviceLog_table.setItem(row_number, column_number, item)
    
    def check_memRenew_fields(self):
        if( not self.ui.mem_fee.text() or
            not self.ui.memRenew_tendered.text()):

            self.ui.fieldNotice.setText('All fields must be filled.')
            self.ui.invalid_notice.setFixedWidth(391)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0))  

        else:
            tenderedAmt =  float(self.ui.memRenew_tendered.text())
            if tenderedAmt < (float(self.ui.mem_fee.text())):
                self.ui.tenderedAmt_notice.setFixedWidth(391)
                QtCore.QTimer.singleShot(1300, lambda: self.ui.tenderedAmt_notice.setFixedWidth(0))  
            else:
                self.confirm_payment_conf()

    #Confirm renew of membership
    def pay_mshipRenew(self):
        mship_fee = self.ui.mem_fee.text()
        mshipRenew_tendered = self.ui.memRenew_tendered.text()
        selected_row = self.ui.mon_serviceLog_table.currentRow()
        monservId = self.ui.mon_serviceLog_table.item(selected_row, 0)
        mon_id = monservId.text()

        renew_membership = {
            "$set" : {
                "start date" : str(datetime.datetime.today()),
                "end date" : str(datetime.datetime.today() + datetime.timedelta(days=365))
            }
        }

        membership = self.membersdb.update_one({"_id" : int(mon_id)}, renew_membership)

        if membership.modified_count > 0:
            self.ui.savechanges_widget.setFixedWidth(341)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.savechanges_widget.setFixedWidth(0)) 
            self.ui.renew_popup.setFixedWidth(0)

            mem_contact = self.membersdb.find_one({"_id" : int(mon_id)})['contact']

            if mem_contact:
                self.add_transaction_DB(None, mship_fee, mshipRenew_tendered, mem_contact)

                if float(mshipRenew_tendered) > float(mship_fee):
                    self.ui.change_popup.setFixedWidth(1381)
                    change = float(mshipRenew_tendered) - float(mship_fee)
                    self.ui.change_field.setText(f"{change:.2f}")
                    self.populate_monServiceLog()
                self.ui.membership_renewal_popup.setFixedWidth(0) 


    #Display details of all membership
    def populate_mshipStat(self):

        selected_collection = {
            '_id': 1,
            'first name': 1,
            'last name': 1,
            'start date': 1,
            'end date': 1
        }
        
        memshipstat = self.membersdb.find({},selected_collection)
        self.ui.mshipStat_table.setRowCount(0)

        for row_number, member in enumerate(memshipstat):
            self.ui.mshipStat_table.insertRow(row_number)
            for col_number, data in enumerate(member):

                if col_number in [3, 4]:
                    data = str(member[data]).split(" ")[0]

                item = QtWidgets.QTableWidgetItem(data if col_number in [3,4] else str(member[data]))
                item.setTextAlignment(Qt.AlignHCenter)
                self.ui.mshipStat_table.setItem(row_number,col_number,item)

    # ===========================================================================================================================================================================
    # List of member functions 
    # ===========================================================================================================================================================================
    
    #Getting the ID of the selected instructor during payment and renew
    def get_EmployeeIndex(self, index):

        self.emp_id = self.employeeIDList[index]
    
    #Confirmation whether to proceed with the register and/or renew payment
    def confirm_RegisterOrRenew(self):
        self.ui.confirm_pay_widget.setFixedWidth(0)
        if self.IsRenew == False:
            self.add_member_into_DB()
        else:
            if self.ui.renew_popup.width() > 0:
                self.pay_renew()
            else:
                self.pay_mshipRenew()

        self.record_done()

    #Functional search bar
    def member_search(self):
        text = self.ui.mem_search.text().lower()  
        for row in range(self.ui.mem_table.rowCount()):
            row_hidden = True
            for col in range(self.ui.mem_table.columnCount()):
                item = self.ui.mem_table.item(row, col)
                if item and text in item.text().lower(): 
                    row_hidden = False
                    break
            self.ui.mem_table.setRowHidden(row, row_hidden)  
    
    #Closing member details view
    def close_view(self):
        self.ui.view_details_popup.setFixedWidth(0)
    
    #Viewing a member's details function
    def select_row_to_view(self):
        self.ui.view_details_popup.setFixedWidth(1381)
        selected_row = self.ui.mem_table.currentRow()
        if selected_row != -1:
            mem_id = self.ui.mem_table.item(selected_row, 0)

            member = self.membersdb.find_one({"_id": int(mem_id.text())})

            if member:
                full_name = member['first name'] + " " + member['last name']
                self.ui.viewmem_Id.setText(mem_id.text())
                self.ui.viewmem_name.setText(full_name)
                self.ui.viewmem_Gender.setText(member['gender'])
                self.ui.viewmem_BP.setText(str(member['bp']))
                self.ui.viewmem_address.setText(member['address'])
                self.ui.viewmem_DOB.setText(str(member['dob']))
                self.ui.viewmem_height.setText(str(member['height']))
                self.ui.viewmem_medicalAilments.setText(member['medical'])
                self.ui.viewmem_physicalAct.setText(member['activity'])
                self.ui.viewmem_telnum.setText(str(member['contact']))
                self.ui.viewmem_weight.setText(str(member['weight']))
                self.ui.viewmem_status.setText(member['status'])
                self.ui.viewmem_type.setText(member['type'])
                self.ui.viewmem_prevGym.setText(member['previous gym'])
                self.ui.viewmem_email.setText(member['email'] if member['email'] is not None else 'NONE')

    #Validating payment fields
    def check_payment_fields(self):
        if(self.ui.payment_instructor.currentText() == 'Instructor' or
            self.ui.paymentServices_cmbBox.currentText() == 'Service' or
            not self.ui.payment_amt.text() or
            not self.ui.payment_memFee.text() or
            not self.ui.payment_tenderedAmt.text()):

            self.ui.fieldNotice.setText('All required fields must be filled.')
            self.ui.invalid_notice.setFixedWidth(391)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0))  

        else:
            memfee =  float(self.ui.payment_memFee.text())
            tenderedAmt =  float(self.ui.payment_tenderedAmt.text())
            if memfee < 1.00:
                self.ui.tenderedfieldNotice.setText('Invalid yearly membership fee.')
                self.ui.tenderedAmt_notice.setFixedWidth(301)
                QtCore.QTimer.singleShot(1300, lambda: self.ui.tenderedAmt_notice.setFixedWidth(0))  
            elif tenderedAmt < (memfee + float(self.ui.payment_amt.text())):
                self.ui.tenderedAmt_notice.setFixedWidth(391)
                QtCore.QTimer.singleShot(1300, lambda: self.ui.tenderedAmt_notice.setFixedWidth(0))  
            else:
                self.confirm_payment_conf()

    #Validating add member fields
    def check_add_member_fields(self):
        memtype = self.get_selected_radio_button()
        current_date = QDate.currentDate()
        age_limit = current_date.addYears(-10)
        if (not self.ui.regismem_lname.text() or
            not self.ui.regismem_fname.text() or
            not self.ui.regismem_address.text() or
            not self.ui.regismem_BP.text() or
            not self.ui.regismem_contact.text() or 
            not self.ui.regismem_weight.text() or 
            not self.ui.regismem_height.text() or 
            self.ui.regismem_Status.currentText() == 'Status' or
            self.ui.registermem_Gender.currentText() == 'Gender' or
            memtype == 'None'):
            
            self.fields_error_message('All required fields must be filled.')
        else:
            if len(self.ui.regismem_contact.text()) != 11 or not self.ui.regismem_contact.text().startswith('09'):
                self.fields_error_message('Please enter a valid phone number.')
            else:
                if self.ui.regismem_DOB.date() > age_limit:
                    self.fields_error_message('Age must be above 9 years old.')
                else:
                    if not self.customerBPValidator.match(self.ui.regismem_BP.text()).hasMatch():
                        self.fields_error_message('Invalid BP.')
                    else:
                        if not self.emailValidator.match(self.ui.regismem_email.text()).hasMatch():
                            self.fields_error_message('Invalid Email.')

                        else:
                            self.check_duplicate_phone_number()
    
    def fields_error_message(self,text):
        self.ui.fieldNotice.setText(text)
        self.ui.invalid_notice.setFixedWidth(391)
        QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 


    #Validating edit member fields
    def check_edit_member_fields(self):
        memtype = self.get_selected_radio_button_update()
        current_date = QDate.currentDate()
        age_limit = current_date.addYears(-10)
        if (not self.ui.mem_lname.text() or
            not self.ui.mem_fname.text() or
            not self.ui.mem_address.text() or
            not self.ui.mem_BP.text() or
            not self.ui.mem_contact.text() or 
            not self.ui.mem_weight.text() or 
            not self.ui.mem_height.text() or 
            self.ui.memStat_comboBox.currentText() == 'Status' or
            self.ui.memGender_comboBox.currentText() == 'Gender' or
            memtype == 'None'):
            
            self.ui.fieldNotice.setText('All required fields must be filled.')
            self.ui.invalid_notice.setFixedWidth(391)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0))  
        else:
            if len(self.ui.mem_contact.text()) != 11 or not self.ui.mem_contact.text().startswith('09'):
                self.ui.fieldNotice.setText('Please enter a valid phone number.')
                self.ui.invalid_notice.setFixedWidth(391)
                QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 
            else:
                if self.ui.mem_DOB.date() > age_limit:
                    self.ui.fieldNotice.setText('Age must be above 9 years old.')
                    self.ui.invalid_notice.setFixedWidth(391)
                    QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 
                else:
                    if '/' not in self.ui.mem_BP.text():
                        self.ui.fieldNotice.setText('Invalid BP.')
                        self.ui.invalid_notice.setFixedWidth(391)
                        QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 
                    else:
                        self.update_member_details()

    #Displaying instructors in the combo box
    def retrieve_employee_from_DB(self):

        employees = self.employeedb.find({"position" : "INSTRUCTOR"})

        if employees:
            self.ui.payment_instructor.clear()
            self.ui.payment_instructor.addItem('Instructor')
            for employee in employees:
                emp_name = employee['fname'] + " " + employee['lname']
                self.ui.payment_instructor.addItem(emp_name)
            self.ui.payment_instructor.addItem('None')
        self.employeeIDList.append(None)

    #Shows the add member page
    def add_member(self):
        if self.AllowOperations == True:
            self.ui.register_popup.setFixedWidth(1381)
            self.IsRenew = False
        else:
            self.ui.addAdmin_notice.setFixedWidth(0)
            QtCore.QTimer.singleShot(40, lambda: self.ui.addAdmin_notice.setFixedWidth(1361))            

    #Canceling the registration
    def regis_cancel(self):
        self.ui.register_popup.setFixedWidth(0)
        self.ui.regismem_fname.setText('')
        self.ui.regismem_lname.setText('')
        self.ui.regismem_DOB.setDate(QDate(2000, 1, 1))
        self.ui.regismem_address.setText('')
        self.ui.regismem_contact.setText('')
        self.ui.regismem_physicalAct.setText('')
        self.ui.regismem_medicAilment.setText('')
        self.ui.regismem_weight.setText('')
        self.ui.regismem_height.setText('')
        self.ui.regismem_BP.setText('')
        self.ui.registermem_Gender.setCurrentText('Gender')
        self.ui.regismem_Status.setCurrentText('Status')
        self.ui.regismemStud_radio.setChecked(False)
        self.ui.regismemProf_radio.setChecked(False)
        self.ui.regismem_prevGym.setText('')

    #Proceeds to payment after entering member details
    def regis_save(self):
        self.ui.payment_popup.setFixedWidth(1381)
        self.ui.register_popup.setFixedWidth(0)

    #Cancel payment 
    def cancel_payment(self):
        self.ui.payment_popup.setFixedWidth(0)
        self.ui.register_popup.setFixedWidth(1381)

    #Show payment confirmation if pay button is clicked
    def confirm_payment_conf(self):
        self.ui.confirm_pay_widget.setFixedWidth(351)
        if self.IsRenew == False:
            self.ui.payment_widget.setEnabled(False)
            self.ui.payment_widget.setStyleSheet("#payment_widget{ background-color: #ddd; border-radius:  15px;}")
        else:

            if self.ui.renew_popup.width() > 0:
                self.ui.renew_widget.setEnabled(False)
                self.ui.renew_widget.setStyleSheet("#renew_widget{ background-color: #ddd; border-radius:  15px;}")
            else:
                self.ui.membership_renewal_widget.setEnabled(False)
                self.ui.membership_renewal_widget.setStyleSheet("#membership_renewal_widget{ background-color: #ddd; border-radius:  15px;}")

    #Cancel payment confirmation
    def cancel_payment_conf(self):
        self.ui.confirm_pay_widget.setFixedWidth(0)
        if self.IsRenew == False:
            self.ui.payment_widget.setEnabled(True)
            self.ui.payment_widget.setStyleSheet("#payment_widget{ background-color: #fff; border-radius:  15px;}")
        else:

            if self.ui.renew_popup.width() > 0:
                self.ui.renew_widget.setEnabled(True)
                self.ui.renew_widget.setStyleSheet("#renew_widget{ background-color: #fff; border-radius:  15px;}")
            else:
                self.ui.membership_renewal_widget.setEnabled(True)
                self.ui.membership_renewal_widget.setStyleSheet("#membership_renewal_widget{ background-color: #fff; border-radius:  15px;}")

    #Shows delete confirmation for member deletion
    def delete_member(self):

        if len(self.ui.mem_table.selectedItems()) > 0:
            self.ui.member_delete_popup.setFixedWidth(1381)
        else:
            self.ui.rowSelection_notice.setFixedWidth(301)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.rowSelection_notice.setFixedWidth(0))  
    
    #Cancel deletion
    def cancel_delete_mem(self):
        self.ui.member_delete_popup.setFixedWidth(0)
    
    #Confirm deletion
    def confirm_delete_mem(self): 
        selected_row = self.ui.mem_table.currentRow()
        if selected_row != -1:
            mem_id = self.ui.mem_table.item(selected_row, 0)
            temp_mem_id = int(mem_id.text())

            result = self.membersdb.delete_one({"_id": temp_mem_id})

            if result:
                # self.ui.mem_table.removeRow(selected_row)
                self.ui.member_delete_popup.setFixedWidth(0)
                self.ui.delete_notif.setFixedWidth(81)
                QtCore.QTimer.singleShot(1300, lambda: self.ui.delete_notif.setFixedWidth(0)) 

                #Delete service log of the deleted member
                self.mon_servicelogdb.delete_one({"_id": temp_mem_id})

                self.populate_mem_table() 

                self.notificationdb.delete_many({"_id": temp_mem_id})
            
    #Displaying the member details in the edit page
    def edit_member(self):
        selected_row = -1

        if len(self.ui.mem_table.selectedItems()) > 0:
            selected_row = self.ui.mem_table.currentRow()

        if selected_row != -1:
            self.ui.edit_details_popup.setFixedWidth(1381)
            mem_id = self.ui.mem_table.item(selected_row, 0)
            
            member = self.membersdb.find_one({"_id" : int(mem_id.text())})

            dateOfBirth = datetime.datetime.strptime(member['dob'], "%Y-%m-%d")

            if member:
                self.ui.mem_fname.setText(member['first name'])
                self.ui.mem_lname.setText(member['last name'])
                self.ui.mem_DOB.setDate(dateOfBirth)
                self.ui.mem_address.setText(member['address'])
                self.ui.mem_contact.setText(member['contact'])
                self.ui.mem_physicalAct.setText(member['activity'])
                self.ui.mem_medic_ailments.setText(member['medical'])
                self.ui.mem_weight.setText(str(member['weight']))
                self.ui.mem_height.setText(str(member['height']))
                self.ui.mem_BP.setText(str(member['bp']))
                self.ui.memGender_comboBox.setCurrentText(member['gender'])
                self.ui.memStat_comboBox.setCurrentText(member['status'])
                if member['type'] == 'STUDENT':
                    self.ui.memStud_radiobtn.setChecked(True)
                else:
                    self.ui.memProf_radiobtn.setChecked(True)
                self.ui.mem_prevGym.setText(member['previous gym'])
                self.ui.mem_email.setText(member['email'])               

        else:
            self.ui.rowSelection_notice.setFixedWidth(301)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.rowSelection_notice.setFixedWidth(0))  

    #Get the value of the selected radio button for edit
    def get_selected_radio_button_update(self):
        selected_radio_button = None
        if self.ui.memProf_radiobtn.isChecked():
            selected_radio_button = "Professional"
        elif self.ui.memStud_radiobtn.isChecked():
            selected_radio_button = "Student"
        else:
            selected_radio_button = "None"

        return selected_radio_button

    #Updating member details in the DB
    def update_member_details(self):

        mem_id = self.ui.mem_table.item(self.ui.mem_table.currentRow(), 0)

        update_fname = self.ui.mem_fname.text().upper()
        update_lname = self.ui.mem_lname.text().upper()
        update_address = self.ui.mem_address.text().upper()
        update_DOB = self.ui.mem_DOB.date().toString('yyyy-MM-dd')
        update_contact = self.ui.mem_contact.text()
        update_email = self.ui.mem_email.text().upper()
        update_medical = self.ui.mem_medic_ailments.text().upper()
        update_type = self.get_selected_radio_button_update()
        update_prevgym = self.ui.mem_prevGym.text().upper()
        update_BP = self.ui.mem_BP.text()
        update_stat = self.ui.memStat_comboBox.currentText()
        update_physAct = self.ui.mem_physicalAct.text().upper()
        update_weight = self.ui.mem_weight.text()
        update_height = self.ui.mem_height.text()
        update_gender = self.ui.memGender_comboBox.currentText()

        update_member = {
            "$set" : {
                'first name' : update_fname,
                'last name' : update_lname,
                'dob' : update_DOB,
                'gender' : update_gender,
                'address' : update_address,
                'contact' : update_contact,
                'email': update_email,
                'medical' : update_medical,
                'previous gym': update_prevgym,
                'bp' : update_BP,
                'status' : update_stat,
                'activity' : update_physAct,
                'weight' : update_weight,
                'height' : update_height,
                'type' : update_type
            }
        }

        used_contact = self.membersdb.find_one({"contact" : update_contact})['_id']
   
        if used_contact is None or used_contact == int(mem_id.text()):
            result = self.membersdb.update_one({"_id" : int(mem_id.text())}, update_member)

            if result.modified_count > 0:
                self.ui.edit_details_popup.setFixedWidth(0)
                self.ui.savechanges_widget.setFixedWidth(341)
                QtCore.QTimer.singleShot(1300, lambda: self.ui.savechanges_widget.setFixedWidth(0))  
        else:
            self.ui.fieldNotice.setText('Phone number is already used.')
            self.ui.invalid_notice.setFixedWidth(391)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0))

    #Cancel edit member
    def cancel_edit_mem(self):
        self.ui.edit_details_popup.setFixedWidth(0)

    #Automatically displays the  cost of service during payment
    def update_payment_amount(self):
        servicename = self.ui.paymentServices_cmbBox.currentText()
        service_id, serv_price = self.get_service_id(servicename)

        if serv_price is not None:
            self.ui.payment_amt.setText(str(serv_price))
            self.ui.payment_memFee.setText('100.0')
        else:
            self.ui.payment_amt.setText('')  

    #Get the value of the selected radio button for add
    def get_selected_radio_button(self):
        selected_radio_button = None
        if self.ui.regismemProf_radio.isChecked():
            selected_radio_button = "Professional"
        elif self.ui.regismemStud_radio.isChecked():
            selected_radio_button = "Student"
        else:
            selected_radio_button = "None"

        return selected_radio_button

    #Getting the id of the selected service type
    def get_service_id(self, servicetype):
        
        service = self.servicesdb.find_one({"type" : servicetype})

        if service:
            serv_id = service['_id']
            serv_price = service['price']
            return serv_id, serv_price
        else:
            return None, None

    #Displaying all members in the members list table
    def populate_mem_table(self):
        
        members = self.membersdb.find()

        if members:
            self.ui.mem_table.setRowCount(0)

            for row_number, member in enumerate(members):
                self.ui.mem_table.insertRow(row_number)
                for column_number, data in enumerate(member):
                    item = QtWidgets.QTableWidgetItem(str(member[data]))
                    item.setTextAlignment(Qt.AlignHCenter)
                    self.ui.mem_table.setItem(row_number, column_number, item)

    def check_duplicate_phone_number(self):
        phonenum = self.ui.regismem_contact.text()
        
        is_phone_exist = self.membersdb.count_documents({"contact" : phonenum})

        if is_phone_exist == 0:
            self.regis_save()
        else:
            self.ui.fieldNotice.setText('Phone number is already used.')
            self.ui.invalid_notice.setFixedWidth(391)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0))  

    #Add a member to DB
    def add_member_into_DB(self):
        
        self.ui.confirm_pay_widget.setFixedWidth(0)

        mem_fname = self.ui.regismem_fname.text().upper()
        mem_lname = self.ui.regismem_lname.text().upper()
        mem_address = self.ui.regismem_address.text().upper()
        mem_DOB = self.ui.regismem_DOB.date().toString('yyyy-MM-dd')
        mem_contact = self.ui.regismem_contact.text()
        mem_email = self.ui.regismem_email.text().upper()
        mem_medical = self.ui.regismem_medicAilment.text().upper()
        mem_prevGym = self.ui.regismem_prevGym.text().upper()
        mem_BP = self.ui.regismem_BP.text()
        mem_stat = self.ui.regismem_Status.currentText().upper()
        mem_act = self.ui.regismem_physicalAct.text().upper()
        mem_weight = float(self.ui.regismem_weight.text())
        mem_height = float(self.ui.regismem_height.text())
        mem_gender = self.ui.registermem_Gender.currentText().upper()
        mem_type = self.get_selected_radio_button().upper()
        servicename = self.ui.paymentServices_cmbBox.currentText()
        service_id ,serv_price= self.get_service_id(servicename)
        tendered_amount = self.ui.payment_tenderedAmt.text()
        mship_fee = self.ui.payment_memFee.text()


        last_memberid = next(self.membersdb.find().sort("_id", -1).limit(1),{}).get('_id',None)
        mem_id = int(last_memberid) + 1 if last_memberid is not None else 0

        member = {
            '_id' : mem_id,
            'first name' : mem_fname,
            'last name' : mem_lname,
            'dob' : mem_DOB,
            'gender' : mem_gender,
            'address' : mem_address,
            'contact' : mem_contact,
            'email': mem_email,
            'medical' : mem_medical,
            'previous gym': mem_prevGym,
            'bp' : mem_BP,
            'status' : mem_stat,
            'activity' : mem_act,
            'weight' : mem_weight,
            'height' : mem_height,
            'type' : mem_type,
            "start date" : str(datetime.datetime.today()),
            "end date" : str(datetime.datetime.today() + datetime.timedelta(days=365)),
            'emp_id' : self.emp_id
        }


        result = self.membersdb.insert_one(member)


        if result:
            if float(tendered_amount) >= (float(serv_price) + float(mship_fee)):

                #--------------Email for Member------------------
                email_text = f"""
                <html>
                <body style="font-family: Arial, sans-serif; color: #333; background-color: #f4f4f4; margin: 0; padding: 0;">
                <div style="background-color: #ffffff; margin: 20px auto; width: 90%; max-width: 600px; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                    <h2 style="color: #1E90FF; text-align: left; margin-bottom: 20px;">Hi {mem_fname},</h2>
                    <p style="line-height: 1.6; font-size: 16px; text-align: center;">Thank you for signing up with <strong>People Fitness Center</strong>!</p>
                    <p style="line-height: 1.6; font-size: 16px;">We're excited to let you know that your membership has been successfully registered, and we can't wait to see you in the gym.</p>
                    <p style="line-height: 1.6; font-size: 16px;">If you have any questions or need help getting started, feel free to reach out. We're here to help and support you along the way.</p>
                    <p style="line-height: 1.6; font-size: 16px;">Thanks again for joining us, and we look forward to seeing you soon!</p>
                    <br>
                    <div style="text-align: center;"> 
                <img src="https://drive.google.com/uc?export=view&id=1Am6E_LO5laC9XbiEQOoDtmZD_F4aOlU5" alt="Welcome Image" width="150" height="150"/>
                </div>
                <h3 style="text-align: center; font-size: 18px; color: #333; margin-top: 20px;">People Fitness Center</h3>
                </div>
                </body>
                </html>
                """
                email_subject = 'Welcome to People Fitness Center!'
                self.send_email(mem_email.lower(), email_text, email_subject)

                if self.emp_id is not None:

                    instructor_members = self. membersdb.find({'emp_id': self.emp_id})
                    instructor = self.employeedb.find_one({'_id': self.emp_id})
                    member_list = ''.join([f'<li>{member["first name"]} {member["last name"] }</li>' for member in instructor_members])

                    #----------Email for Instructor-------------------
                    instructor_text = f"""
                    <html>
                    <body style="font-family: Arial, sans-serif; color: #333; background-color: #f4f4f4; margin: 0; padding: 0;">
                    <div style="background-color: #ffffff; margin: 20px auto; width: 90%; max-width: 600px; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                    <h2 style="color: #1E90FF; text-align: left; margin-bottom: 20px;">Hi {instructor['fname']},</h2>
                        <p style="line-height: 1.6; font-size: 16px; text-align: center;">We hope you're doing well!</p>
                        <p style="line-height: 1.6; font-size: 16px;">We are excited to inform you that a new member has been assigned to you. Below is the updated list of members you will be working with:</p>
                        <ul style="font-size: 16px; line-height: 1.6;">
                        {member_list} 
                        </ul>
                    <p style="line-height: 1.6; font-size: 16px;">Please make sure to provide them with the necessary guidance and support. If you have any questions or need assistance, feel free to reach out.</p>
                    <p style="line-height: 1.6; font-size: 16px;">We look forward to a productive session together. Thanks for your continued dedication and support!</p>
                    <br>
                    <div style="text-align: center;">
                    <img src="https://drive.google.com/uc?export=view&id=1Am6E_LO5laC9XbiEQOoDtmZD_F4aOlU5" alt="Welcome Image" width="150" height="150"/>
                    </div>
                    <h3 style="text-align: center; font-size: 18px; color: #333; margin-top: 20px;">People Fitness Center</h3>
                    </div>
                    </body>
                    </html>
                    """
                    instructor_subject = "A New Member Is Assigned To You"  
                    self.send_email(instructor['email'].lower(), instructor_text, instructor_subject)
                self.ui.change_popup.setFixedWidth(1381)
                change = float(tendered_amount) - (float(serv_price) + float(mship_fee))
                self.ui.change_field.setText(f"{change:.2f}")
            
            self.ui.register_popup.setFixedWidth(0)
            self.ui.payment_popup.setFixedWidth(0) 

            self.ui.success_widget.setFixedWidth(371)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.success_widget.setFixedWidth(0))  


            self.populate_mem_table()
            self.add_service_log_into_DB(service_id, mem_contact)
            self.add_transaction_DB(service_id, float(serv_price) + float(mship_fee), tendered_amount, mem_contact)  
                            
    #Record for registration and/or renewal is done
    def record_done(self): 

        if self.IsRenew == False:
            self.ui.register_popup.setFixedWidth(0)
            self.ui.regismem_fname.setText('')
            self.ui.regismem_lname.setText('')
            self.ui.regismem_DOB.setDate(QDate(2000, 1, 1))
            self.ui.regismem_address.setText('')
            self.ui.regismem_contact.setText('')
            self.ui.regismem_physicalAct.setText('')
            self.ui.regismem_email.setText('')
            self.ui.regismem_medicAilment.setText('')
            self.ui.regismem_weight.setText('')
            self.ui.regismem_height.setText('')
            self.ui.regismem_BP.setText('')
            self.ui.registermem_Gender.setCurrentText('Gender')
            self.ui.regismem_Status.setCurrentText('Status')
            self.ui.regismemStud_radio.setChecked(False)
            self.ui.regismemProf_radio.setChecked(False)
            self.ui.regismem_prevGym.setText('')
            self.ui.payment_instructor.setCurrentText('Instructor')
            self.ui.paymentServices_cmbBox.setCurrentText('Services')
            self.ui.payment_memFee.setText('')
            self.ui.payment_tenderedAmt.setText('')
            self.ui.payment_amt.setText('')
            self.ui.payment_widget.setEnabled(True)
            self.ui.payment_widget.setStyleSheet("#payment_widget{ background-color: #fff; border-radius:  15px;}")
        else:
            self.ui.renew_instructor.setCurrentText('Instructor')
            self.ui.renewService_comboBox.setCurrentText('Services')
            self.ui.renew_tenderedAmt.setText('')
            self.ui.renew_amt.setText('')
            self.ui.renew_widget.setEnabled(True)
            self.ui.renew_widget.setStyleSheet("#renew_widget{ background-color: #fff; border-radius:  15px;}")

    # ===========================================================================================================================================================================
    # Transaction menu functions
    # ===========================================================================================================================================================================

    #Functional search bar
    def transaction_search(self):
        text = self.ui.transac_search.text().lower()  
        for row in range(self.ui.transac_table.rowCount()):
            row_hidden = True
            for col in range(self.ui.transac_table.columnCount()):
                item = self.ui.transac_table.item(row, col)
                if item and text in item.text().lower():  
                    row_hidden = False
                    break
            self.ui.transac_table.setRowHidden(row, row_hidden) 

    #Add transaction details to DB
    def add_transaction_DB(self, serv_id, pay_totalAmount, pay_tenderedAmount, mem_contact):

        last_transact = next(self.transactiondb.find().sort("_id", -1).limit(1),{}).get("_id", None)
        transact_id = int(last_transact) + 1 if last_transact is not None else 0

        mem_id = self.membersdb.find_one({"contact" : mem_contact})['_id']
        member = self.membersdb.find_one({"_id" : mem_id})
        
        data = {
            "_id" : transact_id,
            "mem id" : mem_id,
            "mem name" : member["first name"] + " " + member['last name'],
            "transact date" : str(datetime.datetime.today()),
            "serv type": self.servicesdb.find_one({"_id" : serv_id})['type'],
            "transact price": pay_totalAmount,
            "transact tendered" : pay_tenderedAmount
        }

        self.transactiondb.insert_one(data)

    #Displaying all transactions done in the table
    def populate_transact_table(self):
 
        transactions = self.transactiondb.find()
        
        self.ui.transac_table.setRowCount(0)
        for row_number, transaction in enumerate(transactions):
            self.ui.transac_table.insertRow(row_number)
            for column_number, data in enumerate(transaction):      

                if column_number == 3:
                    data = str(transaction[data].split(" ")[0])

                item = QtWidgets.QTableWidgetItem(data if column_number == 3 else str(transaction[data]))
                item.setTextAlignment(Qt.AlignHCenter)
                self.ui.transac_table.setItem(row_number,column_number,item)

            #Display the change in the last column
            item = QtWidgets.QTableWidgetItem(str(float(transaction['transact tendered']) - float(transaction['transact price'])))
            item.setTextAlignment(Qt.AlignHCenter)
            self.ui.transac_table.setItem(row_number,7,item)

    # ===========================================================================================================================================================================
    #Employee menu functions
    # ===========================================================================================================================================================================
    
    #Functional search bar
    def employee_search(self):
        text = self.ui.emp_search.text().lower()  
        for row in range(self.ui.emp_table.rowCount()):
            row_hidden = True
            for col in range(self.ui.emp_table.columnCount()):
                item = self.ui.emp_table.item(row, col)
                if item and text in item.text().lower(): 
                    row_hidden = False
                    break
            self.ui.emp_table.setRowHidden(row, row_hidden) 
    
    #Validating add employee fields
    def check_add_employee_fields(self):
        current_date = QDate.currentDate()
        age_limit = current_date.addYears(-18)

        if (
        not self.ui.AddEmp_fname.text() or
        not self.ui.AddEmp_lname.text() or
        not self.ui.AddEmp_DOB.text() or
        not self.ui.AddEmp_address.text() or
        not self.ui.AddEmp_email.text() or
        not self.ui.AddEmp_contact.text()):            
            self.ui.fieldNotice.setText('All required fields must be filled.')
            self.ui.invalid_notice.setFixedWidth(391)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0))  
        else:
            if len(self.ui.AddEmp_contact.text())!= 11 or not self.ui.AddEmp_contact.text().startswith('09'):
                self.ui.fieldNotice.setText('Please insert a valid phone number.')
                self.ui.invalid_notice.setFixedWidth(391)
                QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0))  
            else:
                if self.ui.AddEmp_DOB.date() > age_limit:
                    self.ui.fieldNotice.setText('Age must be above 17 years old.')
                    self.ui.invalid_notice.setFixedWidth(391)
                    QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 
                else:
                    if not self.emailValidator.match(self.ui.AddEmp_email.text()).hasMatch():
                        self.fields_error_message('Invalid Email.')

                    else:
                        self.add_employee_into_DB()

    #Displaying page for adding employee for admin
    def add_admin(self):
        self.ui.addAdmin_notice.setFixedWidth(0)
        self.ui.add_employee_popup.setFixedWidth(1381)

    #Display page for adding employee for admin
    def add_employee(self):
        if self.AllowOperations == True:
            self.editEmployee = False
            self.ui.add_employee_popup.setFixedWidth(1381)
        else:
            self.ui.addAdmin_notice.setFixedWidth(0)
            QtCore.QTimer.singleShot(40, lambda: self.ui.addAdmin_notice.setFixedWidth(1361))     
    
    #Cancel add employee
    def cancel_add_employee(self):
        self.ui.add_employee_popup.setFixedWidth(0)
        self.ui.AddEmp_contact.setText('')
        self.ui.AddEmp_fname.setText('')
        self.ui.AddEmp_lname.setText('')
        self.ui.AddEmp_address.setText('')
        self.ui.AddEmp_email.setText('')
        self.ui.AddEmp_DOB.setDate(QDate(2000, 1, 1))
        self.adminIsExist()

    #Confirmation for employee deletion
    def delete_emp(self):
        if len(self.ui.emp_table.selectedItems()) > 0:
            self.check_emp_exist_in_service_log()
        else:
            self.ui.rowSelection_notice.setFixedWidth(301)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.rowSelection_notice.setFixedWidth(0))  

    #Display edit employee page with employee details
    def edit_employee(self):
        selected_row = -1
        if len(self.ui.emp_table.selectedItems()) > 0:
            selected_row = self.ui.emp_table.currentRow()
        if selected_row != -1:
            self.editEmployee = True
            self.ui.add_employee_popup.setFixedWidth(1381)
            emp_id = int(self.ui.emp_table.item(selected_row, 0).text())
            selected_emp = {"_id": emp_id}

            employee_data = self.employeedb.find_one(selected_emp)
            if employee_data:
                    self.ui.AddEmp_fname.setText(employee_data.get('fname'))
                    self.ui.AddEmp_lname.setText(employee_data.get('lname'))
                    self.ui.AddEmp_address.setText(employee_data.get('address'))
                    self.ui.AddEmp_email.setText(employee_data.get('email'))
                    self.ui.AddEmp_contact.setText(str(employee_data.get('contact')))
                    self.ui.AddEmp_email.setText(employee_data.get('email'))
                    year, month, day = (employee_data.get('DOB').split('-'))
                    self.ui.AddEmp_DOB.setDate(QDate(int(year), int(month), int(day)))
                    
            else:
                    print("No service found for EMP_ID:", emp_id.text())

        else:
             self.ui.rowSelection_notice.setFixedWidth(301)
             QtCore.QTimer.singleShot(1300, lambda: self.ui.rowSelection_notice.setFixedWidth(0))  

    #Cancel deletion
    def cancel_delete_employee(self):
        self.ui.employee_delete_popup.setFixedWidth(0)

    #Displaying all employees in the employees list table
    def populate_employee_table(self):
        self.ui.emp_table.setRowCount(0)
        result = self.employeedb.find()


        for row_number, employee in enumerate(result):
                self.ui.emp_table.insertRow(row_number)
                for column_number, data in enumerate(employee):
                    item = QtWidgets.QTableWidgetItem(str(employee[data]))
                    item.setTextAlignment(Qt.AlignHCenter)
                    self.ui.emp_table.setItem(row_number, column_number, item)


    def cancel_assigned_emp_delete(self):
        self.ui.assigned_emp_delete.setFixedWidth(0)

    def check_emp_exist_in_service_log(self):
        selected_row = self.ui.emp_table.currentRow()
        emp_id = self.ui.emp_table.item(selected_row, 0)

        empIsPresent = self.mon_servicelogdb.find({"employee id": emp_id})
        if empIsPresent:
            self.ui.assigned_emp_delete.setFixedWidth(1381)
        else:
            self.ui.employee_delete_popup.setFixedWidth(1381)
     
    #Confirm deletion
    def confirm_delete_employee(self):
        selected_row = self.ui.emp_table.currentRow()
        emp_id = self.ui.emp_table.item(selected_row, 0).text()
        is_Admin = self.employeedb.find_one({"_id": int(emp_id)})
        
        if is_Admin['position'] == "ADMINISTRATOR":
            self.ui.assigned_emp_delete.setFixedWidth(0)
            self.ui.employee_delete_popup.setFixedWidth(0)
            self.ui.fieldNotice.setText('Unable to delete admin')
            self.ui.invalid_notice.setFixedWidth(391)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0))
            return
        
        else:
            result = self.employeedb.delete_one({"_id": int(emp_id)})

            members = {
                "$set" : {
                    "emp_id": None
                }
            }

            servicelog = {
            "$set" : {
                "employee id": None
            }
            }
            
            update_membersdb = self.membersdb.update_many({"emp_id" : int(emp_id)}, members)
            update_service_logdb = self.mon_servicelogdb.update_many({"employee id": int(emp_id)}, servicelog)
            

            if result and update_membersdb and update_service_logdb:
                self.ui.delete_notif.setFixedWidth(81)
                QtCore.QTimer.singleShot(1300, lambda: self.ui.delete_notif.setFixedWidth(0))   
                self.ui.emp_table.removeRow(selected_row)
                self.ui.assigned_emp_delete.setFixedWidth(0)
                self.ui.employee_delete_popup.setFixedWidth(0)
                self.retrieve_employee_from_DB()
                self.retrieve_employee_from_DB_renew()
                self.populate_employee_table()
      

    #Add employee to DB
    def add_employee_into_DB(self,emp_id=None):
        if self.editEmployee == True:
            selected_row = self.ui.emp_table.currentRow()
            emp_id = self.ui.emp_table.item(selected_row, 0).text()

        if self.AllowOperations == False:
            emp_position = 'ADMINISTRATOR'
        else:
            emp_position = 'INSTRUCTOR'

        
        emp_fname = self.ui.AddEmp_fname.text().upper()
        emp_lname = self.ui.AddEmp_lname.text().upper()
        emp_address = self.ui.AddEmp_address.text().upper()
        emp_email = self.ui.AddEmp_email.text().upper()
        emp_contact = self.ui.AddEmp_contact.text()
        emp_email = self.ui.AddEmp_email.text()
        emp_DOB = self.ui.AddEmp_DOB.date().toString('yyyy-MM-dd')
        
        is_phonenum_exist = self.employeedb.count_documents({"contact" : emp_contact})
        same_user = self.employeedb.find_one({"contact": emp_contact})
       
        if self.editEmployee == True:
            if is_phonenum_exist == 0 or (is_phonenum_exist > 0 and int(same_user.get("_id")) == int(emp_id)):

                update_emp = {
                    "$set":{
                        "fname": emp_fname,
                        "lname": emp_lname,
                        "DOB": emp_DOB, 
                        "contact": emp_contact,
                        "address": emp_address,
                        "email" : emp_email,
                    }
                }

                result = self.employeedb.update_one({"_id": int(emp_id)}, update_emp)
                if result:
                    self.ui.AddEmp_contact.setText('')
                    self.ui.AddEmp_fname.setText('')
                    self.ui.AddEmp_lname.setText('')
                    self.ui.AddEmp_address.setText('')
                    self.ui.AddEmp_email.setText('')
                    self.ui.savechanges_widget.setFixedWidth(341 )
                    QtCore.QTimer.singleShot(1300, lambda: self.ui.savechanges_widget.setFixedWidth(0))  
                    self.populate_employee_table()
                    self.ui.add_employee_popup.setFixedWidth(0)

            else:
                self.ui.fieldNotice.setText('Phone number is already used.')
                self.ui.invalid_notice.setFixedWidth(391)
                QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0))

        else:
            if is_phonenum_exist == 0:
                last_empid = next(self.employeedb.find(). sort("_id", -1).limit(1), {}).get('_id', None)
                emp_id = int(last_empid) + 1 if last_empid is not None else 0

                employee = {
                    "_id": emp_id,
                    "fname": emp_fname,
                    "lname": emp_lname,
                    "contact": emp_contact,
                    "address": emp_address,
                    "email" : emp_email,
                    "position": emp_position,
                    "DOB": emp_DOB,
                }

                result = self.employeedb.insert_one(employee)
                if result:
                    self.ui.AddEmp_contact.setText('')
                    self.ui.AddEmp_fname.setText('')
                    self.ui.AddEmp_lname.setText('')
                    self.ui.AddEmp_address.setText('')
                    self.ui.AddEmp_email.setText('')
                    self.ui.AddEmp_DOB.setDate(QDate(2000, 1, 1))
                    self.ui.success_widget.setFixedWidth(341)
                    QtCore.QTimer.singleShot(1300, lambda: self.ui.success_widget.setFixedWidth(0))  
                    self.retrieve_employee_from_DB_renew()
                    self.retrieve_employee_from_DB()
                    self.populate_employee_table()
                    self.adminIsExist()
                    self.ui.add_employee_popup.setFixedWidth(0)

            else:
                self.ui.fieldNotice.setText('Phone number is already used.')
                self.ui.invalid_notice.setFixedWidth(391)
                QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0))
       
    # ===========================================================================================================================================================================
    # Expired membership deletion
    # ===========================================================================================================================================================================

    #Automatically deletes a member if membership has expired
    def delete_expiredMship(self):
        while True:
            self.membersdb.delete_many({"end date" : {"$lte" : datetime.datetime.today()}})
            
    # ===========================================================================================================================================================================
    # Notification
    # ===========================================================================================================================================================================

    #Notification display
    def show_notif(self):
        self.ui.notification_popup.setFixedWidth(581)
        self.display_notifs()
        self.ui.notif_redDot.setFixedWidth(0)

    def close_notif(self):
        self.ui.notification_popup.setFixedWidth(0)

    #Constantly checking the status of monthly service access
    def monitor_monServiceAccess(self):

        interval = [
                    (7, "monthly service access has 7 remaining days."),
                    (1, "monthly service access will expire after 24 hours."),
                    (0, "monthly service access has expired.")
                ] 
                
        while True:
    
            for days, notification in interval:

                pipeline = [
                    {
                        "$project": {
                            "_id": 1,
                            "end date": {
                                "$subtract": [
                                    {
                                        # Converting string to date
                                        "$toDate": {
                                            "$substr": [ "$end date", 0, 19 ] # Extracting the first 19 characters (yyyy-MM-dd HH:mm:ss)
                                        }
                                    },
                                    days * 24 * 60 * 60 * 1000  # Subtract the interval in milliseconds
                                ]
                            }
                        }
                    },
                    {
                        "$match": {
                            "end date": {"$lte": datetime.datetime.today()}  # Compare with current local time
                        }
                    },
                ]

                monthly_serviceAccess = self.mon_servicelogdb.aggregate(pipeline)
                
                for member_access in monthly_serviceAccess:
                    notif_exist = self.notificationdb.find({"content" : notification}, {"_id": 0, "member id" : 1})

                    if notif_exist is not None and member_access['_id'] not in [mem_id['member id'] for mem_id in notif_exist]:

                        last_notifID = next(self.notificationdb.find().sort("_id", -1).limit(1), {}).get("_id", None)
                        notif_id = last_notifID + 1 if last_notifID is not None else 0


                        notification = {
                            "_id" : notif_id,
                            "content" : notification,
                            "date" : str(datetime.datetime.today()),
                            "member id" : member_access['_id'],                    
                        }

                        result = self.notificationdb.insert_one(notification)

                        
                        member_id = notification['member id']
                        member_details = self.membersdb.find_one({'_id' : member_id})
                    
                        if result.acknowledged:
                            if member_details:
                                print(f"Sending email to {member_details['first name']} ({member_details['email'].lower()})")

                                stripped_content = notification['content'].rstrip('.')
                                email_subject = 'Reminder: Days Remaining on Your Monthly Service Access'
                                self.ui.notif_redDot.setFixedWidth(10) 
                                email_text = f"""
                                <html>
                                <body style="font-family: Arial, sans-serif; color: #333; background-color: #f4f4f4; margin: 0; padding: 0;">
                                    <div style="background-color: #ffffff; margin: 20px auto; width: 90%; max-width: 600px; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                                    <h2 style="color: #1E90FF; text-align: left; margin-bottom: 20px;">Hi {member_details['first name']},</h2>
                                    <p style="line-height: 1.6; font-size: 16px;">We hope you're doing well!</p>   
                                    <p style="line-height: 1.6; font-size: 16px;">We would like to remind you that your {stripped_content}.</p>
                                    <p style="line-height: 1.6; font-size: 16px;">To ensure uninterrupted service, we recommend renewing your subscription before the expiration date.</p>
                                    <p style="line-height: 1.6; font-size: 16px;">If you have already renewed your access, please disregard this message.</p>
                                    <p style="line-height: 1.6; font-size: 16px;">Should you need assistance or have any questions, our customer support team is here to help.</p>
                                    <br>
                                    <p style="line-height: 1.6; font-size: 16px;">We appreciate your continued membership and look forward to serving you!</p>
                                    <br>
                                    <div style="text-align: center;">
                                    <img src="https://drive.google.com/uc?export=view&id=1Am6E_LO5laC9XbiEQOoDtmZD_F4aOlU5" alt="People Fitness Center" width="150" height="150"/>
                                    </div>
                                    <h3 style="text-align: center; font-size: 18px; color: #333; margin-top: 20px;">People Fitness Center</h3>
                                    <p style="text-align: center; font-size: 16px;">If you need assistance, please contact us at <strong>peoplefitness2008@gmail.com</strong>.</p>
                                    </div>
                                </body>
                                </html>
                                """
                                self.send_email(member_details['email'].lower(), email_text, email_subject)

                        if days == 0: self.populate_monServiceLog()
                
                time.sleep(1)

    def monitor_membership(self):

        interval = [
                (30, "membership has 30 remaining days."),
                (15, "membership has 15 remaining days."),
                (3, "membership has 3 remaining days."),
                (1, "membership will expire after 24 hours."),
                (0, "membership has expired.")
            ] 
 
        while True:
            
            for days, notification in interval:
 
                pipeline = [
                    {
                        "$project" : {
                            "_id" : 1,
                            "end date" : {
                                "$subtract": [
                                    {
                                        # Converting string to date
                                        "$toDate": {
                                            "$substr": [ "$end date", 0, 19 ] # Extracting the first 19 characters (yyyy-MM-dd HH:mm:ss)
                                        }
                                    },
                                    days * 24 * 60 * 60 * 1000  # Subtract the interval in milliseconds
                                ]
                            }
                        }
                    },
                    {
                        "$match": {
                            "end date": {"$lte": datetime.datetime.today()}  # Compare with current local time
                        }
                    }
                     
                ]

                membership_expiry = self.membersdb.aggregate(pipeline)

                for member in membership_expiry:

                    notif_exist = self.notificationdb.find({"content" : notification}, {"_id" : 0, "member id" : 1})


                    if notif_exist is not None and member['_id'] not in [mem_id['member id'] for mem_id in notif_exist]:
                        
                        last_notifID = next(self.notificationdb.find().sort("_id", -1).limit(1), {}).get("_id", None)
                        notif_id = last_notifID + 1 if last_notifID is not None else 0

                        notification = {
                            "_id" : notif_id,
                            "content" : notification,
                            "date" : str(datetime.datetime.today()),
                            "member id" : member['_id'],                    
                        }

                        result = self.notificationdb.insert_one(notification)
                        member_id = notification['member id']
                        member_details = self.membersdb.find_one({'_id' : member_id})

                        if result.acknowledged:
                             if member_details:
                                print(f"Sending email to {member_details['first name']} ({member_details['email'].lower()})")
                                stripped_content = notification['content'].rstrip('.')
                                email_subject = 'Reminder: Days Remaining on Your Annual Membership'
                                email_text = f"""
                                <html>
                                <body style="font-family: Arial, sans-serif; color: #333; background-color: #f4f4f4; margin: 0; padding: 0;">
                                    <div style="background-color: #ffffff; margin: 20px auto; width: 90%; max-width: 600px; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                                    <h2 style="color: #1E90FF; text-align: left; margin-bottom: 20px;">Hi {member_details['first name']},</h2>
                                    <p style="line-height: 1.6; font-size: 16px;">We hope you're doing well and continuing to achieve your fitness goals!</p>   
                                    <p style="line-height: 1.6; font-size: 16px;">Your annual {stripped_content}</p>
                                    <p style="line-height: 1.6; font-size: 16px;">To ensure you can continue enjoying all the benefits of your membership, we encourage you to renew it as soon as possible. Don't miss out on another year of fitness and wellness!</p>
                                    <p style="line-height: 1.6; font-size: 16px;">If you have already renewed your membership, please disregard this message. Otherwise, don't hesitate to reach out if you need assistance with your renewal!</p>
                                    <br>
                                    <p style="line-height: 1.6; font-size: 16px;">We value your commitment to a healthy lifestyle, and we're here to support you every step of the way!</p>
                                    <br>
                                    <div style="text-align: center;">
                                    <img src="https://drive.google.com/uc?export=view&id=1Am6E_LO5laC9XbiEQOoDtmZD_F4aOlU5" alt="People Fitness Center" width="150" height="150"/>
                                    </div>
                                    <h3 style="text-align: center; font-size: 18px; color: #333; margin-top: 20px;">People Fitness Center</h3>
                                    <p style="text-align: center; font-size: 16px;">If you need assistance, please contact us at <strong>peoplefitness2008@gmail.com</strong>.</p>
                                    </div>
                                </body>
                                </html>
                                """

                                self.send_email(member_details['email'].lower(), email_text, email_subject)
                                self.ui.notif_redDot.setFixedWidth(10)

                        if days == 0: self.populate_mem_table() 
                
                time.sleep(1)

    #Displaying notifications
    def display_notifs(self):

        to_display = {
            '_id': 0,
            'content' : 1,
            'date' : 1,
            'member id' : 1
        }
        notifications = list(self.notificationdb.find({}, to_display))[::-1]


        self.ui.notif_table.setRowCount(0)
        for row_number, notification in enumerate(notifications):
            member_fname = self.membersdb.find_one({"_id" : notification['member id']})['first name']
            member_lname = self.membersdb.find_one({"_id" : notification['member id']})['last name']
            self.ui.notif_table.insertRow(row_number)
            for column_number, data in enumerate(notification):

                if column_number == 1:
                    data = str(notification[data]).split(" ")[0]

                item = QtWidgets.QTableWidgetItem(data if column_number == 1 else (member_fname + ' ' + member_lname + "'s " + str(notification[data])))
                self.ui.notif_table.setItem(row_number, column_number, item)

    # ===========================================================================================================================================================================
    # Monthly Service Log
    # ===========================================================================================================================================================================
    def add_service_log_into_DB(self, serv_id,mem_contact):
 
        member = self.membersdb.find_one({'contact' : mem_contact})
        service = self.servicesdb.find_one({'_id' : serv_id})
        log = {
            "_id" : member['_id'],
            "member_fname" : member['first name'],
            "member_lname" : member['last name'],
            "service type": service['type'],
            "employee id" : self.emp_id,
            "start date": str(datetime.datetime.today()),
            "end date": str(datetime.datetime.today() + datetime.timedelta(days=30)) 
        }

        result = self.mon_servicelogdb.insert_one(log)

        if result:
            self.populate_monServiceLog()


    # ===========================================================================================================================================================================
    # Dashboard
    # ===========================================================================================================================================================================
    def view_Dashboard(self):
        now = datetime.datetime.today()
        active = 0
        expired = 0

        total_employees = self.employeedb.count_documents({})
        total_members = self.membersdb.count_documents({})
        service_log = list(self.mon_servicelogdb.find({}))
        end_date  = [log['end date'] for log in service_log]

        for date in end_date:
            if date > str(now):
                active += 1
            else:
                expired += 1

        self.ui.totalEmployees_dashboard.setText(str(total_employees))
        self.ui.totalMembers_dashboard.setText(str(total_members))
        self.ui.active_dashboard.setText(str(active))
        self.ui.expired_dashboard.setText(str(expired))

    
    # ===========================================================================================================================================================================
    # Send Email and text
    # ===========================================================================================================================================================================
    def send_email(self, receiver_email, email_text, subject):
        sender_email = 'peoplefitnesscenter2008@gmail.com'

        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject

            msg.attach(MIMEText(email_text, 'html'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()  # Start TLS encryption
            server.login(sender_email, 'xmpdacmlmodnppns')  # Login with your Gmail credentials
            server.sendmail(sender_email, receiver_email, msg.as_string())  # Send email

            print(f'Email sent to {receiver_email}')

        except smtplib.SMTPException as e:
            print(f'Error occurred while sending email to {receiver_email}: {e}')

        finally:
            server.quit()  # Close the SMTP connection 


    # ===========================================================================================================================================================================
    # Logout confirmation
    # ===========================================================================================================================================================================

    def logoutpopup(self):
        self.ui.logout_popup.setFixedWidth(1381)

    def confirm_logout(self):
        self.close()
        self.login_window = LoginWindow()
        self.login_window.show()

    def cancel_logout(self):
        self.ui.logout_popup.setFixedWidth(0)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    login = LoginWindow()
    app.exec()
    

