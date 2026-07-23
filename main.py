# monte carlo-based options pricer (european) by Neeam Radia.

import numpy as np
import yfinance as yf

# Basic var definiton:
strike = 0              # price at which the option allows purchase / sale when it expires.
s_0 = 0                 # current stock price at time of purchasing/pricing option
s_t = 0                 # simulated final stock price at expiry
r = r = 0.0415          # UK 1Y gilt yield, BoE yield curve, pulled 2026-07-23    risk-free rate of growth - assumed to be UK gilt yield.
sigma = 0               # Volatility
t = 0                   # number of years till expiry

n = 0                   # number of samples drawn for monte-carlo sim.

call_type =            # is the option a call or a put?

tickerInput = input("Enter the ticker of the stock you desire to price the option for.").upper



###################
# Pulling data from yfinance API
ticker = yf.ticker(tickerInput))
s_0 = ticker.fast_info["lastPrice"]     # pull correct current stock price using API


##########################################
# function
for i in range n:
    Z[i] = np.random.standard_normal() # n-1 to avoid gates and fenceposts error.

    s_t[i] = s_0 * np.exp((r - (sigma^^2)/2)*t + (sigma * (np.sqrt(t)*Z[i])))

    if call_type.lower() == put:
        payoff[i] = max(strike - s_t[i], 0)

    elif call_type.lower() == call:
        payoff[i] = max(s_t[i] - strike, 0)

    else:
        print(f"Error - input call type:  {call_type}")

mean_payoff = np.mean(payoff)

# discount mean payoff for price-estimate
price = np.exp(-r * t) * mean_payoff

std_error = np.exp(-r * t) * np.std(payoff, ddof = 1) / np.sqrt(n)