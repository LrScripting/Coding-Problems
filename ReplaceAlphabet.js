/* Description:

Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
Example

alphabet_position("The sunset sets at twelve o' clock.")

Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )
*/
 let array = [0, 'a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

function alphabetPosition(text){

    let array2 = text.split('');
    const lowercaseArray = array2.map(element => {
  
         return element.toLowerCase();

    })
    let finalarray =[];
    var filtered = lowercaseArray.filter(function (el) {
        return el != ' ';
      });
   
    for(let i = 0; i< array2.length; i++){
        if(array.includes(filtered[i])){
            finalarray.push(array.indexOf(filtered[i]))
        }
       

    }
    let final =  finalarray.join(' ').toString();
    return final;
}
