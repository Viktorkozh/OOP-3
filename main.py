#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class Solider:
    def __init__(s, id, team):
        s.id = id
        s.team = team

    def follow_hero(s, hero):
        if hero.team == s.team:
            hero.level_up(1)
            return f"Soldier {s.id} is following hero {hero.id}"
        else:
            return (f"Soldier {s.id} cannot follow hero {hero.id} " +
                    "because they are not in the same team.")


class Hero:
    lvl = 0

    def __init__(h, id, team):
        h.id = id
        h.team = team

    def __str__(h) -> str:
        return f"Hero {h.id} of {h.team}"

    def level_up(h, lvl):
        h.lvl += lvl
        return f"Hero {h.id} leveled up by {h.lvl}"


if __name__ == '__main__':
    sr = Hero(2, "red")
    sb = Hero(1, "blue")

    red_soldiers = []
    blue_soldiers = []

    for i in range(10):
        team = random.choice(["red", "blue"])
        soldier = Solider(i + 1, team)
        if team == "red":
            red_soldiers.append(soldier)
        else:
            blue_soldiers.append(soldier)

    print(f"Red soldiers count: {len(red_soldiers)}")
    print(f"Blue soldiers count: {len(blue_soldiers)}")

    if len(red_soldiers) > len(blue_soldiers):
        soldier_following = red_soldiers[random.randint(
            0,  len(red_soldiers) - 1)]

    else:
        soldier_following = blue_soldiers[random.randint(
            0,   len(blue_soldiers) - 1)]

    print(soldier_following.follow_hero(
        sr if soldier_following.team == "red" else sb))

    print(
        f"Soldier ID: {soldier_following.id}, Hero ID: " +
        f"{sr.id if soldier_following.team == 'red' else sb.id},  " +
        f"Team: {soldier_following.team}")
