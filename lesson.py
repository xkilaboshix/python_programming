import enum


db = {
    'stack1': 1,
    'stack2': 2,
}

class Status(enum.Enum):
    ACTIVE = 1
    INACTIVE = 2
    RUNNING = 3

if Status(db['stack1']) == Status.ACTIVE:
    print('shutdown')
elif Status(db['stack1']) == Status.INACTIVE:
    print('terminate')

# print(Status.ACTIVE)
# print(Status(2))
# print(repr(Status.ACTIVE))
# print(Status.ACTIVE.name)
# print(Status.ACTIVE.value)
#
# for s in Status:
#     print(s)
#     print(type(s))


