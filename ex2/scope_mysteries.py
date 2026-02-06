def mage_counter() -> callable:
    count = 0

    def count_call() -> int:
        nonlocal count
        count += 1
        return count

    return count_call


def spell_accumulator(initial_power: int) -> callable:
    total_power = 0

    def accumulate_power() -> int:
        nonlocal total_power
        total_power += initial_power
        return total_power

    return accumulate_power


def enchantment_factory(enchantment_type: str) -> callable:
    def apply_enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return apply_enchantment


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key, value) -> dict:
        memory[key] = value
        return memory

    def recall(key):
        if key in memory:
            return memory[key]
        return "Memory not found"

    return {"store": store, "recall": recall}


def main():
    print("\nTesting mage counter...")
    nb_mage = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}: {nb_mage()}")

    print("\nTesting spell accumulator...")
    nb_spell = spell_accumulator(3)
    for i in range(1, 4):
        print(f"Call {i}: {nb_spell()}")

    print("\nTesting enchantment_factory...")
    flaming_factory = enchantment_factory("Flaming")
    frozen_factory = enchantment_factory("Frozen")
    print(flaming_factory("Sword"))
    print(frozen_factory("Shield"))

    print("\nTesting memory_vault...")
    vault = memory_vault()
    print("Storing Precious data: ", end="")
    print(vault["store"]("Precious_data", 42))
    print("Recalling valid data: ", end="")
    print(vault["recall"]("Precious_data"))
    print("Recalling missing data: ", end="")
    print(vault["store"]("Other_data", 100))
    print(vault["recall"]("Precious_data"))
    print(vault["recall"]("Missing_data"), "\n")


if __name__ == "__main__":
    main()
