WITH 
CID_ACCOUNT AS (
	SELECT DISTINCT
	BA.External_ID,
	BA.Company_Name,
	BA.Business_Status,
	BA.Creation_Date,
	BA.Modified_Date,
	BA.Closed_Date,
	BA.Flag_Closed_Date_vs_Creation_Date,
	BA.Flag_Closed_Date_vs_Modified_Date,
	BA.Flag_Closed_Date_vs_Status AS 'Bus_Closed_Date_vs_Status',
	LE.Legal_Account,
	LE.Legal_Firm,
	LE.Legal_Status,
	LE.LE_Creation_Date,
	LE.LE_Modified_Date,
	LE.LE_Closed_Date,
	LE.Flag_LE_Closed_Date_vs_LE_Creation_Date,
	LE.Flag_LE_Closed_Date_vs_LE_Modified_Date,
	LE.Flag_Closed_Date_vs_Status AS 'LE_Closed_Date_vs_Status'

	FROM dbo.[Business Data With Flags] BA
	INNER JOIN dbo.[Legal Data With Flags] LE
	ON BA.External_ID = LE.Bus_External_ID
	WHERE BA.Business_Status = 'ACTIVE'
	AND LE.Legal_Status = 'ACTIVE'
	),

ADDRESS AS (
	SELECT DISTINCT
	AD.Address_ID,
	AD.Address_Street,
	AD.City,
	AD.State,
	AD.Zip_Code,
	AD.Registered_Country,
	AD.Flag_Street_Address,
	AD.Bus_External_ID

	FROM dbo.[Address Data With Flags] AD
),

EMPLOYEE AS (
	SELECT DISTINCT
	EMP.Employee_ID,
	EMP.Emp_First_Name,
	EMP.Emp_Last_Name,
	EMP.Employee_Status,
	EMP.Employee_Email,
	EMP.Job_Title,
	EMP.Flag_Email

	FROM dbo.[Employee Data With Flags] EMP
)

SELECT DISTINCT
C.*,
A.Address_ID,
A.Address_Street,
A.City,
A.State,
A.Zip_Code,
A.Registered_Country,
A.Flag_Street_Address,
A.Bus_External_ID,
E.*,
GETDATE() AS 'Time Stamp'

FROM CID_ACCOUNT C
LEFT JOIN ADDRESS A
ON C.External_ID = A.Bus_External_ID
LEFT JOIN dbo.[Employee System] ES
ON C.Legal_Account = ES.Legal_Account
LEFT JOIN EMPLOYEE E
ON ES.Employee_ID = E.Employee_ID

GO