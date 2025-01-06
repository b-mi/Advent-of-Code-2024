from collections import Counter

# Function to apply the rules to a single number
def apply_rules(number, constant=2024):
    if number == 0:
        return [1]
    elif len(str(number)) % 2 == 0:  # If the number of digits is even
        half = len(str(number)) // 2
        return [int(str(number)[:half]), int(str(number)[half:])]
    else:
        return [number * constant]

# Function to process iterations and count the total numbers in the array
def process_iterations_count(initial_data, num_iterations, constant=2024):
    current_data = Counter(initial_data)  # Use Counter to track frequencies
    total_counts = []
    for iteration in range(num_iterations):
        next_data = Counter()
        for number, count in current_data.items():
            results = apply_rules(number, constant)
            for result in results:
                next_data[result] += count
        current_data = next_data  # Update the state
        total_counts.append((iteration + 1, sum(current_data.values())))  # Track total numbers
    return total_counts

# Main function to run the process
if __name__ == "__main__":
    # Input data
    initial_data = [3279, 998884, 1832781, 517, 8, 18864, 28, 0]  # Example initial data
    num_iterations = 75       # Number of iterations
    constant = 2024           # Multiplication constant

    # Run the process
    iteration_counts = process_iterations_count(initial_data, num_iterations, constant)

    # Display results
    for iteration, total_numbers in iteration_counts:
        print(f"Iteration {iteration}: Total Numbers = {total_numbers}")
