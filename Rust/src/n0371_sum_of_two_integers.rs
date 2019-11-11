pub fn get_sum_fake(a: i32, b: i32) -> i32 {
    let HIGH = 0x80_00_00_00u32;
    let mut ans = 0u32;
    let (mut a, mut b) = (a, b);
    let mut carry = 0;
    for _ in 0..32 {
        ans >>= 1;
        let ai = a & 0x1;
        let bi = b & 0x1;
        a >>= 1;
        b >>= 1;
        let s = ai + bi + carry;
        if s % 2 == 1 {
            ans |= HIGH;
        }
        carry = s / 2;
    }
    ans as i32
}

pub fn get_sum(a: i32, b: i32) -> i32 {
    let mut ans = a ^ b;
    let mut carry = (a & b) << 1;
    while carry != 0 {
        let nxt_carry = (ans & carry) << 1;
        ans ^= carry;
        carry = nxt_carry;
    }
    ans
}

#[test]
fn test_371() {
    assert_eq!(-1, get_sum(-2, 1));
    assert_eq!(1, get_sum(2, -1));
    assert_eq!(17, get_sum(9, 8));
    assert_eq!(-2147483644, get_sum(2147483645, 7));
}
