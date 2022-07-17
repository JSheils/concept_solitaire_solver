def get_last_card_in_stack(stack):
    if (type(stack) is list) and (len(stack) > 0):
        return stack[-1]


def check_for_free_card(tabletop):
    for stack in tabletop["center"]:
        if type(stack) is list:
            card = get_last_card_in_stack(stack)
            if card == "FC":
                stack.pop(-1)
    return tabletop

def move_set_of_dragon_cards_to_freecells(tabletop):
    free = False
    dragon_in_freecell = 0
    freecell_index_list = []
    
    # check if there are free freecells
    i = 0
    for cell in tabletop["freecell"]:
        if cell == None:
            freecell_index_list.append(i)
            free = True
        i += 1

    # for each of the suits
    dragon_dict = {"RD": 0, "GD": 0, "BD": 0}
    for key, value in dragon_dict.items():
        freecell_D_index_list = []
        center_D_index_list = []
    # check if there are dragon cards in free cells
        i = 0
        for cell in tabletop["freecell"]:
            if cell == key:
                freecell_D_index_list.append(i)
                value += 1
    
    # check if there are dragon cards in center
        i = 0
        for stack in tabletop["center"]:
            if (type(stack) is list) and (len(stack) > 0):
                last_card = stack[-1]
            else: last_card = stack
            if last_card == key:
                center_D_index_list.append(i)
                value += 1
    
    # check if there is a complete set of dragon cards
        if value == 4:
            if (dragon_in_freecell > 0) or free:
    
    # move them to freecells if possible
                for index in freecell_D_index_list:
                    # put None in each of the cells
                    tabletop["freecell"][index] = None
                # for each index in center_D_index_list
                for index in center_D_index_list:
                    # pop dragons from their stacks (tabletop["center"][index])
                    tabletop["center"][index].pop(-1)
                # find a freecell to move them to
                # Mark that cell with the key (RX or BX or GX)
                return True
    return False