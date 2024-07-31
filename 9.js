/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    var str=x.toString();
    var length=str.length;
    for (let i=0; i<length/2;i++){
        if (str[i]!=str[length-i-1]){
            return false;
        }

    }
    return true
};
