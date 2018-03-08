"""Test cases for the Map class"""
import game_map
import variables
def test_map_instantiation():
    """Make sure that map instantiation creates a map of a valid size"""
    map_var = game_map.Map()
    assert len(map_var.map) == variables.MAP_WIDTH
