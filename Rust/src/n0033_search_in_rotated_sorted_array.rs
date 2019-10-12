#[allow(clippy::collapsible_if)]
pub fn search(nums: Vec<i32>, target: i32) -> i32 {
    let (mut i, mut j) = (0, nums.len() as i32 - 1);
    while i <= j {
        let mid = i + (j - i) / 2;
        let m = nums[mid as usize];
        let head = nums[i as usize];
        let tail = nums[j as usize];
        if m == target {
            return mid;
        }
        // mid in sorted interval
        if head <= m {
            if head <= target && target < m {
                j = mid - 1;
            } else {
                i = mid + 1;
            }
        } else {
            if m < target && target <= tail {
                i = mid + 1;
            } else {
                j = mid - 1;
            }
        }
    }
    -1
}

#[test]
fn test_33() {
    assert_eq!(4, search(vec![4, 5, 6, 7, 0, 1, 2], 0));
    assert_eq!(-1, search(vec![4, 5, 6, 7, 0, 1, 2], 3));
    assert_eq!(0, search(vec![4, 5, 6, 7, 0, 1, 2], 4));
    assert_eq!(6, search(vec![4, 5, 6, 7, 0, 1, 2], 2));
    assert_eq!(4, search(vec![4, 5, 6, 7, 8, 1, 2, 3], 8));
}
