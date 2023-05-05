/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let mySet = new Set();
  nums.forEach((element) => {
    mySet.add(element);
  });
  if (mySet.size == nums.length) {
    return false;
  }
  return true;
};