fn is_palindrome(s: &str) -> bool {
    let result: String = s
        .to_lowercase()
        .chars()
        .filter(|c| c.is_alphanumeric())
        .collect();

    result.chars().rev().collect::<String>() == result
}

fn main() {
    assert!(is_palindrome("A man, a plan, a canal, Panama!"));
    assert!(is_palindrome("Was it a car or a cat I saw?" ));
    assert!(is_palindrome("No 'x' in Nixon"));
    assert!(! is_palindrome("This is not palindrome"));
}
