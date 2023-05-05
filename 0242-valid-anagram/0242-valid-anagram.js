/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length != t.length) {
    return false;
  }
  const sortedS = s.split("");
  sortedS.sort();
  const sortedT = t.split("");
  sortedT.sort();
  for (let i = 0; i < sortedS.length; i++) {
    if (sortedS[i] != sortedT[i]) {
      return false;
    }
  }
  return true;
    
};