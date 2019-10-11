pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
    // 24ms
    let mut ans: Vec<Vec<i32>> = vec![];
    let mut nums = nums;
    let N = nums.len();
    nums.sort_unstable();
    for (k, &x) in nums.iter().enumerate() {
        if x > 0 {
            break;
        } else if k > 0 && x == nums[k-1] {
            continue;
        }
        let (mut i, mut j) = (k + 1, N - 1);
        while i < j {
            let (a, b) = (nums[i], nums[j]);
            let sum = a + b;
            if sum > -x {
                while i < j && nums[j] == b {
                    j -= 1;
                }
            } else if sum < -x {
                while i < j && nums[i] == a {
                    i += 1;
                }
            } else {
                ans.push(vec![x, a, b]);
                while i < j && nums[j] == b {
                    j -= 1;
                }
            }
        }
    }
    ans
}

pub fn three_sum1(nums: Vec<i32>) -> Vec<Vec<i32>> {
    // 152ms
    let mut counter = std::collections::HashMap::new();
    for &x in &nums {
        *counter.entry(x).or_insert(0) += 1;
    }
    println!("{:?}", counter);
    let mut keys: Vec<i32> = counter.keys().cloned().collect();
    keys.sort_unstable();
    let mut ans: Vec<Vec<i32>> = vec![];
    for i in 0..keys.len() {
        for j in i..keys.len() {
            let (a, b) = (keys[i], keys[j]);
            let c = -(a + b);
            if ! counter.contains_key(&c) {
                continue;
            }
            if a == b && b == c && counter[&a] >= 3 {
                ans.push(vec![a, b, c]);
            } else if a == b && b != c && counter[&a] >= 2 {
                ans.push(vec![a, b, c]);
            } else if a < b && b < c {
                ans.push(vec![a, b, c]);
            }
        }
    }
    ans
}


#[test]
fn test_15() {
    assert_eq!(Vec::<Vec<i32>>::new(), three_sum(vec![1, 2, -2, -1]));
    assert_eq!(
        vec![vec![-1, -1, 2], vec![-1, 0, 1]],
        three_sum(vec![-1, 0, 1, 2, -1, -4])
    );
    assert_eq!(vec![vec![0, 0, 0]], three_sum(vec![0, 0, 0, 0, 0, 0]));
    assert_eq!(
        vec![vec![-1, 0, 1], vec![0, 0, 0]],
        three_sum(vec![-1, -1, 0, 0, 0, 0, 0, 0, 1, 1])
    );
}
