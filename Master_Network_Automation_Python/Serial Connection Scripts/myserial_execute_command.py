import myserial

con = myserial.open_console()
myserial.check_initial_configuration_dialog(con)
myserial.run_command(con, 'terminal length 0')
myserial.run_command(con, 'show version', sleep=7)

output = myserial.read_from_console(con)
print(output)
