#include <stdio.h>

extern void ECDSA_256_sign(unsigned char sig[64], const unsigned char hash[32]);

int main()
{
  unsigned char sig[64];
  unsigned char hash[32];

  while (!feof(stdin)) {
    int l = fread(hash, 32, 1, stdin);
    if (l != 1) break;

    ECDSA_256_sign(sig, hash);

    l = fwrite(sig, 64, 1, stdout);
    if (l != 1) break;
  }
  return 0;
}
