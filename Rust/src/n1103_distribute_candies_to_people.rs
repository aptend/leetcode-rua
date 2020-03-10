pub fn distribute_candies(candies: i32, n: i32) -> Vec<i32> {
    let acc = |start: i32, end: i32, n: i32| -> i32 { (start + end) * n / 2 };
    let base = acc(1, n, n);
    let diff = n * n;
    let mut round = 0; // how many rounds were done ?
    while acc(base, base + round * diff, round + 1) < candies {
        round += 1;
    }
    let mut ans = if round == 0 {
        // do this branch because step_by denied step = 0
        vec![0; n as usize]
    } else {
        (acc(1, 1 + n * (round - 1), round)..)
            .step_by(round as usize)
            .take(n as usize)
            .collect()
    };
    let mut left = candies - acc(base, base + (round - 1) * diff, round);
    let mut need = round * n + 1;
    for x in ans.iter_mut() {
        if left >= need {
            *x += need;
            left -= need;
            need += 1;
        } else {
            *x += left;
            break;
        }
    }
    ans
}

#[test]
fn test_1103() {
    assert_eq!(vec![1, 2, 3, 1], distribute_candies(7, 4));
    assert_eq!(vec![5, 2, 3], distribute_candies(10, 3));
}
