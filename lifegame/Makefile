FC=gfortran
FCFLAGS=-O3  
TARGET=a.out
OBJS=main.o init.o const.o life.o

.PHONY : all
.PHONY : clean
.SUFFIXES :
.SUFFIXES : .o .f90

.f90.o :
	$(FC) $(FCFLAGS) -c $<

all: $(TARGET)
$(TARGET) : $(OBJS)
	$(FC) -o $(TARGET) $(FCFLAGS) $(OBJS)

#Dependencies
main.o : init.o const.o life.o
init.o : const.o
life.o : const.o
clean:
	rm -f $(TARGET) $(OBJS) *.mod *.out core
