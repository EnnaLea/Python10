from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heals {target}"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target}"


def dreamleand(target: str, power: int) -> str:
    return f"{target} is now sleeping peacefully"


def base_power(target: str, power: int) -> bool:
    return power > 10


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]
                   ) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str, int],
                                       str]) -> Callable[[str, int],
                                                         str]:
    def new_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return new_spell


def spell_sequence(spells: list[Callable[[str, int], str]]
                   ) -> Callable[[str, int], list[str]]:
    def cast_all_spell(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return cast_all_spell


def main() -> None:
    print("Testing spell combiner...")
    spell_combo = spell_combiner(fireball, heal)
    result = spell_combo("Dragon", 20)
    print(f"Combined spell result: {result[0]}, {result[1]}")
    print("\n")
    super_spell = power_amplifier(fireball, 3)
    print("Testing power amplifier...")
    print(super_spell("Dragon", 10))
    print("\n")
    print("Testing conditional caster...")
    conditional_dreamleand = conditional_caster(base_power, dreamleand)
    print(conditional_dreamleand("Dragon", 20))
    print(conditional_dreamleand("Dragon", 4))
    print("\n")
    print("Testing spell sequence...")
    spell_list = spell_sequence([fireball, heal, dreamleand])
    spells = spell_list("Dragon", 35)
    for s in spells:
        print(s)


if __name__ == "__main__":
    main()
