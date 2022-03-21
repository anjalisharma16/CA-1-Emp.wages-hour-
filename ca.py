#create employee class and attributes
class Employee():

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
        salary['RHW'] = min(Hoursworked, self.Reghours)#Regular Hours Worked
        salary['OHW'] = max(0, Hoursworked - self.Reghours)#OverTime Hours Worked
        salary['Regular rate'] = self.Hourlyrate
        salary['Overtime rate'] = self.Hourlyrate * self.OTMultiple
        salary['Regular pay'] = self.Hourlyrate * salary['RHW']
        salary['Overtime pay'] = max(salary['Overtime rate'] * salary['OHW'], 0)
        salary['Gross pay'] = salary['Regular pay'] + salary['Overtime pay']
        salary['Standard rate pay'] = self.Standardband
        salary['Higher rate pay'] = max(salary['Gross pay'] - self.Standardband, 0)
        salary['Standard tax'] = round(salary['Standard rate pay'] * 0.2, 2)
        salary['Higher tax'] = round(salary['Higher rate pay'] * 0.4, 2)
        salary['Total tax'] = salary['Standard tax'] + salary['Higher tax']
        salary['Tax credit'] = self.Taxcredit
        salary['Net deductions'] = salary['Higher tax'] + salary['Tax credit']
        salary['Net pay'] = max(0, salary['Gross pay'] - salary['Net deductions'])
        return salary
