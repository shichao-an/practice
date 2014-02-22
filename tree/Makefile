CC = gcc-4.2
CFLAGS = -Wall

.PHONY: clean

INCDRS = -I$(PRACTICE_TOPDIR)/list\
		 -I$(PRACTICE_TOPDIR)/queue

SRCFLS = $(PRACTICE_TOPDIR)/list/list.c\
		 $(PRACTICE_TOPDIR)/queue/queue.c\

OBJFLS = tree.o\
		 diameter.o\
		 $(PRACTICE_TOPDIR)/queue/queue.o\
		 $(PRACTICE_TOPDIR)/list/list.o

%.o: %.c $(SRCFLS) tree.h
	$(CC) -c $(CFLAGS) $(INCDRS) -o $@ $<

main: main.o $(OBJFLS) 
	$(CC) -o $@ $^

clean:
	rm *.o
