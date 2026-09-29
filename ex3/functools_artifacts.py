from collections.abc import Callable
from typing import Any
from functools import reduce, partial, lru_cache
from functools import singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0
    match operation:
        case 'add':
            return reduce(add, spells)
        case 'multiply':
            return reduce(mul, spells)
        case 'max':
            return reduce(lambda x, y: x if x > y else y, spells)
        case 'min':
            return reduce(lambda x, y: x if x < y else y, spells)
        case _:
            raise ValueError("Unknow operator")


def enchantment(power: int, element: str, target: str) -> str:
    return (f"An enchatment of element {element} "
            f"attack {target} with a power of{power}")


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]
                      ) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "water": partial(base_enchantment, 50, "water"),
        "wind": partial(base_enchantment, 50, "wind")
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(arg: Any) -> str:
        return "Unknow spell type"

    @spell.register(int)
    def damage_spell(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @spell.register(str)
    def echantment_spell(arg: str) -> str:
        return f"Enchantment spell: {arg}"

    @spell.register(list)
    def multi_cast(arg: list[str]) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return spell


def main() -> None:
    print("Testing spell reducer...")
    power = [4, 9, 8, 3, 7]
    print(f"Sum: {spell_reducer(power, "add")}")
    print(f"Product: {spell_reducer(power, "multiply")}")
    print(f"Max: {spell_reducer(power, "max")}")
    print()
    print("Testing partial enchanter...")
    enchant = partial_enchanter(enchantment)
    for key in enchant:
        print(key)
    print()
    print("Testing memoized fibonacci...")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print()
    dispatcher = spell_dispatcher()
    print(dispatcher(5))
    print(dispatcher("Fireball"))
    print(dispatcher(["SnowRain", "MeteorShower", "Cyclone"]))
    print(dispatcher(3.39))


if __name__ == "__main__":
    main()
