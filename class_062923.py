class Person:
    def __init__(self, name):
        self.name =  name

    def __str__(self) -> str:
        return "Name: " + self.name

agent = Person("Bob")

print(agent)

# def i_am_a_function(foo=0):
#     '''
#     mwilson@student.sdccd.edu
#     6-29-23
#     v 1a

#     parameter
#         foo integer
#     return
#         none
#     '''
#     pass    #noop

# i_am_a_function(1)
# i_am_a_function(2)
# i_am_a_function()
# print(i_am_a_function.__doc__)
