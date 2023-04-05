import Model.TablesModel as tables


place_id = tables.get_place(2, 'no')
desk_id = tables.select_desk(int(2), place_id)

print(desk_id)
