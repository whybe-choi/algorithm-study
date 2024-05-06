def solution(players, callings):
    orders_to_players = dict()
    players_to_orders = dict()
    
    for idx, player in enumerate(players):
        orders_to_players[idx] = player
        players_to_orders[player] = idx
        
    for calling in callings:    
        # 현재 이름이 불린 선수에게 추월당한 선수의 위치를 파악하기 위해 현재 이름이 불린 선수의 위치를 우선 구한다.
        present = players_to_orders[calling]  
        
        # 현재 이름이 불린 선수의 위치를 기존 인덱스에서 1을 빼준다.
        # EX. "kai" -> 3 - 1 = 2
        players_to_orders[calling] -= 1
        
        # 추월당한 선수의 위치를 바탕으로 이름을 구하고 해당 이름의 선수의 위치에서 1을 더한다
        # EX. "poe" -> 2 + 1 = 3 
        overtaken = orders_to_players[present-1]
        players_to_orders[overtaken] += 1
        
        # players_to_orders를 기반으로 orders_to_players 변경 내용 업데이트
        orders_to_players[present] = overtaken
        orders_to_players[present-1] = calling
        
    answer = [v for _, v in orders_to_players.items()]
    
    return answer