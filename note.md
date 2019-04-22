+ two_sum:
    + 提前构建map，做快速查询
+ longest_common_prefix:
    + zip(\*List), 用*来解耦list的每个元素
+ find_median_sorted_arrays:
    + 使用二分查找降低时间复杂度到logN
    + 对输入进行数据处理，标准化流程，达到简化的目的
+ convert_to_z_str:
    + 用index取代filter, 更快速: np.array(filter(lambda x: x > 5, arr))  ====>  arr[arr > 5]
    + 原生python，使用*zip(*2d_list)来转置矩阵
+ **simulate_regular_expression**:
    + 使用**动态规划**，优化迭代（递推），缓存中间结果
    + 动态规划：将一个问题拆成几个子问题，分别求解这些子问题，即可推断出大问题的解(自底向上)。
+ max_area:
    + 使用双指针对有序列表，进行双数遍历
+ three_sum_closest:
    + 双指针遍历时，更有意义的初始化