from . import Observer,Input,Subject
from . import AbastractField
from flask import jsonify
from flask import request
from flask.views import MethodView
class InputAPI(MethodView):
    init_every_request = False
    def __init__(self,input:Observer,subject:Subject) -> None:
        Observer.__init__(self)
        MethodView.__init__(self)
        self.input = input 
        self.subject = subject
        self.RESPONSE = input
    def post(self):
        self.input.dto.include(**request.json())
        self.input.update(self.subject)
        if not(self.input.dto.isFilled()):
            return {}
        self.subject.notify()
        response = self.input.dto.export()
        self.input.dto.reset()
        return jsonify(response)
class InputAPIObserver(Observer):
    def __init__(self,dto:AbastractField) -> None:
        super().__init__()
        self.dto:AbastractField = dto
    def update(self, subject:Subject):
        print(self.dto.export())
        subject.state = self.dto.export()

