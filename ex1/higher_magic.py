def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined_spell(target: str) -> tuple:
        return (spell2(target), spell1(target))
    return combined_spell


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified_spell(target: str) -> int:
        return base_spell(target) * multiplier
    return amplified_spell


def conditional_caster(condition: callable, spell: callable) -> callable:
    def castable(target: str) -> callable | str:
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


def main():
    test_values = [14, 6, 24]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    print("Testing spell combiner...")
    spell_combiner(fireball, heal)
    print("Testing power amplifier...")
    print("Testing conditional caster...")
    print("Testing spell sequence...")

