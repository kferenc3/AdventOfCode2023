use std::collections::HashMap;

pub fn day1solver(i: &str) -> (String, String){
    (part_i(i).to_string(), part_ii(i).to_string())
}

fn part_i(i: &str) -> i32 {
    let mut total = 0;
    let lines = i.lines();

    let mut nums: Vec<char> = Vec::new();
    for l in lines {
        for c in l.chars() {
            if c.is_numeric() {
                nums.push(c);
            }
        }
        let mut val = String::new();
        val.push(nums[0]);
        val.push(nums[nums.len()-1]);

        total += val.parse::<i32>().unwrap();
        nums.clear()
    }
    
    total
}

fn part_ii(i: &str) -> i32 {
    
    let lines = i.lines();
    let mut total = 0;
    let translate = HashMap::from([("one", "o1e"),("two", "t2o"), ("three", "t3e"), ("four", "f4r"),("five", "f5e"),("six", "s6x"),("seven", "s7n"),("eight", "e8t"),("nine", "n9e")]);
    let mut nums: Vec<char> = Vec::new();
    
    for l in lines {
        let mut newline = l.to_string();
        for (key, value) in &translate {
            newline = newline.replace(key, value);
        }
        
        for c in newline.chars() {
            if c.is_numeric() {
                nums.push(c);
            }
        }
        let mut val = String::new();
        val.push(nums[0]);
        val.push(nums[nums.len()-1]);

        total += val.parse::<i32>().unwrap();
        nums.clear()
    };
    
    total
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn day1test1() {
        assert_eq!(142,part_i(&String::from("1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet")));
        assert_eq!(281,part_ii(&String::from("two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen")));   
    }

    #[test]
    fn day1test2() {
        assert_eq!(15,part_i(&String::from("1six15ninebgnzhtbmlxpnrqoneightfhp")));
        assert_eq!(18,part_ii(&String::from("1six15ninebgnzhtbmlxpnrqoneightfhp")));    
    }
}
