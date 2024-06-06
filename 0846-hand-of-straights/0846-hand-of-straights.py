from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:      
# if the cards are not sufficient for placing in groups return False
        if len(hand) % groupSize != 0:
            return False

# card_count stores the count of each card in hand stores in form of dict
        card_count = Counter(hand)
# sort the keys in increasing order and store in hands
        hands = sorted(card_count)

# iterate through each card in hands
        for card in hands:
# if count of the card in hands is not zero continue inside the loop
            if card_count[card] > 0:
# num stores the count of the card in card_count
                num = card_count[card]
# continue inside the loop for the condition
                for i in range(card, card + groupSize):
# if count of the card is less the acutal num count return False 
                    if card_count[i] < num:
                        return False
# decrement the count by num
                    card_count[i] -= num
# if all condition satisfies then return True
        return True