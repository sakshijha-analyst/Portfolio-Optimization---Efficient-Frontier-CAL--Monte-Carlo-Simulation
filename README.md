# Portfolio Optimization using Modern Portfolio Theory (MPT)

**Efficient Frontier, Capital Allocation Line & Monte Carlo VaR**

A quantitative equity portfolio construction project applying Modern Portfolio Theory under real-world allocation constraints.

---

## Project Overview

This project constructs and evaluates an optimal portfolio of five NSE-listed large-cap equities using a constrained mean–variance optimization framework.

The analysis includes:

* Historical data extraction using Python (yfinance)
* Log-return computation and annualization
* Sharpe Ratio maximization under 10%–40% allocation constraints
* Efficient Frontier and Capital Allocation Line (CAL) construction
* 10,000-path Monte Carlo simulation
* 50-day Value at Risk (VaR) estimation

The objective was to demonstrate practical portfolio optimization and risk modeling under realistic investment constraints.

## Assets Analyzed

* Reliance Industries
* Tata Consultancy Services
* HDFC Bank
* Infosys
* ICICI Bank

Historical adjusted price data from 2004 onward was used for return and volatility estimation 

## Optimal Portfolio Results

Using mean–variance optimization with allocation bounds (10%–40%), the optimal risky portfolio produced:

* **Expected Annual Return:** 20.18%
* **Annualized Volatility:** 25.41%
* **Sharpe Ratio:** 0.57
* **Risk-Free Rate Assumed:** 6.68% (10Y G-Sec)

HDFC Bank reached the upper allocation constraint (40%), indicating superior risk-adjusted efficiency within the portfolio universe 

Despite concentration tendencies, portfolio-level volatility remained lower than several individual securities, demonstrating diversification benefits under constrained optimization.

## Efficient Frontier & Capital Allocation Line

Multiple portfolio combinations were generated to construct the Efficient Frontier in risk–return space.

The maximum Sharpe Ratio portfolio was identified and the Capital Allocation Line was plotted from the risk-free rate to illustrate optimal risk-adjusted allocation 


## Risk Modeling – Monte Carlo Simulation

To evaluate downside exposure, 10,000 simulated return paths were generated using historical log-return distribution assumptions.

Parameters:

* Initial Portfolio Value: ₹1,00,00,000
* Time Horizon: 50 Days
* Confidence Level: 95%

**Estimated 50-Day VaR (95%): ₹37.38 lakh**

Interpretation:
There is a 5% probability that portfolio losses may exceed ₹37.38 lakh over a 50-day horizon under simulated market conditions 

## Technical Implementation

**Python (Data Extraction & Preprocessing)**

* yfinance for historical price retrieval
* Pandas for data handling
* Log return computation
* Export to Excel for further modeling

(See `stockprices.py`) 

**Excel (Modeling & Optimization)**

* Covariance matrix construction
* Mean–variance optimization using Solver
* Efficient Frontier generation
* Sharpe maximization
* Monte Carlo simulation (10,000 iterations)
* Percentile-based VaR estimation 

## What This Demonstrates

* Practical application of Modern Portfolio Theory
* Portfolio construction under allocation constraints
* Risk-adjusted performance evaluation
* Scenario-based stress testing
* Quantitative financial modeling across Python & Excel

## Files Included

* `stockprices.py` – Data extraction & preprocessing script
* Excel model – Optimization, Efficient Frontier & Monte Carlo simulation
* Presentation deck – Structured explanation of methodology and results

This project was independently developed to demonstrate quantitative portfolio analytics, risk modeling, and structured financial decision-making using real market data.

