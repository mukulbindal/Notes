import cv2
import numpy as np
from scipy.spatial import distance

def preprocess_image(binary_img, dilation_size=5, extension_length=10):
    """
    Preprocess the binary image to connect shapes and arrows.
    - Dilates shapes to ensure intersections.
    - Extends arrow lines to bridge gaps.
    """
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (dilation_size, dilation_size))
    dilated_img = cv2.dilate(binary_img, kernel, iterations=1)

    # Extend arrows
    edges = cv2.Canny(binary_img, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=20, maxLineGap=10)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            dx, dy = x2 - x1, y2 - y1
            norm = np.sqrt(dx**2 + dy**2)
            if norm != 0:
                dx, dy = (dx / norm) * extension_length, (dy / norm) * extension_length
            cv2.line(dilated_img, 
                     (int(x1 - dx), int(y1 - dy)), 
                     (int(x2 + dx), int(y2 + dy)), 
                     255, thickness=2)
    return dilated_img

def find_nearest_shape(point, shapes, max_distance=20):
    """
    Find the nearest shape to a given point.
    - point: (x, y) coordinates of the arrowhead.
    - shapes: List of shape bounding boxes [(x1, y1, x2, y2), ...].
    """
    x, y = point
    nearest_shape = None
    min_dist = float('inf')

    for shape in shapes:
        x1, y1, x2, y2 = shape['bounding_box']
        dist = min(
            distance.euclidean((x, y), (x1, y1)),
            distance.euclidean((x, y), (x2, y1)),
            distance.euclidean((x, y), (x1, y2)),
            distance.euclidean((x, y), (x2, y2))
        )
        if dist < min_dist and dist <= max_distance:
            min_dist = dist
            nearest_shape = shape

    return nearest_shape

def traverse_with_approximation(binary_img, nodes, arrowheads, max_distance=20):
    """
    Build a directed graph using nearest-point approximation.
    - nodes: List of detected shapes with bounding boxes and names.
    - arrowheads: Detected arrowhead points [(x, y), ...].
    """
    graph = {node['name']: [] for node in nodes}

    for arrow in arrowheads:
        ax, ay = arrow['center']

        # Find the nearest destination shape
        destination_node = find_nearest_shape((ax, ay), nodes, max_distance=max_distance)
        if not destination_node:
            continue

        # Traverse backward from arrowhead to find the source node
        source_node = None
        queue = [(ax, ay)]
        visited = set()

        while queue and not source_node:
            x, y = queue.pop(0)
            if (x, y) in visited:
                continue
            visited.add((x, y))

            # Check if we're inside a node
            source_node = find_nearest_shape((x, y), nodes, max_distance=max_distance)
            if source_node:
                break

            # Add neighboring pixels to the queue
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= nx < binary_img.shape[0] and 0 <= ny < binary_img.shape[1] and binary_img[nx, ny] == 255:
                    queue.append((nx, ny))

        # Add edge to the graph if both source and destination are found
        if source_node and destination_node and source_node['name'] != destination_node['name']:
            graph[source_node['name']].append({
                "to": destination_node['name'],
                "relationship": None  # Add relationship label if available
            })

    return graph

# Example usage
def main():
    # Load binary image
    binary_img = cv2.imread('binary_image.png', 0)
    binary_img = cv2.threshold(binary_img, 128, 255, cv2.THRESH_BINARY)[1]

    # Preprocess to connect shapes and arrows
    processed_img = preprocess_image(binary_img)

    # Detected nodes (shapes) and arrowheads
    nodes = [
        {"name": "Node1", "bounding_box": (50, 50, 100, 100)},
        {"name": "Node2", "bounding_box": (200, 200, 250, 250)},
    ]
    arrowheads = [{"center": (105, 105)}, {"center": (210, 210)}]

    # Build graph
    graph = traverse_with_approximation(processed_img, nodes, arrowheads)
    print("Directed Graph:", graph)

    # Save and display results
    cv2.imwrite('processed_image.png', processed_img)
    cv2.imshow('Processed Image', processed_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
