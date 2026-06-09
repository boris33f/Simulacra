import sims4.commands
import services


@sims4.commands.Command('simulacra.test', command_type=sims4.commands.CommandType.Live)
def simulacra_test(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output("Simulacra  is working!")

@sims4.commands.Command('simulacra.list_sims', command_type=sims4.commands.CommandType.Live)
def simulacra_list_sims(_connection=None):
    sim_info_manager = services.sim_info_manager()
    all_sims_indexed = sim_info_manager.get_all()
    output = sims4.commands.CheatOutput(_connection)
    output(f"All sims : {len(all_sims_indexed)}")