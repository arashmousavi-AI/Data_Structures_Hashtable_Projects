"""
filename: Hashtable.py
Author: Arash Mousavi
Version: 1.0
First date created: 10/1/2026
"""

# h(k, i) = (k + i^3) mod10

class HashTable:
    """Hash table using open addressing for collision resolution."""

    def __init__(self, size=10):
        """creating a hash table with all positions initialized to -1."""
        self.__table = [-1] * size
        self.__size = size

    def hash(self, key, i):
        """calculating the hash index for key at iteration i."""
        return (key + i ** 3) % self.__size

    def insert(self, key):
        """inserting a key into the hash table using open addressing."""

        # start probing with iteration 0.
        for i in range(self.__size):
            index = self.hash(key, i)

            print(f"Iteration {i}: h({key},{i}) = " f"({key} + {i}^3) mod {self.__size} = {index}")

            #inserting the key if the calculated slot is empty.
            if self.__table[index] == -1:
                self.__table[index] = key
                print(f"Key {key} is placed at index {index}.")
                return True

            #If the position is occupied, continue probing.
            print(f"Collision at index {index}.")

        #key cannot be inserted if no empty position is found.
        print(f"Key {key} could not be inserted.")
        return False

    def __str__(self):
        """returning the current contents of the hash table."""
        return str(self.__table)


def main():
    """inserting the required keys and display the table after each insertion."""

    #creating an empty hash table of size 10.
    hash_table = HashTable(10)
    keys = [15, 27, 5, 12, 35]

    print("Initial Hash Table")
    print(hash_table)

    # inserting each required key one at a time.
    for key in keys:
        print(f"\nInserting key {key}")

        hash_table.insert(key)

        print(f"Hash table after inserting {key}:")
        print(hash_table)

    print("\nFinal Hash Table")
    print(hash_table)


if __name__ == "__main__":
    main()