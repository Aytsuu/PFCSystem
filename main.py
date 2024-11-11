from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from PySide6 import QtWidgets, QtCore
from ui_loginUI import *
from ui_mainUI import *
from PySide6.QtGui import *
import datetime
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
        self.AllowOperations = True
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
        
        # ===========================================================================================================================================================================
        # Adding admin and check if admin exists in employees record
        # ===========================================================================================================================================================================

        self.adminIsExist()
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
        customerBPValidator = QRegularExpression("[0-9/.]*")
        validBP = QRegularExpressionValidator(customerBPValidator, self.ui.regismem_BP)
        validBPUpdate = QRegularExpressionValidator(customerBPValidator, self.ui.mem_BP)
        
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

        self.display_notifs()
        self.ui.expand_notif.clicked.connect(self.notif_area_displaySize)
        self.ui.minimize_notif.clicked.connect(self.notif_area_displaySize)
        self.ui.new_notifbtn.clicked.connect(self.select_home)
        
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
        self.ui.notif_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.ui.notif_table.setColumnWidth(0, 580)


        #Remove outline on selecting a row/item
        self.ui.mem_table.setFocusPolicy(Qt.NoFocus)
        self.ui.mon_serviceLog_table.setFocusPolicy(Qt.NoFocus)
        self.ui.mshipStat_table.setFocusPolicy(Qt.NoFocus)
        self.ui.transac_table.setFocusPolicy(Qt.NoFocus)
        self.ui.services_table.setFocusPolicy(Qt.NoFocus)
        self.ui.emp_table.setFocusPolicy(Qt.NoFocus)
        self.ui.notif_table.setFocusPolicy(Qt.NoFocus)

        #remove vertical headers
        self.ui.emp_table.verticalHeader().setVisible(False)
        self.ui.transac_table.verticalHeader().setVisible(False)
        self.ui.mon_serviceLog_table.verticalHeader().setVisible(False)
        self.ui.mshipStat_table.verticalHeader().setVisible(False)
        self.ui.mem_table.verticalHeader().setVisible(False)
        self.ui.services_table.verticalHeader().setVisible(False)
        self.ui.notif_table.verticalHeader().setVisible(False)

        self.ui.notif_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

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
        self.ui.renew_instructor.activated.connect(self.getEmployeeIndex)
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
        self.ui.payment_instructor.activated.connect(self.getEmployeeIndex)
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
        self.display_notifs()
        self.ui.new_notifbtn.setFixedWidth(0)
        
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

        pass
        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)

        #     cursor = conn.cursor()
        #     cursor.execute("SELECT EMP_ID FROM EMPLOYEE WHERE EMP_POSITION = 'ADMINISTRATOR'")
        #     admin = cursor.fetchone()

        #     if admin:
        #         self.AllowOperations = True
        #     else:
        #         self.ui.addAdmin_notice.setFixedWidth(1361)


        # except (Exception, psycopg2.Error) as error:
        #     print("Error retrieving data from the database:", error)

        # finally:
        #     # Close the cursor and database connection
        #     if conn is not None:
        #         conn.close()

    # ===========================================================================================================================================================================
    # Previous Page
    # ===========================================================================================================================================================================

    def previous(self,page):
        self.prev_page = page

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
            service_id = self.ui.services_table.item(selected_row, 0)
            conn = None
            # try:
            #     params = config()
            #     conn = psycopg2.connect(**params)

            #     cursor = conn.cursor()
            #     cursor.execute("SELECT SERV_TYPE, SERV_PRICE FROM SERVICE WHERE SERV_ID = '" + service_id.text() +"';")
            #     service = cursor.fetchone()

            #     if service:
            #         serv_type, serv_price = service
            #         self.ui.service_Update.setText(str(serv_type))
            #         self.ui.service_Amount.setText(str(serv_price))

            #     else:
            #         print("No service found for SERV_ID:", service_id.text())


            # except (Exception, psycopg2.Error) as error:
            #     print("Error retrieving data from the database:", error)

            # finally:
            #     # Close the cursor and database connection
            #     if conn is not None:
            #         conn.close()
        else:
            self.ui.rowSelection_notice.setFixedWidth(301)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.rowSelection_notice.setFixedWidth(0))  

    #Update service in DB
    def update_service(self):
        serv_id = self.ui.services_table.item(self.ui.services_table.currentRow(), 0)

        serv_type = self.ui.service_Update.text().upper()
        serv_price = float(self.ui.service_Amount.text())

        is_service_exist = self.servicesdb.count_documents({"type" : serv_type})

        if is_service_exist == 0:
            update_service = {
                "$set" : {
                    "type" : serv_type,
                    "price" : serv_price
                }
            }

            result = self.servicesdb.update_one({"_id" : int(serv_id.text())}, update_service)

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

        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)
        #     cursor = conn.cursor()
        #     cursor.execute(sql, values)
        #     conn.commit()
        #     print("Service details updated successfully.")
        #     self.ui.services_widget.setFixedWidth(701)
        #     self.ui.update_service_widget.setFixedWidth(0) 
        #     self.ui.service_Update.setText('')
        #     self.ui.service_Amount.setText('')
        #     self.retrieve_services_from_DB()
        #     self.populate_services_table()
        #     self.retrieve_employee_from_DB()
        #     self.retrieve_employee_from_DB_renew()

        # except (Exception, psycopg2.Error) as error:
        #     self.ui.fieldNotice.setText('Service already exists.')
        #     self.ui.invalid_notice.setFixedWidth(391)
        #     QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 

        # finally:
        #     if conn is not None:
        #         conn.close()

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
        exception_flag = False

        if len(self.ui.services_table.selectedItems()) > 0:
            selected_row = self.ui.services_table.currentRow()

        if selected_row != -1:
            serv_id = self.ui.services_table.item(selected_row, 0)

            result = self.servicesdb.delete_one({"_id" : int(serv_id.text())})

            if result:
                self.ui.services_table.removeRow(selected_row)
                self.retrieve_services_from_DB()
                self.populate_services_table()

            # try:
            #     params = config()
            #     conn = psycopg2.connect(**params)
            #     cursor = conn.cursor()
            #     cursor.execute("DELETE FROM SERVICE WHERE SERV_ID = '" + serv_id.text() + "';")
            #     conn.commit()
            #     self.ui.services_table.removeRow(selected_row)
            #     self.retrieve_services_from_DB()
            #     self.populate_services_table()
            #     self.retrieve_employee_from_DB()
            #     self.retrieve_employee_from_DB_renew()
                
            # except (Exception, psycopg2.Error) as error:
            #     exception_flag = True
            #     self.ui.fieldNotice.setText('Unable to delete: Service in use.')
            #     self.ui.invalid_notice.setFixedWidth(391)
            #     QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 
            # finally:
            #     if conn is not None:
            #         conn.close()     
                    
            #         if not exception_flag:
            #             self.ui.delete_notif.setFixedWidth(81)
            #             QtCore.QTimer.singleShot(1300, lambda: self.ui.delete_notif.setFixedWidth(0)) 

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
        conn = None
        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)

        #     cursor = conn.cursor()
        #     cursor.execute("SELECT EMP_ID, CONCAT(EMP_FNAME,' ', EMP_LNAME) FROM EMPLOYEE WHERE EMP_POSITION = 'INSTRUCTOR';")
        #     employees = cursor.fetchall()
        #     self.ui.renew_instructor.clear()

        #     self.ui.renew_instructor.addItem('Instructor')
        #     self.employeeIDList.append(None)
            
        #     for employee in employees:
        #         emp_id = employee[0]
        #         emp_name = employee[1]
        #         self.employeeIDList.append(emp_id)
        #         self.ui.renew_instructor.addItem(emp_name)

        #     self.ui.renew_instructor.addItem('None')
        #     self.employeeIDList.append(None)
        # except (Exception, psycopg2.Error) as error:
        #     print("Error retrieving data from the database:", error)

        # finally:
        #     # Close the cursor and database connection
        #     if conn is not None:
        #         conn.close()

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
            mon_id = self.ui.mon_serviceLog_table.item(selected_row, 0)
            conn = None
            # try:
            #     params = config()
            #     conn = psycopg2.connect(**params)

            #     sql = "SELECT MEM_MEMBERSHIP_END_DATE FROM MONTHLY_SERVICE_LOG INNER JOIN MEMBER ON MEMBER.MEM_ID = MONTHLY_SERVICE_LOG.MEM_ID WHERE MON_SERVICE_LOG_ID = '" + mon_id.text() + "';"
            #     cursor = conn.cursor()
            #     cursor.execute(sql)
            #     membership_exp = cursor.fetchone()

            #     if membership_exp:
            #         expiry_date = membership_exp[0].date()
            #         today = datetime.datetime.today().date()
            #         remaining_days = (expiry_date - today).days
            #         if remaining_days < 30:
            #             self.ui.reminder_text.setText(f"This member's membership will expire within {remaining_days} day/s. Would you like to proceed with the monthly service access renewal or renew membership first?")
            #             self.ui.renewal_reminder_popup.setFixedWidth(1381)   
            #         else:
            #             self.ui.renew_popup.setFixedWidth(1381)   
            # except(Exception, psycopg2.Error) as error:
            #     print(error)
            # finally:
            #     if conn is not None:  
            #         conn.close()

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
        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)

        #     sql = "UPDATE MONTHLY_SERVICE_LOG SET SERV_ID = %s, EMP_ID = %s, MON_SERVICE_START_DATE = CURRENT_TIMESTAMP, MON_SERVICE_END_DATE = CURRENT_TIMESTAMP +  INTERVAL '30 days' WHERE MON_SERVICE_LOG_ID = %s;"
        #     cursor = conn.cursor()
        #     cursor.execute(sql, (service_id, self.emp_id, monserv_id))    
        #     conn.commit()
        #     rows_changed = cursor.rowcount
        #     if rows_changed > 0:
        #         self.ui.savechanges_widget.setFixedWidth(341)
        #         QtCore.QTimer.singleShot(1300, lambda: self.ui.savechanges_widget.setFixedWidth(0)) 
        #         self.ui.renew_popup.setFixedWidth(0)

        #         self.populate_mem_table()
        #         self.populate_monServiceLog()
                
        #         sql = "SELECT MEM_TELEPHONE FROM MONTHLY_SERVICE_LOG JOIN MEMBER ON MEMBER.MEM_ID = MONTHLY_SERVICE_LOG.MEM_ID WHERE MON_SERVICE_LOG_ID = '" + mon_id + "';"
        #         cursor = conn.cursor()
        #         cursor.execute(sql)    
        #         result = cursor.fetchone()

        #         if result:
        #             mem_contact = result
        #             self.add_transaction_DB(service_id, renew_amt, renew_tendered, mem_contact)
            
        # except (Exception, psycopg2.Error) as error:
        #     print("Error retrieving data from the database:", error)
        
        # finally: 
        #     if conn is not None:  
        #         conn.close()

        #         if float(renew_tendered) > float(renew_amt):
        #             self.ui.change_popup.setFixedWidth(1381)
        #             change = float(renew_tendered) - float(renew_amt)
        #             self.ui.change_field.setText(f"{change:.2f}")
        #             self.populate_monServiceLog()
        #         self.ui.renew_popup.setFixedWidth(0) 


    #Displaying all members with monthly service access
    def populate_monServiceLog(self):
        conn = None
        now = datetime.datetime.today()
        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)

        #     sql = "SELECT MON_SERVICE_LOG_ID, MEM_FNAME, MEM_LNAME, SERV_TYPE, CONCAT(EMP_FNAME ,' ', EMP_LNAME), DATE(MON_SERVICE_START_DATE), MON_SERVICE_END_DATE FROM MONTHLY_SERVICE_LOG JOIN MEMBER ON MEMBER.MEM_ID = MONTHLY_SERVICE_LOG.MEM_ID JOIN SERVICE ON SERVICE.SERV_ID = MONTHLY_SERVICE_LOG.SERV_ID LEFT JOIN EMPLOYEE ON EMPLOYEE.EMP_ID = MONTHLY_SERVICE_LOG.EMP_ID"
        #     cursor = conn.cursor()
        #     cursor.execute(sql)
        #     result = cursor.fetchall()
            
        #     self.ui.mon_serviceLog_table.setRowCount(0)
            
        #     if result:
        #         for row_number, row_data in enumerate(result):
        #             self.ui.mon_serviceLog_table.insertRow(row_number)
        #             for column_number, data in enumerate(row_data):
                
        #                 if column_number == 6:
                            
        #                     end_date = data
        #                     new_data = str(data).split(" ")
        #                     data = new_data[0]

        #                     if now < end_date:
        #                         item = QtWidgets.QTableWidgetItem('ACTIVE')
        #                         item.setTextAlignment(Qt.AlignHCenter)
        #                         self.ui.mon_serviceLog_table.setItem(row_number, 7, item)
        #                     else:
        #                         item = QtWidgets.QTableWidgetItem('EXPIRED')
        #                         item.setTextAlignment(Qt.AlignHCenter)
        #                         self.ui.mon_serviceLog_table.setItem(row_number, 7, item)
                        
        #                 item = QtWidgets.QTableWidgetItem(str(data))
        #                 item.setTextAlignment(Qt.AlignHCenter)
        #                 self.ui.mon_serviceLog_table.setItem(row_number, column_number, item)

        # except (Exception, psycopg2.Error) as error:
        #     print("Error retrieving data from the database:", error)
        
        # finally:
        #     if conn is not None:
        #         conn.close()
    
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
        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)

        #     sql = "UPDATE MEMBER SET MEM_MEMBERSHIP_START_DATE = CURRENT_TIMESTAMP, MEM_MEMBERSHIP_END_DATE = CURRENT_TIMESTAMP +  INTERVAL '365 days' WHERE MEM_ID = (SELECT MEM_ID FROM MONTHLY_SERVICE_LOG WHERE MON_SERVICE_LOG_ID = '" + monservId.text() + "');"
        #     cursor = conn.cursor()
        #     cursor.execute(sql)    
        #     conn.commit()
        #     rows_changed = cursor.rowcount

        #     if rows_changed > 0:
        #         self.ui.savechanges_widget.setFixedWidth(341)
        #         QtCore.QTimer.singleShot(1300, lambda: self.ui.savechanges_widget.setFixedWidth(0)) 
        #         self.ui.renew_popup.setFixedWidth(0)

        #         self.populate_mem_table()
        #         self.populate_monServiceLog()

        #         sql = "SELECT MEM_TELEPHONE FROM MONTHLY_SERVICE_LOG JOIN MEMBER ON MEMBER.MEM_ID = MONTHLY_SERVICE_LOG.MEM_ID WHERE MON_SERVICE_LOG_ID = '" + mon_id + "';"
        #         cursor = conn.cursor()
        #         cursor.execute(sql)    
        #         result = cursor.fetchone()

        #         if result:
        #             mem_contact = result
        #             self.add_transaction_DB(None, mship_fee, mshipRenew_tendered, mem_contact)
            
        # except (Exception, psycopg2.Error) as error:
        #     print("Error retrieving data from the database:", error)
        
        # finally: 
        #     if conn is not None:  
        #         conn.close()

        #         if float(mshipRenew_tendered) > float(mship_fee):
        #             self.ui.change_popup.setFixedWidth(1381)
        #             change = float(mshipRenew_tendered) - float(mship_fee)
        #             self.ui.change_field.setText(f"{change:.2f}")
        #             self.populate_monServiceLog()
        #         self.ui.membership_renewal_popup.setFixedWidth(0) 

    #Display details of all membership
    def populate_mshipStat(self):
        conn = None
        now = datetime.date.today()
        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)

        #     sql = "SELECT MEM_ID, MEM_FNAME, MEM_LNAME, DATE(MEM_MEMBERSHIP_START_DATE), DATE(MEM_MEMBERSHIP_END_DATE) FROM MEMBER"
        #     cursor = conn.cursor()
        #     cursor.execute(sql)
        #     result = cursor.fetchall()
            
        #     self.ui.mshipStat_table.setRowCount(0)

        #     for row_number, row_data in enumerate(result):
        #         self.ui.mshipStat_table.insertRow(row_number)
        #         for column_number, data in enumerate(row_data):
                    
        #             item = QtWidgets.QTableWidgetItem(str(data))
        #             item.setTextAlignment(Qt.AlignHCenter)
        #             self.ui.mshipStat_table.setItem(row_number, column_number, item)
        
            
        # except (Exception, psycopg2.Error) as error:
        #     print("Error retrieving data from the database:", error)
        
        # finally:
        #     if conn is not None:
        #         conn.close()

    # ===========================================================================================================================================================================
    # List of member functions 
    # ===========================================================================================================================================================================
    
    #Getting the ID of the selected instructor during payment and renew
    def getEmployeeIndex(self, index):
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
            conn = None
            # try:
            #     params = config()
            #     conn = psycopg2.connect(**params)

            #     sql = "SELECT * FROM MEMBER WHERE MEM_ID = '" + mem_id.text() + "';"
            #     cursor = conn.cursor()
            #     cursor.execute(sql)
            #     member = cursor.fetchone()

            #     if member:
            #         mmbr_id, mmbr_fname, mmbr_lname, mmbr_birthdate, mmbr_address, mmbr_telephone, mmbr_physical, mmbr_ailment, mmbr_weight, mmbr_height, mmbr_bp, mmbr_gender, mmbr_status, mmbr_type, mmbr_prevGym, mmbr_start_date, mmbr_end_date, admin = member  
            #         full_name = mmbr_fname + " " + mmbr_lname
            #         self.ui.viewmem_Id.setText(str(mmbr_id))
            #         self.ui.viewmem_name.setText(str(full_name))
            #         self.ui.viewmem_Gender.setText(str(mmbr_gender))
            #         self.ui.viewmem_BP.setText(str(mmbr_bp))
            #         self.ui.viewmem_address.setText(str(mmbr_address))
            #         self.ui.viewmem_DOB.setText(str(mmbr_birthdate))
            #         self.ui.viewmem_height.setText(str(mmbr_height))
            #         self.ui.viewmem_medicalAilments.setText(str(mmbr_ailment))
            #         self.ui.viewmem_physicalAct.setText(str(mmbr_physical))
            #         self.ui.viewmem_telnum.setText(str(mmbr_telephone))
            #         self.ui.viewmem_weight.setText(str(mmbr_weight))
            #         self.ui.viewmem_status.setText(str(mmbr_status))
            #         self.ui.viewmem_type.setText(str(mmbr_type))
            #         self.ui.viewmem_prevGym.setText(str(mmbr_prevGym))
            #     else:
            #         return None, None
            
            # except (Exception, psycopg2.Error) as error:
            #     print("Error retrieving data from the database:", error)
            
            # finally:
            #     if conn is not None:
            #         conn.close()

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
            
            self.ui.fieldNotice.setText('All required fields must be filled.')
            self.ui.invalid_notice.setFixedWidth(391)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0))  
        else:
            if len(self.ui.regismem_contact.text()) != 11 or not self.ui.regismem_contact.text().startswith('09'):
                self.ui.fieldNotice.setText('Please enter a valid phone number.')
                self.ui.invalid_notice.setFixedWidth(391)
                QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 
            else:
                if self.ui.regismem_DOB.date() > age_limit:
                    self.ui.fieldNotice.setText('Age must be above 9 years old.')
                    self.ui.invalid_notice.setFixedWidth(391)
                    QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 
                else:
                    if '/' not in self.ui.regismem_BP.text():
                        self.ui.fieldNotice.setText('Invalid BP.')
                        self.ui.invalid_notice.setFixedWidth(391)
                        QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 
                    else:
                        self.check_duplicate_phone_number()

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
        conn = None
        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)

        #     cursor = conn.cursor()
        #     cursor.execute("SELECT CONCAT(EMP_FNAME, ' ', EMP_LNAME) FROM EMPLOYEE WHERE EMP_POSITION = 'INSTRUCTOR';")
        #     employees = cursor.fetchall()
        #     self.ui.payment_instructor.clear()

        #     self.ui.payment_instructor.addItem('Instructor')
        #     for employee in employees:
        #         emp_name = employee[0]
        #         self.ui.payment_instructor.addItem(emp_name)

        #     self.ui.payment_instructor.addItem('None')

        # except (Exception, psycopg2.Error) as error:
        #     print("Error retrieving data from the database:", error)

        # finally:
        #     # Close the cursor and database connection
        #     if conn is not None:
        #         conn.close()

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
            conn = None
            # try:
            #     params = config()
            #     conn = psycopg2.connect(**params)

            #     cursor = conn.cursor()
            #     cursor.execute("DELETE FROM MEMBER WHERE MEM_ID = '" + mem_id.text() + "';")
            #     conn.commit()
            #     self.ui.mem_table.removeRow(selected_row)
            #     self.ui.member_delete_popup.setFixedWidth(0)
            #     self.populate_mem_table()
                
            # except (Exception, psycopg2.Error) as error:
            #     print("Error retrieving data from the database:", error)
            # finally:
            #     if conn is not None:
            #         conn.close()    

            #         self.ui.delete_notif.setFixedWidth(81)
            #         QtCore.QTimer.singleShot(1300, lambda: self.ui.delete_notif.setFixedWidth(0)) 
     
            
    #Displaying the member details in the edit page
    def edit_member(self):
        selected_row = -1

        if len(self.ui.mem_table.selectedItems()) > 0:
            selected_row = self.ui.mem_table.currentRow()

        if selected_row != -1:
            self.ui.edit_details_popup.setFixedWidth(1381)
            mem_id = self.ui.mem_table.item(selected_row, 0)
            conn = None
            # try:
            #     params = config()
            #     conn = psycopg2.connect(**params)

            #     cursor = conn.cursor()
            #     cursor.execute("SELECT MEM_FNAME, MEM_LNAME, MEM_BIRTHDATE, MEM_ADDRESS, MEM_TELEPHONE, MEM_PHYSICAL_ACT, MEM_MED_AILMENT, MEM_WEIGHT, MEM_HEIGHT," +
            #                     "MEM_BP, MEM_GENDER, MEM_STATUS, MEM_TYPE, MEM_PREV_GYM FROM MEMBER WHERE MEM_ID = '" + mem_id.text() + "';")
            #     member = cursor.fetchone()

            #     if member:
            #         mem_fname, mem_lname, mem_bod, mem_add, mem_tel, mem_phys_act, mem_med_ailment, mem_weight, mem_height, mem_bp, mem_gender, mem_stat, mem_type, mem_prev_gym = member
            #         self.ui.mem_fname.setText(str(mem_fname))
            #         self.ui.mem_lname.setText(str(mem_lname))
            #         self.ui.mem_DOB.setDate(mem_bod)
            #         self.ui.mem_address.setText(str(mem_add))
            #         self.ui.mem_contact.setText(str(mem_tel))
            #         self.ui.mem_physicalAct.setText(str(mem_phys_act))
            #         self.ui.mem_medic_ailments.setText(str(mem_med_ailment))
            #         self.ui.mem_weight.setText(str(mem_weight))
            #         self.ui.mem_height.setText(str(mem_height))
            #         self.ui.mem_BP.setText(str(mem_bp))
            #         self.ui.memGender_comboBox.setCurrentText(str(mem_gender))
            #         self.ui.memStat_comboBox.setCurrentText(str(mem_stat))
            #         if mem_type == 'STUDENT':
            #             self.ui.memStud_radiobtn.setChecked(True)
            #         else:
            #             self.ui.memProf_radiobtn.setChecked(True)
            #         self.ui.mem_prevGym.setText(str(mem_prev_gym))
            #     else:
            #         print("No member found for MEM_ID:", mem_id.text())
            # except (Exception, psycopg2.Error) as error:
            #     print("Error retrieving data from the database:", error)
            # finally:
            #     if conn is not None:
            #         conn.close()                       

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

        update_fname = self.ui.mem_fname.text()
        update_lname = self.ui.mem_lname.text()
        update_address = self.ui.mem_address.text()
        update_DOB = self.ui.mem_DOB.date().toString('yyyy-MM-dd')
        update_contact = self.ui.mem_contact.text()
        update_medical = self.ui.mem_medic_ailments.text()
        update_type = self.get_selected_radio_button_update()
        update_prevgym = self.ui.mem_prevGym.text()
        update_BP = self.ui.mem_BP.text()
        update_stat = self.ui.memStat_comboBox.currentText()
        update_physAct = self.ui.mem_physicalAct.text()
        update_weight = self.ui.mem_weight.text()
        update_height = self.ui.mem_height.text()
        update_gender = self.ui.memGender_comboBox.currentText()

        sql = "UPDATE MEMBER SET MEM_FNAME = %s, MEM_LNAME = %s, MEM_BIRTHDATE = %s, MEM_ADDRESS = %s, MEM_TELEPHONE = %s, MEM_PHYSICAL_ACT = %s, MEM_MED_AILMENT = %s, MEM_WEIGHT = %s, MEM_HEIGHT = %s, MEM_BP = %s, MEM_GENDER = %s, MEM_STATUS = %s, MEM_TYPE = %s, MEM_PREV_GYM = %s WHERE MEM_ID = %s;"
        values = (update_fname.upper(), update_lname.upper(), update_DOB, update_address.upper(), update_contact, update_physAct.upper(), update_medical.upper(), update_weight, update_height, update_BP, update_gender.upper(), update_stat.upper(), update_type.upper(), update_prevgym.upper(), mem_id.text())
        conn = None
        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)
        #     cursor = conn.cursor()
        #     cursor.execute(sql, values)
        #     conn.commit()
        #     self.ui.mem_fname.setText('')
        #     self.ui.mem_lname.setText('')
        #     self.ui.mem_DOB.setDate(QDate(2000, 1, 1))
        #     self.ui.mem_address.setText('')
        #     self.ui.mem_contact.setText('')
        #     self.ui.mem_physicalAct.setText('')
        #     self.ui.mem_medic_ailments.setText('')
        #     self.ui.mem_weight.setText('')
        #     self.ui.mem_height.setText('')
        #     self.ui.mem_BP.setText('')
        #     self.ui.memGender_comboBox.setCurrentText('Gender')
        #     self.ui.memStat_comboBox.setCurrentText('Status')
        #     self.ui.memProf_radiobtn.setChecked(False)
        #     self.ui.memStud_radiobtn.setChecked(False)
        #     self.ui.mem_prevGym.setText('')
        #     self.populate_mem_table()
        #     self.ui.edit_details_popup.setFixedWidth(0)
        #     self.ui.savechanges_widget.setFixedWidth(341)
        #     QtCore.QTimer.singleShot(1300, lambda: self.ui.savechanges_widget.setFixedWidth(0))  
    
        # except (Exception, psycopg2.Error) as error:
        #     self.ui.fieldNotice.setText('Phone number is already used.')
        #     self.ui.invalid_notice.setFixedWidth(391)
        #     QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0))

        # finally:
        #     if conn is not None:
        #         conn.close()

    #Cancel edit member
    def cancel_edit_mem(self):
        self.ui.edit_details_popup.setFixedWidth(0)

    #Automatically displays the  cost of service during payment
    def update_payment_amount(self):
        servicename = self.ui.paymentServices_cmbBox.currentText()
        service_id, serv_price = self.get_service_id(servicename)

        if serv_price is not None:
            self.ui.payment_amt.setText(str(serv_price))
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
    def get_service_id(self, servicename):
        pass
        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)
        #     cursor = conn.cursor()

        #     cursor.execute("SELECT SERV_ID, SERV_PRICE FROM SERVICE WHERE SERV_TYPE = %s;", (servicename,))
        #     service = cursor.fetchone() 
        #     if service:
        #         serv_id, serv_price = service  
        #         return serv_id, serv_price
        #     else:
        #         return None, None

        # except (Exception, psycopg2.Error) as error:
        #     print("Error retrieving data from the database:", error)
        #     return None, None
        # finally:
        #     if conn is not None:
        #         conn.close()


    #Displaying all members in the members list table
    def populate_mem_table(self):
        conn = None
        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)

        #     sql = "SELECT MEM_ID, MEM_FNAME, MEM_LNAME, MEM_BIRTHDATE, MEM_GENDER, MEM_ADDRESS FROM MEMBER"
        #     cursor = conn.cursor()
        #     cursor.execute(sql)
        #     result = cursor.fetchall()
            
        #     self.ui.mem_table.setRowCount(0)

        #     for row_number, row_data in enumerate(result):
        #         self.ui.mem_table.insertRow(row_number)
        #         for column_number, data in enumerate(row_data):
        #             item = QtWidgets.QTableWidgetItem(str(data))
        #             item.setTextAlignment(Qt.AlignHCenter)
        #             self.ui.mem_table.setItem(row_number, column_number, item)
            
        # except (Exception, psycopg2.Error) as error:
        #     print("Error retrieving data from the database:", error)
        
        # finally:
        #     if conn is not None:
        #         conn.close()

    def check_duplicate_phone_number(self):
        phonenum = self.ui.regismem_contact.text()
        
        is_phone_exist = self.membersdb.count_documents({"contact" : phonenum})

        if is_phone_exist == 0:
            self.regis_save()
        else:
            self.ui.fieldNotice.setText('Phone number is already used.')
            self.ui.invalid_notice.setFixedWidth(391)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 

        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)

        #     sql = "SELECT * FROM MEMBER WHERE MEM_TELEPHONE = '" + phonenum + "';"
        #     cursor = conn.cursor()
        #     cursor.execute(sql)
        #     check = cursor.fetchall()
            
        #     if check:
        #         self.ui.fieldNotice.setText('Phone number is already used.')
        #         self.ui.invalid_notice.setFixedWidth(391)
        #         QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0)) 
        #     else:
        #         self.regis_save()

        # except (Exception, psycopg2.Error) as error:
        #     print("Error retrieving data from the database:", error)
        
        # finally:
        #     if conn is not None:
        #         conn.close()

    #Add a member to DB
    def add_member_into_DB(self):
        self.ui.confirm_pay_widget.setFixedWidth(0)

        mem_fname = self.ui.regismem_fname.text().upper()
        mem_lname = self.ui.regismem_lname.text().upper()
        mem_address = self.ui.regismem_address.text().upper()
        mem_DOB = self.ui.regismem_DOB.date().toString('yyyy-MM-dd')
        mem_contact = self.ui.regismem_contact.text()
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
            'address' : mem_address,
            'dob' : mem_DOB,
            'contact' : mem_contact,
            'medical' : mem_medical,
            'previous gym': mem_prevGym,
            'bp' : mem_BP,
            'status' : mem_stat,
            'activity' : mem_act,
            'weight' : mem_weight,
            'height' : mem_height,
            'gender' : mem_gender,
            'type' : mem_type
        }

        result = self.membersdb.insert_one(member)

        if result:
            if float(tendered_amount) > (float(serv_price) + float(mship_fee)):
                self.ui.change_popup.setFixedWidth(1381)
                change = float(tendered_amount) - (float(serv_price) + float(mship_fee))
                self.ui.change_field.setText(f"{change:.2f}")
                self.populate_mem_table()

            self.ui.register_popup.setFixedWidth(0)
            self.ui.payment_popup.setFixedWidth(0) 

            self.ui.success_widget.setFixedWidth(371)
            QtCore.QTimer.singleShot(1300, lambda: self.ui.success_widget.setFixedWidth(0))  

            self.add_service_log_into_DB(service_id, mem_contact)
            self.add_transaction_DB(service_id, float(serv_price) + float(mship_fee), tendered_amount, mem_contact)  

        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)

        #     cur= conn.cursor()
        #     cur.execute(sql, values)
        #     conn.commit()
        #     cur.close

        #     if float(tendered_amount) > (float(serv_price) + float(mship_fee)):
        #             self.ui.change_popup.setFixedWidth(1381)
        #             change = float(tendered_amount) - (float(serv_price) + float(mship_fee))
        #             self.ui.change_field.setText(f"{change:.2f}")
        #             self.populate_mem_table()
        #     self.ui.register_popup.setFixedWidth(0)
        #     self.ui.payment_popup.setFixedWidth(0) 

        #     self.ui.success_widget.setFixedWidth(371)
        #     QtCore.QTimer.singleShot(1300, lambda: self.ui.success_widget.setFixedWidth(0))  
      
        #     self.add_service_log_into_DB(service_id, mem_contact)
        #     self.add_transaction_DB(service_id, float(serv_price) + float(mship_fee), tendered_amount, mem_contact)  

        # except (Exception, psycopg2.Error) as error:
        #     print(error)
        # finally:
        #     if conn is not None:
        #         conn.close()
                            
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
        conn = None
        sql = "INSERT INTO TRANSACTION_HISTORY(TRAN_DATE, SERV_ID, TRAN_PRICE, TRAN_TENDERED, MEM_ID) VALUES(CURRENT_DATE, %s, %s, %s, (SELECT MEM_ID FROM MEMBER WHERE MEM_TELEPHONE = %s))"
        values = (serv_id, pay_totalAmount, pay_tenderedAmount, mem_contact)

        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)

        #     cur= conn.cursor()
        #     cur.execute(sql, values)
        #     conn.commit()
        #     cur.close

        # except(Exception, psycopg2.DataError) as error:
        #     print(error)
        # finally:
        #     if conn is not None:
        #         conn.close()

        self.populate_transact_table()

    #Displaying all transactions done in the table
    def populate_transact_table(self):
        conn = None
        sql = "SELECT TRAN_ID, MEM_ID, CONCAT(MEM_FNAME, ' ', MEM_LNAME), DATE(TRAN_DATE), SERV_TYPE, TRAN_PRICE, TRAN_TENDERED FROM TRANSACTION_HISTORY LEFT JOIN SERVICE ON TRANSACTION_HISTORY.SERV_ID = SERVICE.SERV_ID NATURAL JOIN MEMBER"

        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)

        #     cur= conn.cursor()
        #     cur.execute(sql)
        #     result = cur.fetchall()
  
        #     self.ui.transac_table.setRowCount(0)
        #     for row_number, row_data in enumerate(result):
        #         self.ui.transac_table.insertRow(row_number)
        #         for column_number, data in enumerate(row_data):
        #             item = QtWidgets.QTableWidgetItem(str(data))
        #             item.setTextAlignment(Qt.AlignHCenter)
        #             self.ui.transac_table.setItem(row_number, column_number, item)
                    
        #             if column_number == 5:
        #                 item = QtWidgets.QTableWidgetItem(f"{float(row_data[6]) - float(row_data[5]):.2f}")
        #                 item.setTextAlignment(Qt.AlignHCenter)
        #                 self.ui.transac_table.setItem(row_number, 7, item)
        
        # except (Exception, psycopg2.Error) as error:
        #     print("Error retrieving data from the database:", error)
        
        # finally:
        #     if conn is not None:
        #         conn.close()
    
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
            emp_id = self.ui.emp_table.item(selected_row, 0)
            conn = None
            # try:
            #     params = config()
            #     conn = psycopg2.connect(**params)

            #     cursor = conn.cursor()
            #     cursor.execute("SELECT EMP_FNAME, EMP_LNAME, EMP_ADDRESS, EMP_BIRTHDATE, EMP_CONTACT_NUM FROM EMPLOYEE WHERE EMP_ID = '" + emp_id.text() +"';")
            #     employee_data = cursor.fetchone()

            #     if employee_data:
            #         emp_fname, emp_lname, emp_address, emp_birthdate, emp_contact_num = employee_data
            #         self.ui.AddEmp_fname.setText(str(emp_fname))
            #         self.ui.AddEmp_lname.setText(str(emp_lname))
            #         self.ui.AddEmp_address.setText(str(emp_address))
            #         self.ui.AddEmp_DOB.setDate(QDate(emp_birthdate))
            #         self.ui.AddEmp_contact.setText(str(emp_contact_num))

            #     else:
            #         print("No service found for SERV_ID:", emp_id.text())


            # except (Exception, psycopg2.Error) as error:
            #     print("Error retrieving data from the database:", error)

            # finally:
            #     # Close the cursor and database connection
            #     if conn is not None:
            #         conn.close()
        else:
             self.ui.rowSelection_notice.setFixedWidth(301)
             QtCore.QTimer.singleShot(1300, lambda: self.ui.rowSelection_notice.setFixedWidth(0))  

    #Cancel deletion
    def cancel_delete_employee(self):
        self.ui.employee_delete_popup.setFixedWidth(0)

    #Displaying all employees in the employees list table
    def populate_employee_table(self):
        conn = None
        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)

        #     sql = "SELECT EMP_ID, EMP_FNAME, EMP_LNAME, EMP_CONTACT_NUM, EMP_ADDRESS, EMP_POSITION FROM EMPLOYEE"
        #     cursor = conn.cursor()
        #     cursor.execute(sql)
        #     result = cursor.fetchall()
            
        #     self.ui.emp_table.setRowCount(0)

        #     for row_number, row_data in enumerate(result):
        #         self.ui.emp_table.insertRow(row_number)
        #         for column_number, data in enumerate(row_data):
        #             item = QtWidgets.QTableWidgetItem(str(data))
        #             item.setTextAlignment(Qt.AlignHCenter)
        #             self.ui.emp_table.setItem(row_number, column_number, item)
            
        # except (Exception, psycopg2.Error) as error:
        #     print("Error retrieving data from the database:", error)
        
        # finally:
        #     if conn is not None:
        #         conn.close()

    def cancel_assigned_emp_delete(self):
        self.ui.assigned_emp_delete.setFixedWidth(0)

    def check_emp_exist_in_service_log(self):
        selected_row = self.ui.emp_table.currentRow()
        emp_id = self.ui.emp_table.item(selected_row, 0)
        conn = None
        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)
        #     sql = "SELECT * FROM MONTHLY_SERVICE_LOG WHERE EMP_ID = '" + emp_id.text() + "';"
        #     cursor = conn.cursor()
        #     cursor.execute(sql)
        #     empIsPresent = cursor.fetchall()

        #     if empIsPresent:
        #         self.ui.assigned_emp_delete.setFixedWidth(1381)
        #     else:
        #         self.ui.employee_delete_popup.setFixedWidth(1381)
        # except (Exception, psycopg2.Error) as error:
        #     print(error)

    
    #Confirm deletion
    def confirm_delete_employee(self):
        selected_row = self.ui.emp_table.currentRow()
        emp_id = self.ui.emp_table.item(selected_row, 0)
        conn = None
        exception_flag = False
        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)
        #     cursor = conn.cursor()
        #     cursor.execute("DELETE FROM EMPLOYEE WHERE EMP_ID = '" + emp_id.text() + "';")
        #     conn.commit()
        #     self.ui.emp_table.removeRow(selected_row)
        #     self.ui.assigned_emp_delete.setFixedWidth(0)
        #     self.ui.employee_delete_popup.setFixedWidth(0)
        #     self.retrieve_employee_from_DB()
        #     self.retrieve_employee_from_DB_renew()
        #     self.populate_employee_table()
            
        # except (Exception, psycopg2.Error) as error:
        #     exception_flag = True
        #     self.ui.assigned_emp_delete.setFixedWidth(0)
        #     self.ui.employee_delete_popup.setFixedWidth(0)
        #     self.ui.fieldNotice.setText('Unable to delete admin')
        #     self.ui.invalid_notice.setFixedWidth(391)
        #     QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0))
        #     return
        # finally:
        #     if conn is not None:
        #         conn.close() 

        #         if not exception_flag:
        #             self.ui.delete_notif.setFixedWidth(81)
        #             QtCore.QTimer.singleShot(1300, lambda: self.ui.delete_notif.setFixedWidth(0))         

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
        emp_contact = self.ui.AddEmp_contact.text()
        emp_DOB = self.ui.AddEmp_DOB.date().toString('yyyy-MM-dd')
        
        if self.editEmployee == True:
            sql = "UPDATE EMPLOYEE SET EMP_FNAME = %s, EMP_LNAME = %s, EMP_ADDRESS = %s, EMP_BIRTHDATE = %s, EMP_CONTACT_NUM = %s WHERE EMP_ID = %s;"
            values = (emp_fname.upper(), emp_lname.upper(), emp_address.upper(), emp_DOB, emp_contact, emp_id)
        else:
            sql = "INSERT INTO EMPLOYEE(EMP_FNAME, EMP_LNAME, EMP_ADDRESS, EMP_BIRTHDATE, EMP_CONTACT_NUM, EMP_POSITION) VALUES(%s, %s, %s, %s, %s, %s)"
            values = (emp_fname, emp_lname, emp_address, emp_DOB, emp_contact, emp_position)   

            

        conn = None
        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)

        #     cur= conn.cursor()
        #     cur.execute(sql, values)
        #     conn.commit()
            
        #     #clear text fields
        #     if self.editEmployee == False:
        #         self.ui.AddEmp_contact.setText('')
        #         self.ui.AddEmp_fname.setText('')
        #         self.ui.AddEmp_lname.setText('')
        #         self.ui.AddEmp_address.setText('')
        #         self.ui.AddEmp_DOB.setDate(QDate(2000, 1, 1))
        #         self.ui.success_widget.setFixedWidth(341)
        #         QtCore.QTimer.singleShot(1300, lambda: self.ui.success_widget.setFixedWidth(0))  
        #         self.retrieve_employee_from_DB_renew()
        #         self.retrieve_employee_from_DB()
        #         self.populate_employee_table()
        #         self.adminIsExist()
        #         self.ui.add_employee_popup.setFixedWidth(0)
        #     else:
        #         self.ui.AddEmp_contact.setText('')
        #         self.ui.AddEmp_fname.setText('')
        #         self.ui.AddEmp_lname.setText('')
        #         self.ui.AddEmp_address.setText('')
        #         self.ui.savechanges_widget.setFixedWidth(341 )
        #         QtCore.QTimer.singleShot(1300, lambda: self.ui.savechanges_widget.setFixedWidth(0))  
        #         self.populate_employee_table()
        #         self.ui.add_employee_popup.setFixedWidth(0)
                
        # except(Exception, psycopg2.DataError) as error:
        #     self.ui.fieldNotice.setText('Phone number is already used.')
        #     self.ui.invalid_notice.setFixedWidth(391)
        #     QtCore.QTimer.singleShot(1300, lambda: self.ui.invalid_notice.setFixedWidth(0))
        # finally:
        #     if conn is not None:
        #         conn.close()

    # ===========================================================================================================================================================================
    # Expired membership deletion
    # ===========================================================================================================================================================================

    #Automatically deletes a member if membership has expired
    def delete_expiredMship(self):
        while True:
            # try:
            #     params = config()
            #     conn = psycopg2.connect(**params)

            #     sql = "DELETE FROM MEMBER WHERE MEM_MEMBERSHIP_END_DATE <= CURRENT_TIMESTAMP"
            #     cursor = conn.cursor()
            #     cursor.execute(sql)
            #     conn.commit()
            # except (Exception, psycopg2.Error) as error:
            #     print("Error retrieving data from the database:", error)
            
            # finally:
            #     if conn is not None:
            #         conn.close()
            break
            
    # ===========================================================================================================================================================================
    # Notification
    # ===========================================================================================================================================================================

    #Notification display
    def notif_area_displaySize(self):
        if self.ui.notif_table.height() == 41:
            self.maximize_notifArea()
        else:
            self.minimize_notifArea()

    def maximize_notifArea(self):
        self.ui.notif_table.setFixedHeight(651)
        self.ui.expand_notif.setFixedWidth(0)
        self.ui.minimize_notif.setFixedWidth(30)

    def minimize_notifArea(self):
        self.ui.notif_table.setFixedHeight(41)
        self.ui.expand_notif.setFixedWidth(30)
        self.ui.minimize_notif.setFixedWidth(0)

    #Constantly checking the status of monthly service access
    def monitor_monServiceAccess(self):
        while True:
            # try:
            #     params = config()
            #     conn = psycopg2.connect(**params)
            #     cursor = conn.cursor()

            #     interval = [
            #         (7, "monthly service access has 7 remaining days."),
            #         (1, "monthly service access will expire after 24 hours."),
            #         (0, "monthly service access has expired.")
            #     ] 
                
            #     for days, notification in interval:
            #         cursor.execute("""
            #                        SELECT MEM_ID FROM MONTHLY_SERVICE_LOG WHERE 
            #                        (MON_SERVICE_END_DATE - INTERVAL '%s days') <= CURRENT_TIMESTAMP 
            #                        AND MEM_ID NOT IN (SELECT MEM_ID 
            #                        FROM NOTIFICATION WHERE NOTIF_CONTENT LIKE %s);
            #                        """,
            #                        (days, f'%{notification}%'))
            #         monthly_serviceAccess = cursor.fetchall()

            #         if monthly_serviceAccess:
            #             for row_data in monthly_serviceAccess:
            #                 mem_id = row_data[0]

            #                 sql = """ 
            #                 INSERT INTO NOTIFICATION (NOTIF_CONTENT, NOTIF_DATE, MEM_ID, EMP_ID)
            #                 VALUES (
            #                     CONCAT('(ID: ', %s, ') ', 
            #                         (SELECT MEM_FNAME FROM MEMBER WHERE MEM_ID = %s), ' ',
            #                         (SELECT MEM_LNAME FROM MEMBER WHERE MEM_ID = %s),
            #                         %s),
            #                     (SELECT (MON_SERVICE_END_DATE - INTERVAL '%s days') FROM MONTHLY_SERVICE_LOG WHERE MEM_ID = %s), 
            #                     %s, 
            #                     (SELECT EMP_ID FROM EMPLOYEE WHERE EMP_POSITION = 'ADMINISTRATOR')
            #                 )
            #                 """
            #                 cursor.execute(sql, (mem_id, mem_id, mem_id, f"'s {notification}", days, mem_id, mem_id))
            #                 conn.commit()
            #                 self.display_notifs()
            #                 self.ui.new_notifbtn.setFixedWidth(271)
            #                 QtCore.QTimer.singleShot(1300, lambda: self.ui.new_notifbtn.setFixedWidth(0))    

            #                 if days == 0: self.populate_monServiceLog()
       

            # except (Exception, psycopg2.Error) as error:
            #     print("Error retrieving data from the database:", error)
            # finally:
            #     if conn is not None:
            #         conn.close()   
                          
            # time.sleep(1)

                break

    def monitor_membership(self):
        while True:
            # try:
            #     params = config()
            #     conn = psycopg2.connect(**params)     
            #     cursor = conn.cursor()

                
            #     interval = [
            #         (30, "membership has 30 remaining days."),
            #         (15, "membership has 15 remaining days."),
            #         (3, "membership has 3 remaining days."),
            #         (1, "membership will expire after 24 hours."),
            #         (0, "membership has expired.")
            #     ] 

            #     for days, notification in interval:
            #         cursor.execute("""
            #                        SELECT MEM_ID FROM MEMBER 
            #                        WHERE (MEM_MEMBERSHIP_END_DATE - INTERVAL '%s days') <= CURRENT_TIMESTAMP 
            #                        AND MEM_ID NOT IN (SELECT MEM_ID 
            #                        FROM NOTIFICATION WHERE NOTIF_CONTENT LIKE %s);
            #                        """,
            #                        (days, f'%{notification}%'))

            #         memberships = cursor.fetchall()
            #         if memberships:
            #             for row_data in memberships:
            #                 mem_id = row_data[0]

            #                 # Insert the notificatioN
            #                 sql = """ 
            #                 INSERT INTO NOTIFICATION (NOTIF_CONTENT, NOTIF_DATE, MEM_ID, EMP_ID)
            #                 VALUES (
            #                     CONCAT('(ID: ', %s, ') ', 
            #                         (SELECT MEM_FNAME FROM MEMBER WHERE MEM_ID = %s), ' ',
            #                         (SELECT MEM_LNAME FROM MEMBER WHERE MEM_ID = %s),
            #                         %s),
            #                     (SELECT (MEM_MEMBERSHIP_END_DATE - INTERVAL '%s days') FROM MEMBER WHERE MEM_ID = %s), 
            #                     %s, 
            #                     (SELECT EMP_ID FROM EMPLOYEE WHERE EMP_POSITION = 'ADMINISTRATOR')
            #                 )
            #                 """

            #                 cursor.execute(sql, (mem_id, mem_id, mem_id, f"'s {notification}", days, mem_id, mem_id))
            #                 conn.commit()
            #                 self.display_notifs()
            #                 self.ui.new_notifbtn.setFixedWidth(271)
            #                 QtCore.QTimer.singleShot(1300, lambda: self.ui.new_notifbtn.setFixedWidth(0))   

            #                 if days == 0: self.populate_mem_table() 

            # except (Exception, psycopg2.Error) as error:
            #     print("Error retrieving data from the database:", error)
            # finally:
            #     if conn is not None:
            #         conn.close()   
                          
            # time.sleep(1)
                break

    #Displaying notifications in the home page
    def display_notifs(self):
        conn = None
        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)

        #     sql = "SELECT NOTIF_CONTENT, CONCAT(TO_CHAR(NOTIF_DATE, 'HH12:MI AM'), '  |  ', DATE(NOTIF_DATE)) FROM NOTIFICATION WHERE NOTIF_DATE BETWEEN CURRENT_TIMESTAMP - INTERVAL '30 Days' AND CURRENT_TIMESTAMP"
        #     cursor = conn.cursor()
        #     cursor.execute(sql)
        #     result = cursor.fetchall()
            
        #     self.ui.notif_table.setRowCount(0)

        #     for row_number, row_data in enumerate(result):
        #         self.ui.notif_table.insertRow(0)
        #         for column_number, data in enumerate(row_data):
        #             self.ui.notif_table.setItem(0, column_number, QtWidgets.QTableWidgetItem(str(data)))
            
        # except (Exception, psycopg2.Error) as error:
        #     print("Error retrieving data from the database:", error)
        
        # finally:
        #     if conn is not None:
        #         conn.close()

    # ===========================================================================================================================================================================
    # Monthly Service Log
    # ===========================================================================================================================================================================
    def add_service_log_into_DB(self, serv_id,mem_contact):

        sql = "INSERT INTO MONTHLY_SERVICE_LOG (MEM_ID, SERV_ID, EMP_ID) VALUES((SELECT MEM_ID FROM MEMBER WHERE MEM_TELEPHONE = %s), %s, %s);"
        values = (mem_contact, serv_id, self.emp_id)

        conn = None
        # try:
        #     params = config()
        #     conn = psycopg2.connect(**params)

        #     cur= conn.cursor()
        #     cur.execute(sql, values)
        #     conn.commit()
        #     cur.close
        #     self.populate_monServiceLog()
        # except (Exception, psycopg2.Error) as error:
        #     print(error)


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
    login = MainWindow()
    app.exec()
    

