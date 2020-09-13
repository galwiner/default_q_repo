from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
from configuration import *

# Open communication with the server.
QMm = QuantumMachinesManager()

# Create a quantum machine based on the configuration.
QM1 = QMm.open_qm(config)

with program() as prog:
        play('playOp', 'qe1')

job = QM1.simulate(prog,
                   SimulationConfig(int(300)))

samples = job.get_simulated_samples()

samples.con1.plot()
