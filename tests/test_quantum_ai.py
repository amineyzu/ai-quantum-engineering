"""
Tests for the quantum AI engineering framework
"""

import pytest
from qiskit import QuantumCircuit
from quantum_ai_engineering.code_generator import QuantumCodeGenerator
from quantum_ai_engineering.optimizer import CircuitOptimizer
from quantum_ai_engineering.verifier import CircuitVerifier

def test_code_generation():
    """Test quantum code generation from natural language."""
    generator = QuantumCodeGenerator()
    
    # Test generating a Bell state circuit
    spec = "Create a Bell state circuit with 2 qubits"
    circuit = generator.generate(spec)
    
    assert circuit.num_qubits == 2
    assert len(circuit.data) > 0
    
    # Verify the circuit creates a Bell state
    verifier = CircuitVerifier()
    result = verifier.verify(circuit, method='state_vector')
    assert result['verified']

def test_circuit_optimization():
    """Test quantum circuit optimization."""
    # Create a simple circuit
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.h(0)
    circuit.cx(0, 1)
    
    # Optimize the circuit
    optimizer = CircuitOptimizer()
    optimized = optimizer.optimize(circuit)
    
    # Verify the optimized circuit
    verifier = CircuitVerifier()
    result = verifier.verify(optimized, method='unitary')
    assert result['verified']
    
    # Check that optimization reduced circuit depth
    assert len(optimized.data) <= len(circuit.data)

def test_error_detection():
    """Test quantum error detection."""
    # Create a circuit with error detection
    circuit = QuantumCircuit(3)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.cx(1, 2)
    
    # Verify error detection capabilities
    verifier = CircuitVerifier()
    result = verifier.verify(circuit, method='error_detection')
    
    assert result['verified']
    assert result['detection_rate'] > 0.9

def test_end_to_end():
    """Test end-to-end workflow."""
    # Generate circuit
    generator = QuantumCodeGenerator()
    spec = "Create a quantum teleportation circuit"
    circuit = generator.generate(spec)
    
    # Optimize circuit
    optimizer = CircuitOptimizer()
    optimized = optimizer.optimize(circuit)
    
    # Verify circuit
    verifier = CircuitVerifier()
    result = verifier.verify(optimized, method='measurement')
    
    assert result['verified']
    assert result['is_normalized']
    assert result['has_expected_basis']

def test_invalid_input():
    """Test handling of invalid inputs."""
    generator = QuantumCodeGenerator()
    
    with pytest.raises(ValueError):
        generator.generate("")
    
    optimizer = CircuitOptimizer()
    with pytest.raises(ValueError):
        optimizer.optimize(None)
    
    verifier = CircuitVerifier()
    with pytest.raises(ValueError):
        verifier.verify(None, method='invalid_method') 