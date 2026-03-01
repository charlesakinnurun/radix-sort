import math

def get_digit(number, place):
    """
    Helper function to extract the digit at a specific place value.
    Example: get_digit(1234, 0) -> 4 (ones place)
             get_digit(1234, 1) -> 3 (tens place)
    """
    # // is floor division, % is modulo
    # We divide by 10^place to shift the target digit to the ones position
    # Then modulo 10 gives us that single digit
    return (number // (10 ** place)) % 10

def counting_sort_for_radix(arr, place):
    """
    A stable counting sort variant used as a subroutine for Radix Sort.
    Stability is crucial here: relative order of elements with the same 
    digit must be preserved for the algorithm to work correctly.
    """
    size = len(arr)
    # Output array that will have sorted numbers for the current digit
    output = [0] * size
    
    # Count array to store frequency of digits (0-9)
    count = [0] * 10

    # Step 1: Store count of occurrences of each digit in count[]
    for i in range(0, size):
        digit = get_digit(arr[i], place)
        count[digit] += 1

    # Step 2: Change count[i] so that count[i] now contains actual
    # position of this digit in output[] (Cumulative count)
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Step 3: Build the output array
    # We iterate backwards to maintain STABILITY.
    i = size - 1
    while i >= 0:
        digit = get_digit(arr[i], place)
        # Find the position in the count array and decrement
        count[digit] -= 1
        output[count[digit]] = arr[i]
        i -= 1

    # Step 4: Copy the output array to arr, so that arr now
    # contains sorted numbers according to current digit
    for i in range(0, size):
        arr[i] = output[i]

def visualize_step(arr, place, max_digits):
    """
    Prints a visual representation of the current state of the array.
    """
    label = ["Ones", "Tens", "Hundreds", "Thousands", "Ten-Thousands"]
    current_label = label[place] if place < len(label) else f"10^{place}"
    
    print(f"\n--- Sorting by {current_label} place ---")
    print("Index: ", "  ".join([f"{i:3}" for i in range(len(arr))]))
    
    # Create strings highlighting the digit being looked at
    highlighted_nums = []
    for num in arr:
        s_num = str(num).zfill(max_digits)
        # Highlight the digit at 'place' (counting from right)
        idx = len(s_num) - 1 - place
        if idx >= 0:
            formatted = s_num[:idx] + "[" + s_num[idx] + "]" + s_num[idx+1:]
        else:
            formatted = s_num
        highlighted_nums.append(formatted)
        
    print("Value: ", " ".join(highlighted_nums))

def radix_sort(arr):
    """
    The main Radix Sort function.
    Complexity: O(d * (n + k)) where d is digits, n is elements, k is base (10).
    """
    if not arr:
        return arr

    # Find the maximum number to know the number of digits
    max_val = max(arr)
    
    # Calculate how many digits the maximum number has
    # Example: log10(999) is ~2.99, floor is 2, +1 = 3 digits.
    max_digits = int(math.log10(max_val)) + 1 if max_val > 0 else 1
    
    print(f"Starting Radix Sort on: {arr}")
    print(f"Max value: {max_val} ({max_digits} digits deep)")

    # Perform counting sort for every digit. 
    # Instead of passing digit number, we pass 'place' (0, 1, 2...)
    for place in range(max_digits):
        visualize_step(arr, place, max_digits)
        counting_sort_for_radix(arr, place)
        print(f"Result: {arr}")

    return arr

def run_demonstration():
    """
    Runs several examples to show Radix Sort in action.
    """
    print("="*60)
    print("RADIX SORT VISUALIZER")
    print("="*60)

    # Example 1: Standard Unsorted List
    test_1 = [170, 45, 75, 90, 802, 24, 2, 66]
    print("\nEXAMPLE 1: Standard mix")
    radix_sort(test_1)

    # Example 2: Large numbers vs small numbers
    test_2 = [1000, 1, 10, 100]
    print("\n" + "="*60)
    print("EXAMPLE 2: Different magnitudes")
    radix_sort(test_2)

    # Example 3: Already sorted
    test_3 = [5, 15, 25, 35]
    print("\n" + "="*60)
    print("EXAMPLE 3: Already sorted")
    radix_sort(test_3)

if __name__ == "__main__":
    run_demonstration()