
from flask import jsonify
from flask.views import MethodView
from . import Observer,Output,Subject,OutputDto
class OutputAPIAdapter(MethodView):
    init_every_request = False
    def __init__(self,subject:Subject):
        MethodView.__init__(self)
        self.subject = subject
    def get(self):
        print(dir(self.subject.handler))
        self.subject.handler.notify()
        return jsonify(self.subject.handler.state.value)
class OutputAPIObserver(Observer):
    def __init__(self,dto:OutputDto) -> None:
        super().__init__()
        self.dto = dto
    def update(self, subject:Subject):
        print("d",subject.state.value)
        self.dto.include(**subject.state.value)
        subject.state.value = self.dto.export()
        #return super().update(subject)