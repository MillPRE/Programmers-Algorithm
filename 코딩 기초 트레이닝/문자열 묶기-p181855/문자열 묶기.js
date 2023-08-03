// https://school.programmers.co.kr/learn/courses/30/lessons/181855

function solution(strArr) {
    const dic = {}
    const answer = [];

    strArr.forEach((s) => {
        if(dic[s.length] === undefined) {
            dic[s.length] = 1;
        } else {
            dic[s.length] += 1;
        }
    });

    for (let key in dic ){
        answer.push(dic[key]);
    }

    return Math.max(...answer);

}
