import functools
from functools import singledispatch
from collections.abc import Callable
from typing import Any
import time


def spell_timer(func: Callable[..., Any]
                ) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapped_spell_timer(*args, **kwargs
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
        def wrapped_validation(power: int) -> Any:
            if power >= min_power:
                value = func(power)
                print("The power is validated.")
                return value
            return("Failed to validate power.")
        return wrapped_validation
    return validation



# def retry_spell(max_attempts: int) -> Callable



def cast_spell() -> Callable[..., Any]:
    @singledispatch
    def spell(arg: Any) -> str:
        return "Unknow spell."

    @spell.register(str)
    @spell_timer
    def enchantemen(arg: str) -> str:
        return (f"{arg.capitalize()} cast!")

    @spell.register(int)
    @power_validator(50)
    def power_spell(arg: int) -> str:
        return f"Power of the spell: {arg}"

    return spell



# class MageGuild:
# @staticmethod
# def validate_mage_name(name: str) -> bool
# def cast_spell(self, spell_name: str, power: int) -> str

def main() -> None:
    print("Testing spell timer..")
    casting_spell = cast_spell()
    print("Result:", casting_spell("fireball"))
    print()
    print("Testing power validation...")
    validation = cast_spell()
    print("Result of validation:", validation(120))


if __name__ == "__main__":
    main()
