import helpers

command_handler,station,config = helpers.setup()

while(True):
    message = raw_input()
    command_handler.parse_command(message)
