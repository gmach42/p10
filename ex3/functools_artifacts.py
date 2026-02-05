# functools, operator
from functools import reduce, partial, lru_cache
import functools
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min,
    }
    if operation not in ops:
        return "Invalid operation"
    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': partial(base_enchantment, 50, 'fire'),
        'ice_enchant': partial(base_enchantment, 50, 'ice'),
        'lightning_enchant': partial(base_enchantment, 50, 'lightning')
        }


def memoized_fibonacci(n: int) -> int:
    @lru_cache(maxsize=None)
    def fib(k: int) -> int:
        if k <= 1:
            return k
        return fib(k - 1) + fib(k - 2)

    return fib(n)


def spell_dispatcher() -> callable:
    @lru_cache(maxsize=None)
    def dispatcher(spell_name: str) -> str:
        spells = {
            "fireball": "Casting Fireball!",
            "heal": "Casting Heal!",
            "lightning": "Casting Lightning!",
        }
        return spells.get(spell_name, "Unknown spell")

    return dispatcher


def main():
    # TODO verif main and fibo (memoized)
    print("\nTesting spell_reducer...")
    spells = [10, 20, 5]
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))
    print("Min:", spell_reducer(spells, "min"))
    print("Invalid operation:", spell_reducer(spells, "divide"))

    print("\nTesting partial_enchanter...")

    def base_enchantment(element: str, item: str) -> str:
        return f"{element} Enchantment on {item}"

    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire"]("Sword"))
    print(enchanters["ice"]("Shield"))
    print(enchanters["lightning"]("Bow"))

    print("\nTesting memoized_fibonacci...")
    for i in range(10):
        print(f"Fibonacci({i}) = {memoized_fibonacci(i)}")

    print("\nTesting spell_dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher("fireball"))
    print(dispatcher("heal"))
    print(dispatcher("lightning"))
    print(dispatcher("unknown_spell"), "\n")


if __name__ == "__main__":
    main()
