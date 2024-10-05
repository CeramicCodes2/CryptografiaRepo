from . import Observer,Output

class OutputCLIAdapter(Observer):
    def update(self, subject:Output):
        for k,v in subject.state.value.items():
            print(k,v)
