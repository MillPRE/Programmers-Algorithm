// https://school.programmers.co.kr/learn/courses/30/lessons/181897?language=javascript

function solution(n, slicer, num_list) {
    if(n === 1) {
        return num_list.slice(0, slicer[1]+1);
    } else if( n === 2) {
        return num_list.slice(slicer[0], );
    } else if( n === 3) {
        return num_list.slice(slicer[0], slicer[1]+1);
    } else {
        return num_list.filter((n, idx) => {
            if (idx % slicer[2] === slicer[0] % slicer[2] && idx >= slicer[0] && idx <= slicer[1]) return n;
        })
    }
}
