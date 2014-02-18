CC = gcc-4.2
CFLAGS = -Wall

.PHONY: clean main

%.o: %.c tree.h
	$(CC) -c $(CFLAGS) -o $@ $<

main: main.o tree.o diameter.o
	$(CC) -o $@ $^

clean:
	rm *.o
