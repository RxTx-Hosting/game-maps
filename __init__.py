from .game_map import GameMapData
from .map_data import MapData
from .icarus.olympus import DATA as icarus_olympus_data


MAPS: dict[tuple[str, str], MapData] = {
    ("game_icarus", "olympus"): icarus_olympus_data,
}


def get_map_data(game_slug: str, map_slug: str) -> MapData | None:
    return MAPS.get((game_slug, map_slug))


def get_game_maps_for_game(game_slug: str) -> list[GameMapData]:
    return [data.map for (g_slug, _), data in MAPS.items() if g_slug == game_slug]


def get_all_game_slugs_with_maps() -> set[str]:
    return {game_slug for (game_slug, _) in MAPS.keys()}
