import sims4.commands

@sims4.commands.Command('simulacra.test', command_type=sims4.commands.CommandType.Live)
def simulacra_test2(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output("Simulacra  is working!")