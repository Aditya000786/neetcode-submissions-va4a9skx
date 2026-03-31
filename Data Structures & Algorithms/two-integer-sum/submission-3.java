class Solution {
        public int[] twoSum(int[] nums, int target) {
            Map<Integer, Integer> indices = new HashMap<>();
            for(int i=0; i< nums.length; i++){
                if(indices.containsKey(target-nums[i])){
                    return new int[]{indices.get(target-nums[i]), i};
                }
                indices.put(nums[i], i);
            }
            return new int[0];
        }
    }
    