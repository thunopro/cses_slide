import os
import json

updates = {
    "01_introductory": "<br><br><strong style='color: #86efac;'>Ví dụ áp dụng:</strong> Bài <em>Weird Algorithm</em> sử dụng vòng lặp cơ bản; bài <em>Missing Number</em> dùng mảng và toán học.",
    "02_sorting_and_searching": "<br><br><strong style='color: #86efac;'>Ví dụ áp dụng:</strong> Bài <em>Distinct Numbers</em> yêu cầu thao tác Sắp xếp (Sorting) hoặc dùng Set.",
    "03_dynamic_programming": "<br><br><strong style='color: #86efac;'>Ví dụ áp dụng:</strong> Bài <em>Dice Combinations</em> yêu cầu thiết lập mảng trạng thái $dp[i]$ để đếm số lượng tổ hợp.",
    "04_graph_algorithms": "<br><br><strong style='color: #86efac;'>Ví dụ áp dụng:</strong> Bài <em>Labyrinth</em> sử dụng thuật toán duyệt đồ thị theo chiều rộng (BFS) để tìm đường ngắn nhất.",
    "05_range_queries": "<br><br><strong style='color: #86efac;'>Ví dụ áp dụng:</strong> Bài <em>Static Range Sum Queries</em> ứng dụng mảng cộng dồn (Prefix Sum) để truy vấn trong $O(1)$.",
    "06_tree_algorithms": "<br><br><strong style='color: #86efac;'>Ví dụ áp dụng:</strong> Bài <em>Subordinates</em> giải bằng Duyệt sâu (DFS) kết hợp Quy hoạch động trên cây (Tree DP).",
    "07_mathematics": "<br><br><strong style='color: #86efac;'>Ví dụ áp dụng:</strong> Bài <em>Exponentiation</em> yêu cầu cài đặt thuật toán Lũy thừa nhị phân modulo.",
    "08_string_algorithms": "<br><br><strong style='color: #86efac;'>Ví dụ áp dụng:</strong> Bài <em>String Matching</em> ứng dụng KMP hoặc String Hashing để so khớp chuỗi nhanh.",
    "09_geometry": "<br><br><strong style='color: #86efac;'>Ví dụ áp dụng:</strong> Bài <em>Point Location Test</em> sử dụng Tích có hướng (Cross Product) của 2 vector.",
    "10_advanced_techniques": "<br><br><strong style='color: #86efac;'>Ví dụ áp dụng:</strong> Bài <em>Meet in the Middle</em> dùng kỹ thuật chia đôi tập hợp để tối ưu $O(2^n)$ xuống $O(2^{n/2})$.",
    "11_sliding_window_problems": "<br><br><strong style='color: #86efac;'>Ví dụ áp dụng:</strong> Bài <em>Sliding Window Median</em> duy trì 2 multiset để quản lý phần tử trong cửa sổ.",
    "12_interactive_problems": "<br><br><strong style='color: #86efac;'>Ví dụ áp dụng:</strong> Bài <em>Guess the Number</em> kết hợp Tìm kiếm nhị phân để đưa ra truy vấn (query) tối ưu.",
    "13_bitwise_operations": "<br><br><strong style='color: #86efac;'>Ví dụ áp dụng:</strong> Bài <em>Apple Division</em> duyệt phân cực bằng bitmask (duyệt $2^n$ trạng thái).",
    "14_construction_problems": "<br><br><strong style='color: #86efac;'>Ví dụ áp dụng:</strong> Bài <em>Palindrome Reorder</em> yêu cầu đếm tần số và xây dựng logic chuỗi đối xứng.",
    "15_advanced_graph_problems": "<br><br><strong style='color: #86efac;'>Ví dụ áp dụng:</strong> Bài <em>Download Speed</em> áp dụng thuật toán Luồng cực đại (Max Flow - Dinic / Edmonds-Karp).",
    "16_counting_problems": "<br><br><strong style='color: #86efac;'>Ví dụ áp dụng:</strong> Bài <em>Counting Divisors</em> dùng phân tích thừa số nguyên tố để đếm số ước nhanh."
}

data_dir = "data"

for folder, append_text in updates.items():
    cat_path = os.path.join(data_dir, folder, "category.json")
    if os.path.exists(cat_path):
        with open(cat_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        # Only append if we haven't already appended
        if "Ví dụ áp dụng:" not in data["content"]:
            data["content"] = data["content"] + append_text
            
            with open(cat_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

print("Updated content successfully.")
