class Scene(object):
    def enter(self):
        pass


class Engine(object):
    """Движок"""
    def __init__(self, scene_map):
        pass

    def play(self):
        pass


class Death(Scene):
    """Смерть"""
    def enter(self):
        pass


class CentralCorridor(Scene):
    """Центральный корридор"""
    def enter(self):
        pass


class LaserWeaponArmory(Scene):
    """Оружейная лаборатория"""
    def enter(self):
        pass


class TheBridge(Scene):
    """Топливный отсек"""
    def enter(self):
        pass


class EscapePod(Scene):
    """Спасательная капсула"""
    def enter(self):
        pass


class Map(object):
    """Карта"""
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
