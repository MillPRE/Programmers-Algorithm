// https://school.programmers.co.kr/learn/courses/30/lessons/181916

function solution(a, b, c, d) {
    const arr = [a,b,c,d];
    const set = new Set(arr);
    const dic = {};

    arr.forEach((a) => {
        if(dic[a] !== undefined) {
            dic[a] += 1;
        } else {
            dic[a] = 1;
        }
    });

    const keys = Object.keys(dic);



    if(set.size === 1) {
        // 4 all p - 1111 * p
        return 1111 * a;
    } else if(set.size === 2) {
        // 3 p 1 q - (10 * p + q)**2
        if(dic[keys[0]] !== dic[keys[1]]) {
            const p = dic[keys[0]] >= dic[keys[1]] ? Number(keys[0]) : Number(keys[1]);
            const q = dic[keys[0]] >= dic[keys[1]] ? Number(keys[1]) : Number(keys[0]);

            return (10*p+q) ** 2;
        }
        // 2p 2q - (p+q) * |p-q|(abs)
        else {
            const p = keys[0] >= keys[1] ? Number(keys[0]) : Number(keys[1]);
            const q = keys[0] >= keys[1] ? Number(keys[1]) : Number(keys[0]);

            return (p+q) * Math.abs(p-q);
        }

    } else if(set.size === 3) {
        // 2p 1q 1r - q*r
        const qr = [];

        keys.forEach((k) => {
            if(dic[k] === 1) {
                qr.push(k);
            }
        });

        return qr[0] * qr[1];

    } else {
        // all different - 가장 작은 숫자
        return Math.min(...arr);
    }


    return 0;
}
