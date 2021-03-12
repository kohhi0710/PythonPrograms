from itertools import product

suit = ["♥", "♦", "♤", "♧"]
rank = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# productで組を作り、joinで繋げている
for card in product(suit,rank):
    print("".join(card))

# ♥A
# ♥2
# ♥3
# ...
# ♥J
# ♥Q
# ♥K
# ♦A
# ♦2
# ♦3
# ...
# ♦J
# ♦Q
# ♦K
# ♤A
# ♤2
# ♤3
# ...
# ♤J
# ♤Q
# ♤K
# ♧A
# ♧2
# ♧3
# ...
# ♧J
# ♧Q
# ♧K