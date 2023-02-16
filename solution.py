def league_points(wins, draws, losses):
    
    wins = 3 * wins 
    draws = 1 * draws 
    losses = 0 * losses
    
    total = wins + draws + losses 
    return total
    
    
    

print(league_points(0, 0, 1))
    
