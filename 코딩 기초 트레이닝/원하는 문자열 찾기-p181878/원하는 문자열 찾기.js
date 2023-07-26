// https://school.programmers.co.kr/learn/courses/30/lessons/181878

function solution(myString, pat) {
    pat = pat.toLowerCase();
    myString = myString.toLowerCase();

    return myString.indexOf(pat) > -1 ? 1 : 0;
}
