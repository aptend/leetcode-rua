use std::collections::HashMap;
pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
    //16ms
    let mut table = HashMap::new();
    for s in strs.into_iter() {
        let mut schars: Vec<_> = s.chars().collect();
        schars.sort_unstable();
        let key: String = schars.into_iter().collect();
        (*table.entry(key).or_insert_with(Vec::<String>::new)).push(s);
    }
    table.into_iter().map(|(_, v)| v).collect()
}

pub fn group_anagrams_counter(strs: Vec<String>) -> Vec<Vec<String>> {
    //12ms
    strs.into_iter()
        .fold(HashMap::new(), |mut map, s| {
            map.entry(s.bytes().fold([0; 26], |mut hash, b| {
                hash[(b - b'a') as usize] += 1u8;
                hash
            }))
            .or_insert_with(Vec::new)
            .push(s);
            map
        })
        .into_iter()
        .map(|s| s.1)
        .collect()
}

#[test]
fn test_49() {
    let a = group_anagrams_counter(vec![
        "eat".to_owned(),
        "tea".to_owned(),
        "tan".to_owned(),
        "ate".to_owned(),
        "nat".to_owned(),
        "bat".to_owned(),
    ]);
    assert_eq!(3, a.len());
}
