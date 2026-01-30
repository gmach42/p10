def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    res = sorted(artifacts, key=lambda x: (-x["power"]))
    return res


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    res = list(filter(lambda x: x["power"] >= min_power, mages))
    return res


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: ("* " + x + " *"), spells))


def mage_stats(mages: list[dict]) -> dict:
    most_powerful = max(mages, key=lambda x: x["power"])
    least_powerful = min(mages, key=lambda x: x["power"])
    average_power = sum(map(lambda x: x["power"], mages)) / len(mages)
    return {
        "most_powerful": most_powerful,
        "least_powerful": least_powerful,
        "average_power": average_power,
    }


def main():
    artifacts = [
        {"name": "Ice Wand", "power": 90, "type": "armor"},
        {"name": "Water Chalice", "power": 74, "type": "weapon"},
        {"name": "Lightning Rod", "power": 86, "type": "weapon"},
        {"name": "Crystal Orb", "power": 81, "type": "relic"},
    ]
    mages = [
        {"name": "River", "power": 58, "element": "fire"},
        {"name": "Morgan", "power": 62, "element": "wind"},
        {"name": "Sage", "power": 67, "element": "ice"},
        {"name": "Morgan", "power": 51, "element": "earth"},
        {"name": "Ash", "power": 62, "element": "earth"},
    ]
    spells = ["shield", "tsunami", "blizzard", "tornado"]

    print("\nTesting artifact sorter...")
    print(
        "\n".join([f"{artifact}" for artifact in artifact_sorter(artifacts)])
    )

    print("\nTesting power filter...")
    filtered_mages = power_filter(mages, 60)
    print("\n".join([f"{mage}" for mage in filtered_mages]))
    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("\nTesting mage stats...")
    print(
        "\n".join(
            [f"{key}: {values}" for key, values in mage_stats(mages).items()])
    )


if __name__ == "__main__":
    main()
