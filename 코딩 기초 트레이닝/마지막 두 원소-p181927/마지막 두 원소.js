function solution(num_list) {
    const LEN = num_list.length;

    const A = num_list[LEN-2];
    const B = num_list[LEN-1];

    num_list.push(A >= B ? B * 2 : B - A);

    return num_list;
}
