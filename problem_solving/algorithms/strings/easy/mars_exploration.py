def marsExploration(s):
    expected_signal = ''
    changed_chars = 0
    while len(expected_signal) != len(s): expected_signal += 'SOS'
    for i in range(len(s)): 
        if s[i] != expected_signal[i]: changed_chars+=1
    return changed_chars
