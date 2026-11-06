NAME          := gvm
SPEC_FILE     := gvm.spec

RPMTOPDIR     ?= $(HOME)/rpmbuild
SPECDIR       := $(RPMTOPDIR)/SPECS
SOURCEDIR     := $(RPMTOPDIR)/SOURCES

MOCKCONF_DIR  := $(CURDIR)/mock
RESULTDIR     := $(CURDIR)/results
GVM_REPO      := $(HOME)/src/gvm-repo
TEST_RELEASE  ?= 0.$(shell date +%s)

MOCK_TARGETS  := el10-x86_64 fc44-x86_64 fc45-x86_64

.PHONY: help prep clean $(addprefix build-,$(MOCK_TARGETS)) \
	build-el10 build-fc44 build-fc45

help:
	@echo "Local test builds (mock):"
	@for t in $(MOCK_TARGETS); do \
	  printf '  build-%s\n' "$$t"; \
	done

prep:
	mkdir -p "$(SPECDIR)" "$(SOURCEDIR)" "$(RPMTOPDIR)/BUILD" "$(RPMTOPDIR)/RPMS" "$(RPMTOPDIR)/SRPMS"
	cp $(SPEC_FILE) "$(SPECDIR)/"
	sed -i 's/^Release:[[:space:]]*RELEASE-AUTO/Release:        $(TEST_RELEASE)/' "$(SPECDIR)/$(SPEC_FILE)"
	tar -C src -czf "$(SOURCEDIR)/gvm.tar.gz" gvm

clean:
	rm -rf "$(RESULTDIR)"

define MOCK_build_template
build-$(1): prep
	mkdir -p "$(RESULTDIR)/$(1)" "$(GVM_REPO)/$(1)"
	mock --configdir="$(MOCKCONF_DIR)" -r $(1) \
		--spec "$(SPECDIR)/$(SPEC_FILE)" \
		--sources "$(SOURCEDIR)" \
		--resultdir="$(RESULTDIR)/$(1)" \
		--enable-network
	cp -a "$(RESULTDIR)/$(1)/"*.rpm "$(GVM_REPO)/$(1)/"
	createrepo_c "$(GVM_REPO)/$(1)"
endef

$(foreach t,$(MOCK_TARGETS),$(eval $(call MOCK_build_template,$(t))))

build-el10: build-el10-x86_64
build-fc44: build-fc44-x86_64
build-fc45: build-fc45-x86_64
