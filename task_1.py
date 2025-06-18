import heapq

def min_connection_cost(cables):
	# Create a min-heap from the cable costs
	heapq.heapify(cables)
	total_cost = 0

	# While there are more than one cable left
	while len(cables) > 1:
		# Pop the two cheapest cables
		first = heapq.heappop(cables)
		second = heapq.heappop(cables)

		# Calculate the cost of connecting them
		connection_cost = first + second
		total_cost += connection_cost

		# Push the new cable back into the heap
		heapq.heappush(cables, connection_cost)
		
	return total_cost

# Example usage
if __name__ == "__main__":
	cables = [4, 3, 2, 6]
	print("Minimum cost to connect all cables:", min_connection_cost(cables))  # Output: 29
	cables = [1, 2, 5, 10, 35, 89]
	print("Minimum cost to connect all cables:", min_connection_cost(cables))  # Output: 224
	cables = [2, 2, 3, 3]
	print("Minimum cost to connect all cables:", min_connection_cost(cables))  # Output: 20
	cables = [1, 2, 3, 4, 5]
	print("Minimum cost to connect all cables:", min_connection_cost(cables))