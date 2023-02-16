import os
a = 'office'
b = 'Reporte_DLP_Office_365_-_FIF_CMR_MX-2022-11-21.csv'

c = os.path.join(os.getcwd(),a, b)
print(c)