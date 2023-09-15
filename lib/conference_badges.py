# import ipdb

def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    # badge_list = []
    # for n in names:
    #     badge_list.append(badge_maker(n))
    # return badge_list
    
    return [badge_maker(n) for n in names]

def assign_rooms(speakers):
    rooms = range(1, 9)

    # room_assignments = []
    # for r in rooms:
    #     room_assignments.append(f"Hello, {speakers[r - 1]}! You'll be assigned to room {r}!")
    # return room_assignments
    
    return [f"Hello, {speakers[r - 1]}! You'll be assigned to room {r}!" for r in rooms]

def printer(searched_names):
    for badge in batch_badge_creator(searched_names):
        print(badge)
    for assignment in assign_rooms(searched_names):
        print(assignment)

# ipdb.set_trace()