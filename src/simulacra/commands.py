import sims4.commands

@sims4.commands.Command(
    'simulacra.test',
    command_type=sims4.commands.CommandType.Live
)
def simulacra_test(_connection=None):
    sims4.commands.output(
        "Simulacra is working!",
        _connection
    )

    print("Simulacra is working!")