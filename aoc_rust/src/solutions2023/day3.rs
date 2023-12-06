//I wasted hours on making this work, but after successfully passing the test input it seems the final result is still incorrect.
//With that said I gave up on this as this code is anyway a monster and not rust-like at all.

use std::{collections::HashMap, usize};

pub fn day3solver(i: &str) -> (String, String){
    (day3_main(i).0.to_string(), day3_main(i).1.to_string())
}

 #[derive(Debug)]
struct PartNumber {
    number: i32,
    coordinates: Vec<(usize, usize)>
}

impl PartNumber {
    fn new(num:&str, coord: Vec<(usize,usize)>) -> PartNumber {
        PartNumber { 
            number: num.parse::<i32>().unwrap(), 
            coordinates: coord, 
        }
    }
}

fn neighbors(c: &(usize,usize), h: usize, w: usize) -> Vec<(usize,usize)> {
    let c1 = c.0;
    let c2 = c.1;
    let c3 = if c.0 !=0 {c.0-1} else {0_usize}; 
    let c4 = if c.1 !=0 {c.1-1} else {0_usize};
    let mut res = vec![(c1+1, c2), (c3, c2), (c1, c2+1), (c1, c4), (c1+1,c2+1), (c3,c4), (c3, c2+1), (c1+1, c4)]
        .iter()
        .filter(|(c3, c4)| *c3<=h && *c4<=w)
        .cloned()
        .collect::<Vec<(usize,usize)>>();
    res.sort();
    res.dedup();
    res
}

fn day3_main(i: &str) -> (i32,i32) {
    
    let matrix: Vec<Vec<char>> = i.lines().map(|line| {line.chars().collect::<Vec<char>>()}).collect::<Vec<Vec<char>>>();
    let height = matrix.len();
    let width = matrix[0].len();
    let mut num_coord: Vec<(usize, usize)> = vec![];
    let mut symbols: Vec<(usize, usize)> = vec![];
    let mut asterisks: Vec<(usize,usize)> = vec![];
    let mut num: Vec<char> = vec![];
    let mut num_dict: HashMap<i32,PartNumber> = HashMap::new();
    let mut id = 0;
    let mut total_part1 = 0;
    let mut total_part2: HashMap<(usize,usize),Vec<i32>> = HashMap::new();
    let mut part2res = 0;

    for (ln, line) in matrix.iter().enumerate() {
        for (cn, cell) in line.iter().enumerate() {
            match cell {
                '1'..='9' => num_coord.push((ln,cn)),
                '*' => {symbols.push((ln,cn)); asterisks.push((ln,cn));},
                '.' => continue,
                _ => symbols.push((ln,cn))
            }    
        } 
    }
    println!("{:?}", matrix); 
    let coord_chunks = num_coord.chunks(2);
    let mut partcoords: Vec<(usize,usize)> = vec![];
        for coord in coord_chunks {
            for coordinate in coord {
                match &partcoords.last() {
                    Some(c) => {
                        if c.0 == coordinate.0 && c.1+1 == coordinate.1 {
                            num.push(matrix[coordinate.0][coordinate.1]);
                            partcoords.push(*coordinate);
                        }
                        else {
                            num_dict.insert(id, PartNumber::new(num.iter().collect::<String>().as_str(),partcoords.clone()));
                            id += 1;
                            num.clear();
                            partcoords.clear();
                            num.push(matrix[coordinate.0][coordinate.1]);
                            partcoords.push(*coordinate);
                        }
                    },
                    None => {
                        num.push(matrix[coordinate.0][coordinate.1]);
                        partcoords.push(*coordinate);
                    },
                }
            }
            num_dict.insert(id, PartNumber::new(num.iter().collect::<String>().as_str(),partcoords.clone()));
        }
    
    for (_i, part) in num_dict.iter() {
        let mut to_sum = false;
        for i in &part.coordinates {
            if neighbors(i, height, width).iter().any(|item| symbols.contains(item)) {
                to_sum = true;
                for a in &asterisks {
                    if neighbors(i, height, width).contains(a) {
                        total_part2.entry(*a).or_insert(vec![part.number]).push(part.number);
                        total_part2.entry(*a).or_insert(vec![part.number]).sort();
                        total_part2.entry(*a).or_insert(vec![part.number]).dedup();
                    }
                }
                break;
            }
        }
        if to_sum {
            total_part1 += part.number;
        }
    }
    for (k,v) in total_part2 {
        if v.len() == 2 {
            part2res += v.iter().fold(1,|a, b| a*b);
        }
    };
    
    (total_part1,part2res)
    
}

// Part I:  Test: 4361   Input: 520135
// Part II: Test: 467835 Input: 72514855

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn day3test1() {
        assert_eq!((4361,467835),day3_main(&String::from("467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598..")));
    }
}
