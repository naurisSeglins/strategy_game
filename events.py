import pygame


class Event():
    def __init__(self):
        pass

    # Event handling
    def handle_events(self, all_units, selected_units, running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Left mouse button (select units)
                if event.button == 1:
                    # Deselect all units if clicking on empty space
                    if not any(unit.rect.collidepoint(mouse_pos)
                               for unit in all_units):
                        selected_units.empty()
                        for unit in all_units:
                            unit.selected = False
                    else:
                        for unit in all_units:
                            if unit.rect.collidepoint(mouse_pos):
                                # allows to select multiple units and
                                # deselect with ctrl
                                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                                    unit.selected = not unit.selected
                                else:
                                    # if just mouse clicked then only
                                    # single unit is selected
                                    # looping through all units and if the
                                    # unit clicked with mouse
                                    # then loop through all units and the unit
                                    # that matches is
                                    # selected and rest are deselected
                                    selected_units.empty()
                                    for units in all_units:
                                        if units == unit:
                                            continue
                                        units.selected = False
                                    unit.selected = True
                                if unit.selected:
                                    selected_units.add(unit)
                                else:
                                    # this deselects unit with ctrl
                                    selected_units.remove(unit)

                # Right mouse button (move units)
                elif event.button == 3 and selected_units:
                    for unit in selected_units:
                        unit.follow = None
                        unit.target = mouse_pos
                        for units in all_units:
                            if units.rect.collidepoint(mouse_pos):
                                if units.original_color != unit.original_color:
                                    unit.target = (units.rect.centerx,
                                                   units.rect.centery)
                                    unit.follow = units

        return running
