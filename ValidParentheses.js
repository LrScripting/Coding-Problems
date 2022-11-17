/* Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
Examples

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

*/

function validParentheses(parens){
    let num = 0;
    for(let i = 0; i < parens.length; i++){
        if(num < 0){
          return false
      }
        else if(parens[i] == "("){
            num +=1
        }
        else if (parens[i] == ")"){
            num -=1
        }
    }   
    if (num == 0){
        return true
    }
    if(num > 0 || num < 0){
        return false
    }
}
