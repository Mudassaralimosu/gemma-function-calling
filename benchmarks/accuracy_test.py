import json
from typing import List, Dict
from statistics import mean
from sklearn.metrics import precision_score, recall_score

class AccuracyEvaluator:
    def __init__(self, test_cases: List[Dict]):
        self.test_cases = test_cases

    def evaluate_function_selection(self, actual: List[str], predicted: List[str]) -> Dict:
        """Evaluate how accurately the system selects functions"""
        # Convert to binary labels for all possible functions
        all_funcs = list(set(actual + predicted))
        actual_bin = [1 if f in actual else 0 for f in all_funcs]
        pred_bin = [1 if f in predicted else 0 for f in all_funcs]
        
        return {
            "precision": precision_score(actual_bin, pred_bin),
            "recall": recall_score(actual_bin, pred_bin),
            "f1": 2 * (precision * recall) / (precision + recall)
        }

    def evaluate_parameter_extraction(self) -> Dict:
        """Evaluate how accurately parameters are extracted"""
        errors = []
        for case in self.test_cases:
            expected = case["expected_params"]
            actual = case["actual_params"]
            
            param_errors = {}
            for param, value in expected.items():
                if param not in actual:
                    param_errors[param] = "missing"
                elif actual[param] != value:
                    param_errors[param] = f"expected {value}, got {actual[param]}"
            
            if param_errors:
                errors.append({
                    "function": case["function"],
                    "errors": param_errors
                })
        
        return {
            "total_tests": len(self.test_cases),
            "failed_tests": len(errors),
            "error_rate": len(errors) / len(self.test_cases),
            "detailed_errors": errors
        }