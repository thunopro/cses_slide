import os
import json

constraints_map = {
    "1068_weird_algorithm": "<ul>\n<li>$1 \\le n \\le 10^6$</li>\n</ul>",
    "1083_missing_number": "<ul>\n<li>$2 \\le n \\le 2 \\cdot 10^5$</li>\n</ul>",
    "1621_distinct_numbers": "<ul>\n<li>$1 \\le n \\le 2 \\cdot 10^5$</li>\n<li>$1 \\le x_i \\le 10^9$</li>\n</ul>",
    "1633_dice_combinations": "<ul>\n<li>$1 \\le n \\le 10^6$</li>\n</ul>",
    "1193_labyrinth": "<ul>\n<li>$1 \\le n,m \\le 1000$</li>\n</ul>",
    "1646_static_range_sum_queries": "<ul>\n<li>$1 \\le n, q \\le 2 \\cdot 10^5$</li>\n<li>$1 \\le x_i \\le 10^9$</li>\n<li>$1 \\le a \\le b \\le n$</li>\n</ul>",
    "1674_subordinates": "<ul>\n<li>$1 \\le n \\le 2 \\cdot 10^5$</li>\n</ul>",
    "1095_exponentiation": "<ul>\n<li>$1 \\le n \\le 2 \\cdot 10^5$</li>\n<li>$0 \\le a,b \\le 10^9$</li>\n</ul>",
    "1753_string_matching": "<ul>\n<li>$1 \\le n, m \\le 10^6$ (lengths of the strings)</li>\n</ul>",
    "2189_point_location_test": "<ul>\n<li>$1 \\le t \\le 10^5$</li>\n<li>$-10^9 \\le x_i, y_i \\le 10^9$</li>\n</ul>",
    "1628_meet_in_the_middle": "<ul>\n<li>$1 \\le n \\le 40$</li>\n<li>$1 \\le x \\le 10^9$</li>\n<li>$1 \\le t_i \\le 10^9$</li>\n</ul>",
    "1076_sliding_window_median": "<ul>\n<li>$1 \\le k \\le n \\le 2 \\cdot 10^5$</li>\n<li>$1 \\le x_i \\le 10^9$</li>\n</ul>",
    "guess_the_number": "<ul>\n<li>$1 \\le x \\le 10^6$</li>\n</ul>",
    "1623_apple_division": "<ul>\n<li>$1 \\le n \\le 20$</li>\n<li>$1 \\le p_i \\le 10^9$</li>\n</ul>",
    "1755_palindrome_reorder": "<ul>\n<li>$1 \\le n \\le 10^6$</li>\n</ul>",
    "1694_download_speed": "<ul>\n<li>$1 \\le n \\le 500$</li>\n<li>$1 \\le m \\le 1000$</li>\n<li>$1 \\le a,b \\le n$</li>\n<li>$1 \\le c \\le 10^9$</li>\n</ul>",
    "1713_counting_divisors": "<ul>\n<li>$1 \\le n \\le 10^5$</li>\n<li>$1 \\le x \\le 10^6$</li>\n</ul>"
}

data_dir = "data"

for root, dirs, files in os.walk(data_dir):
    for f in files:
        if f.endswith(".json") and f != "category.json" and f != "index.json":
            file_path = os.path.join(root, f)
            problem_id = f.replace(".json", "")
            
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            
            if problem_id in constraints_map:
                data["constraints"] = constraints_map[problem_id]
                
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

print("Constraints added to JSON files.")
