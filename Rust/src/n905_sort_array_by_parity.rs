pub fn sort_array_by_parity(a: Vec<i32>) -> Vec<i32> {
    let mut a = a;
    let N = a.len();
    let (mut i, mut j) = (0, N-1);
    loop {
        while i < N && a[i] % 2 == 0 { i += 1; }
        while j > 0 && a[j] % 2 == 1 { j -= 1; }
        if i >= j { break; }
        a.swap(i, j);
        i += 1;
        j -= 1;
    }
    a
}


#[test]
fn test_905() {
    assert_eq!(sort_array_by_parity(vec![3, 1, 2, 4]), vec![4, 2, 1, 3])
}

