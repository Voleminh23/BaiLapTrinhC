#include <stdio.h>

  int ktBoiBay(int num) {
    if (num % 7 == 0) {
      return 1;
    } else {
      return 0;
    }
  }
int main() {
    printf("Các số bội của 7 có 2 chữ số:");
  for (int i = 10; i <= 99; i++) {

    if (ktBoiBay(i)) {
      printf("%d ", i);
    }
  }

  return 0;
}
