from functools import wraps
import time as t
import inspect
from typing import Any


def spell_timer(func: callable) -> callable:
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


def power_validator(min_power: int) -> callable:
    """
    A decorator that checks if the 'power' argument of the decorated
    function is at least min_power. If not, it raises a KeyError.

    **Usage:**
    ```
    @power_validator(10)
    def cast_spell(spell_name: str, power: int):
        ...
    ```
    """
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # Get function signature
            sig = inspect.signature(func)
            params = list(sig.parameters.keys())

            # Find power
            power = None
            if 'power' in kwargs:  # look for power in kwargs
                power = kwargs['power']
            elif 'power' in params:  # look for power in args
                power_index = params.index('power')
                if power_index < len(args):
                    power = args[power_index]

            if power is None:  # if power is neither in args nor kwargs
                raise KeyError("no power key in your function...")
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    """
    A decorator that retries a spell casting up to max_attempts times
    if it raises an exception.

    **Usage:**
    ```
    @retry_spell(3)
    def cast_spell():
        ...
    ```
    """
    def decorator(func: callable) -> callable:
        n = 0

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            nonlocal n
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if n < max_attempts:
                    print(e)
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {n + 1}/{max_attempts} attempts)"
                    )
                    n += 1
                    return wrapper(*args, **kwargs)
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
        return len(name) > 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main():
    print("\nTesting spell timer...")

    @spell_timer
    def fireball() -> str:
        t.sleep(0.42)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\nTesting power validator...")
    weak_spell = power_validator(min_power=2)
    strong_spell = power_validator(min_power=10)

    @weak_spell
    def splash(power: int) -> str:
        _ = power
        return "Splash!"

    @strong_spell
    def final_flash(power: int) -> str:
        _ = power
        return "FINAL FLASH!"

    print(splash(power=3))
    print(final_flash(power=3))

    print("\nTesting retry spell...")
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
