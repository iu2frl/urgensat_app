from station_config import StationConfig
from station import Station
from command_handler import CommandHandler
from message_handler import MessageHandler
import pyfiglet,os,sys
import logging,logging.config
import yaml

station = None

def setup():

    global station

    with open(os.path.join("config","log.yaml"), 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    
    banner = pyfiglet.figlet_format("Urgensat")
    print("\n"+banner+"\n")
    
    logger = logging.getLogger("root")

    print("Initial setup:")
    logger.info('Starting the loggers')
    #print("[*] starting logger")

    #choose and load config file
    available_file = StationConfig.load_available_config_file(".")
    count = 1
    
    #print("[*] select from available config files:")
    logger.info('Fetching available config files')
    
    print()
    for config_file in available_file:
        print("["+str(count)+"] "+config_file)
        count = count + 1
    
    config_choosed = 0

    while(config_choosed<1 or config_choosed>len(available_file)):
        config_choosed = int(input("\n->config number[1-"+str(len(available_file))+"]: "))
    
    print()

    #print("\n[*] loading "+available_file[config_choosed-1]+" ...")
    logger.info("Loading "+available_file[config_choosed-1])
    config = StationConfig(available_file[config_choosed-1])
    
    #print("[*] preparing message handler")
    logger.info("Preparing message handler")
    message_handler = MessageHandler(None)

    #print("[*] starting the station...")
    logger.info("Starting the station")
    station = Station.build_from_config(config,message_handler)
    station.deamon_rx.start()

    #print("[*] preparing command handler")
    logger.info("Preparing command handler")
    command_handler = CommandHandler(config,station)

    print("\n")

    return command_handler,station,config

def terminate():
    
    global station 

    logger = logging.getLogger("root")

    print("\nTerminating session:")
    
    #print("[*] stopping station...")
    logger.info("Stopping station")
    
    #stopping rx deamon
    if station is not None:
        station.deamon_rx.stop()
        station.deamon_rx.join()
    
    #stopping tx deamon
    try:
        station.deamon_tx.sock.close()
    except:
        pass
    
    #print("[*] terminating logger...")
    logger.info("Stopping loggers")
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    
    for log in loggers:
        handlers = log.handlers[:]
        for handler in handlers:
            handler.close()
            log.removeHandler(handler)
    
    sys.exit()
