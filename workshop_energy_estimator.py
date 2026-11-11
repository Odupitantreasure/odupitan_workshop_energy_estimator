# ==========================================
# CTE 213 PYTHON MINI PROJECT
# PROJECT: WORKSHOP ENERGY COST ESTIMATOR
# STUDENT NAME: ODUPITAN TREASURE TEMITOLA
# DEPARTMENT: MECHATRONICS ENGINEERING
# INSTITUTION: YABA COLLEGE OF TECHNOLOGY
# ==========================================


# Function to calculate energy consumption
def calculate_energy(power, hours):
    energy = (power * hours) / 1000
    return energy


# Function to calculate electricity cost
def calculate_cost(energy, tariff):
    cost = energy * tariff
    return cost


# Create a list to store machine information
machines = []

print("======================================")
print("      WORKSHOP ENERGY COST ESTIMATOR")
print("======================================")
print("Student Name: Odupitan Treasure Temitola")
print("Department: Mechatronics Engineering")
print("Institution: Yaba College of Technology")
print("======================================")


try:
    # Get the number of machines
    number_of_machines = int(input("Enter number of machines: "))

    if number_of_machines <= 0:
        print("Please enter a valid number of machines.")

    else:

        # Collect information about each machine
        for i in range(number_of_machines):

            print("\nMachine", i + 1)

            name = input("Enter machine name: ")

            power = float(input("Enter power rating (Watts): "))

            hours = float(input("Enter daily operating hours: "))

            if power <= 0 or hours <= 0 or hours > 24:
                print("Invalid power or operating hours.")
                continue

            # Calculate daily energy
            daily_energy = calculate_energy(power, hours)

            # Calculate monthly energy
            monthly_energy = daily_energy * 30

            # Store machine details
            machines.append({
                "name": name,
                "power": power,
                "hours": hours,
                "daily_energy": daily_energy,
                "monthly_energy": monthly_energy
            })

        if machines:

            # Get electricity tariff
            tariff = float(
                input("\nEnter electricity tariff per kWh: ")
            )

            if tariff <= 0:
                print("Invalid electricity tariff.")

            else:

                total_daily_energy = 0
                total_monthly_energy = 0
                total_monthly_cost = 0

                print("\n========== ENERGY REPORT ==========")

                # Display information for each machine
                for machine in machines:

                    daily_cost = calculate_cost(
                        machine["daily_energy"], tariff
                    )

                    monthly_cost = calculate_cost(
                        machine["monthly_energy"], tariff
                    )

                    total_daily_energy += machine["daily_energy"]

                    total_monthly_energy += machine["monthly_energy"]

                    total_monthly_cost += monthly_cost

                    print("\nMachine:", machine["name"])

                    print("Daily Energy:",
                          round(machine["daily_energy"], 2), "kWh")

                    print("Monthly Energy:",
                          round(machine["monthly_energy"], 2), "kWh")

                    print("Monthly Cost: ₦",
                          round(monthly_cost, 2))

                    # Special Feature: Energy Efficiency Alert
                    if machine["daily_energy"] > 20:
                        print("WARNING: High energy consumption!")

                    else:
                        print("Energy consumption is within the set limit.")

                # Display total energy consumption
                print("\n========== TOTAL SUMMARY ==========")

                print("Total Daily Energy:",
                      round(total_daily_energy, 2), "kWh")

                print("Total Monthly Energy:",
                      round(total_monthly_energy, 2), "kWh")

                print("Total Monthly Cost: ₦",
                      round(total_monthly_cost, 2))


except ValueError:

    print("Invalid input! Please enter numbers where required.")


print("\nThank you for using the Workshop Energy Cost Estimator!")

print("Developed by Odupitan Treasure Temitola.")
