描述
给定一个字符串 S ，定义三种有价值的字符串： A = "nico" ，B = "niconi" , C = "niconiconi"
其中，字符串 A 的价值为 a， 字符串 B 的价值为 b，字符串 C 的价值为 c
她拿到了一个长度为 n 的字符串，你需要在其中找到一些有价值的子串 (指字符串中连续的一段)，并统计价值之和的最大值。
注：已被计算价值过的字符不能重复计算价值！如 "niconico" 要么当作 "nico" + "nico" 计 2a 分，要么当作 "niconi" + "co" 计 b 分（其中 "co" 不计分）。


输入描述：
第一行四个正整数 。 
第二行是一个长度为  的字符串。
输出描述：
一个整数，代表最大的计数分数。