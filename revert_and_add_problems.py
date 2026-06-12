import os
import json
import re

data_dir = "data"

new_problems = {
    "01_introductory": [
        {
            "id": "1624_chessboard_and_queens", "title": "Chessboard and Queens", "source": "CSES 1624",
            "statement": "Your task is to place eight queens on a chessboard so that no two queens are attacking each other...",
            "inputFormat": "The input has eight lines, and each of them has eight characters. Each square is either free (`.`) or reserved (`*`).",
            "outputFormat": "Print one integer: the number of ways you can place the queens.",
            "constraints": "<ul><li>The grid is exactly $8 \\times 8$.</li></ul>",
            "exampleInput": "........\n........\n..*.....\n........\n........\n........\n........\n........", "exampleOutput": "65"
        },
        {
            "id": "1069_repetitions", "title": "Repetitions", "source": "CSES 1069",
            "statement": "You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.",
            "inputFormat": "The only input line contains a string of $n$ characters.",
            "outputFormat": "Print one integer: the length of the longest repetition.",
            "constraints": "<ul><li>$1 \\le n \\le 10^6$</li></ul>",
            "exampleInput": "ATTCGGGG", "exampleOutput": "4"
        }
    ],
    "02_sorting_and_searching": [
        {
            "id": "1620_factory_machines", "title": "Factory Machines", "source": "CSES 1620",
            "statement": "A factory has $n$ machines which can be used to make products. Your goal is to make a total of $t$ products. What is the shortest time needed?",
            "inputFormat": "The first input line has two integers $n$ and $t$: the number of machines and products.\nThe next line has $n$ integers $k_1, k_2, \\dots, k_n$.",
            "outputFormat": "Print one integer: the minimum time needed to make $t$ products.",
            "constraints": "<ul><li>$1 \\le n \\le 2 \\cdot 10^5$</li><li>$1 \\le t \\le 10^9$</li><li>$1 \\le k_i \\le 10^9$</li></ul>",
            "exampleInput": "3 7\n3 2 5", "exampleOutput": "8"
        },
        {
            "id": "1640_sum_of_two_values", "title": "Sum of Two Values", "source": "CSES 1640",
            "statement": "You are given an array of $n$ integers, and your task is to find two values (at distinct positions) whose sum is $x$.",
            "inputFormat": "The first input line has two integers $n$ and $x$: the array size and the target sum.\nThe second line has $n$ integers $a_1, a_2, \\dots, a_n$.",
            "outputFormat": "Print two integers: the positions of the values.",
            "constraints": "<ul><li>$1 \\le n \\le 2 \\cdot 10^5$</li><li>$1 \\le x, a_i \\le 10^9$</li></ul>",
            "exampleInput": "4 8\n2 7 5 1", "exampleOutput": "2 4"
        }
    ],
    "03_dynamic_programming": [
        {
            "id": "1158_book_shop", "title": "Book Shop", "source": "CSES 1158",
            "statement": "You are in a book shop which sells $n$ different books. You have decided that the total price of your purchases will be at most $x$. What is the maximum number of pages you can buy?",
            "inputFormat": "The first line contains two integers $n$ and $x$.\nThe next line contains $n$ integers $h_1, h_2, \\dots, h_n$.\nThe last line contains $n$ integers $s_1, s_2, \\dots, s_n$.",
            "outputFormat": "Print one integer: the maximum number of pages.",
            "constraints": "<ul><li>$1 \\le n \\le 1000$</li><li>$1 \\le x \\le 10^5$</li><li>$1 \\le h_i, s_i \\le 1000$</li></ul>",
            "exampleInput": "4 10\n4 8 5 3\n5 12 8 1", "exampleOutput": "13"
        },
        {
            "id": "1638_grid_paths", "title": "Grid Paths", "source": "CSES 1638",
            "statement": "Consider an $n \\times n$ grid whose squares may have traps. Your task is to calculate the number of paths from the upper-left square to the lower-right square.",
            "inputFormat": "The first input line has an integer $n$.\nAfter this, there are $n$ lines that describe the grid.",
            "outputFormat": "Print the number of paths modulo $10^9+7$.",
            "constraints": "<ul><li>$1 \\le n \\le 1000$</li></ul>",
            "exampleInput": "4\n....\n.*..\n...*\n....", "exampleOutput": "3"
        }
    ],
    "04_graph_algorithms": [
        {
            "id": "1671_shortest_routes_i", "title": "Shortest Routes I", "source": "CSES 1671",
            "statement": "There are $n$ cities and $m$ flight connections between them. Your task is to determine the length of the shortest route from Syrjälä to every city.",
            "inputFormat": "The first input line has two integers $n$ and $m$.\nAfter this, there are $m$ lines describing the flight connections.",
            "outputFormat": "Print $n$ integers: the shortest route lengths.",
            "constraints": "<ul><li>$1 \\le n \\le 10^5$</li><li>$1 \\le m \\le 2 \\cdot 10^5$</li><li>$1 \\le a,b \\le n$</li><li>$1 \\le c \\le 10^9$</li></ul>",
            "exampleInput": "3 4\n1 2 6\n1 3 2\n3 2 3\n1 3 4", "exampleOutput": "0 5 2"
        },
        {
            "id": "1675_road_reparation", "title": "Road Reparation", "source": "CSES 1675",
            "statement": "There are $n$ cities and $m$ roads between them. Your task is to repair some of the roads so that there will be a decent route between any two cities.",
            "inputFormat": "The first input line has two integers $n$ and $m$.\nThen, there are $m$ lines describing the roads.",
            "outputFormat": "Print one integer: the minimum total reparation cost.",
            "constraints": "<ul><li>$1 \\le n \\le 10^5$</li><li>$1 \\le m \\le 2 \\cdot 10^5$</li></ul>",
            "exampleInput": "5 6\n1 2 3\n2 3 5\n2 4 2\n3 4 8\n5 1 7\n5 4 4", "exampleOutput": "14"
        }
    ],
    "05_range_queries": [
        {
            "id": "1648_dynamic_range_sum_queries", "title": "Dynamic Range Sum Queries", "source": "CSES 1648",
            "statement": "Given an array of $n$ integers, your task is to process $q$ queries of the following types:\n1. update the value at position $k$ to $u$\n2. what is the sum of values in range $[a,b]$?",
            "inputFormat": "The first input line has two integers $n$ and $q$.\nThe second line has $n$ integers.\nFinally, $q$ lines describe the queries.",
            "outputFormat": "Print the result of each query of type 2.",
            "constraints": "<ul><li>$1 \\le n, q \\le 2 \\cdot 10^5$</li></ul>",
            "exampleInput": "8 4\n3 2 4 5 1 1 5 3\n2 1 4\n2 5 6\n1 3 1\n2 1 4", "exampleOutput": "14\n2\n11"
        },
        {
            "id": "1652_forest_queries", "title": "Forest Queries", "source": "CSES 1652",
            "statement": "You are given an $n \\times n$ grid representing the map of a forest. Your task is to process $q$ queries: how many trees are inside a given rectangle?",
            "inputFormat": "The first input line has two integers $n$ and $q$.\nThen, there are $n$ lines describing the forest.\nFinally, $q$ lines describing the queries.",
            "outputFormat": "Print the number of trees inside each rectangle.",
            "constraints": "<ul><li>$1 \\le n \\le 1000$</li><li>$1 \\le q \\le 2 \\cdot 10^5$</li></ul>",
            "exampleInput": "4 3\n.*..\n*.**\n**..\n****\n2 2 3 4\n3 1 3 1\n1 1 2 2", "exampleOutput": "3\n1\n2"
        }
    ],
    "06_tree_algorithms": [
        {
            "id": "1131_tree_diameter", "title": "Tree Diameter", "source": "CSES 1131",
            "statement": "You are given a tree consisting of $n$ nodes. The diameter of a tree is the maximum distance between two nodes. Determine the diameter of the tree.",
            "inputFormat": "The first input line contains an integer $n$.\nThen there are $n-1$ lines describing the edges.",
            "outputFormat": "Print one integer: the diameter of the tree.",
            "constraints": "<ul><li>$1 \\le n \\le 2 \\cdot 10^5$</li></ul>",
            "exampleInput": "5\n1 2\n1 3\n3 4\n3 5", "exampleOutput": "3"
        },
        {
            "id": "1688_company_queries_ii", "title": "Company Queries II", "source": "CSES 1688",
            "statement": "A company has $n$ employees. Process $q$ queries: who is the lowest common boss of employees $a$ and $b$?",
            "inputFormat": "The first input line has two integers $n$ and $q$.\nThe next line has $n-1$ integers.\nFinally, there are $q$ lines describing the queries.",
            "outputFormat": "Print the answer for each query.",
            "constraints": "<ul><li>$1 \\le n,q \\le 2 \\cdot 10^5$</li></ul>",
            "exampleInput": "5 3\n1 1 3 3\n4 5\n2 5\n1 4", "exampleOutput": "3\n1\n1"
        }
    ],
    "07_mathematics": [
        {
            "id": "1081_common_divisors", "title": "Common Divisors", "source": "CSES 1081",
            "statement": "Given an array of $n$ positive integers, your task is to find two integers such that their greatest common divisor is as large as possible.",
            "inputFormat": "The first input line has an integer $n$.\nThe second line has $n$ integers.",
            "outputFormat": "Print the maximum greatest common divisor.",
            "constraints": "<ul><li>$2 \\le n \\le 2 \\cdot 10^5$</li><li>$1 \\le x_i \\le 10^6$</li></ul>",
            "exampleInput": "5\n3 14 15 7 9", "exampleOutput": "7"
        },
        {
            "id": "1079_binomial_coefficients", "title": "Binomial Coefficients", "source": "CSES 1079",
            "statement": "Your task is to calculate $n$ binomial coefficients modulo $10^9+7$.",
            "inputFormat": "The first input line contains an integer $n$.\nAfter this, there are $n$ lines, each containing two integers $a$ and $b$.",
            "outputFormat": "Print each binomial coefficient modulo $10^9+7$.",
            "constraints": "<ul><li>$1 \\le n \\le 10^5$</li><li>$1 \\le b \\le a \\le 10^6$</li></ul>",
            "exampleInput": "3\n5 3\n8 1\n9 5", "exampleOutput": "10\n8\n126"
        }
    ],
    "08_string_algorithms": [
        {
            "id": "1732_finding_borders", "title": "Finding Borders", "source": "CSES 1732",
            "statement": "A border of a string is a prefix that is also a suffix of the string but not the whole string. Find all border lengths of a given string.",
            "inputFormat": "The only input line has a string of length $n$ consisting of characters a–z.",
            "outputFormat": "Print all border lengths of the string in increasing order.",
            "constraints": "<ul><li>$1 \\le n \\le 10^6$</li></ul>",
            "exampleInput": "alabaralabal", "exampleOutput": "2 7"
        },
        {
            "id": "1731_word_combinations", "title": "Word Combinations", "source": "CSES 1731",
            "statement": "You are given a string of length $n$ and a dictionary containing $k$ words. In how many ways can you create the string using the words?",
            "inputFormat": "The first line has a string of length $n$.\nThe second line has an integer $k$.\nThen there are $k$ lines describing the dictionary.",
            "outputFormat": "Print the number of ways modulo $10^9+7$.",
            "constraints": "<ul><li>$1 \\le n \\le 5000$</li><li>$1 \\le k \\le 10^5$</li></ul>",
            "exampleInput": "ababc\n4\nab\nabab\nc\ncb", "exampleOutput": "2"
        }
    ],
    "09_geometry": [
        {
            "id": "2191_polygon_area", "title": "Polygon Area", "source": "CSES 2191",
            "statement": "Your task is to calculate the area of a given polygon. The polygon consists of $n$ vertices $(x_1,y_1), (x_2,y_2), \\dots, (x_n,y_n)$.",
            "inputFormat": "The first line has an integer $n$.\nAfter this, there are $n$ lines that describe the vertices.",
            "outputFormat": "Print the area of the polygon multiplied by 2 (an integer).",
            "constraints": "<ul><li>$3 \\le n \\le 1000$</li></ul>",
            "exampleInput": "4\n1 1\n4 2\n3 5\n1 4", "exampleOutput": "16"
        },
        {
            "id": "2195_convex_hull", "title": "Convex Hull", "source": "CSES 2195",
            "statement": "Given a set of $n$ points, your task is to find the convex hull of the points.",
            "inputFormat": "The first input line has an integer $n$: the number of points.\nAfter this, there are $n$ lines that describe the points. Each line has two integers $x$ and $y$.",
            "outputFormat": "First print an integer $k$: the number of points in the convex hull.\nThen print $k$ lines that describe the points.",
            "constraints": "<ul><li>$3 \\le n \\le 2 \\cdot 10^5$</li></ul>",
            "exampleInput": "6\n2 1\n2 5\n3 3\n4 3\n4 4\n6 3", "exampleOutput": "4\n2 1\n6 3\n4 4\n2 5"
        }
    ],
    "10_advanced_techniques": [
        {
            "id": "1690_hamiltonian_flights", "title": "Hamiltonian Flights", "source": "CSES 1690",
            "statement": "There are $n$ cities and $m$ flight connections. You want to travel from city 1 to city $n$ so that you visit each city exactly once. How many possible routes are there?",
            "inputFormat": "The first line has two integers $n$ and $m$.\nThen there are $m$ lines describing the flights.",
            "outputFormat": "Print the number of routes modulo $10^9+7$.",
            "constraints": "<ul><li>$2 \\le n \\le 20$</li><li>$1 \\le m \\le 10^5$</li></ul>",
            "exampleInput": "4 6\n1 2\n1 3\n2 3\n3 2\n2 4\n3 4", "exampleOutput": "2"
        }
    ],
    "11_sliding_window_problems": [
        {
            "id": "1077_sliding_window_cost", "title": "Sliding Window Cost", "source": "CSES 1077",
            "statement": "You are given an array of $n$ integers. For each window of size $k$, you want to make all elements equal. What is the minimum total cost?",
            "inputFormat": "The first line contains two integers $n$ and $k$.\nThen there are $n$ integers $x_1, \\dots, x_n$.",
            "outputFormat": "Print $n-k+1$ values: the costs.",
            "constraints": "<ul><li>$1 \\le k \\le n \\le 2 \\cdot 10^5$</li></ul>",
            "exampleInput": "8 3\n2 4 3 5 8 1 2 1", "exampleOutput": "2 2 2 7 7 1"
        }
    ],
    "13_bitwise_operations": [
        {
            "id": "1617_bit_strings", "title": "Bit Strings", "source": "CSES 1617",
            "statement": "Your task is to calculate the number of bit strings of length $n$.",
            "inputFormat": "The only input line has an integer $n$.",
            "outputFormat": "Print the result modulo $10^9+7$.",
            "constraints": "<ul><li>$1 \\le n \\le 10^6$</li></ul>",
            "exampleInput": "3", "exampleOutput": "8"
        }
    ],
    "14_construction_problems": [
        {
            "id": "1715_creating_strings_ii", "title": "Creating Strings II", "source": "CSES 1715",
            "statement": "Given a string, your task is to calculate the number of different strings that can be created using its characters.",
            "inputFormat": "The only input line has a string of length $n$.",
            "outputFormat": "Print the number of different strings modulo $10^9+7$.",
            "constraints": "<ul><li>$1 \\le n \\le 10^6$</li></ul>",
            "exampleInput": "aabac", "exampleOutput": "20"
        }
    ],
    "15_advanced_graph_problems": [
        {
            "id": "1691_necessary_roads", "title": "Necessary Roads", "source": "CSES 1691",
            "statement": "There are $n$ cities and $m$ roads. A road is necessary if its removal would disconnect the network. Find all necessary roads (bridges).",
            "inputFormat": "The first line has two integers $n$ and $m$.\nThen there are $m$ lines describing the roads.",
            "outputFormat": "First print an integer $k$: the number of necessary roads. Then, print $k$ lines describing the roads.",
            "constraints": "<ul><li>$1 \\le n \\le 10^5$</li><li>$1 \\le m \\le 2 \\cdot 10^5$</li></ul>",
            "exampleInput": "5 5\n1 2\n1 4\n2 4\n3 5\n4 5", "exampleOutput": "1\n3 5"
        },
        {
            "id": "1693_mail_delivery", "title": "Mail Delivery", "source": "CSES 1693",
            "statement": "Your task is to deliver mail to the inhabitants of a city. You have to start and end your route at the post office, and go through every street exactly once.",
            "inputFormat": "The first input line has two integers $n$ and $m$.\nThen there are $m$ lines describing the streets.",
            "outputFormat": "Print all the nodes on the route in the order you will visit them. If there are no solutions, print `IMPOSSIBLE`.",
            "constraints": "<ul><li>$1 \\le n \\le 10^5$</li><li>$1 \\le m \\le 2 \\cdot 10^5$</li></ul>",
            "exampleInput": "6 8\n1 2\n1 3\n2 3\n2 4\n2 6\n3 5\n3 6\n4 5", "exampleOutput": "1 2 4 5 3 6 2 3 1"
        }
    ],
    "16_counting_problems": [
        {
            "id": "1716_distributing_apples", "title": "Distributing Apples", "source": "CSES 1716",
            "statement": "There are $n$ children and $m$ apples that will be distributed to them. In how many ways can you do this?",
            "inputFormat": "The only input line has two integers $n$ and $m$.",
            "outputFormat": "Print the number of ways modulo $10^9+7$.",
            "constraints": "<ul><li>$1 \\le n, m \\le 10^6$</li></ul>",
            "exampleInput": "3 2", "exampleOutput": "6"
        }
    ]
}

for folder in os.listdir(data_dir):
    cat_path = os.path.join(data_dir, folder, "category.json")
    if not os.path.exists(cat_path): continue
    
    with open(cat_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    # Revert the "Ví dụ áp dụng" text
    data["content"] = re.sub(r"<br><br><strong style='color: #86efac;'>Ví dụ áp dụng:.*", "", data["content"])
    
    # Add new problems if any defined for this folder
    if folder in new_problems:
        for new_prob in new_problems[folder]:
            # Write the problem JSON
            prob_file_name = new_prob["id"] + ".json"
            prob_path = os.path.join(data_dir, folder, prob_file_name)
            with open(prob_path, "w", encoding="utf-8") as f:
                json.dump(new_prob, f, ensure_ascii=False, indent=4)
            
            # Add to category problems array if not present
            if prob_file_name not in data["problems"]:
                data["problems"].append(prob_file_name)
                
    # Rewrite category.json
    with open(cat_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

print("Reverted content and added new problems successfully.")
