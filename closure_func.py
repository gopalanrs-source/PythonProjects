def parent_func(child, coins):
    coin_value = int(coins)
    print(f"Printing global coin value: {coin_value}")

    def child_func():
        nonlocal coin_value
        coin_value -= 1
        print(f"Printing nonlocal coin value: {coin_value} for {child}")
        if coin_value >1:
            print(f"{child} has {coin_value} coins left.")
        elif coin_value == 1:
            print(f"{child} has {coin_value} coin left.")
        else:
            print(f"{child} has no coins left. ")
    return child_func

child1 = parent_func("Alice", 5)
child2 = parent_func("Bob", 5)

child1()
child1()
child2()
child1()
child1()



