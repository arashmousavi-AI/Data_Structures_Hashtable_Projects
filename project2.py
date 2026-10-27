import random


class Node:
    """Represent one node in a binary search tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary search tree containing integer values."""

    def __init__(self):
        self.__root = None

    def insert(self, value):
        """Insert value into the binary search tree."""

        # first inserted value becomes the root.
        if self.__root is None:
            self.__root = Node(value)
            return True

        current = self.__root

        while True:
            # smaller values are inserted into the left subtree.
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return True

                current = current.left

            # Larger values are inserted into the right subtree.
            elif value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    return True

                current = current.right

            # duplicate values are not inserted.
            else:
                return False

    def search(self, value):
        """returning True if value is found in the tree."""

        current = self.__root

        while current is not None:

            if value == current.value:
                return True

            if value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def delete(self, value):
        """Delete value from the tree if it exists."""

        self.__root, deleted = self.__delete_recursive(self.__root, value)

        return deleted

    def __delete_recursive(self, node, value):
        """recursively locate and delete a node."""

        if node is None:
            return None, False

        if value < node.value:
            node.left, deleted = self.__delete_recursive(node.left, value)

            return node, deleted

        if value > node.value:
            node.right, deleted = self.__delete_recursive(node.right, value)

            return node, deleted

        # The node has been found.
        # case 1--> no left child.
        if node.left is None:
            return node.right, True

        # case 2--> no right child.
        if node.right is None:
            return node.left, True

        # case 3--> two children.
        # replace the node with the smallest value from its right subtree.
        successor = self.__find_min(node.right)
        node.value = successor.value

        node.right, _ = self.__delete_recursive(node.right, successor.value)

        return node, True

    def __find_min(self, node):
        """return the node containing the smallest value."""

        current = node
        while current.left is not None:
            current = current.left

        return current


    def in_order_traversal(self):
        """return tree values using in-order traversal."""

        result = []
        self.__in_order(self.__root, result)

        return result


    def __in_order(self, node, result):
        """Recursively perform an in-order traversal."""

        if node is not None:
            self.__in_order(node.left,result)

            result.append(node.value)

            self.__in_order(node.right, result)


    def pre_order_traversal(self):
        """return tree values using pre-order traversal."""

        result = []
        self.__pre_order(self.__root,result)

        return result


    def __pre_order(self, node, result):
        """Recursively perform a pre-order traversal."""

        if node is not None:
            result.append(node.value)
            self.__pre_order(node.left, result)

            self.__pre_order(node.right, result)


    def post_order_traversal(self):
        """return tree values using post-order traversal."""

        result = []
        self.__post_order(self.__root, result)

        return result


    def __post_order(self, node, result):
        """recursively perform a post-order traversal."""

        if node is not None:
            self.__post_order(node.left, result)
            self.__post_order(node.right, result)

            result.append(node.value)


    def height(self):
        """return the height of the binary search tree."""

        return self.__height(self.__root)


    def __height(self, node):
        """Recursively calculate the height of a subtree."""

        # an empty tree has height -1.
        if node is None:
            return -1

        left_height = self.__height(node.left)
        right_height = self.__height(node.right)

        return 1 + max(left_height, right_height)


def task2_testing():
    """Perform the required BST operation tests."""

    print("-------------------------" )
    print("TASK 2: BST OPERATIONS AND FUNCTION TESTING")
    print("-------------------------")

    #Generating 64 unique random integers from 1 through 128.
    values = random.sample(range(1, 129),64)

    tree = BinarySearchTree()

    print("\noriginal values:")
    print(values)

    #inserting all values into the BST.
    for value in values:
        tree.insert(value)

    print("\nTree height after insertion:")
    print(tree.height())

    # Search for the first, middle, and last values.
    search_values = [values[0], values[len(values) // 2], values[-1]]

    print("\nSearch Results")

    for value in search_values:
        print(f"Search for {value}: " f"{tree.search(value)}")

    print("\nIn-order Traversal:")
    print(tree.in_order_traversal())

    print("\nPre-order Traversal:")
    print(tree.pre_order_traversal())

    print("\nPost-order Traversal:")
    print(tree.post_order_traversal())


    #deleting the first, middle, and last values.
    delete_values = [values[0], values[len(values) // 2], values[-1]]

    print("\nDeletion Tests")

    for value in delete_values:

        print(f"\nDeleting {value}")
        deleted = tree.delete(value)

        print(f"Deleted: {deleted}")
        print(f"Tree height: {tree.height()}")
        print("In-order Traversal:")
        print(tree.in_order_traversal())

    print("\nFinal Tree Height:")
    print(tree.height())


def test_dataset(values, dataset_name):
    """building and test a fresh BST using one dataset."""

    tree = BinarySearchTree()

    for value in values:
        tree.insert(value)

    print("\n" + "---------------")
    print(dataset_name)
    print("---------------")

    print(f"Number of values: {len(values)}")
    print(f"Tree height: {tree.height()}")

    print("In-order Traversal:")
    print(tree.in_order_traversal())

    return tree.height()


def task3_testing():
    """testing random and worst-case BST datasets."""

    print("\n")
    print("--------------")
    print("TASK 3: TESTING WITH DIFFERENT DATA SETS")
    print("--------------")

    heights = {}

    # Random datasets required by the assignment.
    random_datasets = [("Random Data Set - 64 Integers", random.sample(range(1, 129), 64)),("Random Data Set - 128 Integers", random.sample(range(1, 257), 128)), ("Random Data Set - 256 Integers", random.sample(range(1, 513), 256))]

    for name, values in random_datasets:
        heights[name] = test_dataset(values, name)

    # Ascending input produces a worst-case BST.
    worst_case_datasets = [("Worst-Case Data Set - 64 Integers", list(range(1, 65))), ("Worst-Case Data Set - 128 Integers", list(range(1, 129))), ("Worst-Case Data Set - 256 Integers", list(range(1, 257)))]

    for name, values in worst_case_datasets:
        heights[name] = test_dataset(values, name)

    print("\n")
    print("-------------")
    print("TREE HEIGHT SUMMARY")
    print("-------------")

    for name, height in heights.items():
        print(f"{name}: {height}")


def main():
    """Run all BST project tests."""

    # a fixed seed makes the random tests reproducible.
    random.seed(42)
    task2_testing()
    task3_testing()


if __name__ == "__main__":
    main()