def whitewashing_area(length, width, height):
    return length * width + 2*length*height + 2*width*height
def whitewashing_cost(area, rate_per_sq_m=15):
    return area*rate_per_sq_m
def flooring_cost(length, width, rate_per_sq_m):
    return length * width * rate_per_sq_m
def display_costs(length, width, height):
    print('the cost of whitewashing is: ',whitewashing_cost(whitewashing_area(length, width, height)))
    print('the cost of mosaic flooring is: ',flooring_cost(length,width, 100))
    print('the cost of cement flooring is: ',flooring_cost(length, width, 55))
    return
print("Welcome to Room Costs. Enter the dimensions to know your cost of flooring")
