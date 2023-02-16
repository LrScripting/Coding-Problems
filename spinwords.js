/* Description:

Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"

*/
function spinWords(string){

    let array = string.split(" ")

    for(let i = 0; i < array.length; i++){
        let kek = array[i].split("")
        if(kek.length >= 5){
            let reversedElement = kek.reverse()
            let reversedString = reversedElement.join('')   
            array[i] = reversedString; 
        }
        if (array.length == 1){
            let array = string.split("")
            var reverse = array.reverse();
            var reversestring = reverse.join('')
            return reversestring;
          }   
    }
    return array.join(' ')
  }

#2nd attempt in python

def spinWords(words):
    return " ".join(list(map(lambda x: x[::-1] if len(x) > 5 else x, words.split())))
    
    
    
    
    
