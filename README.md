# Connect-Four-AI
Connect four game engine playable by human players and a variety of AI types. Currently only random AI, and Monte Carlo sampling AI implimented. Future plans include and Minimax. Also in-progress: more elaborate menu system. Selective matchmaking (human vs human, human vs ai, ai vs ai). Board visualization can be disabled for ai games.

Monte Carlo AI surprisingly effective at relatively low sampling. 50 samples beats random 98% of time. 500 Samples holds its own against human players. The critical aspect here is even with a very low sample number, Monte Carlo tends to block the random ai's 4th piece. Both basically play randomly with the exception the Monte Carlo ai will register imminent opponet wins most the time and move to intercept.

Program makes appearent obvious advantage of being player 1. In random ai vs random ai player 1 wins 55.5% of games and player two wins 44.5%.

This advantage can be leveraged by skill. At 7 samples (basically random) in Monte Carlo ai vs Monte Carlo ai matches, win rates are similar. First player ~55% second player ~45%. At 300 samples in Monte Carlo ai vs Monte Carlo ai, player 1 wins ~60% of games while player 2 wins ~40%

