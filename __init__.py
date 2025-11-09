from .game_map import GameMapData
from .games.enshrouded.embervale import DATA as enshrouded_embervale_data
from .games.icarus.olympus import DATA as icarus_olympus_data
from .map_data import MapData


MAPS: dict[tuple[str, str], MapData] = {
    ("game_icarus", "olympus"): icarus_olympus_data,
    ("game_enshrouded", "embervale"): enshrouded_embervale_data,
}


def get_map_data(game_slug: str, map_slug: str) -> MapData | None:
    return MAPS.get((game_slug, map_slug))


def get_game_maps_for_game(game_slug: str) -> list[GameMapData]:
    return [data.map for (g_slug, _), data in MAPS.items() if g_slug == game_slug]


def get_all_game_slugs_with_maps() -> set[str]:
    return {game_slug for (game_slug, _) in MAPS.keys()}
