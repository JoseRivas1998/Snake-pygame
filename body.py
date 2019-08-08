from entity import Entity
from direction import Direction


class Body(Entity):
    def __init__(self, before: Entity = None):
        super().__init__()
        if before is not None:
            self.dir = before.dir
            if self.dir == Direction.DOWN:
                self.pos.x = before.pos.x
                self.pos.y = before.pos.y - 1
            elif self.dir == Direction.LEFT:
                self.pos.x = before.pos.x + 1
                self.pos.y = before.pos.y
            if self.dir == Direction.RIGHT:
                self.pos.x = before.pos.x - 1
                self.pos.y = before.pos.y
            if self.dir == Direction.UP:
                self.pos.x = before.pos.x
                self.pos.y = before.pos.y + 1

    def set_direction(self, before: Entity):
        if before.pos.x > self.pos.x:
            self.dir = Direction.RIGHT
        elif before.pos.y > self.pos.y:
            self.dir = Direction.DOWN
        elif before.pos.x < self.pos.x:
            self.dir = Direction.LEFT
        elif before.pos.y < self.pos.y:
            self.dir = Direction.UP

    def update(self):
        self.move_in_direction()
