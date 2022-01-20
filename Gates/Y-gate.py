from qiskit import *
from qiskit.visualization import plot_bloch_multivector, plot_state_qsphere, plot_histogram
%matplotlib inline
qr = QuantumRegister(1,"qr")
qc = QuantumCircuit(qr)


#Execute Quantum Circuit
backend = Aer.get_backend('statevector_simulator')
result = execute(qc,backend).result()
stateVectorResult = result.get_statevector(qc)
print("\n Qunatum State is :",stateVectorResult)


plot_bloch_multivector(stateVectorResult)


plot_state_qsphere(stateVectorResult)


#Add Y-gate and draw
qc.y(0)
qc.draw(output = 'mpl')


#Execute
result = execute(qc,backend).result()
stateVectorResult = result.get_statevector(qc)
print("\n Qunatum State is :",stateVectorResult)


plot_bloch_multivector(stateVectorResult)


plot_state_qsphere(stateVectorResult)


#Unitary Operator
backend = Aer.get_backend('unitary_simulator')
unitary = execute(qc,backend)
unitary.result().get_unitary(qc,decimals=3)


#Measurement
cr = ClassicalRegister(1,"cr")
qr = QuantumRegister(1,"qr")
qc = QuantumCircuit(qr,cr)
qc.y(qr[0])
qc.measure(0,0)
qc.draw(output = 'mpl')


#Execute Quantum Circuit
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1000)
result = job.result()
counts = result.get_counts(qc)
print("\nTotal Counts are :",counts)


plot_histogram(counts)
