use crate::ListNode;

pub fn merge_two_lists(
    mut l1: Option<Box<ListNode>>,
    mut l2: Option<Box<ListNode>>,
) -> Option<Box<ListNode>> {
    let mut dummy = Box::new(ListNode::new(0));
    let mut tail = &mut dummy;
    while l1.is_some() && l2.is_some() {
        let (v1, v2) = (l1.as_ref().unwrap().val, l2.as_ref().unwrap().val);
        if v1 >= v2 {
            let mut n2 = l2.unwrap();
            l2 = n2.next.take();
            tail.next = Some(n2);
            tail = tail.next.as_mut().unwrap();
        } else {
            let mut n1 = l1.unwrap();
            l1 = n1.next.take();
            tail.next = Some(n1);
            tail = tail.next.as_mut().unwrap();
        }
    }
    tail.next = if l1.is_some() { l1 } else { l2 };
    dummy.next
}
