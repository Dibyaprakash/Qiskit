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


#Plot Single Qubit 
plot_bloch_multivector(stateVectorResult)


#plot qsphere 
plot_state_qsphere(stateVectorResult)


#Add X-gate and draw
qc.x(qr[0])
qc.draw(output = 'mpl')


#Execute
result = execute(qc,backend).result()
stateVectorResult = result.get_statevector(qc)
print("\n Qunatum State is :",stateVectorResult)


#Plot Single Qubit 
plot_bloch_multivector(stateVectorResult)


#plot qsphere 
plot_state_qsphere(stateVectorResult)


#Unitary Operator
backend = Aer.get_backend('unitary_simulator')
unitary = execute(qc,backend)
unitary.result().get_unitary(qc,decimals=3)


#Measurement
cr = ClassicalRegister(1,"cr")
qr = QuantumRegister(1,"qr")
qc = QuantumCircuit(qr,cr)
qc.x(qr[0])
qc.measure(0,0)
qc.draw(output = 'mpl')


#Execute Quantum Circuit
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1000)
result = job.result()
counts = result.get_counts(qc)
print("\nTotal Counts are :",counts)


plot_histogram(counts)


qc = QuantumCircuit(2,2,name ="qc")
qc.x(0)
qc.barrier()
qc.measure(0,0)
qc.measure(1,1)
# qc.measure([0,1], [0,1])
qc.draw('mpl')


# Measuring all at a time
qc = QuantumCircuit(2,name ="qc")
qc.x(0)
qc.measure_all()
qc.draw('mpl')
