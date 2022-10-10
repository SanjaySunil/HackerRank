def bonAppetit(bill, k, b):
    bill.pop(k)
    cost = 0
    for i in bill: cost += i
    cost = cost // 2
    if cost != b: print(b - cost)
    else: print("Bon Appetit")
