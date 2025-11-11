import re
from nameko.rpc import rpc
 
class ServiceFuncoes:
    name = "service_funcoes"

    # expressão regular para validar um e-mail
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    @rpc  # Decorador que expõe este método como um serviço RPC
    def ValidaEmail(self, event):
        if(re.fullmatch(self.regex, event['email'])):
            return True
        else:
            return False
