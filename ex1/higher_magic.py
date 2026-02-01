def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined_spell(target: str) -> tuple:
        return (spell1(target), spell2(target))
    return combined_spell


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified_spell() -> int:
        return base_spell() * multiplier
    return amplified_spell


def conditional_caster(condition: callable, spell: callable) -> callable:
    def castable(target: str) -> callable:
        if condition is True:
            return spell(target)
        else:
            return "Spell fizzled"
    return castable


def spell_sequence(spells: list[callable]) -> callable:
    def cast_in_order() -> list:
        results = []
        for spell in spells:
            results.append(spell)
        return results
    return cast_in_order


class Spell:
    def __init__(self, name: str, type: str, power: int):
        self.name = name
        self.type = type
        self.power = power

    def play_spell(self, target: str):
        if self.type == "harmfull":
            return f"{self.name} hits {target}"
        return f"{self.name} {target}"

    def spell_power(self) -> int:
        return self.power


# def fireball(target: str) -> int:
#     print(f"Fireball hits {target}", end=", ")
#     return 10


# def heal(target: str) -> int:
#     print(f"Heal {target}")
#     return 8


def main():
    # initialize spells
    fireball = Spell("Fireball", "harmfull", 10)
    heal = Spell("Heal", "helpfull", 8)

    print("\nTesting spell combiner...")
    combined_spell = spell_combiner(fireball.play_spell, heal.play_spell)
    result1, result2 = combined_spell("Dragon")
    print(f"Combined spell results: {result1}, {result2}")
    print(combined_spell("Dragon"))

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball.spell_power, 3)
    damage = mega_fireball()
    print(f"Mega Fireball deals {damage} damage")

    print("\nTesting conditional caster...")
    missed_cast = conditional_caster(False, fireball.play_spell)
    print(f"Missed cast: {missed_cast('Dragon')}")
    successful_cast = conditional_caster(True, heal.play_spell)
    print(f"Successful cast: {successful_cast('Dragon')}")

    print("\nTesting spell sequence...")
    spell_list = [fireball.play_spell, heal.play_spell, fireball.play_spell]
    sequence = spell_sequence(spell_list)()
    for spell in sequence:
        print(spell("Dragon"))
    print()


if __name__ == "__main__":
    main()
