import heapq

def merge_k_lists(lists):
	# Create a min-heap to store the head of each list
	min_heap = []

	# Initialize the heap with the head of each list
	for i, lst in enumerate(lists):
		if lst:  # Check if the list is not empty
			heapq.heappush(min_heap, (lst[0], i, 0))  # (value, list index, element index)
			
	# Resultant merged list
	merged_list = []
	while min_heap:
		# Pop the smallest element from the heap
		value, list_index, element_index = heapq.heappop(min_heap)
		merged_list.append(value)

		# If there is a next element in the same list, push it to the heap
		if element_index + 1 < len(lists[list_index]):
			next_value = lists[list_index][element_index + 1]
			heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

	return merged_list	

# Example usage
if __name__ == "__main__":
	lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
	merged_list = merge_k_lists(lists)
	print("Відсортований список:", merged_list)