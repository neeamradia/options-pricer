## Monte-Carlo Options Pricer ##

A Summer 2026 Project by Neeam Radia.

Project Plans:

- Research and understand options and options trading. (DONE)
- Re-familiarise myself with monte-carlo simulations (and therefore geometric brownian motion). (DONE)
- Use the pricer to price a few European options.       (DONE)
- Use the Black-Scholes closed form to compare agianst. (DONE)


Whats Missing:
- Taking into account dividend payouts
- Output could look nicer


Results:
| Ticker | Type | Strike | T (yr) | σ (ann.) | MC price | ± SE | Black–Scholes | z |
|---|---|---|---|---|---|---|---|---|
| AAPL | call | 290 | 1 | 0.2595 | 44.2921 | 0.0871 | 44.2799 | 0.14 |
| SPCX | call | 80 | 1 | 0.9706 | 57.4033 | 0.1882 | 57.2345 | 0.90 |
| SKHY | put | 200 | 3 | 1.6772 | 153.3600 | 0.0679 | 153.3935 | 0.49 |
| BA (NYSE) | call | 2000 | 3 | 0.3347 | 0.0188 | 0.0045 | 0.0218 | 0.66 |
| AZN | call | 100 | 1 | 0.2795 | 62.4789 | 0.0626 | 62.5419 | 1.01 |

All rows: n = 500,000, r = 0.0415.

- Monte-Carlo simulation converges to Black-Scholes closed form, with mean abs(z) being 0.64. 
- I actually intended to test BAE Systems (BA.L) but accidentally tested Boeing (NYSE) (BA). That's why the strike is 8.5x the current share price. This is a good test as it shows that at such a high level of growth, very few simulated paths end up with profit, and the standard error is large. MC is unusable at this level, but so is Black-Scholes as both agreed to 0.66 standard errors.