/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
let check = new Set()

    for(let i=0;i< nums.length;i++){
       if(check.has(nums[i])) {
        return true
       }
       check.add(nums[i])
       if(check.size > k){
        check.delete(nums[i-k])
       }
    }
     return false;
};