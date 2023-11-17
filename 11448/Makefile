# Copyright (c) 2015 Martin VÃ¡Åˆa
#
# Usage in basic contest:
#     make BIN=problem                    compile and run testcase 'program.in'
#     make BIN=problem DBG=T              compile and run testcase 'program.in' with debug message printing
#     make BIN=problem MEM=T              compile and run testcase 'program.in' and check with valgrind
#
# Usage in contest with cmd support:
#     make rank                           display team rank
#     make BIN=problem download           download problem input
#     make BIN=problem submit             submit to grading server
#     make BIN=problem print              print problem source code
#
# For local problem validation:
#     make BIN=problem CMP=T              compiles, runs and compares 'problem.out.tmp' with 'problem.out'
#     make BIN=problem TC=tc1 testcase    runs testcase named 'tc1' produces 'tc1.out.tmp' and compares it with 'tc1.out'

MEM=F# T=TRUE, F=fALSE
DBG=F# T=TRUE, F=fALSE
CMP=F# T=TRUE, F=fALSE
TC=
BIN=main
SHELL=bash
CC=g++
TCFLAGS=-O2 -Wall -static
CFLAGS=-std=c++11 -pipe -lm -O2 -Wall -static
MEMCFLAGS=${CFLAGS} -O1 -g3

.PHONY: build
build: clean
#ifeq (${T},T)
ifeq (${DBG},T)
	$(eval CFLAGS=-DDEBUG= ${CFLAGS})
	$(eval MEMCFLAGS=-DDEBUG= ${MEMCFLAGS})
endif
ifeq (${MEM},T)
	$(CC) $(MEMCFLAGS) ${BIN}.cpp -o ${BIN}
	@make -s clean
	@make -s memcheck
else
	$(CC) $(CFLAGS) ${BIN}.cpp -o ${BIN}
	@make -s clean
	@make -s test
endif
ifeq (${CMP},T)
	@make -s cmp
endif

.PHONY: clean
clean:
	@rm -f *.o

.PHONY: test
test:
	./${BIN} < ${BIN}.in | tee ${BIN}.out.tmp

.PHONY: memcheck
memcheck:
	valgrind --leak-check=full ./${BIN} < ${BIN}.in

.PHONY: cmp
cmp:
	diff -s ${BIN}.out ${BIN}.out.tmp

# For contest with command line support only
.PHONY: rank
rank:
	@echo "Command line rank not available."

.PHONY: download
download:
	@echo "Command line problem input download not available."

.PHONY: submit
submit:
	@echo "Command line submitting not available."

.PHONY: print
print:
	@echo "Command line printing not available."

# For home contest data validation
.PHONY: testcase
testcase:
	time ./${BIN} < ${TC}.in > ${TC}.out.tmp
	diff -s ${TC}.out ${TC}.out.tmp
