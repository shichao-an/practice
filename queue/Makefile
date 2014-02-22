CC = gcc-4.2
CFLAGS = -Wall

.PHONY: clean

INCDRS = -I$(PRACTICE_TOPDIR)/list
SRCFLS = $(PRACTICE_TOPDIR)/list/list.c
OBJFLS = queue.o\
		 $(PRACTICE_TOPDIR)/list/list.o

%.o: %.c $(SRCFLS)
	$(CC) -c $(CFLAGS) $(INCDRS) -o $@ $<

main: main.o $(OBJFLS) 
	$(CC) -o $@ $^

clean:
	rm *.o

