"""Solution to day 7

Note:
    I implemented a sorting algorithm, in history view
Note2:
    I implemented comparison before I discovered an easier way to do it
    using dataclasses: using @dataclass(ordered=True) and sort_index:
        https://realpython.com/python-data-classes/
"""
import sys
from dataclasses import dataclass, field
from enum import Enum, auto
from pathlib import Path
from typing import Iterable, Protocol

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import AOCValueError


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


class CamelHandType(Protocol):
    hand: str

    def get_hand_type(self):
        ...

    def sort(self):
        ...


@dataclass
class CamelHand:
    sort_index: int = field(init=False, repr=False)
    hand: str
    card_rank: dict[str, int] = field(repr=False)
    wild_card: str = field(default="NOTSET", repr=False)
    # is_sorted: bool = False

    def __str__(self):
        return f"{self.hand}"

    def get_hand_type(self) -> HandType:
        match count := self._count_duplicates():
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

    @property
    def n_wild(self):
        return self.hand.count(self.wild_card)

    def _count_duplicates(self) -> int:
        """Count duplicates of cards and returns the highest suit"""
        highest = 0
        for card in set(self.hand):
            this_count = self.hand.count(card)
            if card is not self.wild_card:
                this_count += self.n_wild
            if this_count > highest:
                highest = this_count
        return highest

    def _pick_a_card(self) -> str:
        u_hand = "".join(set(self.hand))
        no_wild = u_hand.replace(self.wild_card, "")
        if no_wild:
            return no_wild[0]
        else:
            return self.hand[0]

    def _is_two_pair(self) -> bool:
        """Determine if hand is a two pair, with n=2, no jokers"""
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
        n_wild = self.n_wild
        for card in set(self.hand):
            count = self.hand.count(card)
            if count == 3:
                n_three += 1
            elif count == 2 and n_wild and (card != self.wild_card):
                n_three += 1
                n_wild -= 1
            elif count == 2:
                n_pair += 1
        return bool(n_pair) and bool(n_three)

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
            if self.card_rank[this_card] == self.card_rank[other_card]:
                continue
            return self.card_rank[this_card] < self.card_rank[other_card]
        return False

    def __hand_le(self, value: CamelHandType) -> bool:
        for this_card, other_card in zip(self.hand, value.hand):
            if self.card_rank[this_card] == self.card_rank[other_card]:
                continue
            return self.card_rank[this_card] <= self.card_rank[other_card]
        return True

    def __hand_eq(self, value: CamelHandType) -> bool:
        for this_card, other_card in zip(self.hand, value.hand):
            if self.card_rank[this_card] != self.card_rank[other_card]:
                return False
        return True


def sort_wagers(ranks: list[int], wagers: list[int]) -> list[int]:
    """Sort wagers by rank"""
    return [(rank, wager) for rank, wager in zip(ranks, wagers)]


def rank_hands(hands: Iterable[CamelHand]) -> list[int]:
    """Rank hands by strength of hand, according to d7.1 rules"""
    sorted_hands = list(hands)
    sorted_hands.sort()
    hand2rank = {hand.hand: rank + 1 for rank, hand in enumerate(sorted_hands)}
    return [hand2rank[hand.hand] for hand in hands]


def calc_result(ranked_wagers: Iterable[tuple[int, int]]):
    """Calculate the final result generated from main"""
    result = 0
    for rank, wager in ranked_wagers:
        result += rank * wager
    return result
