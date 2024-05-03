#include <stdio.h>
#include <math.h> 

int ktSoChinhPhuong(int num) {
  return sqrt(num) == (int)sqrt(num);
}

int demSoChinhPhuong(int n) {
  int count = 0;
  for (int i = 1; i <= n; i++) {
    if (ktSoChinhPhuong(i)) {
      count++;
    }
  }
  return count;
}

int main() {
  int n;
  printf("Nhap n: ");
  scanf("%d", &n);

  if (n <= 0) {
    printf("n phải là số nguyên dương.\n");
    return 1;
  }

  int squareCount = demSoChinhPhuong(n);
  printf("Số lượng số chính phương nhỏ hơn %d là: %d\n", n, squareCount);

  for (int i = 1; i <= squareCount; i++) {
    int squareNum = i * i;
    printf("%d ", squareNum);
  }

  return 0;
}
