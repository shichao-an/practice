CC = gcc-4.2
CFLAGS = -Wall

.PHONY: clean

%.o: %.c sorting.h
	$(CC) -c $(CFLAGS) -o $@ $<

main: main.o sorting.o
	$(CC) -o $@ $^

clean:
	rm *.o
