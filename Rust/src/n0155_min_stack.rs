struct MinStack {
    s1: Vec<i32>,
    s2: Vec<i32>,
}

impl MinStack {
    fn new() -> Self {
        MinStack {
            s1: vec![],
            s2: vec![],
        }
    }

    fn push(&mut self, x: i32) {
        self.s1.push(x);
        if self.s2.is_empty() || self.get_min() >= x {
            self.s2.push(x);
        }
    }

    fn pop(&mut self) {
        let n = self.s1.pop().unwrap();
        if n == self.get_min() {
            self.s2.pop().unwrap();
        }
    }

    fn top(&self) -> i32 {
        *self.s1.last().unwrap()
    }

    fn get_min(&self) -> i32 {
        *self.s2.last().unwrap()
    }
}

#[test]
fn test_155() {
    let mut min_stack = MinStack::new();
    min_stack.push(0);
    min_stack.push(1);
    min_stack.push(0);
    assert_eq!(0, min_stack.get_min());
    min_stack.pop();
    assert_eq!(1, min_stack.top());
    assert_eq!(0, min_stack.get_min());
}
