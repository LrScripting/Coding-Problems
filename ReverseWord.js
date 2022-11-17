""""Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained."""



function reverseWords(str){
    let final = []
    arr1 = str.split(" ");
    for(let j = 0; j < arr1.length; j++){
        arr = arr1[j].split("");
        arrcopy = [...arr];
        for(let i = 0; i < arr.length; i++){
            arrcopy.splice((arr.length-1)-i, 1, arr[i])
        }
        final.push(arrcopy.join("")) 
    }
    return final.join(" ")
   
}
