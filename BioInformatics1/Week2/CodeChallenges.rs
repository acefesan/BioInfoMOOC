use std::fs;
use std::collections::HashMap;
use std::collections::HashSet;


fn main() {
    if let [dna,..]= read_file("BioInformatics1/Week2/dataset_3_5.txt").as_slice() {
        
        println!("{:?}",dna);
          }
}



fn min_skew(dna : &str) {
 let mut skews : [i32;dna.len()];
 skews[0]=0;
 for i in 1..dna.len(){
     match dna[i-1:i] {
            "A" => skews[i] = skews[-i];,
            "T" => skews[i] = skews[-i];,
            "C" => skews[i] = skews[-i] -1;,
            "G" => skews[i] = skews[-i] +1;,
            _ => skews[i] = skews[-i];
     }
 }
 println!("{:?}",skews);


}

fn read_file(filename: &str) -> Vec<String> {
    let content : String = fs::read_to_string(filename).expect("Something went wrong.");
    content.split("\n").map(|s| s.to_string()).collect()
  } 