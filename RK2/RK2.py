import unittest
from typing import List, Dict


class TestStreetManagerTDD(unittest.TestCase):

    def test_1_get_streets_residents_calculation(self):
        streets = [
            Street(1, "Улица Ленина"),
            Street(2, "Проспект Пушкина")
        ]

        houses = [
            House(1, 25, 1),  # Улица 1: 25 жильцов
            House(2, 40, 1),  # Улица 1: еще 40 = 65 всего
            House(3, 15, 2)  # Улица 2: 15 жильцов
        ]

        manager = StreetManager(streets, houses)

        residents = manager.get_streets_residents()

        street1 = manager.get_street_by_id(1)
        street2 = manager.get_street_by_id(2)

        self.assertEqual(residents[street1], 65)  # 25 + 40
        self.assertEqual(residents[street2], 15)
        self.assertIsInstance(residents, dict)

    def test_2_get_sorted_streets_with_houses_ordering(self):
        streets = [
            Street(1, "Улица Центральная"),
            Street(2, "Проспект Ленина"),
            Street(3, "Аллея Победы")
        ]

        houses = [
            House(1, 10, 1),
            House(2, 20, 2),
            House(3, 30, 3)
        ]

        manager = StreetManager(streets, houses)

        sorted_streets = manager.get_sorted_streets_with_houses()

        street_names = [street.name for street, _ in sorted_streets]

        expected_order = ["Аллея Победы", "Проспект Ленина", "Улица Центральная"]

        self.assertEqual(street_names, expected_order)

        self.assertEqual(len(sorted_streets), 3)
        for street, houses_list in sorted_streets:
            self.assertIsInstance(street, Street)
            self.assertIsInstance(houses_list, list)

    def test_3_get_streets_by_name_pattern_search(self):
        streets = [
            Street(1, "улица Ленина"),
            Street(2, "Улица Пушкина"),
            Street(3, "Проспект Мира"),
            Street(4, "площадь Улица")
        ]

        houses = [House(1, 10, i) for i in range(1, 5)]
        manager = StreetManager(streets, houses)

        found_streets = manager.get_streets_by_name_pattern("улица")

        self.assertEqual(len(found_streets), 3)

        found_names = [street.name for street in found_streets]
        self.assertIn("улица Ленина", found_names)
        self.assertIn("площадь Улица", found_names)
        self.assertIn("Улица Пушкина", found_names)
        self.assertNotIn("Проспект Мира", found_names)

# Сам текст программы

class Street:
    def __init__(self, street_id: int, name: str):
        self.street_id = street_id
        self.name = name

    def __str__(self):
        return f"Улица [ID: {self.street_id}, Название: {self.name}]"

    def __eq__(self, other):
        if not isinstance(other, Street):
            return False
        return self.street_id == other.street_id

    def __hash__(self):
        return hash(self.street_id)


class House:
    def __init__(self, house_id: int, residents_count: int, street_id: int):
        self.house_id = house_id
        self.residents_count = residents_count
        self.street_id = street_id

    def __str__(self):
        return f"Дом [ID: {self.house_id}, Жильцов: {self.residents_count}, ID улицы: {self.street_id}]"


class StreetManager:

    def __init__(self, streets: List[Street], houses: List[House]):
        self.streets = streets
        self.houses = houses

    def get_street_by_id(self, street_id: int) -> Street:
        for street in self.streets:
            if street.street_id == street_id:
                return street
        return None

    def get_streets_with_houses(self) -> Dict[Street, List[House]]:
        result = {}
        for house in self.houses:
            street = self.get_street_by_id(house.street_id)
            if street:
                if street not in result:
                    result[street] = []
                result[street].append(house)
        return result

    def get_sorted_streets_with_houses(self) -> List[tuple]:
        streets_houses = self.get_streets_with_houses()
        return sorted(streets_houses.items(), key=lambda x: x[0].name)

    def get_streets_residents(self) -> Dict[Street, int]:
        result = {}
        for house in self.houses:
            street = self.get_street_by_id(house.street_id)
            if street:
                result[street] = result.get(street, 0) + house.residents_count
        return result

    def get_streets_sorted_by_residents(self) -> List[tuple]:
        residents = self.get_streets_residents()
        return sorted(residents.items(), key=lambda x: x[1], reverse=True)

    def get_streets_by_name_pattern(self, pattern: str) -> List[Street]:
        return [s for s in self.streets if pattern in s.name]


# ==================== ДЕМОНСТРАЦИЯ И ЗАПУСК ====================

def demonstrate_tests():
    print("=== ТЕСТИРОВАНИЕ ФУНКЦИЙ ===\n")

    test_streets = [
        Street(1, "Улица Центральная"),
        Street(2, "Проспект Ленина"),
        Street(3, "Аллея Победы")
    ]

    test_houses = [
        House(1, 100, 1),
        House(2, 50, 2),
        House(3, 75, 3)
    ]

    manager = StreetManager(test_streets, test_houses)

    print("1. Тест подсчета жильцов:")
    residents = manager.get_streets_residents()
    for street, count in residents.items():
        print(f"   {street.name}: {count} жильцов")

    print("\n2. Тест сортировки улиц по алфавиту:")
    sorted_data = manager.get_sorted_streets_with_houses()
    for i, (street, houses_list) in enumerate(sorted_data, 1):
        print(f"   {i}. {street.name}: {len(houses_list)} дом(ов)")

    print("\n3. Тест поиска по названию:")
    found = manager.get_streets_by_name_pattern("аллея")
    print(f"   Найдено улиц с 'аллея': {len(found)}")
    for street in found:
        print(f"   - {street.name}")


if __name__ == "__main__":
    print("Запуск 3 тестов для существующих функций...\n")

    suite = unittest.TestLoader().loadTestsFromTestCase(TestStreetManagerTDD)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 50 + "\n")

    if result.wasSuccessful():
        print("Все 3 теста успешно пройдены!")
        print("\nДемонстрация тестируемых функций:\n")
        demonstrate_tests()
    else:
        print("Тесты не прошли. Проверьте реализацию функций.")