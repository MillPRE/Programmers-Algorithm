function solution(a, b, c) {
    var answer = 0;
    const set = new Set([a,b,c]);
    console.log(set.size)

    if(set.size === 3) {
        return a + b + c;
    } else if(set.size === 2) {
        return (a + b + c) * ( a*a + b*b + c*c );
    } else {
        return (a + b + c) * ( a*a + b*b + c*c ) * (a*a*a + b*b*b + c*c*c);
    }


    return answer;
}
