import functools
from collections.abc import Callable
from typing import Any
import time


def spell_timer(func: Callable[..., Any]
                ) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapped_spell_timer(*args: Any, **kwargs: Any
                            ) -> Callable[..., Any]:
        start_time = time.perf_counter()
        print(f"Casting {func.__name__}")
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Spell completed in {run_time:.3f}")
        return value
    return wrapped_spell_timer


def power_validator(min_power: int) -> Callable[..., Any]:
    def validation(func: Callable[..., Any]
                   ) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapped_validation(*args, **kwargs) -> Any:
            power = kwargs.get("power")
            if power is None and args:
                power = args[-1]
            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            else:
                return ("Insufficient power for this spell")
        return wrapped_validation
    return validation


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def retry(func: Callable[..., Any]
              ) -> Callable[..., Any]:
        @functools.wraps(func)
        def retry_wrapper(*args: Any, **kwargs: Any) -> Any:
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {i}/{max_attempts})")
            return (f"Spell casting failed after "
                    f"{max_attempts}/{max_attempts} attempts")
        return retry_wrapper
    return retry


@spell_timer
def enchantement(arg: str) -> str:
    return (f"{arg.capitalize()} cast!")


@power_validator(10)
def power_spell(arg: int) -> str:
    return f"Power of the spell: {arg}"


@retry_spell(4)
def try_spell(arg: str) -> str:
    return (f"{arg.capitalize()} cast!")


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3:
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with {power} power")


def main() -> None:
    print("Testing spell timer..")
    casting_spell = enchantement("fireball")
    print("Result:", casting_spell)
    print()
    print("Testing power validation...")
    validation = power_spell(30)
    print("Result of validation:", validation)
    print()
    print("Testing retrying spell...")
    retrying = try_spell("Iceberg")
    print(retrying)
    print()
    print("Testing MageGuild...")
    mage = MageGuild()
    print(mage.validate_mage_name("Salazar"))
    print(mage.validate_mage_name("Io"))
    print(mage.cast_spell("Windblade", 50))


if __name__ == "__main__":
    main()
