// https://school.programmers.co.kr/learn/courses/30/lessons/181872

function solution(myString, pat) {
    const idx = myString.lastIndexOf(pat);
    myString = myString.slice(0, idx+pat.length);

    return myString;
}
