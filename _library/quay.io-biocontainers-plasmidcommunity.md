---
layout: container
name:  "quay.io/biocontainers/plasmidcommunity"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plasmidcommunity/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/plasmidcommunity/container.yaml"
updated_at: "2025-08-18 03:59:08.874601"
latest: "1.0.2--r44hdfd78af_1"
container_url: "https://biocontainers.pro/tools/plasmidcommunity"
aliases:
 - "PlasmidTransModel.R"
 - "PlasmidTransModel.sh"
 - "assignCommunity.R"
 - "assignCommunity.sh"
 - "enosys"
 - "exch"
 - "fadvise"
 - "getCommunity.R"
 - "getCommunity.sh"
 - "heatmap.full.genome.pipeline.R"
 - "irqtop"
 - "lastlog2"
 - "lsclocks"
 - "lsfd"
 - "lsirq"
 - "nsenter"
 - "pan.R"
 - "pan.sh"
 - "pipesz"
 - "plasmidCommunity.R"
 - "plasmidCommunity.sh"
 - "prlimit"
 - "setpgid"
 - "silhouetteCurve.R"
 - "silhouetteCurve.sh"
 - "subNetwork.R"
 - "uclampset"
 - "bash"
 - "bashbug"
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
 - "fallocate"
 - "fincore"
 - "findmnt"
 - "getopt"
 - "hardlink"
 - "hexdump"
 - "i386"
 - "ionice"
 - "ipcmk"
 - "ipcrm"
 - "ipcs"
 - "isosize"
versions:
 - "1.0.2--r44hdfd78af_0"
 - "1.0.2--r44hdfd78af_1"
description: "singularity registry hpc automated addition for plasmidcommunity"
config: {"url": "https://biocontainers.pro/tools/plasmidcommunity", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for plasmidcommunity", "latest": {"1.0.2--r44hdfd78af_1": "sha256:acade9571d213a70c8ca5c5840e6ebcbb62ccd856e827422d7114ae9e70286e5"}, "tags": {"1.0.2--r44hdfd78af_0": "sha256:2ae9baf6640eb890cad41055f412ed94940802b576b53d255ae8df268b6a6d8d", "1.0.2--r44hdfd78af_1": "sha256:acade9571d213a70c8ca5c5840e6ebcbb62ccd856e827422d7114ae9e70286e5"}, "docker": "quay.io/biocontainers/plasmidcommunity", "aliases": {"PlasmidTransModel.R": "/usr/local/bin/PlasmidTransModel.R", "PlasmidTransModel.sh": "/usr/local/bin/PlasmidTransModel.sh", "assignCommunity.R": "/usr/local/bin/assignCommunity.R", "assignCommunity.sh": "/usr/local/bin/assignCommunity.sh", "enosys": "/usr/local/bin/enosys", "exch": "/usr/local/bin/exch", "fadvise": "/usr/local/bin/fadvise", "getCommunity.R": "/usr/local/bin/getCommunity.R", "getCommunity.sh": "/usr/local/bin/getCommunity.sh", "heatmap.full.genome.pipeline.R": "/usr/local/bin/heatmap.full.genome.pipeline.R", "irqtop": "/usr/local/bin/irqtop", "lastlog2": "/usr/local/bin/lastlog2", "lsclocks": "/usr/local/bin/lsclocks", "lsfd": "/usr/local/bin/lsfd", "lsirq": "/usr/local/bin/lsirq", "nsenter": "/usr/local/bin/nsenter", "pan.R": "/usr/local/bin/pan.R", "pan.sh": "/usr/local/bin/pan.sh", "pipesz": "/usr/local/bin/pipesz", "plasmidCommunity.R": "/usr/local/bin/plasmidCommunity.R", "plasmidCommunity.sh": "/usr/local/bin/plasmidCommunity.sh", "prlimit": "/usr/local/bin/prlimit", "setpgid": "/usr/local/bin/setpgid", "silhouetteCurve.R": "/usr/local/bin/silhouetteCurve.R", "silhouetteCurve.sh": "/usr/local/bin/silhouetteCurve.sh", "subNetwork.R": "/usr/local/bin/subNetwork.R", "uclampset": "/usr/local/bin/uclampset", "bash": "/usr/local/bin/bash", "bashbug": "/usr/local/bin/bashbug", "scriptlive": "/usr/local/bin/scriptlive", "cal": "/usr/local/bin/cal", "chmem": "/usr/local/bin/chmem", "choom": "/usr/local/bin/choom", "chrt": "/usr/local/bin/chrt", "col": "/usr/local/bin/col", "colcrt": "/usr/local/bin/colcrt", "colrm": "/usr/local/bin/colrm", "column": "/usr/local/bin/column", "dmesg": "/usr/local/bin/dmesg", "eject": "/usr/local/bin/eject", "fallocate": "/usr/local/bin/fallocate", "fincore": "/usr/local/bin/fincore", "findmnt": "/usr/local/bin/findmnt", "getopt": "/usr/local/bin/getopt", "hardlink": "/usr/local/bin/hardlink", "hexdump": "/usr/local/bin/hexdump", "i386": "/usr/local/bin/i386", "ionice": "/usr/local/bin/ionice", "ipcmk": "/usr/local/bin/ipcmk", "ipcrm": "/usr/local/bin/ipcrm", "ipcs": "/usr/local/bin/ipcs", "isosize": "/usr/local/bin/isosize"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/plasmidcommunity.
singularity registry hpc automated addition for plasmidcommunity
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plasmidcommunity
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plasmidcommunity:1.0.2--r44hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plasmidcommunity/1.0.2--r44hdfd78af_1
$ module help quay.io/biocontainers/plasmidcommunity/1.0.2--r44hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plasmidcommunity-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plasmidcommunity-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plasmidcommunity-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plasmidcommunity-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plasmidcommunity-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plasmidcommunity-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PlasmidTransModel.R

```bash
$ singularity exec <container> /usr/local/bin/PlasmidTransModel.R
$ podman run --it --rm --entrypoint /usr/local/bin/PlasmidTransModel.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PlasmidTransModel.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PlasmidTransModel.sh

```bash
$ singularity exec <container> /usr/local/bin/PlasmidTransModel.sh
$ podman run --it --rm --entrypoint /usr/local/bin/PlasmidTransModel.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PlasmidTransModel.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assignCommunity.R

```bash
$ singularity exec <container> /usr/local/bin/assignCommunity.R
$ podman run --it --rm --entrypoint /usr/local/bin/assignCommunity.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assignCommunity.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assignCommunity.sh

```bash
$ singularity exec <container> /usr/local/bin/assignCommunity.sh
$ podman run --it --rm --entrypoint /usr/local/bin/assignCommunity.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assignCommunity.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enosys

```bash
$ singularity exec <container> /usr/local/bin/enosys
$ podman run --it --rm --entrypoint /usr/local/bin/enosys   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enosys   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exch

```bash
$ singularity exec <container> /usr/local/bin/exch
$ podman run --it --rm --entrypoint /usr/local/bin/exch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fadvise

```bash
$ singularity exec <container> /usr/local/bin/fadvise
$ podman run --it --rm --entrypoint /usr/local/bin/fadvise   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fadvise   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getCommunity.R

```bash
$ singularity exec <container> /usr/local/bin/getCommunity.R
$ podman run --it --rm --entrypoint /usr/local/bin/getCommunity.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getCommunity.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getCommunity.sh

```bash
$ singularity exec <container> /usr/local/bin/getCommunity.sh
$ podman run --it --rm --entrypoint /usr/local/bin/getCommunity.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getCommunity.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### heatmap.full.genome.pipeline.R

```bash
$ singularity exec <container> /usr/local/bin/heatmap.full.genome.pipeline.R
$ podman run --it --rm --entrypoint /usr/local/bin/heatmap.full.genome.pipeline.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/heatmap.full.genome.pipeline.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irqtop

```bash
$ singularity exec <container> /usr/local/bin/irqtop
$ podman run --it --rm --entrypoint /usr/local/bin/irqtop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irqtop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastlog2

```bash
$ singularity exec <container> /usr/local/bin/lastlog2
$ podman run --it --rm --entrypoint /usr/local/bin/lastlog2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastlog2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lsclocks

```bash
$ singularity exec <container> /usr/local/bin/lsclocks
$ podman run --it --rm --entrypoint /usr/local/bin/lsclocks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lsclocks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lsfd

```bash
$ singularity exec <container> /usr/local/bin/lsfd
$ podman run --it --rm --entrypoint /usr/local/bin/lsfd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lsfd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lsirq

```bash
$ singularity exec <container> /usr/local/bin/lsirq
$ podman run --it --rm --entrypoint /usr/local/bin/lsirq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lsirq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nsenter

```bash
$ singularity exec <container> /usr/local/bin/nsenter
$ podman run --it --rm --entrypoint /usr/local/bin/nsenter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nsenter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pan.R

```bash
$ singularity exec <container> /usr/local/bin/pan.R
$ podman run --it --rm --entrypoint /usr/local/bin/pan.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pan.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pan.sh

```bash
$ singularity exec <container> /usr/local/bin/pan.sh
$ podman run --it --rm --entrypoint /usr/local/bin/pan.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pan.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pipesz

```bash
$ singularity exec <container> /usr/local/bin/pipesz
$ podman run --it --rm --entrypoint /usr/local/bin/pipesz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pipesz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasmidCommunity.R

```bash
$ singularity exec <container> /usr/local/bin/plasmidCommunity.R
$ podman run --it --rm --entrypoint /usr/local/bin/plasmidCommunity.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasmidCommunity.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasmidCommunity.sh

```bash
$ singularity exec <container> /usr/local/bin/plasmidCommunity.sh
$ podman run --it --rm --entrypoint /usr/local/bin/plasmidCommunity.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasmidCommunity.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prlimit

```bash
$ singularity exec <container> /usr/local/bin/prlimit
$ podman run --it --rm --entrypoint /usr/local/bin/prlimit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prlimit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setpgid

```bash
$ singularity exec <container> /usr/local/bin/setpgid
$ podman run --it --rm --entrypoint /usr/local/bin/setpgid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setpgid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### silhouetteCurve.R

```bash
$ singularity exec <container> /usr/local/bin/silhouetteCurve.R
$ podman run --it --rm --entrypoint /usr/local/bin/silhouetteCurve.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/silhouetteCurve.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### silhouetteCurve.sh

```bash
$ singularity exec <container> /usr/local/bin/silhouetteCurve.sh
$ podman run --it --rm --entrypoint /usr/local/bin/silhouetteCurve.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/silhouetteCurve.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subNetwork.R

```bash
$ singularity exec <container> /usr/local/bin/subNetwork.R
$ podman run --it --rm --entrypoint /usr/local/bin/subNetwork.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subNetwork.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uclampset

```bash
$ singularity exec <container> /usr/local/bin/uclampset
$ podman run --it --rm --entrypoint /usr/local/bin/uclampset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uclampset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bash

```bash
$ singularity exec <container> /usr/local/bin/bash
$ podman run --it --rm --entrypoint /usr/local/bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bashbug

```bash
$ singularity exec <container> /usr/local/bin/bashbug
$ podman run --it --rm --entrypoint /usr/local/bin/bashbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bashbug   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### fallocate

```bash
$ singularity exec <container> /usr/local/bin/fallocate
$ podman run --it --rm --entrypoint /usr/local/bin/fallocate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fallocate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fincore

```bash
$ singularity exec <container> /usr/local/bin/fincore
$ podman run --it --rm --entrypoint /usr/local/bin/fincore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fincore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findmnt

```bash
$ singularity exec <container> /usr/local/bin/findmnt
$ podman run --it --rm --entrypoint /usr/local/bin/findmnt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findmnt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getopt

```bash
$ singularity exec <container> /usr/local/bin/getopt
$ podman run --it --rm --entrypoint /usr/local/bin/getopt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getopt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hardlink

```bash
$ singularity exec <container> /usr/local/bin/hardlink
$ podman run --it --rm --entrypoint /usr/local/bin/hardlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hardlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hexdump

```bash
$ singularity exec <container> /usr/local/bin/hexdump
$ podman run --it --rm --entrypoint /usr/local/bin/hexdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hexdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### i386

```bash
$ singularity exec <container> /usr/local/bin/i386
$ podman run --it --rm --entrypoint /usr/local/bin/i386   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/i386   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ionice

```bash
$ singularity exec <container> /usr/local/bin/ionice
$ podman run --it --rm --entrypoint /usr/local/bin/ionice   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ionice   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipcmk

```bash
$ singularity exec <container> /usr/local/bin/ipcmk
$ podman run --it --rm --entrypoint /usr/local/bin/ipcmk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipcmk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipcrm

```bash
$ singularity exec <container> /usr/local/bin/ipcrm
$ podman run --it --rm --entrypoint /usr/local/bin/ipcrm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipcrm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipcs

```bash
$ singularity exec <container> /usr/local/bin/ipcs
$ podman run --it --rm --entrypoint /usr/local/bin/ipcs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipcs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isosize

```bash
$ singularity exec <container> /usr/local/bin/isosize
$ podman run --it --rm --entrypoint /usr/local/bin/isosize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isosize   -v ${PWD} -w ${PWD} <container> -c " $@"
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