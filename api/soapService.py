from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode 
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        for i in range(times):
            yield u'Hello, %s' % name
    
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, a, b):
        return a + b
    
    @rpc(Integer, Integer, Integer, _returns=Integer)
    def get_traject_duration(ctx, dist, tpsRech, nbArr):
        return int(dist*.6) + nbArr*tpsRech

        

application = Application([HelloWorldService], 'spyne.examples.hello.soap',
in_protocol=Soap11(validator='lxml'),
out_protocol=Soap11())
wsgi_application = WsgiApplication(application)

app = wsgi_application