"""Test cases for the Map class"""
import game_map
import variables
def test_map_instantiation():
    """Make sure that map instantiation creates a map of a valid size"""
    map_var = game_map.Map()
    assert len(map_var.map) == variables.MAP_WIDTH


def test_map_validity():
    """Ensure that map remains valid even when generating new terrain"""
    map_var = game_map.Map()

    for i in range(0, variables.MAP_WIDTH):
        map_var.step()
    for i in range(0, variables.MAP_WIDTH):
        assert map_var.map[i] >= 0 and map_var.map[i] <= 10
