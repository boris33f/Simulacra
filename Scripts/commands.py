import sims4.commands
import services
from simulacra_manager import SimulacraManager

from wrapper import inject_after_cls_method, inject_method_after_cls_method
from logger import Logger

@sims4.commands.Command('simulacra.setup', command_type=sims4.commands.CommandType.Live)
def simulacra_setup(_connection=None):
    Logger.set_connection(_connection)
    Logger.log(f"Simulacra setup ended.")

@sims4.commands.Command('simulacra.setup2', command_type=sims4.commands.CommandType.Live)
def simulacra_setup2(_connection=None):
    inject_method_after_cls_method(simulacra_injection_test, type(services.sim_info_manager()), services.sim_info_manager().get_all.__name__)

@sims4.commands.Command('simulacra.list_sims', command_type=sims4.commands.CommandType.Live)
def simulacra_list_sims(_connection=None):
    SimulacraManager.simulacra_list_sims()

@sims4.commands.Command('simulacra.gral_test', command_type=sims4.commands.CommandType.Live)
def simulacra_test_hook(_connection=None):
    simulacra_test(_connection)

def simulacra_test(_connection=None):
    Messenger1.msg1()

class Messenger1:
    @staticmethod
    def msg1():
        Logger.log(f"Simulacra test 1!")

@inject_after_cls_method(Messenger1, Messenger1.msg1.__name__)
def msg2():
    Logger.log(f"Simulacra test 2!")

test_number = 0

@sims4.commands.Command('simulacra.num_test', command_type=sims4.commands.CommandType.Live)
def simulacra_num_test(_connection=None):
    global test_number
    test_number = test_number + 1
    Logger.log(f"Simulacra test number: {test_number}")

def simulacra_injection_test(*args, **kwargs):
    global test_number
    test_number = test_number + 1
    Logger.log(f"Simulacra test number: {test_number} :p")