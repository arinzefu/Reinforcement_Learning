the dataset ifs from https://finance.yahoo.com/quote/BTC-USD/history?period1=1410912000&period2=1681603200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true
 and to maximize the accuracy the parameters can be adjusted and I used the tensorflow framework for this.
The code has inline explanations which i feel is easy to read.
Disclaimer, I did not train for long so using the result here for future trading is not advised.
You can improve the accuracy by changinf some hyperparameters abd the max_iterations is what defines when the training stops.
This is a deep Q-network (DQN) algorithm.