use std::collections::HashMap;
use std::cmp::min;

pub fn max_number_of_balloons(text: String) -> i32 {
    let mut counter: HashMap<char, i32> = HashMap::new();
    for ch in text.chars() {
        *counter.entry(ch).or_insert(0) += 1
    }
    let mut ans = text.len() as i32;
    for ch in "ban".chars(){
        ans = min(ans, *counter.get(&ch).unwrap_or(&0));
    }   
    for ch in "lo".chars(){
        ans = min(ans, *counter.get(&ch).unwrap_or(&0) / 2);
    }
    ans
}

#[test]
fn test_1189() {
    assert_eq!(1, max_number_of_balloons("nlaebolko".to_owned()));
    assert_eq!(2, max_number_of_balloons("loonbalxballpoon".to_owned()));
    assert_eq!(0, max_number_of_balloons("leetcode".to_owned()));
}
