from game.components.power_ups.power_up import PoweUp
from game.utils.constants import SHIELD, SHIELD_TYPE



class Shield(PoweUp):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)
        