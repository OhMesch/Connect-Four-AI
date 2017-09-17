# Connect-Four-AI
Connect four game engine playable by human players and a variety of AI types. Currently only random AI, and Monte Carlo sampling AI implimented. Future plans include implimenting Minimax and a self-play neural net.

Selective matchmaking (human vs human, human vs ai, ai vs ai). Board visualization can be disabled for ai games.

As of September 10th, focus will be shifted to creating generalized game AI that can compete in any 2 player, perfect information game (As opposed to simply just connect four AI). Will continue to experiment primarily in connect four engine.

Monte Carlo AI surprisingly effective at relatively low sampling. 50 samples beats random 98% of time. 500 Samples holds its own against human players. The critical aspect here is even with a very low sample number, Monte Carlo tends to block the random ai's 4th piece. Both basically play randomly with the exception the Monte Carlo ai will register imminent opponet wins most the time and move to intercept.

Program makes appearent obvious advantage of being player 1. In random ai vs random ai player 1 wins 55.5% of games and player two wins 44.5%.

This advantage can be leveraged by skill. At 7 samples (basically random) in Monte Carlo ai vs Monte Carlo ai matches, win rates are similar. First player ~55% second player ~45%. At 300 samples in Monte Carlo ai vs Monte Carlo ai, player 1 wins ~60% of games while player 2 wins ~40%

Currently I've copied all the files and edited them slightly to produce a "trainer". The trainer is running monte carlo sims vs monte carlo sims and writing board state and probability of victory for each move to a separate CSV file. This CSV file will be used to train a neural net to evaluate moves given a board state. I hope to then improve the neural net through self-play. 
