CC = gcc-4.2
CFLAGS = -Wall

.PHONY: clean

%.o: %.c trees.h
	$(CC) -c $(CFLAGS) -o $@ $<

diameter: diameter.o trees.o
	$(CC) -o $@ $^

clean:
	rm *.o
