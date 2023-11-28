// https://school.programmers.co.kr/learn/courses/30/lessons/12977

function solution(nums) {
    let answer = 0;
    const CNT = 3;
    const combinations = [];

    for (i = 0 ; i <= nums.length-CNT ; i++) {
        for(j = i+1 ; j < nums.length-1 ; j++) {
            for(k=j+1; k < nums.length ; k++) {
                const combi = [];
                combi.push(nums[i], nums[j], nums[k]);
                combinations.push(combi);
            }
        }
    }

    combinations.forEach((combi) => {
        const sum = combi[0] + combi[1] + combi[2];
        let flag = true;

        for(i = 2; i < sum; i++) {
            if (sum % i === 0) {
                flag = false;
            }
        }

        if (flag) answer++;
    });

    return answer;
}