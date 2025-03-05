from abc import ABC,abstractmethod

class Old_system():
    def legacy_op(self):
        return "Legacy Operation"

class Adapter(Old_system):
    def new_operation(self):
        return f"Adapter: {self.legacy_op()}"
    
def client_code(adapter):
        result=adapter.new_operation()
        print (result)
if __name__ == "__main__":
    adapter = Adapter()
    client_code(adapter)