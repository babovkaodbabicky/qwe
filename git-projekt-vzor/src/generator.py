"""
Generátor nesmyslných citátů – CLI verze
Spuštění: python3 generator.py
"""

import random

CITATY = [
    "Kachna, která nesnáší vodu, je jen tučný holub.",
    "Kdo maže, ten jede. Kdo nemaže, ten uklízí.",
    "Ponožky se neztrácejí, jen se rozhodly pro jiný životní styl.",
    "Pondělí je jen sobota s horší reklamou.",
    "Nikdy nevěř počítači, který se tváří rychleji, než umí.",
    "Ticho před bouří je jen wifi, co se připojuje.",
    "Kávovar je jediný kolega, který tě nikdy nezklame.",
    "Git je jako paměť slona, jen s víc konflikty.",
]


def hlavni() -> None:
    print("=== Generátor nesmyslných citátů ===")
    citat = random.choice(CITATY)
    print(f"\n„{citat}“\n")


if __name__ == "__main__":
    hlavni()
