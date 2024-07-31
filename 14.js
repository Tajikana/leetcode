/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    
    if(strs.length==0){
        return "";
    }
    var value=strs[0];

    for (let i =1 ; i <strs.length; i++){

      var j=strs[i];
      while(j.indexOf(value)!==0){

        value=value.substr(0,value.length-1);
        if(value==""){

            return ""
        }
      }  
    }
    return value 
};
