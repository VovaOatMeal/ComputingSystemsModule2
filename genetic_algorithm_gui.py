import random
import tkinter as tk
from tkinter import ttk

# Define the items as (weight, value) pairs
items = [
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 8),
    (9, 10)
]

# Initialize a population with random solutions
def initialize_population(population_size, items):
    population = []
    for _ in range(population_size):
        solution = [random.randint(0, 1) for _ in items]
        population.append(solution)
    return population

# Calculate the fitness of a solution
def fitness(solution, items, max_weight):
    total_weight = sum(solution[i] * items[i][0] for i in range(len(items)))
    total_value = sum(solution[i] * items[i][1] for i in range(len(items)))
    if total_weight > max_weight:
        return 0
    return total_value

# Select parents for crossover based on their fitness
def select_parents(population, items, max_weight):
    parents = []
    for _ in range(2):
        parent1 = random.choice(population)
        parent2 = random.choice(population)
        if fitness(parent1, items, max_weight) > fitness(parent2, items, max_weight):
            parents.append(parent1)
        else:
            parents.append(parent2)
    return parents

# Perform crossover to create a new solution
def crossover(parents):
    point = random.randint(1, len(parents[0]) - 1)
    child = parents[0][:point] + parents[1][point:]
    return child

# Perform mutation on a solution
def mutate(solution, mutation_rate):
    for i in range(len(solution)):
        if random.random() < mutation_rate:
            solution[i] = 1 - solution[i]
    return solution

# Main genetic algorithm
def genetic_algorithm(items, max_weight, population_size, mutation_rate, generations):
    population = initialize_population(population_size, items)
    for _ in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parents = select_parents(population, items, max_weight)
            child = crossover(parents)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
    best_solution = max(population, key=lambda x: fitness(x, items, max_weight))
    return best_solution

class GeneticAlgorithmGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Genetic Algorithm for Knapsack Problem")

        # Create and place input fields and labels
        self.label_population = ttk.Label(master, text="Population Size:")
        self.label_population.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_population = ttk.Entry(master)
        self.entry_population.grid(row=0, column=1, padx=10, pady=5)

        self.label_mutation_rate = ttk.Label(master, text="Mutation Rate:")
        self.label_mutation_rate.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_mutation_rate = ttk.Entry(master)
        self.entry_mutation_rate.grid(row=1, column=1, padx=10, pady=5)

        self.label_generations = ttk.Label(master, text="Generations:")
        self.label_generations.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_generations = ttk.Entry(master)
        self.entry_generations.grid(row=2, column=1, padx=10, pady=5)

        self.label_max_weight = ttk.Label(master, text="Max Weight:")
        self.label_max_weight.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_max_weight = ttk.Entry(master)
        self.entry_max_weight.grid(row=3, column=1, padx=10, pady=5)

        self.btn_run_algorithm = ttk.Button(master, text="Run Algorithm", command=self.run_algorithm)
        self.btn_run_algorithm.grid(row=4, column=0, columnspan=2, pady=10)

        # Create and place result labels
        self.label_best_solution = ttk.Label(master, text="Best Solution:")
        self.label_best_solution.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.result_best_solution = ttk.Label(master, text="")
        self.result_best_solution.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        self.label_total_value = ttk.Label(master, text="Total Value:")
        self.label_total_value.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.result_total_value = ttk.Label(master, text="")
        self.result_total_value.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        self.label_total_weight = ttk.Label(master, text="Total Weight:")
        self.label_total_weight.grid(row=7, column=0, padx=10, pady=5, sticky="e")
        self.result_total_weight = ttk.Label(master, text="")
        self.result_total_weight.grid(row=7, column=1, padx=10, pady=5, sticky="w")

    def run_algorithm(self):
        # Get user inputs from the GUI
        population_size = int(self.entry_population.get())
        mutation_rate = float(self.entry_mutation_rate.get())
        generations = int(self.entry_generations.get())
        max_weight = int(self.entry_max_weight.get())

        # Run the genetic algorithm
        best_solution = genetic_algorithm(items, max_weight, population_size, mutation_rate, generations)

        # Update the result labels
        self.result_best_solution.config(text=str(best_solution))
        self.result_total_value.config(text=str(sum(best_solution[i] * items[i][1] for i in range(len(items)))))
        self.result_total_weight.config(text=str(sum(best_solution[i] * items[i][0] for i in range(len(items)))))

# Create the main window and run the GUI
root = tk.Tk()
app = GeneticAlgorithmGUI(root)
root.mainloop()
