class Enemy(Entity):
    def init(self):
        super().init(parent=shootables_parent, model='cube', scale_y=2, origin_y=-.5, color=color.light_gray,
                         collider='box', position=(20, 0, 3))
        self.health_bar = Entity(parent=self, y=1.2, model='cube', color=color.red,
                                 world_scale=(1.5, .1, .1), rotation_y=90)
        self.max_hp = 50
        self.hp = self.max_hp

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value
        if value <= 0:
            destroy(self)
            return
        self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5
        add_script(SmoothFollow(target=player, offset=(0, 0, 0), speed=0))

        för att skada:
        shootables_parent = Entity()
        mouse.traverse_target = shootables_parent

        def hit():
            if mouse.hovered_entity and hasattr(mouse.hovered_entity, 'hp'):
                mouse.hovered_entity.hp -= 10