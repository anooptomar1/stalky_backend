# Import your application as:
# from app import application
# Example:
import time
# import ptvsd

print("Waiting for Database to start.. (20s)")
time.sleep(10)

from app import APP

# Import CherryPy
import cherrypy

if __name__ == '__main__':

    # Enable Debug with Visual Studio Code
    # ptvsd.enable_attach("my_secret", address = ('0.0.0.0', 3000))

    # Mount the application
    cherrypy.tree.graft(APP, "/")

    # Unsubscribe the default server
    cherrypy.server.unsubscribe()

    # Instantiate a new server object
    server = cherrypy._cpserver.Server()

    # Configure the server object
    server.socket_host = "0.0.0.0"
    server.socket_port = 80
    server.thread_pool = 30

    # For SSL Support
    # server.ssl_module            = 'pyopenssl'
    # server.ssl_certificate       = 'ssl/certificate.crt'
    # server.ssl_private_key       = 'ssl/private.key'
    # server.ssl_certificate_chain = 'ssl/bundle.crt'

    # Subscribe this server
    server.subscribe()

    # Start the server engine (Option 1 *and* 2)

    cherrypy.engine.start()
    cherrypy.engine.block()
