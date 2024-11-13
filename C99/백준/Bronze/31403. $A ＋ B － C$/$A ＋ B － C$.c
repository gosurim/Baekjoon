#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {
    int a, b, c;
    
    // 입력을 받습니다.
    scanf("%d %d %d", &a, &b, &c);
    
    // 첫 번째 줄 출력: 숫자로 계산한 결과
    printf("%d\n", a + b - c);
    
    // 두 번째 줄 출력: 문자열로 계산한 결과
    // 문자열 덧셈
    char str_a[10], str_b[10], str_c[10], str_sum[20];
    sprintf(str_a, "%d", a);
    sprintf(str_b, "%d", b);
    sprintf(str_c, "%d", c);
    strcpy(str_sum, str_a);
    strcat(str_sum, str_b);
    
    // 문자열을 숫자로 변환하여 빼기
    int result = atoi(str_sum) - c;
    printf("%d\n", result);

    return 0;
}
