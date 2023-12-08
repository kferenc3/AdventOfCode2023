use std::collections::HashMap;

pub fn day4solver(i: &str) -> (String, String){
    (day4_main(i).0.to_string(), day4_main(i).1.to_string())
}

fn day4_main(i: &str) -> (i32,i32) {

let mut total_part1 = 0;
let mut cards_won: HashMap<usize,i32> = HashMap::new();

let cards = i
    .lines()
    .map(|line| line.split(": ").nth(1).unwrap().split(" | ").collect::<Vec<&str>>())
    .collect::<Vec<Vec<&str>>>();

for (cardnum, i) in cards.iter().enumerate(){
    let winning_numbers = i[0].split(' ').collect::<Vec<&str>>();
    let player_numbers = i[1].split(' ').collect::<Vec<&str>>();
    let mut winners = 0;
    for pn in player_numbers {
        if !pn.is_empty() && winning_numbers.contains(&pn){
            winners += 1;
        }
    }
    if winners > 0 {
        total_part1 += 2_i32.pow(winners-1);
        *cards_won.entry(cardnum).or_insert(0) += 1;
        for _p in 0..cards_won[&cardnum] {
            let mut i = 1;
            for _x in 0..winners{
                *cards_won.entry(cardnum+i).or_insert(0) += 1;
                i += 1;
            }
        }

    }
    else {
        *cards_won.entry(cardnum).or_insert(0) += 1;
    }
}
(total_part1,cards_won.values().sum())

}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn day4test1() {
        assert_eq!((13,30),day4_main(&String::from("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")));
    }
}
