import helpers

command_handler,station,config = helpers.setup()

while(True):
    message = input()
    command_handler.parse_command(message)
