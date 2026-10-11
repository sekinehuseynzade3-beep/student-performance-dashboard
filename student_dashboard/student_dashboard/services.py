"""Business logic: database və UI-dan asılı olmayan qaydalar."""
from dataclasses import dataclass

import config


@dataclass(frozen=True)
class Statistics:
    total_students: int
    average_score: float
    highest_score: int
    lowest_score: int


def calculate_grade(score: int) -> str:
    if score >= config.GRADE_A_MIN_SCORE:
        return "A"
    if score >= config.GRADE_B_MIN_SCORE:
        return "B"
    if score >= config.GRADE_C_MIN_SCORE:
        return "C"
    if score >= config.GRADE_D_MIN_SCORE:
        return "D"
    return "F"


def calculate_statistics(scores: list[int]) -> Statistics:
    if not scores:
        return Statistics(0, 0.0, 0, 0)
    return Statistics(
        total_students=len(scores),
        average_score=round(sum(scores) / len(scores), 1),
        highest_score=max(scores),
        lowest_score=min(scores),
    )


def is_valid_score(score: int) -> bool:
    return config.MIN_SCORE <= score <= config.MAX_SCORE


def is_valid_name(name: str) -> bool:
    return bool(name.strip())
