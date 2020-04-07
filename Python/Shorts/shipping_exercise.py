def ground_shipping(weight):
    if weight <= 2:
        cost = 1.50 * weight
    elif weight <= 6:
        cost = 3.00 * weight
    elif weight <= 10:
        cost = 4.00 * weight
    else:
        cost = 4.75 * weight
    cost += 20.00
    #print ('Ground Shipping')
    return cost

def drone_shipping(weight):
    if weight <= 2:
        cost = 4.50 * weight
    elif weight <= 6:
        cost = 9.00 * weight
    elif weight <= 10:
        cost = 12.00 * weight
    else:
        cost = 14.25 * weight
    #print('Drone Shipping')
    return cost 


def calc_best_shipping(weight):
    if gp_cost < drone_cost and gp_cost < premium:
        print('The cheapest way to ship a '+ str(weight) +' pound package is using Ground Shipping and it will cost: '+str(ground_shipping(weight)))
    elif drone_cost < gp_cost and drone_cost < premium:
        print('The cheapest way to ship a '+ str(weight) +' pound package is using Drone Shipping and it will cost: '+str(drone_shipping(weight)))
    else:
       print('The cheapest way to ship a '+ str(weight) +' pound package is using Premium Shipping and it will cost: ' + str(premium))


weight = 0.5
gp_cost = ground_shipping(weight)
drone_cost = drone_shipping(weight)N
premium = 120.00   

calc_best_shipping(weight)