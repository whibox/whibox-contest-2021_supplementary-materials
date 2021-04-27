LDFLAGS=-L/usr/local/lib
LDLIBS=-lgmp


all: dECDSA

dECDSA.o: dECDSA.c

dECDSA: main.c dECDSA.o

clean:
	rm dECDSA.o dECDSA
