use std::fs;
use std::collections::HashMap;

fn main() {
  if let [dna,pattern, ..]= read_file("BioInformatics1/Week1/dataset_4_5.txt").as_slice() {
let [k,l,t] : [i32; 3] = pattern.split(" ").map(|s| s.parse::<i32>().unwrap()).collect();

    let result = find_clumps(&dna,(usize) k,l,t);
    println!("{:?}",result);
  }
  
}

fn _pattern_count(dna : &str, pattern : &str) -> i32 {
let mut count : i32 = 0;
for i in 0..(dna.len()-(pattern.len()-1)){
  let slice = &dna[i..(i+pattern.len())];
  if pattern == slice { 
  count += 1;
  }
}
count
}

fn _frequent_words(dna :  &str, k : usize) -> Vec<&str> {
  let mut k_mer_frecs = frequent_words_dict(dna, k);
  
  if let Some(max_frec) = k_mer_frecs.values().max() {
    let max_keys =  k_mer_frecs.iter().filter(|(_,val)| val >= &max_frec)
    .map(|(key,_)| *key).collect();


    return max_keys;

  } else {
    return Vec::new();
  }
}


fn frequent_words_dict(dna : &str, k : usize) -> HashMap<&str,usize> {
  let mut k_mer_frecs = HashMap::new();
  for i in 0..(dna.len()-k+1) {
    let k_mer : &str = &dna[i..i+k];
    if let Some(val) = k_mer_frecs.get_mut(&k_mer) {
      *val+=1;
    } else {
      k_mer_frecs.insert(k_mer,1);
    }
  }
  k_mer_frecs
}

fn _reverse_complement(dna : &str) -> String {
  let mut s = String::new();
  for i in (0..dna.len()).rev(){
    let b = &dna[i..(i+1)];
    let c = match b {
      "A" => "T",
      "T" => "A",
      "C" => "G",
      "G" => "C",
      _ => "X"
    };
    s.push_str(c);
  }
  s
}

fn pattern_matching(dna : &str, pattern : &str) -> String {
  let mut v = String::new();
  for i in 0..(dna.len() - pattern.len() + 1) {
     let slice = &dna[i..i+pattern.len()];
     if slice == pattern {
       v.push_str(&i.to_string());
       v.push(' ');
     }
  }
  v
}

fn find_clumps(dna : &str, k : usize , l : usize , t : usize ) -> &str {
    for i in 0..dna.len()-l+1 {  
      let mut table = frequent_words_dict(&dna[i..i+l],k);
      let mut _a = table.iter().filter(|(_,v)| v > &&t).map(|(k,_)| k );
    }
   ""
}


fn read_file(filename: &str) -> Vec<String> {
  let content : String = fs::read_to_string(filename).expect("Something went wrong.");
  content.split("\n").map(|s| s.to_string()).collect()
} 
