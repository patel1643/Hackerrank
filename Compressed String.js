function compressedString(message) {
    // Write your code here
    var size = message.length;
    var compressedStr = "";
    var counter = 1;
    var repeatedLetter = "";

for(var i = 0; i < size; i++){
    for(var j = i+1; j <= size; j++){
        if(message[i] === message[j]){
            repeatedLetter = message[i];
            counter = counter + 1;
        }
        else{
            if(counter > 1){
                compressedStr = compressedStr + repeatedLetter + counter + "";
                i = i+counter-1;
                repeatedLetter = "";
            }else{
                compressedStr = compressedStr + message[i];              
            }
            counter = 1;
            break;
        }
    }   
       
    }

    return compressedStr;

}