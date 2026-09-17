
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact:
                  artifact["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict[str, int | float]:
    return {
        "max_power": max(mages, key=lambda mage: mage["power"])["power"],
        "min_power": min(mages, key=lambda mage: mage["power"])["power"],
        "avg_power": round(sum(map(lambda mage: mage["power"], mages))
                           / len(mages), 2)
    }


artifacts = [
    {"name": "Excalibur", "power": 95, "type": "sword"},
    {"name": "Magic Ring", "power": 60, "type": "jewelry"},
    {"name": "Phoenix Feather", "power": 88, "type": "material"},
    {"name": "Crystal Ball", "power": 72, "type": "tool"},
]


mages = [
    {"name": "Merlin", "power": 95},
    {"name": "Gandalf", "power": 88},
    {"name": "Saruman", "power": 92},
    {"name": "Radagast", "power": 45},
]


spells = ["fireball", "heal", "shield", "teleport"]


def main() -> None:
    print("Testing artifact sorter...")
    artifacts_sorted = artifact_sorter(artifacts)
    print(f"{artifacts_sorted[0]["name"]}"
          f"({artifacts_sorted[0]["power"]} power)"
          f" comes before {artifacts_sorted[1]["name"]}"
          f" ({(artifacts_sorted)[1]["power"]} power)")
    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))


if __name__ == "__main__":
    main()
