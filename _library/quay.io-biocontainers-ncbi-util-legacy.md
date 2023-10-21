---
layout: container
name:  "quay.io/biocontainers/ncbi-util-legacy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ncbi-util-legacy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ncbi-util-legacy/container.yaml"
updated_at: "2023-10-21 02:36:03.668438"
latest: "6.1--h0e27e84_3"
container_url: "https://biocontainers.pro/tools/ncbi-util-legacy"
aliases:
 - "Nentrez"
 - "Psequin"
 - "asn2ff"
 - "asn2gb"
 - "asn2idx"
 - "asndhuff"
 - "asntool"
 - "blastcl3"
 - "cdscan"
 - "checksub"
 - "ddv"
 - "debruijn"
 - "demo_regexp"
 - "demo_regexp_grep"
 - "dosimple"
 - "entrcmd"
 - "entrez2"
 - "errhdr"
 - "fa2htgs"
 - "findspl"
 - "gene2xml"
 - "getmesh"
 - "getpub"
 - "gil2bin"
 - "idfetch"
 - "indexpub"
 - "makeset"
 - "mwm"
 - "ncbisort"
 - "sbtedit"
 - "seqtest"
 - "tcsh"
 - "test_regexp"
 - "testcore"
 - "testobj"
 - "testval"
 - "udv"
 - "uil"
 - "vecscreen"
 - "xmbind"
 - "tbl2asn"
 - "certtool"
 - "gnutls-cli"
 - "gnutls-cli-debug"
 - "gnutls-serv"
 - "nettle-hash"
 - "nettle-lfib-stream"
 - "nettle-pbkdf2"
 - "ocsptool"
 - "pkcs1-conv"
versions:
 - "6.1--h0e27e84_3"
description: "shpc-registry automated BioContainers addition for ncbi-util-legacy"
config: {"url": "https://biocontainers.pro/tools/ncbi-util-legacy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ncbi-util-legacy", "latest": {"6.1--h0e27e84_3": "sha256:a5ccabe573691d689e165ff30e999de79bf58653097c19bcaf83540f3efbcf0b"}, "tags": {"6.1--h0e27e84_3": "sha256:a5ccabe573691d689e165ff30e999de79bf58653097c19bcaf83540f3efbcf0b"}, "docker": "quay.io/biocontainers/ncbi-util-legacy", "aliases": {"Nentrez": "/usr/local/bin/Nentrez", "Psequin": "/usr/local/bin/Psequin", "asn2ff": "/usr/local/bin/asn2ff", "asn2gb": "/usr/local/bin/asn2gb", "asn2idx": "/usr/local/bin/asn2idx", "asndhuff": "/usr/local/bin/asndhuff", "asntool": "/usr/local/bin/asntool", "blastcl3": "/usr/local/bin/blastcl3", "cdscan": "/usr/local/bin/cdscan", "checksub": "/usr/local/bin/checksub", "ddv": "/usr/local/bin/ddv", "debruijn": "/usr/local/bin/debruijn", "demo_regexp": "/usr/local/bin/demo_regexp", "demo_regexp_grep": "/usr/local/bin/demo_regexp_grep", "dosimple": "/usr/local/bin/dosimple", "entrcmd": "/usr/local/bin/entrcmd", "entrez2": "/usr/local/bin/entrez2", "errhdr": "/usr/local/bin/errhdr", "fa2htgs": "/usr/local/bin/fa2htgs", "findspl": "/usr/local/bin/findspl", "gene2xml": "/usr/local/bin/gene2xml", "getmesh": "/usr/local/bin/getmesh", "getpub": "/usr/local/bin/getpub", "gil2bin": "/usr/local/bin/gil2bin", "idfetch": "/usr/local/bin/idfetch", "indexpub": "/usr/local/bin/indexpub", "makeset": "/usr/local/bin/makeset", "mwm": "/usr/local/bin/mwm", "ncbisort": "/usr/local/bin/ncbisort", "sbtedit": "/usr/local/bin/sbtedit", "seqtest": "/usr/local/bin/seqtest", "tcsh": "/usr/local/bin/tcsh", "test_regexp": "/usr/local/bin/test_regexp", "testcore": "/usr/local/bin/testcore", "testobj": "/usr/local/bin/testobj", "testval": "/usr/local/bin/testval", "udv": "/usr/local/bin/udv", "uil": "/usr/local/bin/uil", "vecscreen": "/usr/local/bin/vecscreen", "xmbind": "/usr/local/bin/xmbind", "tbl2asn": "/usr/local/bin/tbl2asn", "certtool": "/usr/local/bin/certtool", "gnutls-cli": "/usr/local/bin/gnutls-cli", "gnutls-cli-debug": "/usr/local/bin/gnutls-cli-debug", "gnutls-serv": "/usr/local/bin/gnutls-serv", "nettle-hash": "/usr/local/bin/nettle-hash", "nettle-lfib-stream": "/usr/local/bin/nettle-lfib-stream", "nettle-pbkdf2": "/usr/local/bin/nettle-pbkdf2", "ocsptool": "/usr/local/bin/ocsptool", "pkcs1-conv": "/usr/local/bin/pkcs1-conv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ncbi-util-legacy.
shpc-registry automated BioContainers addition for ncbi-util-legacy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ncbi-util-legacy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ncbi-util-legacy:6.1--h0e27e84_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ncbi-util-legacy/6.1--h0e27e84_3
$ module help quay.io/biocontainers/ncbi-util-legacy/6.1--h0e27e84_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ncbi-util-legacy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ncbi-util-legacy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ncbi-util-legacy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ncbi-util-legacy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ncbi-util-legacy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ncbi-util-legacy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Nentrez

```bash
$ singularity exec <container> /usr/local/bin/Nentrez
$ podman run --it --rm --entrypoint /usr/local/bin/Nentrez   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Nentrez   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Psequin

```bash
$ singularity exec <container> /usr/local/bin/Psequin
$ podman run --it --rm --entrypoint /usr/local/bin/Psequin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Psequin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn2ff

```bash
$ singularity exec <container> /usr/local/bin/asn2ff
$ podman run --it --rm --entrypoint /usr/local/bin/asn2ff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn2ff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn2gb

```bash
$ singularity exec <container> /usr/local/bin/asn2gb
$ podman run --it --rm --entrypoint /usr/local/bin/asn2gb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn2gb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn2idx

```bash
$ singularity exec <container> /usr/local/bin/asn2idx
$ podman run --it --rm --entrypoint /usr/local/bin/asn2idx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn2idx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asndhuff

```bash
$ singularity exec <container> /usr/local/bin/asndhuff
$ podman run --it --rm --entrypoint /usr/local/bin/asndhuff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asndhuff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asntool

```bash
$ singularity exec <container> /usr/local/bin/asntool
$ podman run --it --rm --entrypoint /usr/local/bin/asntool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asntool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastcl3

```bash
$ singularity exec <container> /usr/local/bin/blastcl3
$ podman run --it --rm --entrypoint /usr/local/bin/blastcl3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastcl3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cdscan

```bash
$ singularity exec <container> /usr/local/bin/cdscan
$ podman run --it --rm --entrypoint /usr/local/bin/cdscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cdscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checksub

```bash
$ singularity exec <container> /usr/local/bin/checksub
$ podman run --it --rm --entrypoint /usr/local/bin/checksub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checksub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ddv

```bash
$ singularity exec <container> /usr/local/bin/ddv
$ podman run --it --rm --entrypoint /usr/local/bin/ddv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ddv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debruijn

```bash
$ singularity exec <container> /usr/local/bin/debruijn
$ podman run --it --rm --entrypoint /usr/local/bin/debruijn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debruijn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### demo_regexp

```bash
$ singularity exec <container> /usr/local/bin/demo_regexp
$ podman run --it --rm --entrypoint /usr/local/bin/demo_regexp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demo_regexp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### demo_regexp_grep

```bash
$ singularity exec <container> /usr/local/bin/demo_regexp_grep
$ podman run --it --rm --entrypoint /usr/local/bin/demo_regexp_grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demo_regexp_grep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dosimple

```bash
$ singularity exec <container> /usr/local/bin/dosimple
$ podman run --it --rm --entrypoint /usr/local/bin/dosimple   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dosimple   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### entrcmd

```bash
$ singularity exec <container> /usr/local/bin/entrcmd
$ podman run --it --rm --entrypoint /usr/local/bin/entrcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/entrcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### entrez2

```bash
$ singularity exec <container> /usr/local/bin/entrez2
$ podman run --it --rm --entrypoint /usr/local/bin/entrez2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/entrez2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### errhdr

```bash
$ singularity exec <container> /usr/local/bin/errhdr
$ podman run --it --rm --entrypoint /usr/local/bin/errhdr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/errhdr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fa2htgs

```bash
$ singularity exec <container> /usr/local/bin/fa2htgs
$ podman run --it --rm --entrypoint /usr/local/bin/fa2htgs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fa2htgs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findspl

```bash
$ singularity exec <container> /usr/local/bin/findspl
$ podman run --it --rm --entrypoint /usr/local/bin/findspl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findspl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene2xml

```bash
$ singularity exec <container> /usr/local/bin/gene2xml
$ podman run --it --rm --entrypoint /usr/local/bin/gene2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getmesh

```bash
$ singularity exec <container> /usr/local/bin/getmesh
$ podman run --it --rm --entrypoint /usr/local/bin/getmesh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getmesh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getpub

```bash
$ singularity exec <container> /usr/local/bin/getpub
$ podman run --it --rm --entrypoint /usr/local/bin/getpub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getpub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gil2bin

```bash
$ singularity exec <container> /usr/local/bin/gil2bin
$ podman run --it --rm --entrypoint /usr/local/bin/gil2bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gil2bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idfetch

```bash
$ singularity exec <container> /usr/local/bin/idfetch
$ podman run --it --rm --entrypoint /usr/local/bin/idfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indexpub

```bash
$ singularity exec <container> /usr/local/bin/indexpub
$ podman run --it --rm --entrypoint /usr/local/bin/indexpub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexpub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeset

```bash
$ singularity exec <container> /usr/local/bin/makeset
$ podman run --it --rm --entrypoint /usr/local/bin/makeset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mwm

```bash
$ singularity exec <container> /usr/local/bin/mwm
$ podman run --it --rm --entrypoint /usr/local/bin/mwm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mwm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbisort

```bash
$ singularity exec <container> /usr/local/bin/ncbisort
$ podman run --it --rm --entrypoint /usr/local/bin/ncbisort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncbisort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sbtedit

```bash
$ singularity exec <container> /usr/local/bin/sbtedit
$ podman run --it --rm --entrypoint /usr/local/bin/sbtedit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sbtedit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqtest

```bash
$ singularity exec <container> /usr/local/bin/seqtest
$ podman run --it --rm --entrypoint /usr/local/bin/seqtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqtest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tcsh

```bash
$ singularity exec <container> /usr/local/bin/tcsh
$ podman run --it --rm --entrypoint /usr/local/bin/tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_regexp

```bash
$ singularity exec <container> /usr/local/bin/test_regexp
$ podman run --it --rm --entrypoint /usr/local/bin/test_regexp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_regexp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testcore

```bash
$ singularity exec <container> /usr/local/bin/testcore
$ podman run --it --rm --entrypoint /usr/local/bin/testcore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testcore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testobj

```bash
$ singularity exec <container> /usr/local/bin/testobj
$ podman run --it --rm --entrypoint /usr/local/bin/testobj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testobj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testval

```bash
$ singularity exec <container> /usr/local/bin/testval
$ podman run --it --rm --entrypoint /usr/local/bin/testval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### udv

```bash
$ singularity exec <container> /usr/local/bin/udv
$ podman run --it --rm --entrypoint /usr/local/bin/udv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/udv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uil

```bash
$ singularity exec <container> /usr/local/bin/uil
$ podman run --it --rm --entrypoint /usr/local/bin/uil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vecscreen

```bash
$ singularity exec <container> /usr/local/bin/vecscreen
$ podman run --it --rm --entrypoint /usr/local/bin/vecscreen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vecscreen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xmbind

```bash
$ singularity exec <container> /usr/local/bin/xmbind
$ podman run --it --rm --entrypoint /usr/local/bin/xmbind   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmbind   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2asn

```bash
$ singularity exec <container> /usr/local/bin/tbl2asn
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certtool

```bash
$ singularity exec <container> /usr/local/bin/certtool
$ podman run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnutls-cli

```bash
$ singularity exec <container> /usr/local/bin/gnutls-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gnutls-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnutls-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnutls-cli-debug

```bash
$ singularity exec <container> /usr/local/bin/gnutls-cli-debug
$ podman run --it --rm --entrypoint /usr/local/bin/gnutls-cli-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnutls-cli-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnutls-serv

```bash
$ singularity exec <container> /usr/local/bin/gnutls-serv
$ podman run --it --rm --entrypoint /usr/local/bin/gnutls-serv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnutls-serv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nettle-hash

```bash
$ singularity exec <container> /usr/local/bin/nettle-hash
$ podman run --it --rm --entrypoint /usr/local/bin/nettle-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nettle-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nettle-lfib-stream

```bash
$ singularity exec <container> /usr/local/bin/nettle-lfib-stream
$ podman run --it --rm --entrypoint /usr/local/bin/nettle-lfib-stream   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nettle-lfib-stream   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nettle-pbkdf2

```bash
$ singularity exec <container> /usr/local/bin/nettle-pbkdf2
$ podman run --it --rm --entrypoint /usr/local/bin/nettle-pbkdf2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nettle-pbkdf2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocsptool

```bash
$ singularity exec <container> /usr/local/bin/ocsptool
$ podman run --it --rm --entrypoint /usr/local/bin/ocsptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocsptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pkcs1-conv

```bash
$ singularity exec <container> /usr/local/bin/pkcs1-conv
$ podman run --it --rm --entrypoint /usr/local/bin/pkcs1-conv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pkcs1-conv   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)