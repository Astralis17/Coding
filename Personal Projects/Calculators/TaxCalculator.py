USC = input("USC? True/False:")
GIncome = int(input("Gross Income:"))
Pension = int(input("Pension %:"))
Tax1 = int(input("Lower Tax Rate %:"))
Tax2 = int(input("Higher Tax Rate %:"))
Cutoffpoint = int(input("Standard Cutoff Point:"))
TaxCredit = int(input("Tax Credits:"))
incomeafterpensionpercent = 1 - Pension / 100
if Pension != 0:
    incomeafterpension =  GIncome * incomeafterpensionpercent
else:
    incomeafterpension = GIncome

if incomeafterpension - Cutoffpoint >= 0:
    cutoff = Cutoffpoint
else:
    cutoff = incomeafterpension
#Income Tax
m = cutoff * Tax1 / 100 

highercutoff = incomeafterpension -cutoff
n = highercutoff * Tax2 / 100

mn = m + n
IncomeTax = mn - TaxCredit
print("tax1",m)
print("tax2",n)
print("Cutoff",cutoff)
print("highercuttoff", highercutoff)
print("Income Tax To Pay: ", IncomeTax)

#Pension Contribution
PensionContribution =GIncome / 100 * Pension




#Universal Social Charge
if USC == True:
    endusc1 =0
    endusc2 =0
    endusc3 =0
    endusc4 =0

    uscnum1 = int(input("USC Income Band 1:"))
    uscnum2 = int(input("USC Income Band 2:"))
    uscnum3 = int(input("USC Income Band 3:"))
    uscnum4 = int(input("USC Income Band 4:"))

    if incomeafterpension < uscnum1:
        uscnum1 = GIncome
    elif incomeafterpension < uscnum2:
        uscnum2 = GIncome
    elif incomeafterpension < uscnum3:
        uscnum3 = GIncome
    elif incomeafterpension < uscnum4:
        uscnum4 = GIncome

    uscmult1 = uscnum1
    uscmult2 = uscnum2 - uscnum1
    uscmult3 = uscnum3 - uscnum2
    uscmult4 = uscnum4 - uscnum3

    if incomeafterpension >= uscnum1:
        endusc1 =uscmult1 * 0.005
    if incomeafterpension >= uscnum2:
        endusc2 =uscmult2 * 0.02
    if incomeafterpension >= uscnum3:
        endusc3 =uscmult3 * 0.045
    if incomeafterpension >= uscnum4:
        endusc4 =uscmult4 * 0.08

    totalUSC = endusc1 + endusc2 + endusc3 + endusc4

#P.R.S.I





netincome = GIncome - PensionContribution - IncomeTax - totalUSC
print("Pension Contributed:",PensionContribution )
print("Total USC deductions", totalUSC)
print("Net Income:",netincome )