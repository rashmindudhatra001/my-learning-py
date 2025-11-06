#public modifier
class PublicClass:
    def __init__(self):
        self.public_attribute = "I am public"

    def public_method(self):
        return "This is a public method"
    
    
    
#private modifier
class PrivateClass:
    def __init__(self):
        self.__private_attribute = "I am private"

    def __private_method(self):
        return "This is a private method"    
    
    
    
#protected modifier
class ProtectedClass:
    def __init__(self):
        self._protected_attribute = "I am protected"

    def _protected_method(self):
        return "This is a protected method"    