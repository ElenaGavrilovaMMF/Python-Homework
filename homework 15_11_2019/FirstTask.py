# V4 По номеру месяца напечатать пору года
try:
    month = int(input('Enter the month:\n'))
    if month > 0:
        if month < 12:
            if month == 12 or month == 1 or month == 2:
                print('Month ', month, ' -> Winter')
            elif 3 <= month <= 5:
                print('Month ', month, ' -> Spring')
            elif 6 <= month <= 8:
                print('Month ', month, ' -> Summer')
            else:
                print('Month ', month, ' -> Autumn')
        else:
            print('There is no month the number of which more 12.')
    else:
        print('There is no negative month.')
except ValueError:
    print('You entered the wrong data type.')
