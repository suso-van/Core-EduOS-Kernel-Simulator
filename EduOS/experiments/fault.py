"""
Fault Injection Module
Simulates realistic system faults and stress conditions
"""

import random
from typing import Dict, List


class FaultInjector:
    """Manages fault injection for system simulation"""
    
    def __init__(self, cpu_fault_rate=0.2, page_fault_rate=0.3, deadlock_risk=0.1):
        """
        Initialize fault injector with configurable fault rates
        
        Args:
            cpu_fault_rate: Probability of CPU delay (0.0-1.0)
            page_fault_rate: Probability of page fault (0.0-1.0)
            deadlock_risk: Probability of deadlock condition (0.0-1.0)
        """
        self.cpu_fault_rate = cpu_fault_rate
        self.page_fault_rate = page_fault_rate
        self.deadlock_risk = deadlock_risk
        
        # Metrics
        self.cpu_faults_injected = 0
        self.page_faults_injected = 0
        self.deadlock_conditions = 0
    
    def inject_cpu_delay(self) -> bool:
        """
        Inject CPU delay fault
        
        Returns:
            bool: True if CPU delay should occur
        """
        if random.random() < self.cpu_fault_rate:
            self.cpu_faults_injected += 1
            return True
        return False
    
    def inject_page_fault(self) -> bool:
        """
        Inject page fault
        
        Returns:
            bool: True if page fault should occur
        """
        if random.random() < self.page_fault_rate:
            self.page_faults_injected += 1
            return True
        return False
    
    def inject_deadlock_condition(self) -> bool:
        """
        Inject deadlock risk
        
        Returns:
            bool: True if deadlock condition should occur
        """
        if random.random() < self.deadlock_risk:
            self.deadlock_conditions += 1
            return True
        return False
    
    def get_fault_statistics(self) -> Dict[str, int]:
        """
        Get fault injection statistics
        
        Returns:
            dict: Statistics of injected faults
        """
        return {
            'cpu_faults': self.cpu_faults_injected,
            'page_faults': self.page_faults_injected,
            'deadlock_conditions': self.deadlock_conditions
        }
    
    def reset_statistics(self):
        """Reset fault statistics"""
        self.cpu_faults_injected = 0
        self.page_faults_injected = 0
        self.deadlock_conditions = 0


# Global fault injector instance
_fault_injector = FaultInjector()


def inject_cpu_delay(probability=None):
    """
    Inject CPU delay fault (backward compatible)
    
    Args:
        probability: Optional probability override
    
    Returns:
        bool: True if fault should occur
    """
    if probability is not None:
        return random.random() < probability
    return _fault_injector.inject_cpu_delay()


def inject_page_fault(probability=None):
    """
    Inject page fault (backward compatible)
    
    Args:
        probability: Optional probability override
    
    Returns:
        bool: True if fault should occur
    """
    if probability is not None:
        return random.random() < probability
    return _fault_injector.inject_page_fault()


def inject_deadlock_risk(probability=None):
    """
    Inject deadlock risk
    
    Args:
        probability: Optional probability override
    
    Returns:
        bool: True if risk should occur
    """
    if probability is not None:
        return random.random() < probability
    return _fault_injector.inject_deadlock_condition()


def get_fault_injector() -> FaultInjector:
    """Get the global fault injector instance"""
    return _fault_injector


def reset_faults():
    """Reset all fault statistics"""
    _fault_injector.reset_statistics()
