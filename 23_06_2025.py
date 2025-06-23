

# list1 = [1,2,3,4]
# list1.

# class BuildingName:
#     dry_run = False
#     def __init__(self, cement123, water):
#         self.cement = cement123
#         self.water = water
#         print("I am being called instantly")

#     def create_wall(self):
#         if BuildingName.dry_run:
#             print('kasdjajsk')
#         else:
#             print("Wall Created")
        

#     def display_info(self, cement, water):
#         print(f"cement: {cement}, water: {water}")


# sample_building = BuildingName(cement123='cement', water = 'water')
# # print(sample_building.cement)
# # print(sample_building.create_wall())
# # print(sample_building.display_info("cement1", 'water1'))

# print(sample_building.area) # this is an object attribute 
# print(BuildingName.area) # This is a class attribute 



class commonToAllProductes:

    def __init__(self, cost, returnable, replace):
        self.cost = "cost"
        self.returnable = "returnable"
        self.replace = "replace"



class Phone(commonToAllProductes):
    def __init__(self, category, service_center_replair):
        commonToAllProductes.__init__(self, 100, True, False)

        self.category = category 
        self.service_center_replair = service_center_replair


phone_obj = Phone(category='Phone', service_center_replair = True)
# print(phone_obj.)
# class cloths:
#     def __init__(self, cost, returnable,replace , exchange_period, feature1, ):
#         self.cost = cost
#         self.returnable = returnable
#         self.replace = replace

