// Definition for a binary tree node.
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
use std::cell::RefCell;
use std::rc::Rc;
pub fn bst_to_gst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
    let mut acc = 0;
    fn walk(node: Option<Rc<RefCell<TreeNode>>>, acc: &mut i32) {
        if let Some(inner) = node {
            walk(inner.borrow().right.clone(), acc);
            inner.borrow_mut().val += *acc;
            *acc = inner.borrow().val;
            walk(inner.borrow().left.clone(), acc);
        }
    }
    walk(root.clone(), &mut acc);
    root
}
