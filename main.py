# monte carlo-based options pricer (european) by Neeam Radia.

import numpy as np


# Basic var definiton:
strike = 0              # price at which the option allows purchase / sale when it expires.
s_0 = 0                 # current stock price at time of purchasing/pricing option
s_t = 0                 # simulated final stock price at expiry
risk_free_rate = 0      # risk-free rate of growth - assumed to be UK gilt yield.
volatility = 0          # UNKNOWN
expiry = 0              # number of years till expiry

n = 0                   # number of samples drawn for monte-carlo sim.

sigma = 

call_type =             # is option a call or a put


# function

Z = np.random.standard_normal(n) # n-1 to avoid gates and fenceposts error.

s_t[i] = s_0 * np.exp((r - (sigma^^2)/2)*t + (sigma * (np.sqrt(t)*Z[i])))

if call_type = put:
    payoff[i] = max(s_t[i] - strike, 0)

elif call_type = call:
    payoff[i] = max(strike - s_t[i], 0)

else:
    print(f"Error - input call type: " {call_type})

mean_payoff = np.mean(payoff)

# discount mean payoff for price-estimate
price = np.exp(-r * t) * mean_payoff

std_error = np.exp(-r * t) * np.std(payoff, ddof = 1) / np.sqrt(n)