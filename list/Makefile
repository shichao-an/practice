CC = gcc-4.2
CFLAGS = -Wall

.PHONY: clean

%.o: %.c list.h 
	$(CC) -c $(CFLAGS) -o $@ $<

list: list.o list.o
	$(CC) -o $@ $^

clean:
	rm *.o
