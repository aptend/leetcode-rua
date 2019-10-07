#![allow(non_snake_case)]

use reqwest;
use serde::Deserialize;
use serde_json::json;
use std::collections::HashMap;
use std::env;
use std::fs;
use std::io::Write;
use std::path::Path;

const GRAPHQL_URL: &str = "https://leetcode-cn.com/graphql";
const QUESTION_QUERY_STRING: &str = r#"
query questionData($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        codeSnippets {
            langSlug
            code
        }
        sampleTestCase
    }
}"#;
const QUESTION_QUERY_OPERATION: &str = "questionData";

const ENTRY_JSON_PATH: &str = r#"C:\Users\cresc\AppData\Local\Temp\leeyzer_problems.json"#;

const TEST_TMPL: &str = r#"

#[test]
fn test_{id}() {
    assert_eq!(42, {func_name}());
}
"#;

#[derive(Debug, Deserialize)]
struct ProblemEntry {
    #[serde(rename = "question__title_slug")]
    question_title_slug: String,
    #[serde(rename = "question__title")]
    question_title: String,
    difficulty: String,
}

#[derive(Deserialize)]
struct RawProblem {
    pub data: Data,
}

#[derive(Deserialize)]
struct Data {
    pub question: Problem,
}

#[derive(Debug, Deserialize)]
struct Problem {
    #[serde(rename = "codeSnippets")]
    pub code_snippets: Vec<CodeSnippet>,
    #[serde(rename = "sampleTestCase")]
    pub sample_test_case: String,
}

#[derive(Debug, Deserialize)]
pub struct CodeSnippet {
    #[serde(rename = "langSlug")]
    pub lang: String,
    pub code: String,
}

fn main() {
    let id_arg = env::args().nth(1).expect("a problem id is needed");
    let id: i32 = id_arg
        .parse()
        .unwrap_or_else(|_| panic!("{} is not a number", &id_arg));

    let repo_json = fs::read_to_string(ENTRY_JSON_PATH).unwrap();
    let entry_repo: HashMap<i32, ProblemEntry> = serde_json::from_str(&repo_json).unwrap();

    let entry = &entry_repo[&id];
    let file_name = format!("n{:04}_{}", id, entry.question_title_slug.replace("-", "_"));
    let file_path = Path::new("./src").join(format!("{}.rs", file_name));

    let query = json!({
        "operationName": QUESTION_QUERY_OPERATION.to_owned(),
        "variables": json!({"titleSlug": entry.question_title_slug}),
        "query": QUESTION_QUERY_STRING.to_owned(),
    });
    let client = reqwest::Client::new();
    let resp: RawProblem = client
        .post(GRAPHQL_URL)
        .json(&query)
        .send()
        .unwrap()
        .json()
        .unwrap();

    let problem = resp.data.question;
    let snippet = problem
        .code_snippets
        .iter()
        .find(|p| p.lang == "rust")
        .expect("this problem does't support Rust solution yet");

    let code = &snippet.code;
    let mut file = fs::OpenOptions::new()
        .write(true)
        .create(true)
        .truncate(true)
        .open(&file_path)
        .unwrap();

    // 写入题解文件
    // 对单个函数定义的，解析函数名，填充测试模板
    if code.match_indices(" fn ").count() > 1 {
        file.write_all(code.as_bytes()).unwrap();
    } else {
        let func_part = code
            .split(" pub fn ")
            .nth(1)
            .unwrap_or_else(|| panic!("{} bad fn format?", code))
            .trim_end_matches(|x| x == '}' || x == '\n' || x == ' ');
        file.write_all(b"pub fn ").unwrap();
        file.write_all(func_part.as_bytes()).unwrap();
        file.write_all(b"\n}").unwrap();

        let func_name = func_part.split('(').next().unwrap();
        let test_code = TEST_TMPL
            .replace("{id}", &id_arg)
            .replace("{func_name}", func_name);
        file.write_all(test_code.as_bytes()).unwrap();
    }

    // 避免重复地导入题解模块
    let lib_content = fs::read_to_string("./src/lib.rs").unwrap();
    if lib_content.matches(&file_name).count() == 0 {
        let mut lib_file = fs::OpenOptions::new()
            .write(true)
            .append(true)
            .open("./src/lib.rs")
            .unwrap();
        writeln!(lib_file, "mod {};", file_name).unwrap();
    }
}
