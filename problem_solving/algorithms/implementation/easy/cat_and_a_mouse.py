def catAndMouse(x, y, z):
    if z > x:
        distance_x = z - x
    elif x > z:
        distance_x = x - z
    else:
        distance_x = 0
        
    if z > y:
        distance_y = z - y
    elif y > z:
        distance_y = y - z
    else:
        distance_y = 0
        
    if distance_x < distance_y: return "Cat A"
    elif distance_y < distance_x: return "Cat B"
    else: return "Mouse C"
