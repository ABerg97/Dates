#-------------------------------------------------------------------------------
# Date Printer
#-------------------------------------------------------------------------------

def main():

    date = input('Enter date in form of mm/dd/yyyy')
    datefinal = convert(date)

    print (datefinal)

def convert(date):
    month = date[0:2]
    day = date[3:5]
    year = date [6:]
    transmonth = translate(month)
    dateconvert = transmonth + ' ' + day + ','+ ' ' + year
    dateconvert = str(dateconvert)
    return dateconvert

def translate(month):
    if month == '01':
        month = 'January'
    elif month == '02':
        month = 'February'
    elif month == '03':
        month = 'March'
    elif month == '04':
        month = 'April'
    elif month == '05':
        month = 'May'
    elif month == '06':
        month = 'June'
    elif month == '07':
        month = 'July'
    elif month == '08':
        month = 'August'
    elif month == '09':
        month = 'September'
    elif month == '10':
        month = 'October'
    elif month == '11':
        month = 'November'
    else:
        month = 'December'

    return month
main()
