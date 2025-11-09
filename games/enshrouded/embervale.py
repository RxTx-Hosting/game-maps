from ...game_map import GameMapData, GridStyleOptions
from ...map_category import MapCategoryData
from ...map_data import MapData
from ...map_marker import MapMarkerData


DATA = MapData(
    map=GameMapData(
        name="Embervale",
        slug="embervale",
        description="The various biomes of Embervale",
        tile_url="https://cdn.rxtx-hosting.com/images/games/game_enshrouded/maps/{x}_{y}.webp",
        tile_size=1280,
        image_width=10240,
        image_height=10240,
        min_zoom=-4,
        max_zoom=1,
        default_zoom=0,
        default_center_x=0.5,
        default_center_y=0.5,
        grid_system="generic_8x8",
        grid_options=GridStyleOptions(
            line_color="#ffffff",
            line_opacity=0.5,
            line_weight=1.5,
            label_color="#ffffff",
            label_opacity=0.9,
            label_size=20,
        ),
        grid_visible_by_default=False,
    ),
    categories=[
        MapCategoryData(
            slug="locations-cinder-vault",
            name="Cinder Vault",
            color="#544951",
            default_description="Initial Spawn Location",
            markers=[
                MapMarkerData(
                    name="Cinder Vault", position_x=0.361084, position_y=0.119141
                ),
            ],
        ),
        MapCategoryData(
            slug="locations-elixir-well",
            name="Elixir Well",
            color="#eecaf4",
            icon="https://cdn.rxtx-hosting.com/images/games/game_enshrouded/maps/icons/elixir_well.webp",
            default_name="Elixir Well",
            default_description="Elixir Well",
            use_pin_style=False,
            markers=[
                MapMarkerData(position_x=0.377608, position_y=0.162064),
                MapMarkerData(position_x=0.327818, position_y=0.197742),
                MapMarkerData(position_x=0.309259, position_y=0.248984),
                MapMarkerData(position_x=0.406816, position_y=0.294515),
                MapMarkerData(position_x=0.463489, position_y=0.279649),
                MapMarkerData(position_x=0.439990, position_y=0.163672),
                MapMarkerData(position_x=0.536508, position_y=0.167929),
                MapMarkerData(position_x=0.864624, position_y=0.180273),
                MapMarkerData(position_x=0.716049, position_y=0.225321),
                MapMarkerData(position_x=0.726357, position_y=0.286647),
                MapMarkerData(position_x=0.624683, position_y=0.264673),
                MapMarkerData(position_x=0.586279, position_y=0.344946),
                MapMarkerData(position_x=0.452295, position_y=0.387451),
                MapMarkerData(position_x=0.695068, position_y=0.433350),
                MapMarkerData(position_x=0.763525, position_y=0.556055),
                MapMarkerData(position_x=0.842041, position_y=0.309229),
            ],
        ),
        MapCategoryData(
            slug="locations-hallow-halls",
            name="Hallow Halls",
            color="#f8dea7",
            icon="https://cdn.rxtx-hosting.com/images/games/game_enshrouded/maps/icons/hallow_halls.webp",
            default_description="Hallow Halls",
            use_pin_style=False,
            markers=[
                MapMarkerData(
                    name="Halls of the Extinct",
                    position_x=0.264307,
                    position_y=0.142236,
                ),
                MapMarkerData(
                    name="Revelwood", position_x=0.271587, position_y=0.383108
                ),
                MapMarkerData(
                    name="Nomad Highlands", position_x=0.580670, position_y=0.422192
                ),
                MapMarkerData(
                    name="Kindlewastes", position_x=0.882266, position_y=0.301076
                ),
                MapMarkerData(
                    name="Albaneve Summits", position_x=0.732715, position_y=0.665576
                ),
            ],
        ),
        MapCategoryData(
            slug="locations-hidden-tomb",
            name="Hidden Tombs",
            color="#ff9194",
            icon="https://cdn.rxtx-hosting.com/images/games/game_enshrouded/maps/icons/hidden_tomb.webp",
            default_name="Hidden Tomb",
            default_description="Hidden Tomb",
            use_pin_style=False,
            markers=[
                MapMarkerData(position_x=0.339941, position_y=0.215771),
                MapMarkerData(position_x=0.851758, position_y=0.319824),
                MapMarkerData(position_x=0.658350, position_y=0.639600),
            ],
        ),
        MapCategoryData(
            slug="locations-ancient-spire",
            name="Ancient Spire",
            color="#f8c461",
            icon="https://cdn.rxtx-hosting.com/images/games/game_enshrouded/maps/icons/spire.webp",
            default_name="Ancient Spire",
            default_description="Ancient Spire",
            use_pin_style=False,
            markers=[
                MapMarkerData(position_x=0.344092, position_y=0.191211),
                MapMarkerData(position_x=0.374121, position_y=0.356006),
                MapMarkerData(position_x=0.479639, position_y=0.161670),
                MapMarkerData(position_x=0.332699, position_y=0.542345),
                MapMarkerData(position_x=0.661035, position_y=0.367627),
                MapMarkerData(position_x=0.821346, position_y=0.241709),
                MapMarkerData(position_x=0.727930, position_y=0.483057),
            ],
        ),
        MapCategoryData(
            slug="locations-ancient-obelisk",
            name="Ancient Obelisk",
            color="#ffedb6",
            icon="https://cdn.rxtx-hosting.com/images/games/game_enshrouded/maps/icons/obelisk.webp",
            default_name="Ancient Obelisk",
            default_description="Ancient Obelisk",
            use_pin_style=False,
            markers=[
                MapMarkerData(position_x=0.273584, position_y=0.178711),
                MapMarkerData(position_x=0.310107, position_y=0.332568),
                MapMarkerData(position_x=0.428223, position_y=0.293848),
                MapMarkerData(position_x=0.444531, position_y=0.231738),
                MapMarkerData(position_x=0.518408, position_y=0.287109),
                MapMarkerData(position_x=0.652588, position_y=0.331299),
                MapMarkerData(position_x=0.748887, position_y=0.282437),
                MapMarkerData(position_x=0.812818, position_y=0.322967),
                MapMarkerData(position_x=0.698389, position_y=0.582812),
                MapMarkerData(position_x=0.771826, position_y=0.674609),
                MapMarkerData(position_x=0.305811, position_y=0.539795),
            ],
        ),
        MapCategoryData(
            slug="locations-farm",
            name="Farm",
            color="#92e0da",
            icon="https://cdn.rxtx-hosting.com/images/games/game_enshrouded/maps/icons/farm.webp",
            default_name="Farm",
            default_description="Farm",
            use_pin_style=False,
            markers=[
                MapMarkerData(
                    name="Peaceful Acres", position_x=0.293262, position_y=0.158594
                ),
                MapMarkerData(
                    name="Harvest Homestead", position_x=0.313477, position_y=0.196533
                ),
                MapMarkerData(
                    name="Fenrig's Farm", position_x=0.273633, position_y=0.250977
                ),
                MapMarkerData(
                    name="Hazelnut Farm", position_x=0.344092, position_y=0.348242
                ),
                MapMarkerData(
                    name="Lush Pasture", position_x=0.414502, position_y=0.320801
                ),
                MapMarkerData(
                    name="Cloverbrooke Farm", position_x=0.462500, position_y=0.350244
                ),
                MapMarkerData(
                    name="Wistful Fields", position_x=0.480615, position_y=0.233887
                ),
                MapMarkerData(
                    name="Rootsnook", position_x=0.527930, position_y=0.368213
                ),
                MapMarkerData(
                    name="Mayfair Lot", position_x=0.632617, position_y=0.322070
                ),
                MapMarkerData(
                    name="Fanning Ranch", position_x=0.681833, position_y=0.344507
                ),
                MapMarkerData(
                    name="Bounty Barn", position_x=0.689258, position_y=0.269629
                ),
                MapMarkerData(
                    name="Sunsimmer Southterrain",
                    position_x=0.689111,
                    position_y=0.230615,
                ),
                MapMarkerData(
                    name="Rose Shell Burrow", position_x=0.821321, position_y=0.309912
                ),
                MapMarkerData(
                    name="Wickmouth Goat Farm", position_x=0.820215, position_y=0.411621
                ),
                MapMarkerData(
                    name="Grassy Pasture Goat Farm",
                    position_x=0.831006,
                    position_y=0.680615,
                ),
            ],
        ),
        MapCategoryData(
            slug="locations-mine",
            name="Mine",
            color="#90e3e9",
            icon="https://cdn.rxtx-hosting.com/images/games/game_enshrouded/maps/icons/mine.webp",
            default_name="Mine",
            default_description="Mine",
            use_pin_style=False,
            markers=[
                MapMarkerData(
                    name="Hidden Flint Mine", position_x=0.323954, position_y=0.125889
                ),
                MapMarkerData(
                    name="Saline Quarry", position_x=0.399499, position_y=0.123566
                ),
                MapMarkerData(
                    name="Salt Mine", position_x=0.456374, position_y=0.108138
                ),
            ],
        ),
    ],
)
