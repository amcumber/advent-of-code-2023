"""Solution to day 7 part 1"""
import sys
from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path
from typing import Iterable, Protocol

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import AOCValueError, parse_line, read_input


class HandType(Enum):
    high_card = auto()
    one_pair = auto()
    two_pair = auto()
    three_of_a_kind = auto()
    full_house = auto()
    four_of_a_kind = auto()
    five_of_a_kind = auto()

    def __eq__(self, value: object) -> bool:
        return self.value == value.value

    def __lt__(self, value: object) -> bool:
        return self.value < value.value

    def __le__(self, value: object) -> bool:
        return self.value <= value.value


CARD_RANK = {card: rank for rank, card in enumerate(reversed("AKQJT98765432"))}


class CamelHandType(Protocol):
    hand: str

    def get_hand_type(self):
        ...

    def sort(self):
        ...


@dataclass
class CamelHand:
    hand: str
    is_sorted: bool = False

    def get_hand_type(self) -> HandType:
        match count := self._count_pairs():
            case 5:
                hand_type = HandType.five_of_a_kind
            case 4:
                hand_type = HandType.four_of_a_kind
            case 3:
                if self._is_full_house():
                    hand_type = HandType.full_house
                else:
                    hand_type = HandType.three_of_a_kind
            case 2:
                if self._is_two_pair():
                    hand_type = HandType.two_pair
                else:
                    hand_type = HandType.one_pair
            case 1:
                hand_type = HandType.high_card
            case _:
                raise AOCValueError(f"Unknown count, {count}")
        return hand_type

    def _count_pairs(self) -> str:
        """Count duplicates of cards and returns the highest suit"""
        count = 0
        for card in set(self.hand):
            this_count = self.hand.count(card)
            if this_count > count:
                count = this_count
        return count

    def _is_two_pair(self) -> bool:
        """Determine if hand is a two pair"""
        n_pair = 0
        for card in set(self.hand):
            count = self.hand.count(card)
            if count == 2:
                n_pair += 1
        return n_pair == 2

    def _is_full_house(self) -> bool:
        """Determine if hand is a full house"""
        n_pair = 0
        n_three = 0
        for card in set(self.hand):
            count = self.hand.count(card)
            if count == 2:
                n_pair += 1
            if count == 3:
                n_three += 1
        return bool(n_pair) and bool(n_three)

    def _sort_four_of(self) -> str:
        """Sort a four-of-a-kind hand by high card"""
        return self._one_match_sort(self.hand, 4)

    def _sort_three_of(self) -> str:
        """Sort a three-of-a-kind hand by high card"""
        return self._one_match_sort(self.hand, 3)

    def _sort_one_pair(self) -> str:
        """Sort a one pair hand by high card"""
        return self._one_match_sort(self.hand, 2)

    def _sort_high_card(self) -> str:
        """Sort a unmatched hand by high card"""
        return "".join(self._simple_sort(self.hand))

    @classmethod
    def _one_match_sort(cls, hand: str, n: int) -> str:
        """sort a single match hand e.g. 2K22J -> 222KJ"""
        for card in set(hand):
            if hand.count(card) > 1:
                break
        unpaired = cls._simple_sort(hand.replace(card, ""))
        sorted_hand = [card] * n
        sorted_hand.extend(unpaired)
        return "".join(sorted_hand)

    def _sort_full(self) -> str:
        """sort a full-house hand"""
        for three_of in set(self.hand):
            if self.hand.count(three_of) == 3:
                break
        two_of = self.hand.replace(three_of, "")
        sorted_hand = [three_of] * 3
        sorted_hand.extend(two_of)
        return "".join(sorted_hand)

    def _sort_two_pair(self) -> str:
        """sort a two_pair hand"""
        hits = 0
        two_pair = []
        for two_of in set(self.hand):
            if self.hand.count(two_of) == 2:
                hits += 1
                two_pair.append(two_of)
            if hits > 1:
                break
        two_pair.sort(lambda x: CARD_RANK[x])

        unmatched = self.hand
        sorted_hand = []
        for two_of in two_pair:
            unmatched = self.hand.replace(unmatched, "")
            sorted_hand.extend([two_of] * 2)
        return "".join(sorted_hand.extend(self._simple_sort(unmatched)))

    @staticmethod
    def _simple_sort(value: str) -> list[str]:
        hand_list = list(value)
        hand_list.sort(key=lambda x: CARD_RANK[x])
        return hand_list

    def sort_hand(self) -> str:
        """Sort hand and return the sorted string"""
        if self.is_sorted:
            return self.hand

        match hand_type := self.get_hand_type():
            case HandType.five_of_a_kind:
                sorted_hand = self.hand
            case HandType.four_of_a_kind:
                sorted_hand = self._sort_four_of()
            case HandType.full_house:
                sorted_hand = self._sort_full()
            case HandType.three_of_a_kind:
                sorted_hand = self._sort_three_of()
            case HandType.two_pair:
                sorted_hand = self._sort_two_pair()
            case HandType.one_pair:
                sorted_hand = self._sort_one_pair()
            case HandType.high_card:
                sorted_hand = self._sort_high_card()
            case _:
                raise AOCValueError(f"Unknown hand type: {hand_type}")
        return sorted_hand

    def sort(self) -> CamelHandType:
        """Sort The CamelHand to generated a sorted class"""
        return self.__class__(self.sort_hand(), True)

    def __getattr__(self, idx: int) -> str:
        return self.hand[idx]

    def get_nth(self, i: int):
        """Get n-th rank card in hand,
        e.g.
        get_nth('AAJJK2', 0) -> 'A'
        get_nth('AAJJK2', 1) -> 'A'
        get_nth('AAJJK2', 2) -> 'J'

        get_nth('AJAJK2', 1) -> 'J'
        """
        # top = hand = [i]
        # if i == 1:
        #     return top
        # return self.get_n_th(hand.replace(top, ""), i - 1)
        return self[i]

    def __lt__(self, value: CamelHandType) -> bool:
        this_hand = self.get_hand_type()
        other_hand = value.get_hand_type()
        if this_hand == other_hand:
            return self.__hand_lt(value)
        return this_hand < other_hand

    def __le__(self, value: CamelHandType) -> bool:
        this_hand = self.get_hand_type()
        other_hand = value.get_hand_type()
        if this_hand == other_hand:
            return self.__hand_le(value)
        return this_hand <= other_hand

    def __eq__(self, value: CamelHandType) -> bool:
        this_hand = self.get_hand_type()
        other_hand = value.get_hand_type()
        if this_hand == other_hand:
            return self.__hand_eq(value)
        return False

    def __hand_lt(self, value: CamelHandType) -> bool:
        for this_card, other_card in zip(self.hand, value.hand):
            if CARD_RANK[this_card] == CARD_RANK[other_card]:
                continue
            return CARD_RANK[this_card] < CARD_RANK[other_card]
        return False

    def __hand_le(self, value: CamelHandType) -> bool:
        for this_card, other_card in zip(self.hand, value.hand):
            if CARD_RANK[this_card] == CARD_RANK[other_card]:
                continue
            return CARD_RANK[this_card] <= CARD_RANK[other_card]
        return True

    def __hand_eq(self, value: CamelHandType) -> bool:
        for this_card, other_card in zip(self.hand, value.hand):
            if CARD_RANK[this_card] != CARD_RANK[other_card]:
                return False
        return True


def parse_camel_line(line: str) -> tuple[CamelHand, int]:
    """Parse camel cards hand into the hand and wager"""
    hand = parse_line(line, divider=" ", idx=0)
    wager = parse_line(line, divider=" ", idx=1)

    return CamelHand(hand), int(wager)


def rank_hands_7p1(hands: Iterable[CamelHand]) -> list[int]:
    """Rank hands by strength of hand, according to d7.1 rules"""
    sorted_hands = list(hands)
    sorted_hands.sort()
    hand2rank = {hand.hand: rank + 1 for rank, hand in enumerate(sorted_hands)}
    return [hand2rank[hand.hand] for hand in hands]


def sort_wagers(ranks: list[int], wagers: list[int]) -> list[int]:
    """Sort wagers by rank"""
    return [(rank, wager) for rank, wager in zip(ranks, wagers)]


def main(input_data: list[str]) -> list[int]:
    """Main for day7 part 1 - camel cards"""
    hands, wagers = list(zip(*[parse_camel_line(line) for line in input_data]))
    ranks = rank_hands_7p1(hands)
    return sort_wagers(ranks, wagers)


def calc_result(ranked_wagers: Iterable[tuple[int, int]]):
    """Calculate the final result generated from main"""
    result = 0
    for rank, wager in ranked_wagers:
        result += rank * wager
    return result


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent / "input.txt"
    input_data = read_input(input_file)
    result = main(input_data)
    val = calc_result(result)

    output_file = Path(__file__).parent / "result.txt"
    with open(output_file, "w") as fh:
        fh.write(str(val))
    print(f"The results are: {result} with a n_possible solution of: {val}")
