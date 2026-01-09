---
layout: container
name:  "quay.io/biocontainers/psipred"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/psipred/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/psipred/container.yaml"
updated_at: "2026-01-09 04:32:21.665166"
latest: "4.0--h7b50bb2_0"
container_url: "https://biocontainers.pro/tools/psipred"
aliases:
 - "chkparse"
 - "psipass2"
 - "psipred"
 - "runpsipred"
 - "runpsipred_single"
 - "runpsipredplus"
 - "seq2mtx"
 - "tcsh"
 - "asn1Coding"
 - "asn1Decoding"
 - "asn1Parser"
 - "p11-kit"
 - "p11tool"
 - "trust"
 - "certtool"
 - "gnutls-cli"
 - "gnutls-cli-debug"
 - "gnutls-serv"
 - "nettle-hash"
 - "nettle-lfib-stream"
 - "nettle-pbkdf2"
 - "ocsptool"
 - "pkcs1-conv"
 - "psktool"
 - "sexp-conv"
 - "bl2seq"
 - "blastall"
 - "blastclust"
 - "blastpgp"
 - "copymat"
 - "fastacmd"
 - "formatdb"
 - "formatrpsdb"
versions:
 - "4.0--h7b50bb2_0"
description: "singularity registry hpc automated addition for psipred"
config: {"url": "https://biocontainers.pro/tools/psipred", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for psipred", "latest": {"4.0--h7b50bb2_0": "sha256:bd1fdf9b51c353de2641347b1459cd8d18c2859061db056d04bcd53ba57cb8ec"}, "tags": {"4.0--h7b50bb2_0": "sha256:bd1fdf9b51c353de2641347b1459cd8d18c2859061db056d04bcd53ba57cb8ec"}, "docker": "quay.io/biocontainers/psipred", "aliases": {"chkparse": "/usr/local/bin/chkparse", "psipass2": "/usr/local/bin/psipass2", "psipred": "/usr/local/bin/psipred", "runpsipred": "/usr/local/bin/runpsipred", "runpsipred_single": "/usr/local/bin/runpsipred_single", "runpsipredplus": "/usr/local/bin/runpsipredplus", "seq2mtx": "/usr/local/bin/seq2mtx", "tcsh": "/usr/local/bin/tcsh", "asn1Coding": "/usr/local/bin/asn1Coding", "asn1Decoding": "/usr/local/bin/asn1Decoding", "asn1Parser": "/usr/local/bin/asn1Parser", "p11-kit": "/usr/local/bin/p11-kit", "p11tool": "/usr/local/bin/p11tool", "trust": "/usr/local/bin/trust", "certtool": "/usr/local/bin/certtool", "gnutls-cli": "/usr/local/bin/gnutls-cli", "gnutls-cli-debug": "/usr/local/bin/gnutls-cli-debug", "gnutls-serv": "/usr/local/bin/gnutls-serv", "nettle-hash": "/usr/local/bin/nettle-hash", "nettle-lfib-stream": "/usr/local/bin/nettle-lfib-stream", "nettle-pbkdf2": "/usr/local/bin/nettle-pbkdf2", "ocsptool": "/usr/local/bin/ocsptool", "pkcs1-conv": "/usr/local/bin/pkcs1-conv", "psktool": "/usr/local/bin/psktool", "sexp-conv": "/usr/local/bin/sexp-conv", "bl2seq": "/usr/local/bin/bl2seq", "blastall": "/usr/local/bin/blastall", "blastclust": "/usr/local/bin/blastclust", "blastpgp": "/usr/local/bin/blastpgp", "copymat": "/usr/local/bin/copymat", "fastacmd": "/usr/local/bin/fastacmd", "formatdb": "/usr/local/bin/formatdb", "formatrpsdb": "/usr/local/bin/formatrpsdb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/psipred.
singularity registry hpc automated addition for psipred
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/psipred
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/psipred:4.0--h7b50bb2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/psipred/4.0--h7b50bb2_0
$ module help quay.io/biocontainers/psipred/4.0--h7b50bb2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### psipred-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### psipred-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### psipred-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### psipred-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### psipred-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### psipred-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chkparse

```bash
$ singularity exec <container> /usr/local/bin/chkparse
$ podman run --it --rm --entrypoint /usr/local/bin/chkparse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chkparse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psipass2

```bash
$ singularity exec <container> /usr/local/bin/psipass2
$ podman run --it --rm --entrypoint /usr/local/bin/psipass2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psipass2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psipred

```bash
$ singularity exec <container> /usr/local/bin/psipred
$ podman run --it --rm --entrypoint /usr/local/bin/psipred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psipred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runpsipred

```bash
$ singularity exec <container> /usr/local/bin/runpsipred
$ podman run --it --rm --entrypoint /usr/local/bin/runpsipred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runpsipred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runpsipred_single

```bash
$ singularity exec <container> /usr/local/bin/runpsipred_single
$ podman run --it --rm --entrypoint /usr/local/bin/runpsipred_single   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runpsipred_single   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runpsipredplus

```bash
$ singularity exec <container> /usr/local/bin/runpsipredplus
$ podman run --it --rm --entrypoint /usr/local/bin/runpsipredplus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runpsipredplus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq2mtx

```bash
$ singularity exec <container> /usr/local/bin/seq2mtx
$ podman run --it --rm --entrypoint /usr/local/bin/seq2mtx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq2mtx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tcsh

```bash
$ singularity exec <container> /usr/local/bin/tcsh
$ podman run --it --rm --entrypoint /usr/local/bin/tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn1Coding

```bash
$ singularity exec <container> /usr/local/bin/asn1Coding
$ podman run --it --rm --entrypoint /usr/local/bin/asn1Coding   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn1Coding   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn1Decoding

```bash
$ singularity exec <container> /usr/local/bin/asn1Decoding
$ podman run --it --rm --entrypoint /usr/local/bin/asn1Decoding   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn1Decoding   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn1Parser

```bash
$ singularity exec <container> /usr/local/bin/asn1Parser
$ podman run --it --rm --entrypoint /usr/local/bin/asn1Parser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn1Parser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### p11-kit

```bash
$ singularity exec <container> /usr/local/bin/p11-kit
$ podman run --it --rm --entrypoint /usr/local/bin/p11-kit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/p11-kit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### p11tool

```bash
$ singularity exec <container> /usr/local/bin/p11tool
$ podman run --it --rm --entrypoint /usr/local/bin/p11tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/p11tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trust

```bash
$ singularity exec <container> /usr/local/bin/trust
$ podman run --it --rm --entrypoint /usr/local/bin/trust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trust   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### psktool

```bash
$ singularity exec <container> /usr/local/bin/psktool
$ podman run --it --rm --entrypoint /usr/local/bin/psktool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psktool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sexp-conv

```bash
$ singularity exec <container> /usr/local/bin/sexp-conv
$ podman run --it --rm --entrypoint /usr/local/bin/sexp-conv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sexp-conv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl2seq

```bash
$ singularity exec <container> /usr/local/bin/bl2seq
$ podman run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastall

```bash
$ singularity exec <container> /usr/local/bin/blastall
$ podman run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastclust

```bash
$ singularity exec <container> /usr/local/bin/blastclust
$ podman run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastpgp

```bash
$ singularity exec <container> /usr/local/bin/blastpgp
$ podman run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### copymat

```bash
$ singularity exec <container> /usr/local/bin/copymat
$ podman run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastacmd

```bash
$ singularity exec <container> /usr/local/bin/fastacmd
$ podman run --it --rm --entrypoint /usr/local/bin/fastacmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastacmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatdb

```bash
$ singularity exec <container> /usr/local/bin/formatdb
$ podman run --it --rm --entrypoint /usr/local/bin/formatdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatrpsdb

```bash
$ singularity exec <container> /usr/local/bin/formatrpsdb
$ podman run --it --rm --entrypoint /usr/local/bin/formatrpsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatrpsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
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