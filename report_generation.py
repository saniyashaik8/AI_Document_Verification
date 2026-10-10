import os, csv
def generate_report(a,b,c,d):
    os.makedirs('output_reports', exist_ok=True)
    open('output_reports/report.csv','w').write(f'{b}')
    print('Report saved')
