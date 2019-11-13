use rand::Rng;

struct Solution {
    origin: Vec<i32>,
    data: Vec<i32>,
}

impl Solution {
    fn new(nums: Vec<i32>) -> Self {
        Solution {
            origin: nums.clone(),
            data: nums,
        }
    }
    fn reset(&mut self) -> Vec<i32> {
        self.data = self.origin.clone();
        self.origin.clone()
    }
    fn shuffle(&mut self) -> Vec<i32> {
        let mut rng = rand::thread_rng();
        for i in 0..self.data.len() {
            let j = rng.gen_range(i, self.data.len());
            self.data.swap(i, j);
        }
        self.data.clone()
    }
}

#[test]
fn test_384() {
    let mut deck = Solution::new(vec![1, 2, 3, 4]);
    deck.shuffle();
    assert_eq!(vec![1, 2, 3, 4], deck.reset());
}
