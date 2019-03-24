TARGETS		:= minHeapTest
OBJS		:= minHeapTest.o
CC			:= g++
CFLAGS		:= -std=c++14 -Wall
CFLAGS		+= -g
#PANDOC		:= pandoc # For creating HTMl readme

ifneq ($(V),1)
Q = @
endif

all: $(TARGETS)

DEPS	:= $(patsubst %.o,%.d,$(OBJS))
-include $(DEPS)
DEPFLAGS = -MMD -MF $(@:.o=.d)

minHeapTest: $(OBJS)
	@echo "CC $@"
	$(Q)$(CC) $(CFLAGS) -o $@ $^ $(LIBS)

%.o: %.cpp
	@echo "CC $@"
	$(Q)$(CC) $(CFLAGS) -c -o $@ $< $(DEPFLAGS)

# For HTML readme
#%.html: %.md
	#@echo "MD $@"
	#(Q)$(PANDOC) -o $@ $<

clean:
	@echo "clean"
	$(Q)rm -f $(TARGETS) $(OBJS) $(DEPS)
