from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def count_call() -> int:
        nonlocal count
        count += 1
        return count

    return count_call


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulate_power(added_power: int) -> int:
        nonlocal total_power
        total_power += added_power
        return total_power

    return accumulate_power


def enchantment_factory(enchantment_type: str) -> Callable:

    def apply_enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return apply_enchantment


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, int] = {}

    def store(key: str, value: int) -> None:
        memory[key] = value

    def recall(key: str) -> int | str:
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main():
    print("\nTesting mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    for i in range(1, 4):
        print(f"counter_a call {i}: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    initial_power = 100
    nb_spell = spell_accumulator(initial_power)
    print(f"Base {initial_power}: add 20: {nb_spell(20)}")
    print(f"Base {initial_power}: add 30: {nb_spell(30)}")

    print("\nTesting enchantment_factory...")
    flaming_factory = enchantment_factory("Flaming")
    frozen_factory = enchantment_factory("Frozen")
    print(flaming_factory("Sword"))
    print(frozen_factory("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()

    key = "secret"
    value = 42
    missing_key = "unknown"

    print(f"Store '{key}' = {value}")
    vault["store"](key, value)
    print(f"Recall '{key}': {vault['recall'](key)}")
    print(f"Recall '{missing_key}': {vault['recall'](missing_key)}")
    print()


if __name__ == "__main__":
    main()
