# -*- coding: utf-8 -*-
from application import app,manager
from flask_script import Server
import www

##web server
# manager.add_command( "runserver", Server( host='0.0.0.0',port=app.config['SERVER_PORT'],use_debugger = True ,use_reloader = True) )
manager.add_command( "runserver", Server( host='127.0.0.1',port=app.config['SERVER_PORT'],use_debugger = True ,use_reloader = True) )

def main():
    print(print(app.url_map))
    manager.run( )

if __name__ == '__main__':
    try:
        import sys
        sys.exit( main() )
    except Exception as e:
        import traceback
        traceback.print_exc()