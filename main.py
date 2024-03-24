from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.quick_sort import quick_sort
from data_generator.data_generator import generate_word_list
from metrics.metrics import measure_time
from graphs.graphs import create_graph
import pandas as pd

def main():
    """
    Main function to demonstrate sorting algorithms with randomly generated words and measure execution time.

    This function generates a list of random words, sorts them using three different sorting algorithms,
    measures the execution time of each sorting algorithm, and prints the sorted lists along with their execution times.

    Args:
        None

    Returns:
        None
    """
    # Generate a list of random words
    num_words = [5, 10, 15, 20, 30, 40, 50, 80]
    sorts = ["random", "sort", "reverse"]
    word_length = 10

    results = []
    for sort in sorts:
        for num_word in num_words:
            iteration = []
            word_list = generate_word_list(num_word, word_length, sort)

            iteration.append(word_length)
            iteration.append(num_word)

            # Sort the list using each sorting algorithm and measure execution time
            time_bubble = measure_time(bubble_sort, word_list.copy())
            iteration.append(time_bubble)

            time_merge = measure_time(merge_sort, word_list.copy())
            iteration.append(time_merge)

            time_quick = measure_time(quick_sort, word_list.copy())
            iteration.append(time_quick)
            
            results.append(iteration)

    df = pd.DataFrame(results)
    print(df)
    create_graph(results=results, graphs=3, sorts=sorts)

if __name__ == "__main__":
    main()
