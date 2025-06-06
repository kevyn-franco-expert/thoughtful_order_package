import unittest
from package_sorter import sort


class TestPackageSorter(unittest.TestCase):
    """
    Comprehensive test suite for the package sorting function
    """
    
    def test_standard_packages(self):
        """Test packages that should go to STANDARD stack"""
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")
        
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")
        
        self.assertEqual(sort(99, 99, 99, 19.9), "STANDARD")
        
        self.assertEqual(sort(0, 0, 0, 0), "STANDARD")
    
    def test_bulky_packages_by_volume(self):
        """Test packages that are bulky due to volume >= 1,000,000 cm³"""
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")
        
        self.assertEqual(sort(150, 150, 150, 15), "SPECIAL")
        
        self.assertEqual(sort(200, 200, 25, 5), "SPECIAL")
    
    def test_bulky_packages_by_dimension(self):
        """Test packages that are bulky due to dimension >= 150 cm"""
        self.assertEqual(sort(150, 50, 50, 10), "SPECIAL")
        self.assertEqual(sort(200, 10, 10, 5), "SPECIAL")
        
        self.assertEqual(sort(50, 150, 50, 10), "SPECIAL")
        self.assertEqual(sort(10, 200, 10, 5), "SPECIAL")
        
        self.assertEqual(sort(50, 50, 150, 10), "SPECIAL")
        self.assertEqual(sort(10, 10, 200, 5), "SPECIAL")
        
        self.assertEqual(sort(150, 150, 50, 10), "SPECIAL")
        self.assertEqual(sort(200, 200, 200, 15), "SPECIAL")
    
    def test_heavy_packages(self):
        """Test packages that are heavy (mass >= 20 kg)"""
        self.assertEqual(sort(50, 50, 50, 20), "SPECIAL")
        
        self.assertEqual(sort(30, 30, 30, 25), "SPECIAL")
        self.assertEqual(sort(10, 10, 10, 100), "SPECIAL")
    
    def test_rejected_packages(self):
        """Test packages that are both heavy and bulky (REJECTED)"""
        self.assertEqual(sort(100, 100, 100, 25), "REJECTED")
        
        self.assertEqual(sort(150, 50, 50, 20), "REJECTED")
        self.assertEqual(sort(50, 150, 50, 30), "REJECTED")
        self.assertEqual(sort(50, 50, 150, 40), "REJECTED")
        
        self.assertEqual(sort(200, 200, 200, 50), "REJECTED")
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions"""
        self.assertEqual(sort(100, 100, 100, 19.9), "SPECIAL")
        
        self.assertEqual(sort(99, 99, 99, 20), "SPECIAL")
        
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
        self.assertEqual(sort(150, 50, 50, 20), "REJECTED")
        
        self.assertEqual(sort(0.1, 0.1, 0.1, 0.1), "STANDARD")
        
        self.assertEqual(sort(0, 100, 100, 10), "STANDARD")
        self.assertEqual(sort(100, 0, 100, 10), "STANDARD")
        self.assertEqual(sort(100, 100, 0, 10), "STANDARD")
    
    def test_input_validation(self):
        """Test input validation for negative values"""
        with self.assertRaises(ValueError):
            sort(-1, 10, 10, 10)
        
        with self.assertRaises(ValueError):
            sort(10, -1, 10, 10)
        
        with self.assertRaises(ValueError):
            sort(10, 10, -1, 10)
        
        with self.assertRaises(ValueError):
            sort(10, 10, 10, -1)
        
        with self.assertRaises(ValueError):
            sort(-1, -1, -1, -1)
    
    def test_floating_point_precision(self):
        """Test floating point precision handling"""
        self.assertEqual(sort(99.9, 99.9, 100.1, 19.99), "STANDARD")
        self.assertEqual(sort(149.99, 50, 50, 10), "STANDARD")
        self.assertEqual(sort(150.01, 50, 50, 10), "SPECIAL")
        self.assertEqual(sort(50, 50, 50, 19.999), "STANDARD")
        self.assertEqual(sort(50, 50, 50, 20.001), "SPECIAL")


def run_performance_test():
    """
    Simple performance test to ensure function runs efficiently
    """
    import time
    
    print("Running performance test...")
    start_time = time.time()
    
    # Run function 10,000 times with various inputs
    for i in range(10000):
        sort(i % 200, (i * 2) % 200, (i * 3) % 200, (i * 0.01) % 50)
    
    end_time = time.time()
    print(f"Processed 10,000 packages in {end_time - start_time:.4f} seconds")
    print(f"Average time per package: {(end_time - start_time) * 1000 / 10000:.4f} ms")


if __name__ == "__main__":
    print("=== Running Unit Tests ===")
    unittest.main(verbosity=2, exit=False)
    
    print("\n" + "="*50)
    
    run_performance_test()