---
layout: container
name:  "quay.io/biocontainers/paraview"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/paraview/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/paraview/container.yaml"
updated_at: "2026-01-18 04:32:50.118532"
latest: "5.2.0--py27_2"
container_url: "https://biocontainers.pro/tools/paraview"
aliases:
 - "bugpoint"
 - "c-index-test"
 - "cftp"
 - "ckeygen"
 - "clang"
 - "clang++"
 - "clang-check"
 - "clang-format"
 - "clang-tblgen"
 - "conch"
 - "llc"
 - "lli"
 - "llvm-ar"
 - "llvm-as"
 - "llvm-bcanalyzer"
 - "llvm-config"
 - "llvm-cov"
 - "llvm-diff"
 - "llvm-dis"
 - "llvm-dwarfdump"
 - "llvm-extract"
 - "llvm-link"
 - "llvm-mc"
 - "llvm-mcmarkup"
 - "llvm-nm"
 - "llvm-objdump"
 - "llvm-prof"
 - "llvm-ranlib"
 - "llvm-readobj"
 - "llvm-rtdyld"
 - "llvm-size"
 - "llvm-stress"
 - "llvm-symbolizer"
 - "llvm-tblgen"
 - "macho-dump"
 - "mailmail"
 - "opt"
 - "paraview-config"
 - "pvbatch"
 - "pvdataserver"
 - "pvpython"
 - "pvrenderserver"
 - "pvserver"
 - "pyhtmlizer"
 - "tkconch"
 - "trial"
 - "twist"
 - "twistd"
 - "easy_install-2.7"
 - "protoc"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
 - "gif2h5"
 - "h52gif"
 - "h5c++"
versions:
 - "5.2.0--py27_2"
description: "shpc-registry automated BioContainers addition for paraview"
config: {"url": "https://biocontainers.pro/tools/paraview", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for paraview", "latest": {"5.2.0--py27_2": "sha256:07e78a38d3a7f23b82ecf1fa824a97d345e9d2b9334198a0b19bf57083bb0996"}, "tags": {"5.2.0--py27_2": "sha256:07e78a38d3a7f23b82ecf1fa824a97d345e9d2b9334198a0b19bf57083bb0996"}, "docker": "quay.io/biocontainers/paraview", "aliases": {"bugpoint": "/usr/local/bin/bugpoint", "c-index-test": "/usr/local/bin/c-index-test", "cftp": "/usr/local/bin/cftp", "ckeygen": "/usr/local/bin/ckeygen", "clang": "/usr/local/bin/clang", "clang++": "/usr/local/bin/clang++", "clang-check": "/usr/local/bin/clang-check", "clang-format": "/usr/local/bin/clang-format", "clang-tblgen": "/usr/local/bin/clang-tblgen", "conch": "/usr/local/bin/conch", "llc": "/usr/local/bin/llc", "lli": "/usr/local/bin/lli", "llvm-ar": "/usr/local/bin/llvm-ar", "llvm-as": "/usr/local/bin/llvm-as", "llvm-bcanalyzer": "/usr/local/bin/llvm-bcanalyzer", "llvm-config": "/usr/local/bin/llvm-config", "llvm-cov": "/usr/local/bin/llvm-cov", "llvm-diff": "/usr/local/bin/llvm-diff", "llvm-dis": "/usr/local/bin/llvm-dis", "llvm-dwarfdump": "/usr/local/bin/llvm-dwarfdump", "llvm-extract": "/usr/local/bin/llvm-extract", "llvm-link": "/usr/local/bin/llvm-link", "llvm-mc": "/usr/local/bin/llvm-mc", "llvm-mcmarkup": "/usr/local/bin/llvm-mcmarkup", "llvm-nm": "/usr/local/bin/llvm-nm", "llvm-objdump": "/usr/local/bin/llvm-objdump", "llvm-prof": "/usr/local/bin/llvm-prof", "llvm-ranlib": "/usr/local/bin/llvm-ranlib", "llvm-readobj": "/usr/local/bin/llvm-readobj", "llvm-rtdyld": "/usr/local/bin/llvm-rtdyld", "llvm-size": "/usr/local/bin/llvm-size", "llvm-stress": "/usr/local/bin/llvm-stress", "llvm-symbolizer": "/usr/local/bin/llvm-symbolizer", "llvm-tblgen": "/usr/local/bin/llvm-tblgen", "macho-dump": "/usr/local/bin/macho-dump", "mailmail": "/usr/local/bin/mailmail", "opt": "/usr/local/bin/opt", "paraview-config": "/usr/local/bin/paraview-config", "pvbatch": "/usr/local/bin/pvbatch", "pvdataserver": "/usr/local/bin/pvdataserver", "pvpython": "/usr/local/bin/pvpython", "pvrenderserver": "/usr/local/bin/pvrenderserver", "pvserver": "/usr/local/bin/pvserver", "pyhtmlizer": "/usr/local/bin/pyhtmlizer", "tkconch": "/usr/local/bin/tkconch", "trial": "/usr/local/bin/trial", "twist": "/usr/local/bin/twist", "twistd": "/usr/local/bin/twistd", "easy_install-2.7": "/usr/local/bin/easy_install-2.7", "protoc": "/usr/local/bin/protoc", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/paraview.
shpc-registry automated BioContainers addition for paraview
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/paraview
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/paraview:5.2.0--py27_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/paraview/5.2.0--py27_2
$ module help quay.io/biocontainers/paraview/5.2.0--py27_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### paraview-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### paraview-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### paraview-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### paraview-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### paraview-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### paraview-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bugpoint

```bash
$ singularity exec <container> /usr/local/bin/bugpoint
$ podman run --it --rm --entrypoint /usr/local/bin/bugpoint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bugpoint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c-index-test

```bash
$ singularity exec <container> /usr/local/bin/c-index-test
$ podman run --it --rm --entrypoint /usr/local/bin/c-index-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c-index-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cftp

```bash
$ singularity exec <container> /usr/local/bin/cftp
$ podman run --it --rm --entrypoint /usr/local/bin/cftp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cftp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ckeygen

```bash
$ singularity exec <container> /usr/local/bin/ckeygen
$ podman run --it --rm --entrypoint /usr/local/bin/ckeygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ckeygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang

```bash
$ singularity exec <container> /usr/local/bin/clang
$ podman run --it --rm --entrypoint /usr/local/bin/clang   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang++

```bash
$ singularity exec <container> /usr/local/bin/clang++
$ podman run --it --rm --entrypoint /usr/local/bin/clang++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-check

```bash
$ singularity exec <container> /usr/local/bin/clang-check
$ podman run --it --rm --entrypoint /usr/local/bin/clang-check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-format

```bash
$ singularity exec <container> /usr/local/bin/clang-format
$ podman run --it --rm --entrypoint /usr/local/bin/clang-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-tblgen

```bash
$ singularity exec <container> /usr/local/bin/clang-tblgen
$ podman run --it --rm --entrypoint /usr/local/bin/clang-tblgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-tblgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conch

```bash
$ singularity exec <container> /usr/local/bin/conch
$ podman run --it --rm --entrypoint /usr/local/bin/conch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llc

```bash
$ singularity exec <container> /usr/local/bin/llc
$ podman run --it --rm --entrypoint /usr/local/bin/llc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lli

```bash
$ singularity exec <container> /usr/local/bin/lli
$ podman run --it --rm --entrypoint /usr/local/bin/lli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-ar

```bash
$ singularity exec <container> /usr/local/bin/llvm-ar
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-ar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-ar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-as

```bash
$ singularity exec <container> /usr/local/bin/llvm-as
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-as   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-as   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-bcanalyzer

```bash
$ singularity exec <container> /usr/local/bin/llvm-bcanalyzer
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-bcanalyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-bcanalyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-config

```bash
$ singularity exec <container> /usr/local/bin/llvm-config
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-cov

```bash
$ singularity exec <container> /usr/local/bin/llvm-cov
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-cov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-cov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-diff

```bash
$ singularity exec <container> /usr/local/bin/llvm-diff
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-dis

```bash
$ singularity exec <container> /usr/local/bin/llvm-dis
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-dis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-dis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-dwarfdump

```bash
$ singularity exec <container> /usr/local/bin/llvm-dwarfdump
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-dwarfdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-dwarfdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-extract

```bash
$ singularity exec <container> /usr/local/bin/llvm-extract
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-link

```bash
$ singularity exec <container> /usr/local/bin/llvm-link
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-mc

```bash
$ singularity exec <container> /usr/local/bin/llvm-mc
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-mc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-mc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-mcmarkup

```bash
$ singularity exec <container> /usr/local/bin/llvm-mcmarkup
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-mcmarkup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-mcmarkup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-nm

```bash
$ singularity exec <container> /usr/local/bin/llvm-nm
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-nm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-nm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-objdump

```bash
$ singularity exec <container> /usr/local/bin/llvm-objdump
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-objdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-objdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-prof

```bash
$ singularity exec <container> /usr/local/bin/llvm-prof
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-prof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-prof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-ranlib

```bash
$ singularity exec <container> /usr/local/bin/llvm-ranlib
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-readobj

```bash
$ singularity exec <container> /usr/local/bin/llvm-readobj
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-readobj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-readobj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-rtdyld

```bash
$ singularity exec <container> /usr/local/bin/llvm-rtdyld
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-rtdyld   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-rtdyld   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-size

```bash
$ singularity exec <container> /usr/local/bin/llvm-size
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-size   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-size   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-stress

```bash
$ singularity exec <container> /usr/local/bin/llvm-stress
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-stress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-stress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-symbolizer

```bash
$ singularity exec <container> /usr/local/bin/llvm-symbolizer
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-symbolizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-symbolizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llvm-tblgen

```bash
$ singularity exec <container> /usr/local/bin/llvm-tblgen
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-tblgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-tblgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### macho-dump

```bash
$ singularity exec <container> /usr/local/bin/macho-dump
$ podman run --it --rm --entrypoint /usr/local/bin/macho-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/macho-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mailmail

```bash
$ singularity exec <container> /usr/local/bin/mailmail
$ podman run --it --rm --entrypoint /usr/local/bin/mailmail   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mailmail   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opt

```bash
$ singularity exec <container> /usr/local/bin/opt
$ podman run --it --rm --entrypoint /usr/local/bin/opt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paraview-config

```bash
$ singularity exec <container> /usr/local/bin/paraview-config
$ podman run --it --rm --entrypoint /usr/local/bin/paraview-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paraview-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pvbatch

```bash
$ singularity exec <container> /usr/local/bin/pvbatch
$ podman run --it --rm --entrypoint /usr/local/bin/pvbatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pvbatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pvdataserver

```bash
$ singularity exec <container> /usr/local/bin/pvdataserver
$ podman run --it --rm --entrypoint /usr/local/bin/pvdataserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pvdataserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pvpython

```bash
$ singularity exec <container> /usr/local/bin/pvpython
$ podman run --it --rm --entrypoint /usr/local/bin/pvpython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pvpython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pvrenderserver

```bash
$ singularity exec <container> /usr/local/bin/pvrenderserver
$ podman run --it --rm --entrypoint /usr/local/bin/pvrenderserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pvrenderserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pvserver

```bash
$ singularity exec <container> /usr/local/bin/pvserver
$ podman run --it --rm --entrypoint /usr/local/bin/pvserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pvserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyhtmlizer

```bash
$ singularity exec <container> /usr/local/bin/pyhtmlizer
$ podman run --it --rm --entrypoint /usr/local/bin/pyhtmlizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyhtmlizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tkconch

```bash
$ singularity exec <container> /usr/local/bin/tkconch
$ podman run --it --rm --entrypoint /usr/local/bin/tkconch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tkconch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trial

```bash
$ singularity exec <container> /usr/local/bin/trial
$ podman run --it --rm --entrypoint /usr/local/bin/trial   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trial   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twist

```bash
$ singularity exec <container> /usr/local/bin/twist
$ podman run --it --rm --entrypoint /usr/local/bin/twist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twistd

```bash
$ singularity exec <container> /usr/local/bin/twistd
$ podman run --it --rm --entrypoint /usr/local/bin/twistd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twistd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-2.7

```bash
$ singularity exec <container> /usr/local/bin/easy_install-2.7
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc

```bash
$ singularity exec <container> /usr/local/bin/protoc
$ podman run --it --rm --entrypoint /usr/local/bin/protoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h52gif

```bash
$ singularity exec <container> /usr/local/bin/h52gif
$ podman run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5c++

```bash
$ singularity exec <container> /usr/local/bin/h5c++
$ podman run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
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