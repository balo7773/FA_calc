# Surface Level Features

* User Defined Ratios ✅
* Ratio Deconstruction
* Built in xlsx format file which User can use and send back to server
* Tradingview plugins and widget
* Various link to company's profile on NGX
* Rating of Brokers
* Market News from various publishers✅
* Print out analysis report on companies
* See what users are Investing in
* 
* Use of Plot and graph to display ratios for both single and multi entities

# Advanced Level Features

* Application Of Quantitative Analysis
* Summary of analysis and what ratio entails for user to make better decision
* Portfolio Optimization
* Use of AI to streamline Analysis using various ratio analysis and plot putting them into a whole frame with better insight


# DB Structure
COMPANIES
- ticker (primary key)
- full_name
- sector
- listing_date
- status (active/delisted)

FINANCIAL_STATEMENTS
- id (primary key)
- ticker (foreign key)
- period_type (FY/Q1/Q2/Q3/Q4)
- period_end_date
- revenue
- gross_profit
- operating_profit
- net_income
- total_assets
- total_liabilities
- equity
- ... (all line items)
- submitted_by (user_id)
- submitted_date
- verified (boolean)
- verification_count

MARKET_DATA
- ticker
- date
- open_price
- close_price
- volume
- market_cap

USERS
- user_id
- username
- email
- contribution_score
- premium_status
- joined_date

DATA_VALIDATION_FLAGS
- statement_id
- flagged_by (user_id)
- flag_reason
- flag_date
- resolved (boolean)

# Token System
Token Packages:
- Starter: ₦500 = 10 tokens (₦50/token)
- Standard: ₦2,000 = 50 tokens (₦40/token) - 20% discount
- Pro: ₦5,000 = 150 tokens (₦33/token) - 33% discount

Token Usage:
- Basic stock analysis: FREE (hook users)
- AI query: 1 token
- Portfolio optimization: 3 tokens
- Monte Carlo simulation: 2 tokens
- Detailed PDF report: 2 tokens
- QA forecasting: 3 tokens

VIP Subscription (when launched):
- ₦10,000/month = Unlimited everything + priority support + API access

# THREE LEGGED STOOL
Leg 1: PRODUCT/TECHNICAL EXECUTION
    [Foundation: Data Infrastructure & Management]
    |
    ├── 1.1: Fundamental Analysis Engine
    │   • Financial ratios & interpretations
    │   • Multi-company comparison
    │   • Graphs & reports
    │   • Red flag detection
    │
    ├── 1.2: Portfolio Construction & Optimization
    │   • Portfolio risk/return calculator
    │   • Diversification checker
    │   • Basic optimizer (max Sharpe)
    │   • Scenario analysis
    │
    └── 1.3: Quantitative & Predictive Analytics
        • Risk/return metrics (Sharpe, volatility, VaR)
        • Statistical forecasting (factor models)
        • Monte Carlo simulation
        • Backtesting validation

Leg 2: USER ADOPTION/EXPERIENCE
    |
    ├── Child 2.1: Product Design & User Interface
    ├── Child 2.2: Onboarding & Education
    ├── Child 2.3: User Acquisition & Growth
    └── Child 2.4: Community & Engagement

Leg 3: BUSINESS SUSTAINABILITY
    |
    ├── Child 3.1: Revenue Model & Monetization
    ├── Child 3.2: Cost Management & Optimization
    ├── Child 3.3: Partnerships & B2B
    └── Child 3.4: Risk Management & Compliance