/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
    let check = {}
    let result = []

    for(let num of nums1){
       check[num] = (check[num] || 0)+1
    }

    for(let num of nums2){
        if(check[num]>0){
            result.push(num)
            check[num]--
        }
    }
     return result;
};