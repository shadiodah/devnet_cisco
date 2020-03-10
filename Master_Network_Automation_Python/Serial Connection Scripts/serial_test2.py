import myserial

console = myserial.open_console()
myserial.check_initial_configuration_dialog(console)
with open('config.txt') as f:
    commands = f.readlines()

for cmd in commands:
    myserial.run_command(console, cmd)

output = myserial.read_from_console(console)
print(output)
