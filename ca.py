#create employee class and attributes
class Employee:

    def __init__(self, staffId, Firstname, Lastname, Reghours, Hourlyrate, OTMultiple, Taxcredit, Standardband):
        self.staffId = int(staffId)
        self.Firstname = str(Firstname)
        self.Lastname = str(Lastname)
        self.Reghours = int(Reghours)
        self.Hourlyrate = int(Hourlyrate)
        self.OTMultiple = float(OTMultiple)
        self.Taxcredit = int(Taxcredit)
        self.Standardband = int(Standardband)

    def computepayment(self, Hoursworked, Date):
        salary = dict()
        salary['Name'] = self.Firstname + " "
        salary['Date'] = Date
        salary['RHW'] = min(Hoursworked, self.Reghours)#To calculate Regular Hours Worked
        salary['OHW'] = max(0, Hoursworked - self.Reghours)#To calculate OverTime Hours Worked
        salary['Regular rate'] = self.Hourlyrate
        salary['Overtime rate'] = self.Hourlyrate * self.OTMultiple#To calculate Overtime rate
        salary['Regular pay'] = self.Hourlyrate * salary['RHW']#To calculate Regular pay
        salary['Overtime pay'] = max(salary['Overtime rate'] * salary['OHW'], 0)#To calculate Overtime pay
        salary['Gross pay'] = salary['Regular pay'] + salary['Overtime pay']#To calculate Gross pay
        salary['Standard rate pay'] = self.Standardband
        salary['Higher rate pay'] = max(salary['Gross pay'] - self.Standardband, 0)#To calculate Higher rate pay
        salary['Standard tax'] = salary['Standard rate pay'] * 0.2#To calculate Standard tax
        salary['Higher tax'] = round(salary['Higher rate pay'] * 0.4, 2)#To calculate Higher tax
        salary['Total tax'] = round(salary['Standard tax'] + salary['Higher tax'], 2)#To calculate Total tax 
        salary['Tax credit'] = self.Taxcredit
        salary['Net deductions'] = round(salary['Net tax'] + salary['PRSI'], 2)#To calculate Net deduction
        salary['Net pay'] = max(0, salary['Gross pay'] - salary['Net deductions'])#To calculate Net pay
        salary['Net tax'] =round(salary['Total tax'] - salary['Tax credit'], 2)#To calculate Net tax
        salary['PRSI'] = salary['Gross pay'] * 0.4#To calculate PRSI
        return salary