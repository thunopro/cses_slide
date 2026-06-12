import os
import json
import shutil

data_dir = "data"
if os.path.exists(data_dir):
    shutil.rmtree(data_dir)
os.makedirs(data_dir, exist_ok=True)

slideData = [
    {
        "folder": "01_introductory",
        "title": "Introductory Problems",
        "subtitle": "Các bài toán nhập môn",
        "content": "<ul><li>Kiến thức cơ bản về vòng lặp, mảng, và chuỗi.</li><li>Thuật toán quay lui (Backtracking).</li><li>Khởi động tư duy lập trình thi đấu.</li></ul>",
        "problems": [
            {
                "id": "1068_weird_algorithm",
                "title": "Weird Algorithm",
                "source": "CSES 1068",
                "statement": "Consider an algorithm that takes as input a positive integer $n$. If $n$ is even, the algorithm divides it by two, and if $n$ is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until $n$ is one.",
                "inputFormat": "The only input line contains an integer $n$.",
                "outputFormat": "Print a line that contains all values of $n$ during the algorithm.",
                "exampleInput": "3",
                "exampleOutput": "3 10 5 16 8 4 2 1"
            },
            {
                "id": "1083_missing_number",
                "title": "Missing Number",
                "source": "CSES 1083",
                "statement": "You are given all numbers between $1,2,\\ldots,n$ except one. Your task is to find the missing number.",
                "inputFormat": "The first input line contains an integer $n$.\nThe second line contains $n-1$ numbers. Each number is distinct and between $1$ and $n$ (inclusive).",
                "outputFormat": "Print the missing number.",
                "exampleInput": "5\n2 3 1 5",
                "exampleOutput": "4"
            }
        ]
    },
    {
        "folder": "02_sorting_and_searching",
        "title": "Sorting and Searching",
        "subtitle": "Sắp xếp và Tìm kiếm",
        "content": "<ul><li>Tìm kiếm nhị phân (Binary Search).</li><li>Kỹ thuật Two Pointers, Sweep Line.</li><li>Sử dụng thành thạo Set, Map và Custom Sorting.</li></ul>",
        "problems": [
            {
                "id": "1621_distinct_numbers",
                "title": "Distinct Numbers",
                "source": "CSES 1621",
                "statement": "You are given a list of $n$ integers, and your task is to calculate the number of distinct values in the list.",
                "inputFormat": "The first input line has an integer $n$: the number of values.\nThe second line has $n$ integers $x_1,x_2,\\ldots,x_n$.",
                "outputFormat": "Print one integers: the number of distinct values.",
                "exampleInput": "5\n2 3 2 2 3",
                "exampleOutput": "2"
            }
        ]
    },
    {
        "folder": "03_dynamic_programming",
        "title": "Dynamic Programming",
        "subtitle": "Quy hoạch động",
        "content": "<ul><li>Bài toán cái túi (Knapsack), Dãy con tăng dài nhất (LIS).</li><li>Quy hoạch động trên lưới và trên mảng 2D.</li><li>Tối ưu bài toán bằng mảng trạng thái.</li></ul>",
        "problems": [
            {
                "id": "1633_dice_combinations",
                "title": "Dice Combinations",
                "source": "CSES 1633",
                "statement": "Your task is to count the number of ways to construct sum $n$ by throwing a dice one or more times. Each throw produces an outcome between $1$ and $6$.",
                "inputFormat": "The only input line has an integer $n$.",
                "outputFormat": "Print the number of ways modulo $10^9+7$.",
                "exampleInput": "3",
                "exampleOutput": "4"
            }
        ]
    },
    {
        "folder": "04_graph_algorithms",
        "title": "Graph Algorithms",
        "subtitle": "Thuật toán Đồ thị",
        "content": "<ul><li>Duyệt đồ thị BFS, DFS và Flood Fill.</li><li>Đường đi ngắn nhất: Dijkstra, Bellman-Ford, Floyd-Warshall.</li><li>Cây khung nhỏ nhất (MST) và Topological Sort.</li></ul>",
        "problems": [
            {
                "id": "1193_labyrinth",
                "title": "Labyrinth",
                "source": "CSES 1193",
                "statement": "You are given a map of a labyrinth, and your task is to find a path from start to end. You can walk left, right, up and down.",
                "inputFormat": "The first input line has two integers $n$ and $m$: the height and width of the map.\nThen there are $n$ lines of $m$ characters describing the labyrinth. Each character is `.` (floor), `#` (wall), `A` (start), or `B` (end).",
                "outputFormat": "First print \"YES\", if there is a path, and \"NO\" otherwise.\nIf there is a path, print the length of the shortest such path and its description as a string consisting of characters `L` (left), `R` (right), `U` (up), and `D` (down).",
                "exampleInput": "5 8\n########\n#.A#...#\n#.##.#B#\n#......#\n########",
                "exampleOutput": "YES\n9\nLDDRRRRRU"
            }
        ]
    },
    {
        "folder": "05_range_queries",
        "title": "Range Queries",
        "subtitle": "Truy vấn trên đoạn",
        "content": "<ul><li>Mảng cộng dồn (Prefix Sum) và Difference Array.</li><li>Segment Tree và Lazy Propagation.</li><li>Fenwick Tree (Binary Indexed Tree).</li></ul>",
        "problems": [
            {
                "id": "1646_static_range_sum_queries",
                "title": "Static Range Sum Queries",
                "source": "CSES 1646",
                "statement": "Given an array of $n$ integers, your task is to process $q$ queries of the form: what is the sum of values in range $[a,b]$?",
                "inputFormat": "The first input line has two integers $n$ and $q$: the number of values and queries.\nThe second line has $n$ integers $x_1,x_2,\\dots,x_n$: the array values.\nFinally, there are $q$ lines describing the queries. Each line has two integers $a$ and $b$: what is the sum of values in range $[a,b]$?",
                "outputFormat": "Print the result of each query on a new line.",
                "exampleInput": "8 4\n3 2 4 5 1 1 5 3\n2 4\n5 6\n1 8\n3 3",
                "exampleOutput": "11\n2\n24\n4"
            }
        ]
    },
    {
        "folder": "06_tree_algorithms",
        "title": "Tree Algorithms",
        "subtitle": "Thuật toán trên Cây",
        "content": "<ul><li>Đường kính của cây và khoảng cách các nút.</li><li>Tổ tiên chung gần nhất (LCA - Lowest Common Ancestor).</li><li>Quy hoạch động trên cây (Tree DP).</li></ul>",
        "problems": [
            {
                "id": "1674_subordinates",
                "title": "Subordinates",
                "source": "CSES 1674",
                "statement": "Given the structure of a company, your task is to calculate for each employee the number of their subordinates.",
                "inputFormat": "The first input line has an integer $n$: the number of employees. The employees are numbered $1,2,\\dots,n$, and employee $1$ is the general director of the company.\nAfter this, there are $n-1$ integers: for each employee $2,3,\\dots,n$ their direct boss in the company.",
                "outputFormat": "Print $n$ integers: for each employee $1,2,\\dots,n$ the number of their subordinates.",
                "exampleInput": "5\n1 1 2 3",
                "exampleOutput": "4 1 1 0 0"
            }
        ]
    },
    {
        "folder": "07_mathematics",
        "title": "Mathematics",
        "subtitle": "Toán học và Số học",
        "content": "<ul><li>Số học Modular, Lũy thừa ma trận.</li><li>Lý thuyết số: Sàng nguyên tố, Ước chung.</li><li>Tổ hợp, hoán vị và Công thức bao hàm - loại trừ.</li></ul>",
        "problems": [
            {
                "id": "1095_exponentiation",
                "title": "Exponentiation",
                "source": "CSES 1095",
                "statement": "Your task is to efficiently calculate values $a^b$ modulo $10^9+7$.",
                "inputFormat": "The first input line contains an integer $n$: the number of calculations.\nAfter this, there are $n$ lines, each containing two integers $a$ and $b$.",
                "outputFormat": "Print each value $a^b$ modulo $10^9+7$.",
                "exampleInput": "3\n3 4\n2 8\n123 123",
                "exampleOutput": "81\n256\n921450052"
            }
        ]
    },
    {
        "folder": "08_string_algorithms",
        "title": "String Algorithms",
        "subtitle": "Thuật toán Chuỗi",
        "content": "<ul><li>Băm xâu (String Hashing - Polynomial Hash).</li><li>Thuật toán KMP, Z-Algorithm để so khớp chuỗi.</li><li>Trie và Suffix Array.</li></ul>",
        "problems": [
            {
                "id": "1753_string_matching",
                "title": "String Matching",
                "source": "CSES 1753",
                "statement": "Given a string and a pattern, your task is to count the number of positions where the pattern occurs in the string.",
                "inputFormat": "The first input line has a string of length $n$, and the second input line has a pattern of length $m$. Both of them consist of characters a–z.",
                "outputFormat": "Print one integer: the number of occurrences.",
                "exampleInput": "saippuakauppias\npp",
                "exampleOutput": "2"
            }
        ]
    },
    {
        "folder": "09_geometry",
        "title": "Geometry",
        "subtitle": "Hình học",
        "content": "<ul><li>Tính diện tích đa giác, kiểm tra điểm nằm trong đa giác.</li><li>Giao điểm của các đoạn thẳng.</li><li>Bao lồi (Convex Hull).</li></ul>",
        "problems": [
            {
                "id": "2189_point_location_test",
                "title": "Point Location Test",
                "source": "CSES 2189",
                "statement": "There is a line that goes through the points $p_1=(x_1,y_1)$ and $p_2=(x_2,y_2)$. There is also a point $p_3=(x_3,y_3)$.\nYour task is to determine whether $p_3$ is located on the left or right side of the line or if it touches the line when we are looking from $p_1$ to $p_2$.",
                "inputFormat": "The first input line has an integer $t$: the number of tests.\nAfter this, there are $t$ lines. Each line has six integers $x_1$, $y_1$, $x_2$, $y_2$, $x_3$ and $y_3$.",
                "outputFormat": "For each test, print \"LEFT\", \"RIGHT\" or \"TOUCH\".",
                "exampleInput": "3\n1 1 5 3 2 3\n1 1 5 3 4 1\n1 1 5 3 3 2",
                "exampleOutput": "LEFT\nRIGHT\nTOUCH"
            }
        ]
    },
    {
        "folder": "10_advanced_techniques",
        "title": "Advanced Techniques",
        "subtitle": "Các kỹ thuật nâng cao",
        "content": "<ul><li>Quy hoạch động Bitmask (DP on Subsets).</li><li>Meet-in-the-middle.</li><li>Chia căn (Mo's Algorithm) và Centroid Decomposition.</li></ul>",
        "problems": [
            {
                "id": "1628_meet_in_the_middle",
                "title": "Meet in the Middle",
                "source": "CSES 1628",
                "statement": "You are given an array of $n$ numbers. In how many ways can you choose a subset of the numbers with sum $x$?",
                "inputFormat": "The first input line has two numbers $n$ and $x$: the array size and the required sum.\nThe second line has $n$ integers $t_1, t_2, \\dots, t_n$: the numbers in the array.",
                "outputFormat": "Print the number of ways you can create the sum $x$.",
                "exampleInput": "4 5\n1 2 3 2",
                "exampleOutput": "3"
            }
        ]
    },
    {
        "folder": "11_sliding_window_problems",
        "title": "Sliding Window Problems",
        "subtitle": "Cửa sổ trượt",
        "content": "<ul><li>Xử lý bài toán trên các đoạn con liên tiếp.</li><li>Sử dụng Monotonic Queue và Deque.</li></ul>",
        "problems": [
            {
                "id": "1076_sliding_window_median",
                "title": "Sliding Window Median",
                "source": "CSES 1076",
                "statement": "You are given an array of $n$ integers. Your task is to calculate the median of each window of $k$ elements, from left to right.",
                "inputFormat": "The first input line contains two integers $n$ and $k$: the number of elements and the size of the window.\nThen there are $n$ integers $x_1, x_2, \\dots, x_n$: the contents of the array.",
                "outputFormat": "Print $n - k + 1$ values: the medians.",
                "exampleInput": "8 3\n2 4 3 5 8 1 2 1",
                "exampleOutput": "3 4 5 5 2 1"
            }
        ]
    },
    {
        "folder": "12_interactive_problems",
        "title": "Interactive Problems",
        "subtitle": "Bài toán tương tác",
        "content": "<ul><li>Tương tác trực tiếp với chương trình chấm (Grader).</li><li>Tối ưu hóa số lượng truy vấn.</li></ul>",
        "problems": [
            {
                "id": "guess_the_number",
                "title": "Guess the Number",
                "source": "Interactive Example",
                "statement": "In this problem, there is a hidden integer $x$ such that $1 \\le x \\le 10^6$. You can make up to $50$ queries.\nIn each query, you can ask if $x \\ge y$. The grader will answer \"YES\" or \"NO\".",
                "inputFormat": "This is an interactive problem. You do not read the size of the input.",
                "outputFormat": "To guess the number, print \"! x\" and terminate your program.",
                "exampleInput": "YES\nNO\nYES",
                "exampleOutput": "? 500000\n? 750000\n? 625000"
            }
        ]
    },
    {
        "folder": "13_bitwise_operations",
        "title": "Bitwise Operations",
        "subtitle": "Thao tác Bit",
        "content": "<ul><li>Sử dụng AND, OR, XOR để tối ưu thuật toán.</li><li>Giải các bài toán trạng thái bằng bit.</li></ul>",
        "problems": [
            {
                "id": "1623_apple_division",
                "title": "Apple Division",
                "source": "CSES 1623",
                "statement": "There are $n$ apples with known weights. Your task is to divide the apples into two groups so that the difference between the weights of the groups is minimal.",
                "inputFormat": "The first input line has an integer $n$: the number of apples.\nThe next line has $n$ integers $p_1, p_2, \\dots, p_n$: the weight of each apple.",
                "outputFormat": "Print one integer: the minimum difference between the weights of the groups.",
                "exampleInput": "5\n3 2 7 4 1",
                "exampleOutput": "1"
            }
        ]
    },
    {
        "folder": "14_construction_problems",
        "title": "Construction Problems",
        "subtitle": "Bài toán cấu tạo",
        "content": "<ul><li>Xây dựng kết quả thỏa mãn một số điều kiện nhất định.</li><li>Yêu cầu khả năng quan sát và phân tích logic tốt.</li></ul>",
        "problems": [
            {
                "id": "1755_palindrome_reorder",
                "title": "Palindrome Reorder",
                "source": "CSES 1755",
                "statement": "Given a string, your task is to reorder its characters so that it becomes a palindrome (i.e., it reads the same forwards and backwards).",
                "inputFormat": "The only input line has a string of length $n$ consisting of characters A–Z.",
                "outputFormat": "Print a palindrome consisting of the characters of the original string. You may print any valid solution. If there are no solutions, print \"NO SOLUTION\".",
                "exampleInput": "AAAACACBA",
                "exampleOutput": "AACABACAA"
            }
        ]
    },
    {
        "folder": "15_advanced_graph_problems",
        "title": "Advanced Graph Problems",
        "subtitle": "Đồ thị nâng cao",
        "content": "<ul><li>Luồng cực đại (Max Flow) và Lát cắt cực tiểu (Min Cut).</li><li>Khớp và cầu trong đồ thị (Bridges & Articulation points).</li><li>Chu trình Euler và Hamilton.</li></ul>",
        "problems": [
            {
                "id": "1694_download_speed",
                "title": "Download Speed",
                "source": "CSES 1694",
                "statement": "Consider a network of $n$ computers and $m$ connections. Each connection specifies how fast a computer can send data to another computer.\nWhat is the maximum speed you can send data from computer $1$ to computer $n$?",
                "inputFormat": "The first input line has two integers $n$ and $m$: the number of computers and connections.\nAfter this, there are $m$ lines that describe the connections. Each line has three integers $a$, $b$ and $c$: computer $a$ can send data to computer $b$ at speed $c$.",
                "outputFormat": "Print one integer: the maximum download speed.",
                "exampleInput": "4 5\n1 2 3\n2 4 2\n1 3 4\n3 4 5\n4 1 3",
                "exampleOutput": "6"
            }
        ]
    },
    {
        "folder": "16_counting_problems",
        "title": "Counting Problems",
        "subtitle": "Bài toán đếm",
        "content": "<ul><li>Đếm số lượng cấu hình, số lượng cách sắp xếp.</li><li>Sử dụng Toán tổ hợp và Quy hoạch động.</li></ul>",
        "problems": [
            {
                "id": "1713_counting_divisors",
                "title": "Counting Divisors",
                "source": "CSES 1713",
                "statement": "Given $n$ integers, your task is to report for each integer the number of its divisors.\nFor example, if $x=18$, the correct answer is $6$ because its divisors are $1,2,3,6,9,18$.",
                "inputFormat": "The first input line has an integer $n$: the number of integers.\nAfter this, there are $n$ lines, each containing an integer $x$.",
                "outputFormat": "For each integer, print the number of its divisors.",
                "exampleInput": "3\n16\n17\n18",
                "exampleOutput": "5\n2\n6"
            }
        ]
    }
]

categories_index = []

for item in slideData:
    folder_name = item["folder"]
    folder_path = os.path.join(data_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    problem_ids = []
    
    for prob in item.get("problems", []):
        prob_id = prob["id"]
        prob_file = os.path.join(folder_path, f"{prob_id}.json")
        with open(prob_file, "w", encoding="utf-8") as f:
            json.dump(prob, f, ensure_ascii=False, indent=4)
        problem_ids.append(f"{prob_id}.json")
    
    cat_data = {
        "title": item["title"],
        "subtitle": item.get("subtitle", ""),
        "content": item["content"],
        "problems": problem_ids
    }
    with open(os.path.join(folder_path, "category.json"), "w", encoding="utf-8") as f:
        json.dump(cat_data, f, ensure_ascii=False, indent=4)
        
    categories_index.append(folder_name)

with open(os.path.join(data_dir, "index.json"), "w", encoding="utf-8") as f:
    json.dump(categories_index, f, ensure_ascii=False, indent=4)

print("Data extraction complete!")
