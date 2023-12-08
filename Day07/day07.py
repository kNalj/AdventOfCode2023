with open("day07", "r") as f:
    hands = [line.strip().split(" ") for line in f.readlines()]

cards = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
combos = {(1, 1, 1, 1, 1): 1, (2, 1, 1, 1): 2, (2, 2, 1): 3, (3, 1, 1): 4, (3, 2): 5, (4, 1): 6, (5, ): 7}


def parse_hand(hand):
    combo = {}
    for card in hand:
        if card not in combo:
            combo[card] = 1
        else:
            combo[card] += 1
    return tuple(sorted(combo.values(), reverse=True))


for i, hand in enumerate(hands):
    hands[i].append(combos[parse_hand(hand[0])])

sorted_list = sorted(hands, key=lambda x: (x[2], cards[x[0][0]], cards[x[0][1]], cards[x[0][2]], cards[x[0][3]], cards[x[0][4]]))

total = 0
for i, hand in enumerate(sorted_list):
    total += (i+1) * int(hand[1])

print("Part 1 solution: ", total)

cards_1 = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

for i, hand in enumerate(hands):
    new_hands = []
    for card in hand[0]:
        if card == "J":
            for replacement_card in cards_1:
                if replacement_card != "J":
                    new_hands.append([hand[0].replace("J", replacement_card), hand[1]])

    for j, new_hand in enumerate(new_hands):
        new_hands[j].append(combos[parse_hand(new_hand[0])])
    sorted_list = sorted(new_hands, key=lambda x: (x[2], cards_1[x[0][0]], cards_1[x[0][1]], cards_1[x[0][2]], cards_1[x[0][3]], cards_1[x[0][4]]))
    if sorted_list:
        hands[i][2] = sorted_list[-1][2]

sorted_list = sorted(hands, key=lambda x: (x[2], cards_1[x[0][0]], cards_1[x[0][1]], cards_1[x[0][2]], cards_1[x[0][3]], cards_1[x[0][4]]))
total = 0
for i, hand in enumerate(sorted_list):
    total += (i + 1) * int(hand[1])

print("Part 2 solution: ", total)
