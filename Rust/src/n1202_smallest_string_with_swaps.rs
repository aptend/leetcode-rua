pub fn smallest_string_with_swaps(s: String, pairs: Vec<Vec<i32>>) -> String {
    let N = s.len();
    let mut adj: Vec<Vec<usize>> = vec![vec![]; N];
    for p in pairs.iter() {
        adj[p[0] as usize].push(p[1] as usize);
        adj[p[1] as usize].push(p[0] as usize);
    }

    let mut state = vec![0; N];
    fn dfs(state: &mut Vec<i32>, cc: &mut Vec<usize>, adj: &[Vec<usize>], v: usize) {
        if state[v] == 1 {
            return;
        }
        state[v] = 1;
        cc.push(v);
        for &w in adj[v as usize].iter() {
            dfs(state, cc, adj, w);
        }
    }

    let mut groups: Vec<Vec<usize>> = vec![];
    for i in 0..N {
        if state[i] == 0 {
            let mut cc = vec![];
            dfs(&mut state, &mut cc, &adj, i);
            groups.push(cc);
        }
    }

    let mut ans = vec![0; N];
    let str = s.as_bytes();
    for g in groups.iter_mut() {
        g.sort();
        // TLE because of nth operation is linear-cost
        //let mut g_chars: Vec<char> = g.iter().map(|&i| s.chars().nth(i).unwrap()).collect();
        let mut g_chars: Vec<u8> = g.iter().map(|&i| str[i]).collect();
        g_chars.sort();
        for (&i, ch) in g.iter().zip(g_chars) {
            ans[i] = ch;
        }
    }
    String::from_utf8(ans).unwrap()
}

#[test]
fn test_1202() {
    assert_eq!(
        "bacd".to_owned(),
        smallest_string_with_swaps("dcab".to_owned(), vec![vec![1, 2], vec![0, 3]])
    )
}
