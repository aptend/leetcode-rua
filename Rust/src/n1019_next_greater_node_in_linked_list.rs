#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

pub fn next_larger_nodes(head: Option<Box<ListNode>>) -> Vec<i32> {
    let mut nodes = vec![];
    let mut head = head;
    while let Some(node) = head {
        nodes.push(node.val);
        head = node.next;
    }

    let mut stack = vec![];
    let mut ans = vec![0; nodes.len()];
    for (i, &x) in nodes.iter().enumerate() {
        while !stack.is_empty() && nodes[*stack.last().unwrap()] < x {
            let idx = stack.pop().unwrap();
            ans[idx] = x;
        }
        stack.push(i);
    }
    ans
}
