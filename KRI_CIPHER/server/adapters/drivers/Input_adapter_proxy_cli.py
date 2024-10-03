from . import Observer,Input


class InputCLI(Observer):
    def update(self, subject:Input):
        for k,v in subject.state.value.items():
            c = input(v)
            subject.state.value[k] = c
        # impl of print
