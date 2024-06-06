 CREATE TABLE SERVICE(
	SERV_ID				SERIAL					PRIMARY KEY,
	SERV_TYPE			VARCHAR(35)			NOT NULL,
	SERV_PRICE			NUMERIC(9,2)		DEFAULT 0.0
);



CREATE TABLE EMPLOYEE(
	EMP_ID				SERIAL 				PRIMARY KEY,
	EMP_NAME			VARCHAR(100)		NOT NULL,
	EMP_ADDRESS			VARCHAR(100)		NOT NULL,
	EMP_BIRTHDATE		DATE				DEFAULT CURRENT_TIMESTAMP,
	EMP_CONTACT_NUM		VARCHAR(20)			NOT NULL,	
	EMP_POSITION		VARCHAR(30)			NOT NULL
);

CREATE TABLE MEMBERS(
	MEM_ID				SERIAL					PRIMARY KEY,
	MEM_NAME			VARCHAR(100)		NOT NULL,
	MEM_BIRTHDATE		DATE				DEFAULT CURRENT_TIMESTAMP,
	MEM_ADDRESS			VARCHAR(100)		NOT NULL,
	MEM_TELEPHONE		VARCHAR(20)			NOT NULL,
	MEM_PHYSICAL_ACT	VARCHAR(100)		DEFAULT 'N/A',
	MEM_MED_AILMENT		VARCHAR(100)		DEFAULT 'N/A',
	MEM_WEIGHT			NUMERIC				NOT NULL,
	MEM_HEIGHT			NUMERIC				NOT NULL,
	MEM_BP				VARCHAR(35)			NOT NULL,
	MEM_GENDER			VARCHAR(20)			NULL,
	MEM_STATUS			VARCHAR(35)			NOT NULL,
	MEM_TYPE			VARCHAR(35)			NOT NULL,
	MEM_PREV_GYM		VARCHAR(50)			DEFAULT 'N/A',
	SERV_ID				INT					REFERENCES SERVICE ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
	EMP_ID				INT 				REFERENCES EMPLOYEE ON DELETE CASCADE ON UPDATE CASCADE
);

	
CREATE TABLE TRANSACTION_HISTORY(
	TRAN_ID				SERIAL					PRIMARY KEY,
	MEM_ID				INT					REFERENCES MEMBERS ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
	TRAN_DATE			DATE				DEFAULT CURRENT_TIMESTAMP,
	SERV_ID				INT					REFERENCES SERVICE ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
	TRAN_PRICE			NUMERIC(9,2)		NOT NULL,
	TRAN_TENDERED		NUMERIC(9,2)		NOT NULL,
	TRAN_CHANGE			NUMERIC(9,2)		NOT NULL
);
	
CREATE TABLE MEMBERSHIP(
	MEM_ID				INT 				REFERENCES MEMBERS ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
	SERV_ID				INT					REFERENCES SERVICE ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
	PRIMARY KEY(MEM_ID, SERV_ID)	
);