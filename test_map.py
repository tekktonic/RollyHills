"""Test cases for the Map class"""
import game_map

def test_map_instantiation():
    m = game_map.Map()
    assert(len(m.map) == 30)
