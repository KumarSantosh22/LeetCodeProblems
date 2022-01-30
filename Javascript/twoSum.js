var twoSum = function (nums, target) {
  result = [];
  dict = new Map();
  for (let i = 0; i < nums.length; i++) {
    let diff = target - nums[i];
    if (dict.has(diff)) {
      result[0] = i;
      result[1] = dict.get(diff);
      break;
    } else {
      dict.set(nums[i], i);
    }
  }
  return result;
};

var twoSum2 = function (nums, target) {
  result = [];
  dict = new Map();
    nums.forEach((x, i) => {
        let diff = target - x;
        if (dict.has(diff)) {
            result[0] = i;
            result[1] = dict.get(diff);
            return;
        } else {
            dict.set(x, i);
        }
    });
    return result;
};

console.log(twoSum([2, 7, 11, 15], 9));
console.log(twoSum2([2, 7, 11, 15], 9));
