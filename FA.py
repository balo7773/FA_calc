#!/usr/bin/python3

# Income Statement Formulas

class Company:

    def __init__(self, name: str, FY: int):
        self.company_name = name
        self.var_list = list() # list for financial input
        self.output = dict()
        self.no_of_fy = FY

    def add_params(self, *var: dict):
        # addition of financial input
        var_1 = list(var) # turns tuple to list
        for  finance_input in var_1:
            if 'year' in finance_input: # checks for year input
                self.var_list.append(finance_input)
            else:
                return 'financial year not found'

    def show_params(self):
        return self.var_list
    
    def calculate_metrics(self, metrics_name, calc_function):
        check_year = set()
        answer = None
        result = 0
        if self.var_list is not None:
            for financial_input in self.var_list:
                year = financial_input.get('year')

                if year and year not in check_year:       
                    check_year.add(year)
                    try:
                        result = calc_function(financial_input)
                        answer = round(result, 2)
                    except ZeroDivisionError:
                        answer = 'Division by zero'
                    except Exception:
                        continue

                    if year not in self.output:
                        self.output[year] = {metrics_name : answer}
                    else:
                        self.output[year].update({metrics_name : answer})
                else:
                    return 'duplicate financial year exits'
        
        return answer
    
    def net_profit_margin(self):
        return self.calculate_metrics('net_profit_margin',
                                      lambda fi: ((fi.get('net_profit', 0) / fi.get('revenue', 1)) * 100)
        )
    
    def opr_profit_margin(self):
        return self.calculate_metrics('operating_profit_margin',
                                      lambda fi: ((fi.get('operating_income', 0) / fi.get('revenue', 1)) * 100)
        )
    
    def gross_profit_margin(self):
        return self.calculate_metrics('gross_profit_margin',
                                      lambda fi: ((fi.get('revenue', 0) - fi.get('COGS', 0)) / fi.get('revenue', 1)) * 100
        )
    
    def return_on_equity(self):
        return self.calculate_metrics('ROE',
                                      lambda  fi: (fi.get('net_profit', 0) / fi.get('book_value', 1)) * 100
        )
    
    def return_on_investment(self):
        return self.calculate_metrics('ROI',
                                      lambda fi: (fi.get('net_profit', 0) / (fi.get('asset', 1) - fi.get('current_liabilities', 0))) * 100
        )
    
    def return_on_asset(self):
        return self.calculate_metrics('ROA',
                                      lambda fi: (fi.get('net_profit', 0) / fi.get('asset', 1)) * 100
        )

    def return_on_capital_employed(self):
        return self.calculate_metrics('ROCE',
                                      lambda fi: (fi.get('operating_income', 0) / (fi.get('asset', 1) - fi.get('current_liabilities', 0))) * 100
        )
    
    def debt_to_equity(self):
        return self.calculate_metrics('debt_to_equity',
                                      lambda fi: (fi.get('short_term_debt', 0) + fi.get('long_term_debt', 0))  / fi.get('book_value', 1)
        )
    
    def equity_ratio(self):
        return self.calculate_metrics('equity_ratio',
                                      lambda fi: fi.get('book_value', 0) / fi.get('asset', 1)
        )
    
    def debt_ratio(self):
        return self.calculate_metrics('debt_to_asset',
                                      lambda fi: (fi.get('short_term_debt', 0) + fi.get('long_term_debt', 0)) / fi.get('asset', 1)
        )
    
    def asset_turnover_ratio(self):
        return self.calculate_metrics('asset_turnover',
                                      lambda fi: fi.get('revenue', 0) / fi.get('asset', 1)
        )
    
    def current_ratio(self):
        return self.calculate_metrics('current_ratio',
                                      lambda fi: fi.get('current_asset', 0) / fi.get('current_liabilities', 1)
        )
    
    def quick_ratio(self):
        return self.calculate_metrics('quick_ratio',
                                      lambda fi: (fi.get('cash_and_equivalent', 0) + fi.get('trade_recv', 0) 
                                                  + fi.get('mktble_securities', 0) )  / fi.get('current_liabilities', 1)
        )
    
    def cash_ratio(self):
        return self.calculate_metrics('cash_ratio',
                                      lambda fi: fi.get('cash_and_equivalent', 0)  / fi.get('current_liabilities', 1)
        )
    
    
    def cf_interest_coverage_ratio(self):
        return self.calculate_metrics('cash_flow_interest_coverage_ratio',
                                      lambda fi: fi.get('cash_from_opr', 0)  / fi.get('finance_cost', 1)
        )

    def ocf_to_capex_ratio(self):
        return self.calculate_metrics('ocf_to_capex',
                                      lambda fi: fi.get('cash_from_opr', 0)  / fi.get('capex', 1)
        )
    
    def operating_cf_ratio(self):
        return self.calculate_metrics('operating_cash_flow_ratio',
                                      lambda fi: fi.get('cash_from_opr', 0)  / fi.get('current_liabilities', 1)
        )
    
    def bvps(self):
        return self.calculate_metrics('book_value_per_share',
                                      lambda fi: fi.get('book_value', 0)  / fi.get('outstanding_shares', 1)
        )
    
    def earning_yield(self):
        return self.calculate_metrics('earnings_yield',
                                      lambda fi: ( fi.get('net_profit', 1) / fi.get('market_cap', 1)) * 100
        )
    
    def price_to_earnings(self):
        return self.calculate_metrics('price_to_earnings',
                                      lambda fi: fi.get('market_cap', 0)  / ( fi.get('net_profit', 1) / fi.get('outstanding_shares', 1) )
        )
    
    def price_to_book(self):
        return self.calculate_metrics('price_to_book',
                                      lambda fi: fi.get('market_cap', 0)  / fi.get('book_value', 1)
        )
    
    def price_to_sale(self):
        return self.calculate_metrics('price_to_sale',
                                      lambda fi: fi.get('market_cap', 0)  / fi.get('revenue', 1)
        )
    
    def price_to_fcf(self):
        return self.calculate_metrics('price_to_fcf',
                                      lambda fi: fi.get('market_cap', 0) / (fi.get('cash_from_opr', 1) - fi.get('capex', 0))
        )
    
    def entity_value(self):
        return self.calculate_metrics('EV',
                                      lambda fi: fi.get('market_cap', 0)
                                      + (fi.get('short_term_debt', 0) +  fi.get('long_term_debt', 0))
                                      - fi.get('cash_and_equivalent', 0)
        )
    

    def ev_to_operating_income(self):
        return self.calculate_metrics('EV_EBIT',
                                      lambda fi: (fi.get('market_cap', 0)
                                      + (fi.get('short_term_debt', 0) +  fi.get('long_term_debt', 0))
                                      - fi.get('cash_and_equivalent', 0)) / fi.get('operating_income', 0)
        )
    
    def ev_to_revenue(self):
        return self.calculate_metrics('EV_Revenue',
                                      lambda fi: (fi.get('market_cap', 0)
                                      + (fi.get('short_term_debt', 0) +  fi.get('long_term_debt', 0))
                                      - fi.get('cash_and_equivalent', 0)) / fi.get('revenue', 0)
        )

    def cagr(self, start_year, end_year, no_of_period):
        ans = ((end_year / start_year) ** (1 / no_of_period) - 1) * 100
        return f'CAGR between the period is {ans}%'


    def inventory_ratio(self):
        if self.no_of_fy < 2:
            return 'min no of period must not be less than 2'

        year_bfor_inventory = 0
        year_inventory = 0
        cogs = 0
        calc_year = int(input('Enter which year period is to be calculated from: '))
        year_bfor = calc_year - 1
        for financial_input in self.var_list:
            if calc_year == financial_input['year']:
                year_inventory = financial_input['inventory']
                cogs = financial_input['COGS']
            if year_bfor == financial_input['year']:
                year_bfor_inventory = financial_input['inventory']

        if year_inventory == 0 or year_bfor_inventory == 0:
            return None
        
        itr = cogs / (0.5 * (year_bfor_inventory + year_inventory))
        inv_days = 365 / itr
        if calc_year not in self.output:
            self.output[calc_year] = {}
        
        self.output[calc_year].update({'inventory_turnover_ratio': itr, 'inventory_days': inv_days})


    def calculate_all_metrics(self):
        # Call all metric methods to populate self.output
        self.net_profit_margin()
        self.opr_profit_margin()
        self.gross_profit_margin()
        self.return_on_equity()
        self.return_on_investment()
        self.return_on_asset()
        self.return_on_capital_employed()
        self.debt_to_equity()
        self.equity_ratio()
        self.debt_ratio()
        self.asset_turnover_ratio()
        self.current_ratio()
        self.quick_ratio()
        self.cash_ratio()
        self.cf_interest_coverage_ratio()
        self.ocf_to_capex_ratio()
        self.operating_cf_ratio()
        self.bvps()
        self.earning_yield()
        self.price_to_earnings()
        self.price_to_book()
        self.price_to_sale()
        self.price_to_fcf()
        self.entity_value()
        self.ev_to_operating_income()
        self.ev_to_revenue()

    def display_metrics(self):
        # Pretty print the output dictionary
        import pprint
        print(f"\nFinancial Metrics for {self.company_name}:")
        pprint.pprint(self.output)

    def custom_metric(self, metric_name: str, formula: str):
        """
        Calculates a user-defined financial metric for each year using a safe arithmetic formula.

        Args:
            metric_name (str): Name of the custom metric.
            formula (str): Arithmetic formula using financial parameters (e.g., 'net_profit / revenue * 100').

        Returns:
            dict: Results for each year, or error message if invalid.

        Raises:
            ValueError: If the formula is invalid or unsafe.
        """
        import re
        try:
            from simpleeval import simple_eval
        except ImportError:
            raise ImportError("simpleeval package is required for custom metric evaluation.")

        # Gather all allowed variable names from financial input
        allowed_vars = set()
        for fi in self.var_list:
            allowed_vars.update(fi.keys())

        # Tokenize the formula and validate each token
        token_pattern = r"[\w\.]+|[\+\-\*/\(\)\^]"
        tokens = re.findall(token_pattern, formula)
        for token in tokens:
            # Accept only allowed variable names, numbers, and arithmetic operators
            if not (
                token in allowed_vars or
                re.match(r"^[\d\.]+$", token) or
                token in '+-*/()^'
            ):
                raise ValueError(f"Invalid token in formula: {token}")

        # Replace '^' with '**' for Python exponentiation
        safe_formula = formula.replace('^', '**')

        results = {}
        for fi in self.var_list:
            # Prepare local variables for evaluation
            local_vars = {k: v for k, v in fi.items() if k in allowed_vars}
            try:
                # Evaluate formula safely using simple_eval
                val = simple_eval(safe_formula, names=local_vars)
                results[fi.get('year', 'unknown')] = round(val, 2)
            except ZeroDivisionError:
                results[fi.get('year', 'unknown')] = 'Division by zero'
            except Exception as e:
                results[fi.get('year', 'unknown')] = f'Error: {str(e)}'

        # Store results in output dictionary
        for year, value in results.items():
            if year not in self.output:
                self.output[year] = {}
            self.output[year][metric_name] = value

        return results



'''BUA_CEMENT = Company()

BUA_CEMENT.add_params({'year' : 2025, 'revenue' : 300000000, 'net_profit' : 40000000}, {'year' : 2024, 'revenue' : 200000000, 'net_profit' : 8000000})

print(BUA_CEMENT.net_profit_margin())'''