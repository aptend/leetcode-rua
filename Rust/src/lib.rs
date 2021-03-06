#![allow(non_snake_case)]
#![allow(dead_code)]

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

mod bisect;

mod n0003_longest_substring_without_repeating_characters;
mod n0005_longest_palindromic_substring;
mod n0007_reverse_integer;
mod n0008_string_to_integer_atoi;
mod n0009_palindrome_number;
mod n0010_regular_expression_matching;
mod n0011_container_with_most_water;
mod n0014_longest_common_prefix;
mod n0015_3sum;
mod n0020_valid_parentheses;
mod n0021_merge_two_sorted_lists;
mod n0022_generate_parentheses;
mod n0026_remove_duplicates_from_sorted_array;
mod n0029_divide_two_integers;
mod n0033_search_in_rotated_sorted_array;
mod n0043_multiply_strings;
mod n0046_permutations;
mod n0049_group_anagrams;
mod n0054_spiral_matrix;
mod n0055_jump_game;
mod n0059_spiral_matrix_ii;
mod n0062_unique_paths;
mod n0069_sqrtx;
mod n0073_set_matrix_zeroes;
mod n0074_search_a_2d_matrix;
mod n0076_minimum_window_substring;
mod n0084_largest_rectangle_in_histogram;
mod n0088_merge_sorted_array;
mod n0089_gray_code;
mod n0090_subsets_ii;
mod n0091_decode_ways;
mod n0121_best_time_to_buy_and_sell_stock;
mod n0122_best_time_to_buy_and_sell_stock_ii;
mod n0131_palindrome_partitioning;
mod n0150_evaluate_reverse_polish_notation;
mod n0152_maximum_product_subarray;
mod n0155_min_stack;
mod n0171_excel_sheet_column_number;
mod n0198_house_robber;
mod n0204_count_primes;
mod n0213_house_robber_ii;
mod n0215_kth_largest_element_in_an_array;
mod n0217_contains_duplicate;
mod n0231_power_of_two;
mod n0238_product_of_array_except_self;
mod n0268_missing_number;
mod n0279_perfect_squares;
mod n0290_word_pattern;
mod n0300_longest_increasing_subsequence;
mod n0313_super_ugly_number;
mod n0322_coin_change;
mod n0334_increasing_triplet_subsequence;
mod n0343_integer_break;
mod n0344_reverse_string;
mod n0371_sum_of_two_integers;
mod n0384_shuffle_an_array;
mod n0387_first_unique_character_in_a_string;
mod n0395_longest_substring_with_at_least_k_repeating_characters;
mod n0400_nth_digit;
mod n0406_queue_reconstruction_by_height;
mod n0412_fizz_buzz;
mod n0438_find_all_anagrams_in_a_string;
mod n0442_find_all_duplicates_in_an_array;
mod n0491_increasing_subsequences;
mod n0494_target_sum;
mod n0518_coin_change_2;
mod n0543_diameter_of_binary_tree;
mod n0557_reverse_words_in_a_string_iii;
mod n0560_subarray_sum_equals_k;
mod n0581_shortest_unsorted_continuous_subarray;
mod n0583_delete_operation_for_two_strings;
mod n0611_valid_triangle_number;
mod n0621_task_scheduler;
mod n0646_maximum_length_of_pair_chain;
mod n0647_palindromic_substrings;
mod n0696_count_binary_substrings;
mod n0739_daily_temperatures;
mod n0740_delete_and_earn;
mod n0795_number_of_subarrays_with_bounded_maximum;
mod n0818_race_car;
mod n0820_short_encoding_of_words;
mod n0825_friends_of_appropriate_ages;
mod n0869_reordered_power_of_2;
mod n0870_advantage_shuffle;
mod n0904_fruit_into_baskets;
mod n0905_sort_array_by_parity;
mod n0918_maximum_sum_circular_subarray;
mod n0923_3sum_with_multiplicity;
mod n0945_minimum_increment_to_make_array_unique;
mod n0950_reveal_cards_in_increasing_order;
mod n0962_maximum_width_ramp;
mod n0967_numbers_with_same_consecutive_differences;
mod n0991_broken_calculator;
mod n0992_subarrays_with_k_different_integers;
mod n0997_find_the_town_judge;
mod n1001_grid_illumination;
mod n1005_maximize_sum_of_array_after_k_negations;
mod n1011_capacity_to_ship_packages_within_d_days;
mod n1013_partition_array_into_three_parts_with_equal_sum;
mod n1019_next_greater_node_in_linked_list;
mod n1027_longest_arithmetic_sequence;
mod n1038_binary_search_tree_to_greater_sum_tree;
mod n1039_minimum_score_triangulation_of_polygon;
mod n1043_partition_array_for_maximum_sum;
mod n1071_greatest_common_divisor_of_strings;
mod n1081_smallest_subsequence_of_distinct_characters;
mod n1103_distribute_candies_to_people;
mod n1155_number_of_dice_rolls_with_target_sum;
mod n1177_can_make_palindrome_from_substring;
mod n1189_maximum_number_of_ballons;
mod n1190_reverse_substrings_between_each_pair_of_parentheses;
mod n1191_k_concatenation_maximum_sum;
mod n1200_minimum_absolute_difference;
mod n1201_ugly_number_iii;
mod n1202_smallest_string_with_swaps;
mod n1213_intersection_of_three_sorted_arrays;
mod n1217_play_with_chips;
mod n1218_longest_arithmetic_subsequence_of_given_difference;
mod n1219_path_with_maximum_gold;
mod n1220_count_vowels_permutation;
