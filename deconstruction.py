#!/usr/bn/python3
from .FA_calc.FA import Company


class Ratio_Components:
    RATIO_MAP = {
    "ROE" : {
        "components": {'1' : ["net_profit_margin", "asset_turnover", "equity_multiplier"]},
        "type": {'1' : ["multiplicative"]},
        "formula": {'1' : "net_profit_margin * asset_turnover * equity_multiplier"},
        "analysis_depth": None,
        "aliases": ["ROE"],
    },

    "ROA" : {
        "components": {'1' : ["net_profit_margin", "asset_turnover"]},
        "type": {'1' : ["multiplicative"]},
        "formula": {'1' : "net_profit_margin * asset_turnover"},
        "analysis_depth": None,
        "aliases": ["ROA"],
    },

    "Net_Profit_Margin" : {
        "components": {'1' : ["tax_burden", "interest_burden", "operating_profit_margin"]},
        "type": {'1' : ["multiplicative"]},
        "formula": {'1' : "tax_burden * interest_burden * operating_profit_margin"},
        "analysis_depth": None,
        "aliases": ["net_profit_margin"],
    },

    "Price_to_Earnings" : {
        "components": {'1' : ["price_to_book", "return_on_equity"], '2': ["price_to_sales", "net_profit_margin"]},
        "type": {'1' : ["fraction"], '2': ["fraction"]},
        "formula": {'1' : "price_to_book / return_on_equity", '2': "price_to_sales / net_profit_margin"},
        "analysis_depth": None,
        "aliases": ["price_to_earnings"],
    },

    "Price_to_Sales" : {
        "components": {'1' : ["price_to_earnings", "net_profit_margin"]},
        "type": {'1' : ["multiplicative"]},
        "formula": {'1' : "price_to_earnings * net_profit_margin"},
        "analysis_depth": None,
        "aliases": ["price_to_sales"],
    },

    "Price_to_Book" : {
        "components": {'1' : ["price_to_earnings", "return_on_equity"]},
        "type": {'1' : ["multiplicative"]},
        "formula": {'1' : "price_to_earnings * return_on_equity"},
        "analysis_depth": None,
        "aliases": ["price_to_book"],
    },

    "EV_to_EBITDA": {
        "components": {'1' : ["ev_to_sales", "ebitda_margin"]},
        "type": {'1' : ["fraction"]},
        "formula": {'1' : "ev_to_sales / ebitda_margin"},
        "analysis_depth": None,
        "aliases": ["EV_to_EBITDA"],
    },

    "ROCE": {
        "components": {'1' : ["operating_profit_margin", "capital_turnover"]},
        "type": {'1' : ["multiplicative"]},
        "formula": {'1' : "operating_profit_margin * capital_turnover"},
        "analysis_depth": None,
        "aliases": ["ROCE"],
    },



    "Gross_Profit_Margin": {
        "components": {"1" : ["gross_profit", "revenue"]},
        "type": {"1" : ["fraction"]},
        "formula": {"1" : "gross_profit / revenue"},
        "analysis_depth": None,
        "aliases": ["gross_profit_margin"],
    }

}

    def __init__(self, company: Company):
        self.company_inputs = company.financial_inputs # stores revenue, profit .e.t.c.
        self.company_ratios = company.output # stores ratios

    
        
