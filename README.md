#Gamit
An RMI-based engine for game developing.
This engine depends on Twisted and AutobahnPython.

* ##gamit
    The engine module of the whole things.

     *app: Application Instance types
     
     *asio: A network implementation based on ASIO
     
     *log: Logger
     
     *message: Message queue. Send and receive messages
     
     *mongodb: A database implementation based on MongoDB
     
     *rmi: RMI implementation
     
     *serialize: Serializer for data serializing and de-serializing
     
     *singleton: Make sure subclasses cannot be initiated
     
     *timer: Scheduler for handling timer.
             This is an advanced version of twisted.internet.reactor.callLater
             which can deal with FUTURE time long than a day
             
     -websocket: A network implementation based on WebSocket(AutobahnPython)
     
* ##autotools
    Some automation tools.

    *db2gmt: Translate MySQL tables into gmt files
    
    *db2json: Translate MySQL table data into json files
    
    *gmt2py: Translate gmt files into python files

* ##client_test
    A client example

* ##gate
    A server example

* ##dbcache
    A server example dealing with mongodb

* ##message
    Auto-Generated python files

* ##config
    Application Level Configs are SUGGESTED to be grouped into a FOLDER like this

* ##staticdata
    Logic Level Configs are SUGGESTED to be grouped into a FOLDER like this

