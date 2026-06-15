def atomic_mass_calculator():
    print("Atomic Mass Calculator")
    print("Calculates average atomic mass from isotopes\n")

    n = int(input("Enter number of isotopes: "))
    total_mass = 0
    total_abundance = 0

    for i in range(n):
        print(f"\nIsotope {i+1}:")
        mass = float(input("  Enter isotope mass (amu): "))
        abundance = float(input("  Enter percentage abundance (%): "))
        total_mass += mass * (abundance / 100)
        total_abundance += abundance

    if round(total_abundance) != 100:
        print("\nWarning: Total abundance should equal 100%")

    print(f"\nAverage Atomic Mass = {round(total_mass, 4)} amu")

atomic_mass_calculator()
