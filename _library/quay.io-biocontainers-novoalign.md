---
layout: container
name:  "quay.io/biocontainers/novoalign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/novoalign/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/novoalign/container.yaml"
updated_at: "2023-09-01 02:56:40.284526"
latest: "4.03.04--h43eeafb_3"
container_url: "https://biocontainers.pro/tools/novoalign"
aliases:
 - "IONTorrent.R"
 - "installpackages.R"
 - "irqtop"
 - "isnovoindex"
 - "lsirq"
 - "novo2maq"
 - "novo2paf"
 - "novoalign"
 - "novoalign-license-register"
 - "novoalignMPI"
 - "novobarcode"
 - "novoindex"
 - "novolrcleaver"
 - "novolrcorrector"
 - "novolrpolish"
 - "novomethyl"
 - "novope2bed.pl"
 - "novorun.pl"
 - "novosort"
 - "novoutil"
 - "nsenter"
 - "prlimit"
 - "qcalplot.R"
 - "rrbsreference"
 - "scriptlive"
 - "cal"
 - "chmem"
 - "choom"
 - "chrt"
 - "col"
 - "colcrt"
 - "colrm"
 - "column"
 - "dmesg"
 - "eject"
versions:
 - "4.03.04--h5b5514e_1"
 - "4.03.04--h43eeafb_3"
description: "shpc-registry automated BioContainers addition for novoalign"
config: {"url": "https://biocontainers.pro/tools/novoalign", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for novoalign", "latest": {"4.03.04--h43eeafb_3": "sha256:975866a89e6ab0c3ba5a222e4455d0a5c9b5966185eb0040a3af7b1a1f2510b5"}, "tags": {"4.03.04--h5b5514e_1": "sha256:2bb7ac3cb85142370801a9c6db466b23d820fe1777b6e5a9d54e2cfdfea1c0ed", "4.03.04--h43eeafb_3": "sha256:975866a89e6ab0c3ba5a222e4455d0a5c9b5966185eb0040a3af7b1a1f2510b5"}, "docker": "quay.io/biocontainers/novoalign", "aliases": {"IONTorrent.R": "/usr/local/bin/IONTorrent.R", "installpackages.R": "/usr/local/bin/installpackages.R", "irqtop": "/usr/local/bin/irqtop", "isnovoindex": "/usr/local/bin/isnovoindex", "lsirq": "/usr/local/bin/lsirq", "novo2maq": "/usr/local/bin/novo2maq", "novo2paf": "/usr/local/bin/novo2paf", "novoalign": "/usr/local/bin/novoalign", "novoalign-license-register": "/usr/local/bin/novoalign-license-register", "novoalignMPI": "/usr/local/bin/novoalignMPI", "novobarcode": "/usr/local/bin/novobarcode", "novoindex": "/usr/local/bin/novoindex", "novolrcleaver": "/usr/local/bin/novolrcleaver", "novolrcorrector": "/usr/local/bin/novolrcorrector", "novolrpolish": "/usr/local/bin/novolrpolish", "novomethyl": "/usr/local/bin/novomethyl", "novope2bed.pl": "/usr/local/bin/novope2bed.pl", "novorun.pl": "/usr/local/bin/novorun.pl", "novosort": "/usr/local/bin/novosort", "novoutil": "/usr/local/bin/novoutil", "nsenter": "/usr/local/bin/nsenter", "prlimit": "/usr/local/bin/prlimit", "qcalplot.R": "/usr/local/bin/qcalplot.R", "rrbsreference": "/usr/local/bin/rrbsreference", "scriptlive": "/usr/local/bin/scriptlive", "cal": "/usr/local/bin/cal", "chmem": "/usr/local/bin/chmem", "choom": "/usr/local/bin/choom", "chrt": "/usr/local/bin/chrt", "col": "/usr/local/bin/col", "colcrt": "/usr/local/bin/colcrt", "colrm": "/usr/local/bin/colrm", "column": "/usr/local/bin/column", "dmesg": "/usr/local/bin/dmesg", "eject": "/usr/local/bin/eject"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/novoalign.
shpc-registry automated BioContainers addition for novoalign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/novoalign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/novoalign:4.03.04--h43eeafb_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/novoalign/4.03.04--h43eeafb_3
$ module help quay.io/biocontainers/novoalign/4.03.04--h43eeafb_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### novoalign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### novoalign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### novoalign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### novoalign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### novoalign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### novoalign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### IONTorrent.R

```bash
$ singularity exec <container> /usr/local/bin/IONTorrent.R
$ podman run --it --rm --entrypoint /usr/local/bin/IONTorrent.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IONTorrent.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### installpackages.R

```bash
$ singularity exec <container> /usr/local/bin/installpackages.R
$ podman run --it --rm --entrypoint /usr/local/bin/installpackages.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/installpackages.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irqtop

```bash
$ singularity exec <container> /usr/local/bin/irqtop
$ podman run --it --rm --entrypoint /usr/local/bin/irqtop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irqtop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isnovoindex

```bash
$ singularity exec <container> /usr/local/bin/isnovoindex
$ podman run --it --rm --entrypoint /usr/local/bin/isnovoindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isnovoindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lsirq

```bash
$ singularity exec <container> /usr/local/bin/lsirq
$ podman run --it --rm --entrypoint /usr/local/bin/lsirq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lsirq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novo2maq

```bash
$ singularity exec <container> /usr/local/bin/novo2maq
$ podman run --it --rm --entrypoint /usr/local/bin/novo2maq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novo2maq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novo2paf

```bash
$ singularity exec <container> /usr/local/bin/novo2paf
$ podman run --it --rm --entrypoint /usr/local/bin/novo2paf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novo2paf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novoalign

```bash
$ singularity exec <container> /usr/local/bin/novoalign
$ podman run --it --rm --entrypoint /usr/local/bin/novoalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novoalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novoalign-license-register

```bash
$ singularity exec <container> /usr/local/bin/novoalign-license-register
$ podman run --it --rm --entrypoint /usr/local/bin/novoalign-license-register   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novoalign-license-register   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novoalignMPI

```bash
$ singularity exec <container> /usr/local/bin/novoalignMPI
$ podman run --it --rm --entrypoint /usr/local/bin/novoalignMPI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novoalignMPI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novobarcode

```bash
$ singularity exec <container> /usr/local/bin/novobarcode
$ podman run --it --rm --entrypoint /usr/local/bin/novobarcode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novobarcode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novoindex

```bash
$ singularity exec <container> /usr/local/bin/novoindex
$ podman run --it --rm --entrypoint /usr/local/bin/novoindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novoindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novolrcleaver

```bash
$ singularity exec <container> /usr/local/bin/novolrcleaver
$ podman run --it --rm --entrypoint /usr/local/bin/novolrcleaver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novolrcleaver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novolrcorrector

```bash
$ singularity exec <container> /usr/local/bin/novolrcorrector
$ podman run --it --rm --entrypoint /usr/local/bin/novolrcorrector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novolrcorrector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novolrpolish

```bash
$ singularity exec <container> /usr/local/bin/novolrpolish
$ podman run --it --rm --entrypoint /usr/local/bin/novolrpolish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novolrpolish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novomethyl

```bash
$ singularity exec <container> /usr/local/bin/novomethyl
$ podman run --it --rm --entrypoint /usr/local/bin/novomethyl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novomethyl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novope2bed.pl

```bash
$ singularity exec <container> /usr/local/bin/novope2bed.pl
$ podman run --it --rm --entrypoint /usr/local/bin/novope2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novope2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novorun.pl

```bash
$ singularity exec <container> /usr/local/bin/novorun.pl
$ podman run --it --rm --entrypoint /usr/local/bin/novorun.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novorun.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novosort

```bash
$ singularity exec <container> /usr/local/bin/novosort
$ podman run --it --rm --entrypoint /usr/local/bin/novosort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novosort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novoutil

```bash
$ singularity exec <container> /usr/local/bin/novoutil
$ podman run --it --rm --entrypoint /usr/local/bin/novoutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novoutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nsenter

```bash
$ singularity exec <container> /usr/local/bin/nsenter
$ podman run --it --rm --entrypoint /usr/local/bin/nsenter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nsenter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prlimit

```bash
$ singularity exec <container> /usr/local/bin/prlimit
$ podman run --it --rm --entrypoint /usr/local/bin/prlimit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prlimit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qcalplot.R

```bash
$ singularity exec <container> /usr/local/bin/qcalplot.R
$ podman run --it --rm --entrypoint /usr/local/bin/qcalplot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qcalplot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rrbsreference

```bash
$ singularity exec <container> /usr/local/bin/rrbsreference
$ podman run --it --rm --entrypoint /usr/local/bin/rrbsreference   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rrbsreference   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scriptlive

```bash
$ singularity exec <container> /usr/local/bin/scriptlive
$ podman run --it --rm --entrypoint /usr/local/bin/scriptlive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scriptlive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cal

```bash
$ singularity exec <container> /usr/local/bin/cal
$ podman run --it --rm --entrypoint /usr/local/bin/cal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chmem

```bash
$ singularity exec <container> /usr/local/bin/chmem
$ podman run --it --rm --entrypoint /usr/local/bin/chmem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chmem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### choom

```bash
$ singularity exec <container> /usr/local/bin/choom
$ podman run --it --rm --entrypoint /usr/local/bin/choom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/choom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chrt

```bash
$ singularity exec <container> /usr/local/bin/chrt
$ podman run --it --rm --entrypoint /usr/local/bin/chrt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chrt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### col

```bash
$ singularity exec <container> /usr/local/bin/col
$ podman run --it --rm --entrypoint /usr/local/bin/col   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/col   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### colcrt

```bash
$ singularity exec <container> /usr/local/bin/colcrt
$ podman run --it --rm --entrypoint /usr/local/bin/colcrt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/colcrt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### colrm

```bash
$ singularity exec <container> /usr/local/bin/colrm
$ podman run --it --rm --entrypoint /usr/local/bin/colrm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/colrm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### column

```bash
$ singularity exec <container> /usr/local/bin/column
$ podman run --it --rm --entrypoint /usr/local/bin/column   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/column   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dmesg

```bash
$ singularity exec <container> /usr/local/bin/dmesg
$ podman run --it --rm --entrypoint /usr/local/bin/dmesg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dmesg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eject

```bash
$ singularity exec <container> /usr/local/bin/eject
$ podman run --it --rm --entrypoint /usr/local/bin/eject   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eject   -v ${PWD} -w ${PWD} <container> -c " $@"
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