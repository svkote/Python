from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):
    def enter(self):
        print("Эта сцена еще не настроена."
              "Создайте подкласс и реализуйте функцию enter()")
        exit(1)


class Engine(object):
    """Движок"""
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


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
