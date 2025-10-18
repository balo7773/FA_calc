#!/usr/bin/python3

# Income Statement Formulas

class Company:

    def __init__(self, name: str, no_of_periods: int, period_type: str = 'annual'):
        """
        Initializes the Company object.

        Args:
            name (str): The name of the company.
            no_of_periods (int): The number of periods (years or quarters) to be analyzed.
            period_type (str): The type of period, either 'annual' or 'quarterly'.
        """
        self.company_name = name
        self.no_of_periods = no_of_periods
        self.period_type = period_type

        if period_type not in ['annual', 'quarterly']:
            raise ValueError("period_type must be either 'annual' or 'quarterly'.")

        # Stores a list of financial input dictionaries, one for each period.
        self.var_list = list()
        # The main dictionary to store all calculated outputs.
        self.output = dict()

    def add_period_data(self, finance_input: dict):
        """
        Adds a dictionary of financial data for a single period (annual or quarterly).

        This method validates the input based on the company's period_type and ensures
        that the period has not already been added. It adds a '_period' key to the
        dictionary for internal use.

        Args:
            finance_input (dict): A dictionary containing financial parameters for one period.

        Raises:
            ValueError: If required keys are missing or if the period is a duplicate.
        """
        period_id = None
        if self.period_type == 'annual':
            if 'year' not in finance_input:
                raise ValueError("Input for annual data is missing the 'year' key.")
            period_id = finance_input['year']

        elif self.period_type == 'quarterly':
            if 'year' not in finance_input or 'quarter' not in finance_input:
                raise ValueError("Input for quarterly data is missing 'year' or 'quarter' keys.")
            if finance_input['quarter'] not in [1, 2, 3, 4]:
                raise ValueError("Quarter must be an integer between 1 and 4.")
            # Use a tuple for quarterly periods to make them sortable and unique
            period_id = (finance_input['year'], finance_input['quarter'])

        if period_id is None:
            raise ValueError("Could not determine the period identifier.")

        # Check for duplicate periods
        if any(fi.get('_period') == period_id for fi in self.var_list):
            raise ValueError(f"Financial data for period {period_id} already exists.")

        # Add the internal period identifier to the dictionary
        finance_input['_period'] = period_id

        self.var_list.append(finance_input)

    def show_params(self):
        """Returns the list of raw financial data dictionaries."""
        return self.var_list
    
    def calculate_metrics(self, metrics_name, calc_function):
        """
        A generic helper method to calculate a given metric for all fiscal years.

        This method iterates through the financial data for each year, applies the
        provided calculation function, and stores the result in the `self.output`
        dictionary, keyed by year. It handles errors like division by zero gracefully
        by storing `None` for the failed calculation, allowing other years to be processed.

        Args:
            metrics_name (str): The name of the metric to be calculated (e.g., 'net_profit_margin').
            calc_function (callable): A lambda or function that takes one argument
                                      (the financial input dict for a year) and returns the calculated metric.
        """
        check_year = set()
        result = 0
        if self.var_list is not None:
            # Sort by the internal period identifier to ensure chronological order
            self.var_list.sort(key=lambda x: x.get('_period', 0))
            for financial_input in self.var_list:
                period = financial_input.get('_period')

                if period and period not in check_year:
                    check_year.add(year)
                    answer = None  # Default to None in case of an error
                    try:
                        result = calc_function(financial_input)
                        answer = round(result, 2) if result is not None else None
                    except ZeroDivisionError:
                        # The calculation failed, 'answer' remains None
                        pass
                    
                    # Create the year's dictionary if it doesn't exist
                    self.output.setdefault(period, {})[metrics_name] = answer
                else:
                    # It's better to raise an error here or handle it in add_params
                    # For now, we'll just print a warning and skip.
                    print(f"Warning: Duplicate or missing period found. Skipping entry: {financial_input}")
    
    def net_profit_margin(self):
        """Calculates Net Profit Margin for all fiscal years."""
        self.calculate_metrics('net_profit_margin',
                                      lambda fi: ((fi.get('net_profit', 0) / fi.get('revenue', 1)) * 100)
        )
    
    def opr_profit_margin(self):
        """Calculates Operating Profit Margin for all fiscal years."""
        self.calculate_metrics('operating_profit_margin',
                                      lambda fi: ((fi.get('operating_income', 0) / fi.get('revenue', 1)) * 100)
        )
    
    def gross_profit_margin(self):
        """Calculates Gross Profit Margin for all fiscal years."""
        self.calculate_metrics('gross_profit_margin',
                                      lambda fi: ((fi.get('revenue', 0) - fi.get('COGS', 0)) / fi.get('revenue', 1)) * 100
        )
    
    def return_on_equity(self):
        """Calculates Return on Equity (ROE) for all fiscal years."""
        self.calculate_metrics('ROE',
                                      lambda  fi: (fi.get('net_profit', 0) / fi.get('book_value', 1)) * 100
        )
    
    def return_on_investment(self):
        """Calculates Return on Investment (ROI) for all fiscal years."""
        self.calculate_metrics('ROI',
                                      lambda fi: (fi.get('net_profit', 0) / (fi.get('asset', 1) - fi.get('current_liabilities', 0))) * 100
        )
    
    def return_on_asset(self):
        """Calculates Return on Assets (ROA) for all fiscal years."""
        self.calculate_metrics('ROA',
                                      lambda fi: (fi.get('net_profit', 0) / fi.get('asset', 1)) * 100
        )

    def return_on_capital_employed(self):
        """Calculates Return on Capital Employed (ROCE) for all fiscal years."""
        self.calculate_metrics('ROCE',
                                      lambda fi: (fi.get('operating_income', 0) / (fi.get('asset', 1) - fi.get('current_liabilities', 0))) * 100
        )
    
    def debt_to_equity(self):
        """Calculates Debt to Equity ratio for all fiscal years."""
        self.calculate_metrics('debt_to_equity',
                                      lambda fi: (fi.get('short_term_debt', 0) + fi.get('long_term_debt', 0))  / fi.get('book_value', 1)
        )
    
    def equity_ratio(self):
        """Calculates the Equity Ratio for all fiscal years."""
        self.calculate_metrics('equity_ratio',
                                      lambda fi: fi.get('book_value', 0) / fi.get('asset', 1)
        )
    
    def debt_ratio(self):
        """Calculates the Debt to Asset Ratio for all fiscal years."""
        self.calculate_metrics('debt_to_asset',
                                      lambda fi: (fi.get('short_term_debt', 0) + fi.get('long_term_debt', 0)) / fi.get('asset', 1)
        )
    
    def asset_turnover_ratio(self):
        """Calculates the Asset Turnover Ratio for all fiscal years."""
        self.calculate_metrics('asset_turnover',
                                      lambda fi: fi.get('revenue', 0) / fi.get('asset', 1)
        )
    
    def current_ratio(self):
        """Calculates the Current Ratio for all fiscal years."""
        self.calculate_metrics('current_ratio',
                                      lambda fi: fi.get('current_asset', 0) / fi.get('current_liabilities', 1)
        )
    
    def quick_ratio(self):
        """Calculates the Quick Ratio (Acid-Test Ratio) for all fiscal years."""
        self.calculate_metrics('quick_ratio',
                                      lambda fi: (fi.get('cash_and_equivalent', 0) + fi.get('trade_recv', 0) 
                                                  + fi.get('mktble_securities', 0) )  / fi.get('current_liabilities', 1)
        )
    
    def cash_ratio(self):
        """Calculates the Cash Ratio for all fiscal years."""
        self.calculate_metrics('cash_ratio',
                                      lambda fi: fi.get('cash_and_equivalent', 0)  / fi.get('current_liabilities', 1)
        )
    
    
    def cf_interest_coverage_ratio(self):
        """Calculates the Cash Flow Interest Coverage Ratio for all fiscal years."""
        self.calculate_metrics('cash_flow_interest_coverage_ratio',
                                      lambda fi: fi.get('cash_from_opr', 0)  / fi.get('finance_cost', 1)
        )

    def ocf_to_capex_ratio(self):
        """Calculates the Operating Cash Flow to CAPEX Ratio for all fiscal years."""
        self.calculate_metrics('ocf_to_capex',
                                      lambda fi: fi.get('cash_from_opr', 0)  / fi.get('capex', 1)
        )
    
    def operating_cf_ratio(self):
        """Calculates the Operating Cash Flow Ratio for all fiscal years."""
        self.calculate_metrics('operating_cash_flow_ratio',
                                      lambda fi: fi.get('cash_from_opr', 0)  / fi.get('current_liabilities', 1)
        )
    
    def bvps(self):
        """Calculates the Book Value Per Share (BVPS) for all fiscal years."""
        self.calculate_metrics('book_value_per_share',
                                      lambda fi: fi.get('book_value', 0)  / fi.get('outstanding_shares', 1)
        )
    
    def earning_yield(self):
        """Calculates the Earnings Yield for all fiscal years."""
        self.calculate_metrics('earnings_yield',
                                      lambda fi: ( fi.get('net_profit', 1) / fi.get('market_cap', 1)) * 100
        )
    
    def price_to_earnings(self):
        """Calculates the Price to Earnings (P/E) Ratio for all fiscal years."""
        self.calculate_metrics('price_to_earnings',
                                      lambda fi: fi.get('market_cap', 0)  / ( fi.get('net_profit', 1) / fi.get('outstanding_shares', 1) )
        )
    
    def price_to_book(self):
        """Calculates the Price to Book (P/B) Ratio for all fiscal years."""
        self.calculate_metrics('price_to_book',
                                      lambda fi: fi.get('market_cap', 0)  / fi.get('book_value', 1)
        )
    
    def price_to_sale(self):
        """Calculates the Price to Sales (P/S) Ratio for all fiscal years."""
        self.calculate_metrics('price_to_sale',
                                      lambda fi: fi.get('market_cap', 0)  / fi.get('revenue', 1)
        )
    
    def price_to_fcf(self):
        """Calculates the Price to Free Cash Flow (P/FCF) Ratio for all fiscal years."""
        self.calculate_metrics('price_to_fcf',
                                      lambda fi: fi.get('market_cap', 0) / (fi.get('cash_from_opr', 1) - fi.get('capex', 0))
        )

    def _calculate_ev(self, fi: dict) -> float:
        """Internal helper to calculate Enterprise Value for a single year."""
        return (fi.get('market_cap', 0)
                + fi.get('short_term_debt', 0)
                + fi.get('long_term_debt', 0)
                - fi.get('cash_and_equivalent', 0))
    
    def entity_value(self):
        """Calculates Enterprise Value (EV) for all years."""
        self.calculate_metrics('EV', self._calculate_ev)
    

    def ev_to_operating_income(self):
        """Calculates the EV to Operating Income (EBIT) ratio for all years."""
        self.calculate_metrics(
            'EV_EBIT',
            lambda fi: self._calculate_ev(fi) / fi.get('operating_income', 1)
        )
    
    def ev_to_revenue(self):
        """Calculates the EV to Revenue ratio for all years."""
        self.calculate_metrics(
            'EV_Revenue',
            lambda fi: self._calculate_ev(fi) / fi.get('revenue', 1)
        )

    def cagr(self, metric_name: str, start_year: int, end_year: int) -> float | None:
        """
        Calculates the Compound Annual Growth Rate (CAGR) for a specific metric.

        This method requires that the base metrics have already been calculated and
        are present in the `self.output` dictionary.

        Args:
            metric_name (str): The name of the metric to analyze (e.g., 'revenue', 'net_profit').
            start_year (int): The beginning year of the period.
            end_year (int): The ending year of the period.

        Returns:
            float: The calculated CAGR as a percentage, or None if data is invalid.
        
        Raises:
            ValueError: If start_year is after end_year, or if data is missing.
        """
        if start_year >= end_year:
            raise ValueError("The end_year must be after the start_year.")

        try:
            # We need the raw input values, not the calculated ratios for CAGR
            data_by_year = {fi['year']: fi for fi in self.var_list}
            start_value = data_by_year[start_year][metric_name]
            end_value = data_by_year[end_year][metric_name]
        except KeyError:
            raise ValueError(f"Metric '{metric_name}' or data for year not found.")

        if start_value <= 0 or end_value <= 0:
            return None  # CAGR is not meaningful for non-positive values

        num_periods = end_year - start_year
        cagr_value = ((end_value / start_value) ** (1 / num_periods) - 1) * 100
        return round(cagr_value, 2)


    def inventory_turnover_ratio(self):
        """Calculates inventory turnover for all years where prior year data is available."""
        # Create a dictionary for quick year-based lookups
        data_by_year = {fi['year']: fi for fi in self.var_list if 'year' in fi}

        for year, current_fi in data_by_year.items():
            previous_year_fi = data_by_year.get(year - 1)
            answer = None

            # Proceed only if we have data for the previous year
            if previous_year_fi:
                try:
                    cogs = current_fi.get('COGS', 0)
                    current_inventory = current_fi.get('inventory', 0)
                    previous_inventory = previous_year_fi.get('inventory', 0)
                    
                    # Avoid division by zero if average inventory is zero
                    avg_inventory = 0.5 * (current_inventory + previous_inventory)
                    if avg_inventory != 0:
                        turnover = cogs / avg_inventory
                        answer = round(turnover, 2)
                except (TypeError, KeyError):
                    # Handles cases where keys might be missing or data is not numeric
                    answer = None
            
            self.output.setdefault(year, {})['inventory_turnover_ratio'] = answer

    def inventory_days(self):
        """Calculates inventory days for all years where inventory turnover is available."""
        for year, metrics in self.output.items():
            answer = None
            # This metric depends on the inventory_turnover_ratio being calculated first
            turnover_ratio = metrics.get('inventory_turnover_ratio')

            if turnover_ratio is not None and turnover_ratio != 0:
                try:
                    days = 365 / turnover_ratio
                    answer = round(days, 2)
                except (TypeError, ZeroDivisionError):
                    answer = None
            
            # This assumes the year key already exists from previous calculations
            self.output.setdefault(year, {})['inventory_days'] = answer

    def calculate_qoq_growth(self):
        """
        Calculates the Quarter-on-Quarter (QoQ) growth for raw inputs and calculated metrics.

        This method is functionally similar to calculate_yoy_growth but is adapted for
        quarterly periods represented as (year, quarter) tuples.
        """
        # Helper function to safely calculate growth percentage
        def _get_growth(current_val, prev_val):
            if not all(isinstance(v, (int, float)) for v in [current_val, prev_val]):
                return None
            if prev_val == 0:
                return None
            try:
                growth = ((current_val - prev_val) / abs(prev_val)) * 100
                return round(growth, 2)
            except (TypeError, ZeroDivisionError):
                return None

        # Helper function to get the previous quarter from a (year, quarter) tuple
        def _get_prev_quarter(period):
            year, quarter = period
            if quarter == 1:
                return (year - 1, 4)
            else:
                return (year, quarter - 1)

        data_by_period = {fi['_period']: fi for fi in self.var_list if '_period' in fi}
        sorted_periods = sorted(self.output.keys())

        for period in sorted_periods:
            prev_period = _get_prev_quarter(period)
            if prev_period not in sorted_periods:
                continue

            # --- 1. Calculate QoQ for Raw Input Values ---
            current_inputs = data_by_period.get(period, {})
            prev_inputs = data_by_period.get(prev_period, {})
            all_input_keys = set(current_inputs.keys()) | set(prev_inputs.keys())
            
            for key in all_input_keys:
                if key not in ['year', 'quarter', '_period']:
                    current_val = current_inputs.get(key)
                    prev_val = prev_inputs.get(key)
                    growth = _get_growth(current_val, prev_val)
                    self.output[period][f'{key}_qoq_growth'] = growth

            # --- 2. Calculate QoQ for Calculated Ratios ---
            current_ratios = self.output.get(period, {})
            prev_ratios = self.output.get(prev_period, {})
            all_ratio_keys = {k for k in current_ratios if not k.endswith('_growth')}

            for key in all_ratio_keys:
                current_val = current_ratios.get(key)
                prev_val = prev_ratios.get(key)
                growth = _get_growth(current_val, prev_val)
                self.output[period][f'{key}_qoq_growth'] = growth


    def calculate_yoy_growth(self):
        """
        Calculates the Year-over-Year (YoY) growth for raw inputs and calculated metrics.

        This method should be called after all other metrics are calculated. It iterates
        through all years, calculating the percentage change from the prior year for each
        numerical data point and stores it back into the `self.output` dictionary.
        """
        # Helper function to safely calculate growth percentage
        def _get_growth(current_val, prev_val):
            # Ensure values are valid numbers for calculation
            if not all(isinstance(v, (int, float)) for v in [current_val, prev_val]):
                return None
            # Avoid division by zero
            if prev_val == 0:
                return None
            
            try:
                growth = ((current_val - prev_val) / abs(prev_val)) * 100
                return round(growth, 2)
            except (TypeError, ZeroDivisionError):
                return None

        # Create a dictionary of raw inputs for quick lookups by year
        data_by_year = {fi['year']: fi for fi in self.var_list if 'year' in fi}
        
        # Sort years to process chronologically
        sorted_years = sorted(self.output.keys())

        for year in sorted_years:
            prev_year = year - 1
            if prev_year not in sorted_years:
                # No previous year to compare against, so skip
                continue

            # --- 1. Calculate YoY for Raw Input Values ---
            current_inputs = data_by_year.get(year, {})
            prev_inputs = data_by_year.get(prev_year, {})
            
            # Find all numeric keys present in the input data
            all_input_keys = set(current_inputs.keys()) | set(prev_inputs.keys())
            
            for key in all_input_keys:
                if key != 'year': # Don't calculate growth for the year itself
                    current_val = current_inputs.get(key)
                    prev_val = prev_inputs.get(key)
                    growth = _get_growth(current_val, prev_val)
                    self.output[year][f'{key}_yoy_growth'] = growth

            # --- 2. Calculate YoY for Calculated Ratios ---
            current_ratios = self.output.get(year, {})
            prev_ratios = self.output.get(prev_year, {})

            # Find all ratio keys (excluding already calculated growth metrics)
            all_ratio_keys = {k for k in current_ratios if not k.endswith('_yoy_growth')}

            for key in all_ratio_keys:
                current_val = current_ratios.get(key)
                prev_val = prev_ratios.get(key)
                growth = _get_growth(current_val, prev_val)
                self.output[year][f'{key}_yoy_growth'] = growth

    def calculate_all_metrics(self):
        """
        Orchestrator method to run all standard metric calculations.
        
        This method calls each individual metric calculation function in sequence to fully populate the `self.output` dictionary.
        """
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
        # These must be called in order, as inventory_days depends on the turnover ratio
        self.inventory_turnover_ratio()
        self.inventory_days()

        # Based on the object's mode, call the correct growth calculation.
        if self.period_type == 'annual':
            self.calculate_yoy_growth()
        elif self.period_type == 'quarterly':
            self.calculate_qoq_growth()

    def display_metrics(self):
        """
        Prints the final calculated metrics to the console in a readable format.
        
        This is a helper method for debugging and command-line usage.
        """
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
                results[fi.get('_period', 'unknown')] = round(val, 2)
            except ZeroDivisionError:
                results[fi.get('_period', 'unknown')] = 'Division by zero'
            except Exception as e:
                results[fi.get('_period', 'unknown')] = f'Error: {str(e)}'

        # Store results in output dictionary
        for period, value in results.items():
            if period not in self.output:
                self.output[period] = {}
            self.output[period][metric_name] = value

        return results



'''BUA_CEMENT = Company()

BUA_CEMENT.add_params({'year' : 2025, 'revenue' : 300000000, 'net_profit' : 40000000}, {'year' : 2024, 'revenue' : 200000000, 'net_profit' : 8000000})

print(BUA_CEMENT.net_profit_margin())'''