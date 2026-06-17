import services
from sims.sim_info import SimInfo

from logger import Logger
from typing import cast, List


class SimulacraManager(object):
    player_sims: List[SimInfo] = []
    known_sims: List[SimInfo] = []
    unknown_sims: List[SimInfo] = []

    @classmethod
    def simulacra_list_sims(cls):
        sim_info_manager = services.sim_info_manager()
        all_sims_indexed = sim_info_manager.get_all()
        Logger.log(f"All sims len: {len(all_sims_indexed)}")

        for value in all_sims_indexed:
            sim_info = cast(SimInfo, value)
            if sim_info.is_player_sim or sim_info.is_played_sim:
                cls.player_sims.append(sim_info)

        cls.determine_known_sims()

        for sim in cls.player_sims:
            Logger.log(f"P.Sim {sim.first_name}")
        for sim in cls.known_sims:
            Logger.log(f"K.Sim {sim.first_name}")

        Logger.log("Simulacra list_sims done")

    @classmethod
    def determine_known_sims(cls):
        relationship_service = services.relationship_service()
        for p_sim in cls.player_sims:
            relationships = relationship_service.get_all_sim_relationships(p_sim.sim_id)
            for relationship in relationships:
                cls.known_sims.append(relationship.find_sim_info_b())
