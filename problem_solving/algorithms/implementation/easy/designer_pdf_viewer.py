def designerPdfViewer(h, word):
    height_arr = []
    values = []
    for i in range(len(h)): height_arr.append([h[i], chr(i+97)])
    for i in word:
        for x in height_arr: 
            if x[1] == i: values.append(x[0])
                
    return max(values) * 1 * len(word)
