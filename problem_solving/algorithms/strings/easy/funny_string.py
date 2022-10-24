def funnyString(s):
    list_s_ascii = list(map(ord, list(s)))
    reversed_s_ascii = list(map(ord, list(reversed(s))))

    diff_s = [abs(list_s_ascii[i+1] - list_s_ascii[i]) for i in range(len(list_s_ascii)) if i < len(list_s_ascii) - 1]
    
    diff_reverse_s = [abs(reversed_s_ascii[i+1] - reversed_s_ascii[i]) for i in range(len(reversed_s_ascii)) if i < len(reversed_s_ascii) - 1]
    
    if diff_s == diff_reverse_s: return "Funny"
    else: return "Not Funny"
