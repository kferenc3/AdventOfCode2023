use std::cmp;

pub fn day2solver(i: &str) -> (String, String){
    (part_i(i).to_string(), part_ii(i).to_string())
}

//Today's rust solution is not my own, but I based it on a reddit submission. 
//Python was easy, but couldn't crack the rust version. 
//However it was still good practice.

fn part_i(i: &str) -> i32 {
    i
        .lines()
        .map(|line| {
            let (game, rounds) = line.split_once(": ").unwrap();
            if rounds.split("; ").all(|round| {
                round.split(", ").all(|pair| {
                    let (num, color) = pair.split_once(' ').unwrap();
                    let pn = num.parse::<i32>().unwrap();
                    match color {
                        "red" => pn <= 12,
                        "blue" => pn <= 14,
                        "green" => pn <= 13,
                        _ => panic!(),
                    }
                })
            }) {
                game.split_once(' ').unwrap().1.parse::<i32>().unwrap()
            } else {
                0
            }
        })
        .sum()
    }    

fn part_ii(i: &str) -> i32 {
    i
        .lines()
        .map(|line| {
            let (_, rounds) = line.split_once(": ").unwrap();
            let (mut max_red, mut max_green, mut max_blue) = (0,0,0);
            rounds.split("; ").for_each(|round| {
                round.split(", ").for_each(|pair| {
                    let (num, color) = pair.split_once(" ").unwrap();
                    let point = num.parse::<i32>().unwrap();
                    match color {
                        "red" => max_red = cmp::max(max_red, point),
                        "green" => max_green = cmp::max(max_green, point),
                        "blue" => max_blue = cmp::max(max_blue, point),
                        _ => panic!(),
                    }
                })
            });
            max_red * max_green * max_blue
        })
        .sum()
        
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn day2test1() {
        assert_eq!(8,part_i(&String::from("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")));
        assert_eq!(2286,part_ii(&String::from("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")));   
    }
}
