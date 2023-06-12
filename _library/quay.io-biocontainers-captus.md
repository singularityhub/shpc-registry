---
layout: container
name:  "quay.io/biocontainers/captus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/captus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/captus/container.yaml"
updated_at: "2023-06-12 05:14:48.171500"
latest: "0.9.91--pyhdfd78af_2"
container_url: "https://biocontainers.pro/tools/captus"
aliases:
 - "Xcalcmem.sh"
 - "bloomfilterparser.sh"
 - "captus_assembly"
 - "clipkit"
 - "f2py3.11"
 - "falco"
 - "2to3-3.11"
 - "idle3.11"
 - "kmutate.sh"
 - "megahit_core"
 - "megahit_core_no_hw_accel"
 - "megahit_core_popcnt"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "runhmm.sh"
 - "megahit"
 - "megahit_toolkit"
 - "kmerposition.sh"
 - "reformatpb.sh"
 - "summarizecoverage.sh"
 - "alltoall.sh"
 - "analyzesketchresults.sh"
 - "comparessu.sh"
 - "filtersilva.sh"
 - "sketchblacklist2.sh"
 - "splitribo.sh"
 - "addssu.sh"
 - "adjusthomopolymers.sh"
 - "analyzeaccession.sh"
 - "analyzegenes.sh"
versions:
 - "0.9.91--pyhdfd78af_0"
 - "0.9.91--pyhdfd78af_2"
description: "singularity registry hpc automated addition for captus"
config: {"url": "https://biocontainers.pro/tools/captus", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for captus", "latest": {"0.9.91--pyhdfd78af_2": "sha256:2ce18ac402d51f5ec4b7977357c3ab09b42af0c3123b265e8079964b298b2151"}, "tags": {"0.9.91--pyhdfd78af_0": "sha256:7b81e5c5d4241d3021b84032a0b38bee159a998528c212a7db6ab9a6d5656ee9", "0.9.91--pyhdfd78af_2": "sha256:2ce18ac402d51f5ec4b7977357c3ab09b42af0c3123b265e8079964b298b2151"}, "docker": "quay.io/biocontainers/captus", "aliases": {"Xcalcmem.sh": "/usr/local/bin/Xcalcmem.sh", "bloomfilterparser.sh": "/usr/local/bin/bloomfilterparser.sh", "captus_assembly": "/usr/local/bin/captus_assembly", "clipkit": "/usr/local/bin/clipkit", "f2py3.11": "/usr/local/bin/f2py3.11", "falco": "/usr/local/bin/falco", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "kmutate.sh": "/usr/local/bin/kmutate.sh", "megahit_core": "/usr/local/bin/megahit_core", "megahit_core_no_hw_accel": "/usr/local/bin/megahit_core_no_hw_accel", "megahit_core_popcnt": "/usr/local/bin/megahit_core_popcnt", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "runhmm.sh": "/usr/local/bin/runhmm.sh", "megahit": "/usr/local/bin/megahit", "megahit_toolkit": "/usr/local/bin/megahit_toolkit", "kmerposition.sh": "/usr/local/bin/kmerposition.sh", "reformatpb.sh": "/usr/local/bin/reformatpb.sh", "summarizecoverage.sh": "/usr/local/bin/summarizecoverage.sh", "alltoall.sh": "/usr/local/bin/alltoall.sh", "analyzesketchresults.sh": "/usr/local/bin/analyzesketchresults.sh", "comparessu.sh": "/usr/local/bin/comparessu.sh", "filtersilva.sh": "/usr/local/bin/filtersilva.sh", "sketchblacklist2.sh": "/usr/local/bin/sketchblacklist2.sh", "splitribo.sh": "/usr/local/bin/splitribo.sh", "addssu.sh": "/usr/local/bin/addssu.sh", "adjusthomopolymers.sh": "/usr/local/bin/adjusthomopolymers.sh", "analyzeaccession.sh": "/usr/local/bin/analyzeaccession.sh", "analyzegenes.sh": "/usr/local/bin/analyzegenes.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/captus.
singularity registry hpc automated addition for captus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/captus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/captus:0.9.91--pyhdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/captus/0.9.91--pyhdfd78af_2
$ module help quay.io/biocontainers/captus/0.9.91--pyhdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### captus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### captus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### captus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### captus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### captus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### captus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Xcalcmem.sh

```bash
$ singularity exec <container> /usr/local/bin/Xcalcmem.sh
$ podman run --it --rm --entrypoint /usr/local/bin/Xcalcmem.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Xcalcmem.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bloomfilterparser.sh

```bash
$ singularity exec <container> /usr/local/bin/bloomfilterparser.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bloomfilterparser.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bloomfilterparser.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### captus_assembly

```bash
$ singularity exec <container> /usr/local/bin/captus_assembly
$ podman run --it --rm --entrypoint /usr/local/bin/captus_assembly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/captus_assembly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clipkit

```bash
$ singularity exec <container> /usr/local/bin/clipkit
$ podman run --it --rm --entrypoint /usr/local/bin/clipkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clipkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### falco

```bash
$ singularity exec <container> /usr/local/bin/falco
$ podman run --it --rm --entrypoint /usr/local/bin/falco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/falco   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmutate.sh

```bash
$ singularity exec <container> /usr/local/bin/kmutate.sh
$ podman run --it --rm --entrypoint /usr/local/bin/kmutate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmutate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core

```bash
$ singularity exec <container> /usr/local/bin/megahit_core
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core_no_hw_accel

```bash
$ singularity exec <container> /usr/local/bin/megahit_core_no_hw_accel
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core_no_hw_accel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core_no_hw_accel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core_popcnt

```bash
$ singularity exec <container> /usr/local/bin/megahit_core_popcnt
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core_popcnt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core_popcnt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runhmm.sh

```bash
$ singularity exec <container> /usr/local/bin/runhmm.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runhmm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runhmm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit

```bash
$ singularity exec <container> /usr/local/bin/megahit
$ podman run --it --rm --entrypoint /usr/local/bin/megahit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_toolkit

```bash
$ singularity exec <container> /usr/local/bin/megahit_toolkit
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_toolkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_toolkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmerposition.sh

```bash
$ singularity exec <container> /usr/local/bin/kmerposition.sh
$ podman run --it --rm --entrypoint /usr/local/bin/kmerposition.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmerposition.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reformatpb.sh

```bash
$ singularity exec <container> /usr/local/bin/reformatpb.sh
$ podman run --it --rm --entrypoint /usr/local/bin/reformatpb.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reformatpb.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summarizecoverage.sh

```bash
$ singularity exec <container> /usr/local/bin/summarizecoverage.sh
$ podman run --it --rm --entrypoint /usr/local/bin/summarizecoverage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summarizecoverage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alltoall.sh

```bash
$ singularity exec <container> /usr/local/bin/alltoall.sh
$ podman run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzesketchresults.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzesketchresults.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzesketchresults.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzesketchresults.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### comparessu.sh

```bash
$ singularity exec <container> /usr/local/bin/comparessu.sh
$ podman run --it --rm --entrypoint /usr/local/bin/comparessu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/comparessu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filtersilva.sh

```bash
$ singularity exec <container> /usr/local/bin/filtersilva.sh
$ podman run --it --rm --entrypoint /usr/local/bin/filtersilva.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filtersilva.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sketchblacklist2.sh

```bash
$ singularity exec <container> /usr/local/bin/sketchblacklist2.sh
$ podman run --it --rm --entrypoint /usr/local/bin/sketchblacklist2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sketchblacklist2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitribo.sh

```bash
$ singularity exec <container> /usr/local/bin/splitribo.sh
$ podman run --it --rm --entrypoint /usr/local/bin/splitribo.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitribo.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addssu.sh

```bash
$ singularity exec <container> /usr/local/bin/addssu.sh
$ podman run --it --rm --entrypoint /usr/local/bin/addssu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addssu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adjusthomopolymers.sh

```bash
$ singularity exec <container> /usr/local/bin/adjusthomopolymers.sh
$ podman run --it --rm --entrypoint /usr/local/bin/adjusthomopolymers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adjusthomopolymers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzeaccession.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzeaccession.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzeaccession.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzeaccession.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzegenes.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzegenes.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzegenes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzegenes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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