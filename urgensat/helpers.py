from station.station_config import StationConfig
from station.station import Station
from handler.command_handler import CommandHandler
import pyfiglet,os,sys

def setup():
    banner = pyfiglet.figlet_format("Urgensat")
    print("\n"+banner+"\n")
    
    print("Initial setup:")

    #choose and load config file
    available_file = StationConfig.load_available_config_file(".")
    count = 1
    
    print("[*] select from available config files:")
    
    for config_file in available_file:
        print("["+str(count)+"] "+config_file)
        count = count + 1
    
    config_choosed = 0

    while(config_choosed<1 or config_choosed>len(available_file)):
        config_choosed = int(input("\n->config number[1-"+str(len(available_file))+"]: "))
    
    print("\n[*] loading "+available_file[config_choosed-1]+" ...")
    config = StationConfig(available_file[config_choosed-1])
    
    print("[*] setting up the station")
    station = Station.build_from_config(config)

    print("[*] preparing command handler")
    command_handler = CommandHandler("urgensat.log",config,station)
    
    print("[*] starting deamons")
    #far partire server per ricezione pacchetti

    print("\n")

    return command_handler,station,config

def terminate():
    print("\nTerminating session:")
    
    print("[*] stopping deamons")
    
    sys.exit()
