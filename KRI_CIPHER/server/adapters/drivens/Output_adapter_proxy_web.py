
from flask import jsonify
from flask.views import MethodView
from . import Observer,Output,Subject
class OutputAPIAdapter(MethodView):
    init_every_request = False
    def __init__(self,subject:Subject):
        MethodView.__init__(self)
        self.subject = subject
    def get(self):
        return jsonify(self.subject.state.value)
class OutputAPIObserver(Observer):
    def update(self, subject:Subject):
        return subject.state.value
        #return super().update(subject)