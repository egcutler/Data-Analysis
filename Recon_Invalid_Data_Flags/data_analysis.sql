WITH CID_ACCOUNT AS (
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
	)

SELECT DISTINCT
CID.*,
AD.Address_ID,
AD.Address_Street,
AD.City,
AD.State,
AD.Zip_Code,
AD.Registered_Country,
AD.Flag_Street_Address

FROM CID_ACCOUNT CID
LEFT JOIN [Address Data With Flags] AD
ON CID.External_ID = AD.Bus_External_ID
GO