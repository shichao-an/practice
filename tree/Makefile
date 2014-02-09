CC = gcc-4.2
CFLAGS = -Wall

.PHONY: clean

%.o: %.c tree.h
	$(CC) -c $(CFLAGS) -o $@ $<

diameter: diameter.o tree.o
	$(CC) -o $@ $^

clean:
	rm *.o
