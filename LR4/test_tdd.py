import unittest
from main import QuadraticSolver


class TestQuadraticSolverTDD(unittest.TestCase):

    def test_1_no_real_roots(self):
        # Уравнение: x^4 + 2x^2 + 5 = 0 (D < 0)
        solver = QuadraticSolver()
        roots = solver.solve_biquadratic(1, 2, 5)

        # Должно вернуть пустой список
        self.assertEqual(roots, [])

    def test_2_four_real_roots(self):
        # Уравнение: x^4 - 5x^2 + 4 = 0
        # Корни: ±2, ±1
        solver = QuadraticSolver()
        roots = solver.solve_biquadratic(1, -5, 4)

        self.assertEqual(len(roots), 4)

        expected = [2.0, -2.0, 1.0, -1.0]
        for root in expected:
            self.assertIn(root, roots)

    def test_3_single_root_zero(self):
        # Уравнение: x^4 = 0
        solver = QuadraticSolver()
        roots = solver.solve_biquadratic(1, 0, 0)

        # Должен быть один корень: 0
        self.assertEqual(len(roots), 1)
        self.assertEqual(roots[0], 0.0)


if __name__ == "__main__":
    unittest.main()