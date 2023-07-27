// https://school.programmers.co.kr/learn/courses/30/lessons/181834

function solution(myString) {
    const ASCII_I = 108
    myString = myString.split("").map((m) => {
        if(m.charCodeAt(0) < ASCII_I) {
            return 'l';
        } else {
            return m;
        }
    });

    return myString.join('');
}
