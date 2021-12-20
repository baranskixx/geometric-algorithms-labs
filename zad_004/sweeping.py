from sortedcontainers import SortedDict

EPS_POINT = 1e-5

def find_intersections_nlogn(S, bounds = None):
    sections = map_input(S)
    root_Q = generate_events_structure(sections)
    node = find_min_bst(root_Q)
    state = SortedDict()

    if bounds is None:
        sweep_bounds = (-0.06, 0.06)
    else:
        sweep_bounds = bounds

    scenes = [Scene([], [LinesCollection(S)])]
    end_points = []
    intersections = []

    while node != None:
        curr_point = node.point
        sdk = state.keys()
        if isinstance(curr_point.index, list):
            key1 = state[curr_point.index[0]].p
            key2 = state[curr_point.index[1]]

            s1 = state.pop(key1)
            s2 = state.pop(key2)

            s1.shorten(curr_point.x + EPS_POINT)
            s2.shorten(curr_point.x + EPS_POINT)

            if s1.a < s2.a:
                s1, s2 = s2, s1
            
            state[key1] = s1
            state[key2] = s2
            index1 = state.index(key1)
            index2 = state.index(key2)
            sdk = state.keys()

            if index1 < len(sdk) - 1:
                x, y = state[key1].find_intersection_point(state[sdk[index1+1]])
                if x != None:
                    new_point = Point(x, y, [key1, sdk[index1 + 1]])
                    root_Q.insert(new_point)
                    intersections.append(new_point.get_coords())
            
            sdk = state.keys()

            if index2 > 0 :
                x, y = state[key2].find_intersection_point(state[sdk[index2-1]])
                if x != None:
                    new_point = Point(x, y, [key2, sdk[index2 - 1]])
                    root_Q.insert(new_point)    
                    intersections.append(new_point.get_coords())

        else:
            section = sections[curr_point.index]
            end_points.append(curr_point.get_coords())
            tmp = state.get(section[curr_point.index], None)
            if tmp == None:
                state[section] = section
                index = state.index(curr_point.x)

                if index < len(state) - 1:
                    neigh = state[sdk[index + 1]]
                    x, y = section.find_intersection_point(neigh)
                    if x != None:
                        new_point = Point(x, y, [sdk[index], sdk[index+1]])
                        root_Q.insert(new_point)
                        intersections.append(new_point.get_coords())

                if index > 0:
                    neigh = state[sdk[index - 1]]
                    x, y = section.find_intersection_point(neigh)
                    if x != None:
                        new_point = Point(x, y, [sdk[index], sdk[index-1]])
                        root_Q.insert(new_point)
                        intersections.append(new_point.get_coords())
            
            else:
                index = state.index(sections[curr_point.index].p.x)
                if index > 0 and index < len(sdk) - 1:
                    x, y = state[sdk[index-1]].find_intersection_point(sdk[index+1])
                    if x != None:
                        new_point = Point(x, y, [sdk[index-1], sdk[index+1]])
                        root_Q.insert(new_point)
                        intersections.append(new_point.get_coords())
                
                state.pop(curr_point.x)
        
        node = next_bst(node)

        sweep = ((curr_point.x, sweep_bounds[0]), (curr_point.x, sweep_bounds[1]))

        scenes.append(Scene([
            PointsCollection(deepcopy(end_points)),
            PointsCollection(deepcopy(intersections), color = 'red')], [
            LinesCollection(S),
            LinesCollection([sweep], color = 'red')]))
    
    return scenes + [Scene([PointsCollection(deepcopy(intersections), color = 'red'),
                            PointsCollection(deepcopy(end_points))],
                            [LinesCollection(S)])]
                        



