from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[Callable, Callable]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> Callable:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def castable(target: str, power: int) -> Callable:
        if condition is True:
            return spell(target, power)
        else:
            return "Spell fizzled"
    return castable


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_in_order(target: str, power: int) -> list[Callable]:
        results = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return cast_in_order


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def main() -> None:
    # initialize spells
    print("\nTesting spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    print(combined_spell("Dragon", 5))

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original spell: {fireball('Dragon', 5)}")
    print(f"Augmented spell: {mega_fireball('Dragon', 5)}")

    print("\nTesting conditional caster...")
    missed_cast = conditional_caster(False, fireball)
    print(missed_cast("Dragon", 5))
    successful_cast = conditional_caster(True, heal)
    print(successful_cast("Dragon", 3))

    print("\nTesting spell sequence...")
    spell_list = [fireball, heal, fireball]
    print(spell_sequence(spell_list)("Dragon", 5))
    print()


if __name__ == "__main__":
    main()
