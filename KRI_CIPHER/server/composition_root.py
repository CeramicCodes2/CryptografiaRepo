from .RSA.rsa import RSA
from .DiffHellman.diff_h import DiffHellman
from .kri_cipher import Output as OutputHandler
from .kri_cipher import Input as InputHandler
from .kri_cipher import State,EventObservableHandler

from .adapters.drivers.input_adapter_proxy_web import InputAPI,InputAPIObserver
from .adapters.drivens.Output_adapter_proxy_web import OutputAPIAdapter,OutputAPIObserver

from .adapters.drivens.Output_adapter_proxy_cli import OutputCLIAdapter
from .adapters.drivers.Input_adapter_proxy_cli import InputCLI

from flask import Flask,request
from flask.views import MethodView
from flask_cors import CORS
from .models.dto.Input import InputRsa,InputDiff



def web_composition_root():
    app = Flask(__name__)
    CORS(app)



    # observers
    output_h = OutputHandler(handler=EventObservableHandler(State()))
    input_h = InputHandler(handler=EventObservableHandler(State()))
    dto_rsa = InputRsa()
    dto_diff = InputDiff()
    inp_e = InputAPIObserver(dto_rsa) 
    inp_d = InputAPIObserver(dto_diff) 
    input_h.handler.suscribe(inp_e)
    input_h.handler.suscribe(inp_d)

    # inputs
    input_rsa = InputAPI.as_view("rsa_i",inp_e,input_h)
    output_rsa = OutputAPIAdapter.as_view("rsa_o",output_h)

    input_diff = InputAPI.as_view("diff_i",inp_d,input_h)
    output_diff = OutputAPIAdapter.as_view("diff_o",output_h)
    

    # impls
    app.add_url_rule("/rsa/input",view_func=input_rsa)
    app.add_url_rule("/rsa/output",view_func=output_rsa)

    app.add_url_rule("/diff/input",view_func=input_diff)
    app.add_url_rule("/diff/output",view_func=output_diff)




    # hex
    rsa = RSA(input=input_h,output=output_h)
    diffHellman = DiffHellman(input=input_h,output=output_h)
    app.run()

def cli_composition_root():

    input_h =  InputHandler(handler=EventObservableHandler(State()))
    input_h.handler.suscribe(InputCLI())

    output_h = OutputHandler(handler=EventObservableHandler(State()))
    output_h.handler.suscribe(OutputCLIAdapter())
    rsa = RSA(input=input_h,output=output_h)
    diffHellman = DiffHellman(input=input_h,output=output_h)
if __name__ == "__main__":
    web_composition_root()
    #cli_composition_root()