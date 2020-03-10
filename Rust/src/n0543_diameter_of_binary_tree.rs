#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

struct Solution;

use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    fn walk(node: Option<Rc<RefCell<TreeNode>>>, out: &mut i32) -> i32 {
        match node {
            None => 0,
            Some(node) => {
                let left_cnt = Solution::walk(node.borrow().left.clone(), out);
                let right_cnt = Solution::walk(node.borrow().right.clone(), out);
                *out = std::cmp::max(*out, left_cnt + right_cnt);
                std::cmp::max(left_cnt, right_cnt) + 1
            }
        }
    }
    pub fn diameter_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut ans = 0i32;
        Solution::walk(root, &mut ans);
        ans
    }
}
