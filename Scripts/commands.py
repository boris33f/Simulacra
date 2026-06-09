import sims4.commands
import services
from sims.sim_info import SimInfo

from typing import cast, List

player_sims: List[SimInfo] = []
known_sims: List[SimInfo] = []
unknown_sims: List[SimInfo] = []

@sims4.commands.Command('simulacra.test', command_type=sims4.commands.CommandType.Live)
def simulacra_test(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output("Simulacra  is working!")

@sims4.commands.Command('simulacra.list_sims', command_type=sims4.commands.CommandType.Live)
def simulacra_list_sims(_connection=None):
    sim_info_manager = services.sim_info_manager()
    all_sims_indexed = sim_info_manager.get_all()
    output = sims4.commands.CheatOutput(_connection)
    output(f"All sims len: {len(all_sims_indexed)}")

    for value in all_sims_indexed:
        sim_info = cast(SimInfo, value)
        if sim_info.is_player_sim or sim_info.is_played_sim:
            player_sims.append(sim_info)

    determine_known_sims(_connection)

    for sim in player_sims:
        output(f"P.Sim {sim.first_name}")
    for sim in known_sims:
        output(f"K.Sim {sim.first_name}")

    output("Simulacra list_sims done")

def determine_known_sims(_connection):
    relationship_service = services.relationship_service()
    for p_sim in player_sims:
        relationships = relationship_service.get_all_sim_relationships(p_sim.sim_id)
        for relationship in relationships:
            known_sims.append(relationship.find_sim_info_b())
