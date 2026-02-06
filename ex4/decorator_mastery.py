from functools import wraps
import time as t
from inspect import signature, Signature, BoundArguments
from typing import Any, Callable


def spell_timer(func: Callable) -> Callable:
    """
    A decorator that measures and prints the execution time of the
    decorated spell-casting function.

    **Usage:**
    ```
    @spell_timer
    def cast_spell():
        ...
    ```
    """

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = t.time()
        result = func(*args, **kwargs)
        end_time = t.time() - start_time
        print(f"Spell completed in {end_time:.2f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    """
    A decorator that checks if the 'power' argument of the decorated
    function is at least min_power. If not, it raises a KeyError.

    **Usage:**
    ```
    @power_validator(10)
    def cast_spell(spell_name: str, power: int):
        ...
    or
    validate_power_10 = power_validator(10)
    @validate_power_10
    def cast_spell(spell_name: str, power: int):
        ...
    ```
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # Get function signature
            sig: Signature = signature(func)
            params: BoundArguments = sig.bind(*args, **kwargs)
            params.apply_defaults()

            if "power" not in params.arguments:
                raise KeyError("no power key in your function...")
            power = params.arguments["power"]

            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """
    A decorator that retries a spell casting up to max_attempts times
    if it raises an exception.

    **Usage:**
    ```
    @retry_spell(3)
    def cast_spell():
        ...
    or
    retry_3 = retry_spell(3)
    @retry_3
    def cast_spell():
        ...
    ```
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for n in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if n < max_attempts:
                        print(e)
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {n}/{max_attempts} attempts)"
                        )
                    else:
                        return (
                            "Spell casting failed after "
                            f"{max_attempts} attempts"
                        )

        return wrapper

    return decorator


class MageGuild:
    """
    A class that validates mage names and spell casting power.
    """

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
        Check that the mage name is longer than 3 characters and
        contains only letters and spaces.
        """
        return len(name) > 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main():
    print("\nTesting spell timer...")
    # Simulate a spell that takes some time to cast

    @spell_timer
    def fireball() -> str:
        t.sleep(0.42)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\nTesting power validator...")
    # Create two spells with different power requirements
    weak_spell = power_validator(min_power=2)
    strong_spell = power_validator(min_power=10)

    @weak_spell
    def splash(power: int) -> str:
        _ = power  # void power because I'm lazy
        return "Splash!"

    @strong_spell
    def final_flash(power: int) -> str:
        _ = power  # void power because I'm lazy
        return "FINAL FLASH!"

    print(splash(power=3))
    print(final_flash(power=3))

    print("\nTesting retry spell...")
    # Create a spell that fails twice and succeeds on the 3rd attempt
    attempt_count = 0

    @retry_spell(3)
    def wingardium_leviosa() -> str:
        nonlocal attempt_count
        attempt_count += 1

        if attempt_count < 3:  # Fail first 2 attempts
            raise ValueError("C'est Leviosa! et pas Leviossaaa")
        else:
            return "Wingardium Leviosa!"

    print(wingardium_leviosa())
    print()

    # Test that the spell reset correctly after max attempts
    attempt_count = 0
    print(wingardium_leviosa())

    # Test name validation and spell casting in MageGuild
    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Gandalf the Grey"))
    print(guild.validate_mage_name("Al"))
    print(guild.cast_spell("Arcane Blast", power=15))
    try:
        print(guild.cast_spell("Minor Spark", power=5))
    except KeyError as e:
        print(e)

    print()


if __name__ == "__main__":
    main()
