pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
    let mut i = m as usize;
    let mut j = n as usize;
    for k in (0..(m + n) as usize).rev() {
        if j == 0 {
            break;
        } else if i == 0 || nums1[i - 1] < nums2[j - 1] {
            nums1[k] = nums2[j - 1];
            j -= 1;
        } else {
            nums1[k] = nums1[i - 1];
            i -= 1;
        }
    }
}

#[test]
fn test_88() {
    let mut nums1 = vec![1, 2, 3, 0, 0, 0];
    let mut nums2 = vec![2, 5, 6];
    merge(&mut nums1, 3, &mut nums2, 3);
    assert_eq!(vec![1, 2, 2, 3, 5, 6], nums1);
}
