fn insertion_sort<T: std::cmp::Ord>(list: &mut [T]) {
    for i in 1..list.len() {
        let mut j = i;

        while j > 0 && list[j] < list[j-1] {
            list.swap(j, j-1);
            j -= 1;
        }
    }
}

fn main() {
    let mut list = vec![5, 4, 3, 2, 1];
    insertion_sort(&mut list);
    assert_eq!(list, vec![1, 2, 3, 4, 5]);
}
