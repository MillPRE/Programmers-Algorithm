// https://school.programmers.co.kr/learn/courses/30/lessons/181864

function solution(myString, pat) {
    myString = myString.split("").map((d) => {
        return d === 'A' ? 'B' : 'A';
    }).join('');

    return myString.includes(pat) ? 1 : 0;
}
