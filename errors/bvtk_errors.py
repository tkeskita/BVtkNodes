import exception

class BVTKException(Exception):
    def __init__(self, message, nested_ex=None):
        super().__init__(message)
        self.nested_ex = nested_ex

    def __repr__(self):
        err_str = ("BVTKException: " + self.message)

        if self.nested_ex is not None:
            err_str += "\nNested message: " + str(self.nested_ex)
            
        return err_str