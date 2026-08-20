/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let check = new Set()
    for(let num of nums){
        if (check.has(num)){
            return true
        }
        else{
            check.add(num)
        }

    }
     return false;
};