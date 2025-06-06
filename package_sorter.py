def sort(width, height, length, mass):
    """
    Sort packages into appropriate stacks based on their dimensions and mass.
    
    Args:
        width (float): Package width in centimeters
        height (float): Package height in centimeters  
        length (float): Package length in centimeters
        mass (float): Package mass in kilograms
        
    Returns:
        str: Stack name where package should go ('STANDARD', 'SPECIAL', or 'REJECTED')
        
    Rules:
        - Bulky: volume >= 1,000,000 cm³ OR any dimension >= 150 cm
        - Heavy: mass >= 20 kg
        - STANDARD: not bulky and not heavy
        - SPECIAL: either heavy or bulky (but not both)
        - REJECTED: both heavy and bulky
    """
    
    if width < 0 or height < 0 or length < 0 or mass < 0:
        raise ValueError("Dimensions and mass must be non-negative")
    
    volume = width * height * length
    
    is_bulky = False
    if volume >= 1000000:
        is_bulky = True
    if width >= 150 or height >= 150 or length >= 150:
        is_bulky = True
    
    is_heavy = False
    if mass >= 20:
        is_heavy = True
    
    if is_heavy and is_bulky:
        return "REJECTED"
    
    if is_heavy or is_bulky:
        return "SPECIAL"
    
    return "STANDARD"


def main():
    print("=== Thoughtful Robotic Package Sorter ===\n")
    
    test_packages = [
        (10, 10, 10, 5, "Small standard package"),
        (200, 50, 50, 15, "Large but light package (bulky)"),
        (50, 50, 50, 25, "Small but heavy package (heavy)"),
        (200, 100, 100, 30, "Large and heavy package (rejected)"),
        (149, 149, 149, 19.9, "Edge case - just under limits"),
        (150, 50, 50, 10, "Edge case - exactly 150cm dimension"),
        (100, 100, 100, 20, "Edge case - exactly 20kg mass")
    ]
    
    for width, height, length, mass, description in test_packages:
        result = sort(width, height, length, mass)
        volume = width * height * length
        print(f"{description}:")
        print(f"  Dimensions: {width}×{height}×{length} cm (Volume: {volume:,} cm³)")
        print(f"  Mass: {mass} kg")
        print(f"  Stack: {result}")
        print()


if __name__ == "__main__":
    main()