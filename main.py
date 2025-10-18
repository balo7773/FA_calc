#!/usr/bin/python3

from FA import Company
import pprint

if __name__ == '__main__':
    company_name = str(input('Enter Company Name\n'))
    No_of_FY = int(input('Enter No of FY to be checked, (max of 5): '))
    financial_data = list()
    company = Company(company_name, No_of_FY)
# ...existing code...
    for no in range(company.no_of_fy):
        params = dict()
        print(f'Enter Financial Values for year {no + 1}: ')
        params['year'] = int(input('Enter Year: '))
        params['revenue'] = int(input('Enter Revenue: '))
        params['COGS'] = int(input('Enter cost of goods sold: '))
       # params['total_expenses'] = int(input('Enter total expenses(S,G&A): '))
        params['operating_income'] = int(input('Enter operating income: '))
       # params['deprcn_amotzn'] = int(input('Enter depreciation/amortization: '))
        params['finance_income'] = int(input('Enter finance income: '))
        params['finance_cost'] = int(input('Enter finance cost/interestexpense: '))
        params['PBT'] = int(input('Enter profit before task: '))
        params['net_profit'] = int(input('Enter net profit: '))
        params['outstanding_shares'] = int(input('Enter total number of outstanding shares: '))
        print()
        print('ENTER VALUES FROM BALANCE SHEET')
        params['asset'] = int(input('Enter total asset value: '))
        params['non_current_asset'] = int(input('Enter non current asset value: '))
        params['PPE'] = int(input('Enter PPE value: '))
        params['current_asset'] = int(input('Enter current asset vaue: '))
        params['cash_and_equivalent'] = int(input('Enter cash and equivalent: '))
        params['mktble_securities'] = int(input('Enter marketable securities .e.g. bond/stock in possesion: '))
        params['trade_recv'] = int(input('Enter trade receivables: '))
        params['inventory'] = int(input('Enter inventories: '))
        params['liabilities'] = int(input('Enter total liabilities: '))
        params['current_liabilities'] = int(input('Enter current liabilities: '))
        params['trade_payables'] = int(input('Enter trade payables: '))
        params['short_term_debt'] = int(input('Enter short term debt: '))
        params['non_current_liabilities'] = int(input('Enter non current liabilities: '))
        params['long_term_debt'] = int(input('Enter long term debt: '))
        params['book_value'] = int(input('Enter shareholders equity: '))
        params['retained_earnings'] = int(input('Enter retained earnings: '))
        print()
        print('ENTER VALUES FROM CASH FLOW STATEMENT')
        params['cash_from_opr'] = int(input('Enter cash from operating activities: '))
        params['capex'] = int(input('Enter capital expenditure: '))
        params['cash_from_invst'] = int(input('Enter cash from investing activities: '))
        params['cash_from_finance'] = int(input('Enter cash from financial activities: '))
        print('___________')
        params['market_cap'] = int(input('Enter market cap: '))
          
        try:
            company.add_params(params)
        except ValueError as e:
            print(f"Error adding data: {e}")
            print("Please re-enter the data for this year.")
            # In a real app, you might want to re-prompt for this year's data
            # For this script, we'll exit to prevent bad calculations.
            exit()

    # Calculate and display all metrics
    company.calculate_all_metrics()
    company.display_metrics()
