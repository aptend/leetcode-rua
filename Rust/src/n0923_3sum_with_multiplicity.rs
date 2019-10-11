use std::collections::HashMap;
pub fn three_sum_multi1(a: Vec<i32>, target: i32) -> i32 {
    let mut counter: HashMap<i32, i64> = HashMap::new();
    for &x in &a {
        *counter.entry(x).or_insert(0) += 1;
    }
    let mut keys: Vec<i32> = counter.keys().cloned().collect();
    keys.sort_unstable();
    let mut ans = 0i64;
    for (k, x) in keys.iter().enumerate() {
        // use only one x
        let (mut i, mut j) = (0, k.saturating_sub(1));
        while i < j {
            let sum = keys[i] + keys[j];
            if sum > target - x {
                j -= 1;
            } else if sum < target - x {
                i += 1;
            } else {
                ans += counter[&keys[i]] * counter[&keys[j]] * counter[x];
                j -= 1;
                i += 1;
            }
        }
        // use three x
        if 3 * x == target {
            // if counter[k] < 3, rhs is zero, which does not increse ans
            ans += counter[x] * (counter[x] - 1) * (counter[x] - 2) / 6
        } else if counter.contains_key(&(target - 2 * x)) {
            // use two x
            ans += counter[&(target - 2 * x)] * counter[x] * (counter[x] - 1) / 2
        }
    }
    let MOD = 1e9 as i64 + 7;
    (ans % MOD) as i32
}

pub fn three_sum_multi(a: Vec<i32>, target: i32) -> i32 {
    let mut counter: HashMap<i32, i64> = HashMap::new();
    for &x in &a {
        *counter.entry(x).or_insert(0) += 1;
    }
    let mut keys: Vec<i32> = counter.keys().cloned().collect();
    keys.sort_unstable();
    let mut ans = 0i64;
    for i in 0..keys.len() {
        for j in i..keys.len() {
            let (a, b) = (keys[i], keys[j]);
            let c = target - a - b;
            if a == b && b == c {
                // xxx type
                ans += counter[&a] * (counter[&a] - 1) * (counter[&a] - 2) / 6;
            } else if a == b && b != c {
                // xxy type both x < y and x > y are ok
                ans += counter.get(&c).unwrap_or(&0) * counter[&a] * (counter[&a] - 1) / 2;
            } else if c > b {
                // c > b > a
                ans += counter[&a] * counter[&b] * counter.get(&c).unwrap_or(&0);
            }
        }
    }
    let MOD = 1e9 as i64 + 7;
    (ans % MOD) as i32
}

#[test]
fn test_923() {
    assert_eq!(20, three_sum_multi(vec![1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8));
    assert_eq!(12, three_sum_multi(vec![1, 1, 2, 2, 2, 2], 5));
    assert_eq!(1, three_sum_multi(vec![0, 0, 0], 0));
    assert_eq!(6, three_sum_multi(vec![2, 3, 3, 1, 0, 0, 1], 5));
    assert_eq!(
        10,
        three_sum_multi(
            vec![
                52, 53, 86, 11, 35, 1, 41, 34, 52, 64, 90, 54, 84, 99, 67, 8, 80, 100, 51, 66, 37,
                31, 13, 13, 22, 31, 81, 96, 81, 96
            ],
            79
        )
    );
}
