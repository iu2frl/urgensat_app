import helpers

'''
+ordinare classi scritte in sotto cartelle https://docs.python-guide.org/writing/structure/  fatto
+caricare codice su git
+inserire metodi per la l'avvio fatto
+inserire metodo per la terminazione del programma
+TODO command helper
+creare classi per il controllo a distanza di attuatori e sensori
+inserire parte di ricezione messaggi->message dispatcher
'''

'''
station="IU3GNB"
config = StationConfig.load_station_config(station)
test_station = Station.build_from_config(config)
command_handler = CommandHandler("urgensat.log",config,test_station)
'''

command_handler,station,config = helpers.setup()

while(True):
    message = input(station.call+"> ")
    command_handler.parse_command(message)
