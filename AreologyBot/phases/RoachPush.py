import functions
from functions.Train import *
from functions.Unit import *

class RoachPush:
    async def power_up(self):
        await Train.train_overlord(self)
        await Train.train_queen(self)
        await Train.rp_train_army(self)

    async def start_push(self):
        if self.army_supply >= 35:
            # Update Status
            if not self.roach_push_started:
                self.roach_push_started.append(True)
                await self.chat_send("starting roach push!")
            # Gather available army units
            army = self.army_units
            for unit in army:
                # If we see enemy units
                if self.known_enemy_ground_units:
                    enemy = self.known_enemy_ground_units.closest_to(unit)
                    self.actions.append(unit.attack(enemy))

    async def end_push(self):
        if not self.roach_push_started:
            return
        if self.army_supply < 30:
            # Update Status
            self.buildorder_step += 1
            await self.chat_send("ending roach push!")

            # Retreat surviving army units
            army = self.army_units
            for unit in army:
                self.actions.append(unit.move(self.hatcheries.first.position))
