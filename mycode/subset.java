class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if( nums == null || nums.length == 0){
            return res;
        }
        Arrays.sort(nums);
        List<Integer> list = new ArrayList<>();
        helper(res, nums, 0,list);
        return res;
    }
    public void helper( List<List<Integer>> res, int[] nums, int start, List<Integer> list){
        res.add(new ArrayList<>(list));
        for( int i = start; i<nums.length ;i++){
            list.add(nums[i]);
            helper(res, nums, i+1,list);
            list.remove(list.size()-1);
        }

    }

}