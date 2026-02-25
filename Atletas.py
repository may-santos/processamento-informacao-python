from dataclasses import dataclass
import sys
from typing import List, Tuple


@dataclass
class Athlete:
    age: int
    height: float
    weight: float
    gender: str


def read_athletes(n: int) -> List[Athlete]:
    athletes: List[Athlete] = []
    for _ in range(n):
        try:
            age = int(input())
            height = float(input())
            weight = float(input())
            gender = input().strip().upper()
        except EOFError:
            break
        athletes.append(Athlete(age, height, weight, gender))
    return athletes


def compute_counts(athletes: List[Athlete]) -> Tuple[int, int, float, float]:
    male_heights = [a.height for a in athletes if a.gender == 'M']
    female_weights = [a.weight for a in athletes if a.gender == 'F']

    male_mean = sum(male_heights) / len(male_heights) if male_heights else 0.0
    female_mean = sum(female_weights) / len(female_weights) if female_weights else 0.0

    males_above = sum(1 for h in male_heights if h > male_mean)
    females_below = sum(1 for w in female_weights if w < female_mean)

    count_females = sum(1 for a in athletes if a.gender == 'F')
    count_males = sum(1 for a in athletes if a.gender == 'M')
    return males_above, females_below, count_females, count_males


def main() -> None:
    n = 100
    athletes = read_athletes(n)

    males_above, females_below,count_females, count_males = compute_counts(athletes)
    
    if count_males == 0:
        print("Nao houve entrada de atletas homens.")
    else:
        print(f"Ha {males_above} atletas homens acima da media da altura dos homens.")


    if count_females == 0:
        print("Nao houve entrada de atletas mulheres.")
    else:
        print(f"Ha {females_below} atletas mulheres abaixo da media do peso das mulheres.")


if __name__ == '__main__':
    main()

