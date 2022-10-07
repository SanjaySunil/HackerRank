def breakingRecords(scores):
    min_record = scores[0]
    min_record_count = 0
    max_record = scores[0]
    max_record_count = 0
    
    for i in range(len(scores)):
        if scores[i] < min_record:
            min_record = scores[i]
            min_record_count += 1
        if scores[i] > max_record:
            max_record = scores[i]
            max_record_count += 1
            
    return max_record_count, min_record_count
