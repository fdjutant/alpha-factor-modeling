[![Github commit](https://img.shields.io/github/last-commit/fdjutant/alpha-factor-modeling/master)](https://github.com/fdjutant/alpha-factor-modeling)

# Alpha factor research and modeling
## Project overview
Alpha factor modeling aims to decode mispricing through a list of alpha values across stocks at a given time. The alpha vector indicates the relative weights to execute in trading throughout the stock universe.

In this project, an alpha factor model was constructed through three steps. First, a risk factor model was built using principal component analysis (PCA) to generate an annualized factor covariance matrix and subsequently the idiosyncratic variance matrix. Second, three alpha factors based on momentum, mean-reversion, and overnight sentiment were considered to compute the factor returns. To evaluate the alpha factors, quantile analysis, turnover analysis, and Sharpe ratio estimation were performed. Third, the risk factor model and alpha factor model were combined through an optimization step to obtain optimal holdings.

Throughout this project, actual stock price data were used and implemented using the Zipline API. A total of 500 indices spanning over 5 years were used for the factor modeling.

## Project description
### Risk factor model using PCA
PCA allows a practical risk modeling. Given the large number of stocks, it is inefficient to compute the covariance matrix of returns. By using PCA, the factor exposures for each index can be obtained from the principal components. The corresponding factor returns can then be computed by applying the transformation of returns into the factor exposures, that is, the principal components. The risk model factor returns from each factor exposure are shown below.

![Alt text](./images/risk-model-factor-returns.png?raw=true "Risk model factor returns")

Using the risk model factor returns, both the factor covariance matrix and the idiosyncratic variance matrix can then be obtained to estimate the portfolio risk. The factor covariance matrix indicates the risk factor associated with the variance estimated from the PCA. On the other hand, the idiosyncratic variance matrix indicates the risk factor that cannot be explained by the principal component analysis. Finally, the risk model portfolio can then be estimated from the portfolio weights, factor exposures, factor covariance matrix, and idiosyncratic variance matrix.

### Alpha factor model
Three alpha factors were evaluated: the 1-year momentum factor, the 5-day sector-neutral mean reversion, and overnight sentiment. For the last two factors, both unsmoothed and smoothed versions were considered. The smoothed factors were computed through a simple moving average. The factor returns from the five strategies are shown below.

![Alt text](./images/alpha-factor-returns.png?raw=true "Factor returns of various alpha factors")

To evaluate the alpha factors, three analyses were performed. A quantile analysis can reveal whether the alpha factors are well-scaled throughout the stock universe. By ranking the stocks based on their mean returns and dividing them into five groups, a good alpha factor must be strictly monotonic. A plot showing the result of quantile analysis is shown below. Following that, a turnover analysis shows the stability of the alphas over time, which impacts trading costs and practicality. Lastly, the Sharpe ratio represents the risk-adjusted returns. A high Sharpe ratio indicates high expected factor returns with low variance.

![Alt text](./images/quantile-analysis.png?raw=true "Quantile analysis of five alpha factors")

### Optimal holdings by combining risk factor and alpha factor
An optimal holding was then constructed by combining both the alpha model and the risk model. This is done by optimizing portfolio weights considering the models developed above. Various optimization strategies were tested. First, objective functions maximize alpha vectors and weights while incorporating risk factors into constraints. Second, a regularization parameter λ is introduced to incorporate a term that enforces greater diversification in objective function. Third, an objective function that attempts to optimize weights to follow an ideal portfolio is also considered. A sample of portfolio holdings across the stock universe from second optimization strategy is shown below.

![Alt text](./images/portfolio-holdings.png?raw=true "Portfolio holdings across stock universe")

## Credits
The project was built as part of a practical course in systematic trading from Udacity: [AI for trading](https://www.udacity.com/course/ai-for-trading--nd880)