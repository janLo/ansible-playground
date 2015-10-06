

def has_member(mylist, member=None):
    return [item for item in mylist if member in item]

class FilterModule(object):

    def filters(self):
        return {"has_member": has_member,
                }
