// https://school.programmers.co.kr/learn/courses/30/lessons/181874

function solution(myString) {
    myString = myString.split("");
    myString = myString.map((d) => {
        if(d === 'a' || d === 'A') {
            return 'A';
        } else {
            return d.toLowerCase();
        }
    });

    return myString.join('');
}
