---
layout: container
name:  "quay.io/biocontainers/coot-headless"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/coot-headless/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/coot-headless/container.yaml"
updated_at: "2025-10-23 03:34:12.907613"
latest: "1.1.18--py312h7c3e029_1"
container_url: "https://biocontainers.pro/tools/coot-headless"
aliases:
 - "debuginfod"
 - "debuginfod-find"
 - "eu-addr2line"
 - "eu-ar"
 - "eu-elfclassify"
 - "eu-elfcmp"
 - "eu-elfcompress"
 - "eu-elflint"
 - "eu-findtextrel"
 - "eu-make-debug-archive"
 - "eu-nm"
 - "eu-objdump"
 - "eu-ranlib"
 - "eu-readelf"
 - "eu-size"
 - "eu-srcfiles"
 - "eu-stack"
 - "eu-strings"
 - "eu-strip"
 - "eu-unstrip"
 - "gemmi"
 - "asn1Coding"
 - "asn1Decoding"
 - "asn1Parser"
 - "p11-kit"
 - "p11tool"
 - "trust"
 - "ldapadd"
 - "ldapcompare"
 - "ldapdelete"
 - "ldapexop"
 - "ldapmodify"
 - "ldapmodrdn"
 - "ldappasswd"
 - "ldapsearch"
 - "ldapurl"
 - "ldapvc"
 - "ldapwhoami"
 - "bsdunzip"
 - "certtool"
 - "gnutls-cli"
 - "gnutls-cli-debug"
 - "gnutls-serv"
 - "nettle-hash"
 - "nettle-lfib-stream"
 - "nettle-pbkdf2"
versions:
 - "1.1.17--py310h5b8adf8_0"
 - "1.1.17--py311he85460a_2"
 - "1.1.18--py39h0a7431f_0"
 - "1.1.18--py312h7c3e029_1"
description: "singularity registry hpc automated addition for coot-headless"
config: {"url": "https://biocontainers.pro/tools/coot-headless", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for coot-headless", "latest": {"1.1.18--py312h7c3e029_1": "sha256:63a574fefe7b97633d246556372b9de3a1218640ac2f663843cc6b0026b1acde"}, "tags": {"1.1.17--py310h5b8adf8_0": "sha256:9016d29c37cf7c494b1e636cfd45a90d3463f4df13be3efdd7e19127bbdf1aee", "1.1.17--py311he85460a_2": "sha256:14ba5a89b9888e5066dd30d4714343d976308572e8216d2fb6c007602619edb8", "1.1.18--py39h0a7431f_0": "sha256:8f3f49fee062a3f94d576c3b125a15b904b776afee54c0d99a0a42ffd5305710", "1.1.18--py312h7c3e029_1": "sha256:63a574fefe7b97633d246556372b9de3a1218640ac2f663843cc6b0026b1acde"}, "docker": "quay.io/biocontainers/coot-headless", "aliases": {"debuginfod": "/usr/local/bin/debuginfod", "debuginfod-find": "/usr/local/bin/debuginfod-find", "eu-addr2line": "/usr/local/bin/eu-addr2line", "eu-ar": "/usr/local/bin/eu-ar", "eu-elfclassify": "/usr/local/bin/eu-elfclassify", "eu-elfcmp": "/usr/local/bin/eu-elfcmp", "eu-elfcompress": "/usr/local/bin/eu-elfcompress", "eu-elflint": "/usr/local/bin/eu-elflint", "eu-findtextrel": "/usr/local/bin/eu-findtextrel", "eu-make-debug-archive": "/usr/local/bin/eu-make-debug-archive", "eu-nm": "/usr/local/bin/eu-nm", "eu-objdump": "/usr/local/bin/eu-objdump", "eu-ranlib": "/usr/local/bin/eu-ranlib", "eu-readelf": "/usr/local/bin/eu-readelf", "eu-size": "/usr/local/bin/eu-size", "eu-srcfiles": "/usr/local/bin/eu-srcfiles", "eu-stack": "/usr/local/bin/eu-stack", "eu-strings": "/usr/local/bin/eu-strings", "eu-strip": "/usr/local/bin/eu-strip", "eu-unstrip": "/usr/local/bin/eu-unstrip", "gemmi": "/usr/local/bin/gemmi", "asn1Coding": "/usr/local/bin/asn1Coding", "asn1Decoding": "/usr/local/bin/asn1Decoding", "asn1Parser": "/usr/local/bin/asn1Parser", "p11-kit": "/usr/local/bin/p11-kit", "p11tool": "/usr/local/bin/p11tool", "trust": "/usr/local/bin/trust", "ldapadd": "/usr/local/bin/ldapadd", "ldapcompare": "/usr/local/bin/ldapcompare", "ldapdelete": "/usr/local/bin/ldapdelete", "ldapexop": "/usr/local/bin/ldapexop", "ldapmodify": "/usr/local/bin/ldapmodify", "ldapmodrdn": "/usr/local/bin/ldapmodrdn", "ldappasswd": "/usr/local/bin/ldappasswd", "ldapsearch": "/usr/local/bin/ldapsearch", "ldapurl": "/usr/local/bin/ldapurl", "ldapvc": "/usr/local/bin/ldapvc", "ldapwhoami": "/usr/local/bin/ldapwhoami", "bsdunzip": "/usr/local/bin/bsdunzip", "certtool": "/usr/local/bin/certtool", "gnutls-cli": "/usr/local/bin/gnutls-cli", "gnutls-cli-debug": "/usr/local/bin/gnutls-cli-debug", "gnutls-serv": "/usr/local/bin/gnutls-serv", "nettle-hash": "/usr/local/bin/nettle-hash", "nettle-lfib-stream": "/usr/local/bin/nettle-lfib-stream", "nettle-pbkdf2": "/usr/local/bin/nettle-pbkdf2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/coot-headless.
singularity registry hpc automated addition for coot-headless
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/coot-headless
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/coot-headless:1.1.18--py312h7c3e029_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/coot-headless/1.1.18--py312h7c3e029_1
$ module help quay.io/biocontainers/coot-headless/1.1.18--py312h7c3e029_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### coot-headless-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### coot-headless-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### coot-headless-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### coot-headless-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### coot-headless-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### coot-headless-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### debuginfod

```bash
$ singularity exec <container> /usr/local/bin/debuginfod
$ podman run --it --rm --entrypoint /usr/local/bin/debuginfod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debuginfod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debuginfod-find

```bash
$ singularity exec <container> /usr/local/bin/debuginfod-find
$ podman run --it --rm --entrypoint /usr/local/bin/debuginfod-find   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debuginfod-find   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-addr2line

```bash
$ singularity exec <container> /usr/local/bin/eu-addr2line
$ podman run --it --rm --entrypoint /usr/local/bin/eu-addr2line   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-addr2line   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-ar

```bash
$ singularity exec <container> /usr/local/bin/eu-ar
$ podman run --it --rm --entrypoint /usr/local/bin/eu-ar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-ar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-elfclassify

```bash
$ singularity exec <container> /usr/local/bin/eu-elfclassify
$ podman run --it --rm --entrypoint /usr/local/bin/eu-elfclassify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-elfclassify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-elfcmp

```bash
$ singularity exec <container> /usr/local/bin/eu-elfcmp
$ podman run --it --rm --entrypoint /usr/local/bin/eu-elfcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-elfcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-elfcompress

```bash
$ singularity exec <container> /usr/local/bin/eu-elfcompress
$ podman run --it --rm --entrypoint /usr/local/bin/eu-elfcompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-elfcompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-elflint

```bash
$ singularity exec <container> /usr/local/bin/eu-elflint
$ podman run --it --rm --entrypoint /usr/local/bin/eu-elflint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-elflint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-findtextrel

```bash
$ singularity exec <container> /usr/local/bin/eu-findtextrel
$ podman run --it --rm --entrypoint /usr/local/bin/eu-findtextrel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-findtextrel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-make-debug-archive

```bash
$ singularity exec <container> /usr/local/bin/eu-make-debug-archive
$ podman run --it --rm --entrypoint /usr/local/bin/eu-make-debug-archive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-make-debug-archive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-nm

```bash
$ singularity exec <container> /usr/local/bin/eu-nm
$ podman run --it --rm --entrypoint /usr/local/bin/eu-nm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-nm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-objdump

```bash
$ singularity exec <container> /usr/local/bin/eu-objdump
$ podman run --it --rm --entrypoint /usr/local/bin/eu-objdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-objdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-ranlib

```bash
$ singularity exec <container> /usr/local/bin/eu-ranlib
$ podman run --it --rm --entrypoint /usr/local/bin/eu-ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-readelf

```bash
$ singularity exec <container> /usr/local/bin/eu-readelf
$ podman run --it --rm --entrypoint /usr/local/bin/eu-readelf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-readelf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-size

```bash
$ singularity exec <container> /usr/local/bin/eu-size
$ podman run --it --rm --entrypoint /usr/local/bin/eu-size   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-size   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-srcfiles

```bash
$ singularity exec <container> /usr/local/bin/eu-srcfiles
$ podman run --it --rm --entrypoint /usr/local/bin/eu-srcfiles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-srcfiles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-stack

```bash
$ singularity exec <container> /usr/local/bin/eu-stack
$ podman run --it --rm --entrypoint /usr/local/bin/eu-stack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-stack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-strings

```bash
$ singularity exec <container> /usr/local/bin/eu-strings
$ podman run --it --rm --entrypoint /usr/local/bin/eu-strings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-strings   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-strip

```bash
$ singularity exec <container> /usr/local/bin/eu-strip
$ podman run --it --rm --entrypoint /usr/local/bin/eu-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-unstrip

```bash
$ singularity exec <container> /usr/local/bin/eu-unstrip
$ podman run --it --rm --entrypoint /usr/local/bin/eu-unstrip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-unstrip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gemmi

```bash
$ singularity exec <container> /usr/local/bin/gemmi
$ podman run --it --rm --entrypoint /usr/local/bin/gemmi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gemmi   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ldapadd

```bash
$ singularity exec <container> /usr/local/bin/ldapadd
$ podman run --it --rm --entrypoint /usr/local/bin/ldapadd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapadd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapcompare

```bash
$ singularity exec <container> /usr/local/bin/ldapcompare
$ podman run --it --rm --entrypoint /usr/local/bin/ldapcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapdelete

```bash
$ singularity exec <container> /usr/local/bin/ldapdelete
$ podman run --it --rm --entrypoint /usr/local/bin/ldapdelete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapdelete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapexop

```bash
$ singularity exec <container> /usr/local/bin/ldapexop
$ podman run --it --rm --entrypoint /usr/local/bin/ldapexop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapexop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapmodify

```bash
$ singularity exec <container> /usr/local/bin/ldapmodify
$ podman run --it --rm --entrypoint /usr/local/bin/ldapmodify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapmodify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapmodrdn

```bash
$ singularity exec <container> /usr/local/bin/ldapmodrdn
$ podman run --it --rm --entrypoint /usr/local/bin/ldapmodrdn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapmodrdn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldappasswd

```bash
$ singularity exec <container> /usr/local/bin/ldappasswd
$ podman run --it --rm --entrypoint /usr/local/bin/ldappasswd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldappasswd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapsearch

```bash
$ singularity exec <container> /usr/local/bin/ldapsearch
$ podman run --it --rm --entrypoint /usr/local/bin/ldapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapurl

```bash
$ singularity exec <container> /usr/local/bin/ldapurl
$ podman run --it --rm --entrypoint /usr/local/bin/ldapurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapurl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapvc

```bash
$ singularity exec <container> /usr/local/bin/ldapvc
$ podman run --it --rm --entrypoint /usr/local/bin/ldapvc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapvc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapwhoami

```bash
$ singularity exec <container> /usr/local/bin/ldapwhoami
$ podman run --it --rm --entrypoint /usr/local/bin/ldapwhoami   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapwhoami   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdunzip

```bash
$ singularity exec <container> /usr/local/bin/bsdunzip
$ podman run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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