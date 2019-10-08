pub fn count_primes(n: i32) -> i32 {
    let N = n as usize;
    let sqrtn = (N as f32).sqrt() as usize;
    let mut prime_map = vec![true; N];
    for i in 2..=sqrtn {
        if !prime_map[i] {
            continue;
        }
        for j in (i * i..N).step_by(i) {
            prime_map[j] = false;
        }
    }
    let ans = prime_map.iter().skip(2).filter(|&p| *p).count();
    ans as i32
}

#[test]
fn test_nxx() {
    assert_eq!(0, count_primes(0));
    assert_eq!(0, count_primes(2));
    assert_eq!(4, count_primes(10));
    assert_eq!(2, count_primes(4));
    assert_eq!(1, count_primes(3));
}
