
use std::fs;
use std::collections::HashMap;

fn main() {
  let (dna,pattern) = read_file("BioInformatics1/Week1/1.2/dataset_2_13.txt");
  let result = frequent_words(&dna,pattern.parse::<usize>().unwrap());
  println!("{:?}",result);
}

fn pattern_count(dna : &str, pattern : &str) -> i32 {
let mut count : i32 = 0;
for i in 0..(dna.len()-(pattern.len()-1)){
  let slice = &dna[i..(i+pattern.len())];
  if pattern == slice { 
  count += 1;
  }
}
count
}

fn frequent_words(dna :  &str, k : usize) -> Vec<&str> {
  let mut k_mer_frecs = HashMap::new();
  for i in 0..(dna.len()-k+1) {
    let k_mer : &str = &dna[i..i+k];
    if let Some(val) = k_mer_frecs.get_mut(&k_mer) {
      *val+=1;
    } else {
      k_mer_frecs.insert(k_mer,1);
    }
  }
  
  if let Some(max_frec) = k_mer_frecs.values().max() {
    let max_keys =  k_mer_frecs.iter().filter(|(_,val)| val >= &max_frec)
    .map(|(key,_)| *key).collect();


    return max_keys;

  } else {
    return Vec::new();
  }
}


fn read_file(filename: &str) -> (String,String) {
  let content : String = fs::read_to_string(filename).expect("Something went wrong.");
  let args : Vec<&str> = content.split("\n").collect();
  (args[0].to_string(),args[1].to_string())
} 

