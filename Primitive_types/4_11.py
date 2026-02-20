def rectangle_intersection(rectangle1x,rectangle1y,rectangle2x,rectangle2y):

    if (min(rectangle1x[0],rectangle1x[1])> max(rectangle2x[0],rectangle2x[1])) or (max(rectangle1x[0],rectangle1x[1])< min(rectangle2x[0],rectangle2x[1])): 
        return -1
    
    if (min(rectangle1y[0],rectangle1y[1])> max(rectangle2y[0],rectangle2y[1])) or (max(rectangle1y[0],rectangle1y[1])< min(rectangle2y[0],rectangle2y[1])): 
        return -1

    intersect_rect = [min(rec)]

