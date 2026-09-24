from collections.abc import Callable


def mage_counter() -> Callable[[], int]:
    count_a = 0

    def counting_mage() -> int:
        nonlocal count_a
        count_a += 1
        return count_a
    return counting_mage


def spell_accumulator(initial_power: int
                      ) -> Callable[[int], int]:
    def accumulation(add_power: int) -> int:
        nonlocal initial_power
        initial_power += add_power
        return initial_power
    return accumulation


def enchantment_factory(enchantment_type: str
                        ) -> Callable[[str], str]:
    def enchanted_item(name: str) -> str:
        return (f"{enchantment_type.capitalize()} "
                f"{name.capitalize()}")
    return enchanted_item


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, str] = {}

    def store(key: str, value: str) -> None:
        memory[key] = value

    def recall(key: str) -> str:
        return memory.get(key, "Memory not found")
    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print()
    print("Testing spell accumulator...")
    add_power = spell_accumulator(100)
    print(f"base: 100, add 20: {add_power(20)}")
    print(f"base: 100, add 20: {add_power(30)}")
    print()
    print("Testing enchantment factory...")
    item_a = enchantment_factory("flaming")
    item_b = enchantment_factory("frozen")
    print(item_a("sword"))
    print(item_b("shield"))
    print()
    print("Testing memory vault...")
    memory_a = memory_vault()
    memory_a["store"]("secret", "42")
    print("Store 'secret' = 42")
    result = memory_a["recall"]("secret")
    print(f"Recall 'secret': {result}")
    result = memory_a["recall"]("unknow")
    print(f"Recall 'unknow': {result}")


if __name__ == "__main__":
    main()
