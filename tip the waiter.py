def total_calc(bill_amount,tip_percent):
    total=bill_amount*(1+0.01*tip_percent)
    total=round(total,2)
    print(f'Please pay ${total}')



total_calc(133,50)