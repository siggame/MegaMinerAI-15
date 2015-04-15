DFILES=$(shell ls *.d 2> /dev/null)

all: ../library/client.a ../library/sexp/libclient_sexp.a client

submit: client
	@echo "$(shell cd ..;sh submit.sh c)"

client: $(DFILES) ../library/client.a ../library/sexp/libclient_sexp.a
	gdc $(DFILES) -lstdc++ ../library/client.a ../library/sexp/libclient_sexp.a -o run

../library/client.a:
	$(MAKE) -C $(dir $@) $(notdir $@)

../library/sexp/libclient_sexp.a:
	$(MAKE) -C $(dir $@) $(notdir $@)

clean:
	make -C library clean
