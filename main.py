# monte carlo-based options pricer (european) by Neeam Radia.

import numpy as np
import yfinance as yf
from scipy.stats import norm        #for black-scholes comparison

# Basic var definition:
strike = float(input("Input the strike price of the option: "))                 # price at which the option allows purchase / sale when it expires.
s_0 = 0                 # current stock price at time of purchasing/pricing option
s_t = 0                 # simulated final stock price at expiry
r = 0.0415              # UK 1Y gilt yield, BoE yield curve, pulled 2026-07-23    risk-free rate of growth - assumed to be UK gilt yield.
sigma = 0               # Volatility
t = float(input("Input the integer number of years till expiry: "))                   # number of years till expiry

n = int(input("Input the number of samples drawn for the monte-carlo simulation. Larger numbers take longer but give a higher resolution: "))                   # number of samples drawn for monte-carlo sim.

call_type = input("Is the option a call or a put?\n")                             # is the option a call or a put?

tickerInput = input("Enter the ticker of the stock you desire to price the option for: ").upper()

s_t = np.zeros(n)      # initialise arrays
payoff = np.zeros(n)
Z = np.zeros(n)

###################
# Pulling data from yfinance API
ticker = yf.Ticker(tickerInput)
s_0 = ticker.fast_info["lastPrice"]     # pull correct current stock price using API
####################
# Calculating volatility
ticker_history = ticker.history(period='1y', interval='1d', auto_adjust=True)

if ticker_history.empty:
    raise ValueError("Invalid ticker entered")
    

closes = ticker_history['Close'].to_numpy()

log_closes = np.log(closes)
log_returns = np.diff(log_closes)
std = np.std(log_returns, ddof=1)
sigma = std*np.sqrt(252)
##########################################
# function


for i in range(n):
    Z[i] = np.random.standard_normal()

    s_t[i] = s_0 * np.exp((r - (sigma**2)/2)*t + (sigma * (np.sqrt(t)*Z[i])))

    if call_type.lower() == 'put':
        payoff[i] = max(strike - s_t[i], 0)
        call = False

    elif call_type.lower() == 'call':
        payoff[i] = max(s_t[i] - strike, 0)
        call = True

    else:
        raise ValueError(f"Error - input call type:  {call_type}")

    


mean_payoff = np.mean(payoff)

# discount mean payoff for price-estimate
price = np.exp(-r * t) * mean_payoff

std_error = np.exp(-r * t) * np.std(payoff, ddof=1) / np.sqrt(n)

print(f'Monte-Carlo simulated price with {n} trials: {price:.4f} +- {std_error:.4f}')
print(f'Volatility: {sigma}')

################
# black-scholes to test

d1 = (np.log(s_0 / strike) + (r + sigma**2/2)*t) / (sigma * np.sqrt(t))
d2 = d1 - (sigma*np.sqrt(t))

if call:
    bs = (s_0 * norm.cdf(d1)) - (strike * np.exp(-r*t)*norm.cdf(d2))
else:
    bs = (strike*np.exp(-r*t) * norm.cdf(-d2)) - (s_0*norm.cdf(-d1))


print(f'Black-Scholes closed-form value: {bs:.4f}')

z = abs(price - bs) / std_error

print(f'MC is {z} standard deviations away from the Black-Scholes result.')