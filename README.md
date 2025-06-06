# Thoughtful Robotic Package Sorter

A Python implementation of a package sorting system for Thoughtful's robotic automation factory. This system classifies packages based on their dimensions and mass to dispatch them to the appropriate handling stack.

## 🎯 Objective

The robotic arm sorts packages into three stacks based on volume and mass criteria:

- **STANDARD**: Packages that can be handled normally (not bulky or heavy)
- **SPECIAL**: Packages requiring special handling (either heavy OR bulky)
- **REJECTED**: Packages that cannot be processed (both heavy AND bulky)

## 📏 Classification Rules

### Bulky Package
A package is considered **bulky** if:
- Its volume (Width × Height × Length) ≥ 1,000,000 cm³, **OR**
- Any single dimension ≥ 150 cm

### Heavy Package
A package is considered **heavy** if:
- Its mass ≥ 20 kg

## 🚀 Quick Start

### Running the Demo
```bash
python package_sorter.py
```

This will run a demonstration with various package examples showing how the sorting works.

### Running Tests
```bash
python test_package_sorter.py
```

## 📊 Example Classifications

| Dimensions (cm) | Mass (kg) | Volume (cm³) | Classification | Stack |
|----------------|-----------|--------------|----------------|-------|
| 10×10×10 | 5 | 1,000 | Standard | STANDARD |
| 200×50×50 | 15 | 500,000 | Bulky (dimension) | SPECIAL |
| 50×50×50 | 25 | 125,000 | Heavy | SPECIAL |
| 100×100×100 | 10 | 1,000,000 | Bulky (volume) | SPECIAL |
| 150×50×50 | 20 | 375,000 | Heavy + Bulky | REJECTED |
| 200×100×100 | 30 | 2,000,000 | Heavy + Bulky | REJECTED |

## 🔧 Implementation Details

- **Language**: Python 3.x
- **No ternary operators**: Code uses explicit if-else statements for clarity
- **Input validation**: Prevents negative dimensions and mass
- **Comprehensive error handling**: Clear error messages for invalid inputs
- **Performance optimized**: Efficient classification logic
- **Well documented**: Clear docstrings and comments
---

