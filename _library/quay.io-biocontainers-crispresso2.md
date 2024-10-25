---
layout: container
name:  "quay.io/biocontainers/crispresso2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/crispresso2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/crispresso2/container.yaml"
updated_at: "2024-10-25 03:22:19.118605"
latest: "2.3.1--py310h581d4b6_3"
container_url: "https://biocontainers.pro/tools/crispresso2"
aliases:
 - "CRISPResso"
 - "CRISPRessoAggregate"
 - "CRISPRessoBatch"
 - "CRISPRessoCompare"
 - "CRISPRessoPooled"
 - "CRISPRessoPooledWGSCompare"
 - "CRISPRessoWGS"
 - "flash"
 - "trimmomatic"
 - "cups-config"
 - "ippeveprinter"
 - "ipptool"
 - "bowtie2"
 - "bowtie2-align-l"
 - "bowtie2-align-s"
 - "bowtie2-build"
 - "bowtie2-build-l"
versions:
 - "2.2.8--py38h6eac312_0"
 - "2.2.14--py310hd6be1da_0"
 - "2.3.0--py39hec7c8de_1"
 - "2.3.1--py39hec7c8de_0"
 - "2.3.1--py39h24fbfe6_1"
 - "2.3.1--py310h581d4b6_3"
description: "shpc-registry automated BioContainers addition for crispresso2"
config: {"url": "https://biocontainers.pro/tools/crispresso2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for crispresso2", "latest": {"2.3.1--py310h581d4b6_3": "sha256:a28cd42882e891873c09ac13635234fe38b6dfbd59b580ac8c695630154b9624"}, "tags": {"2.2.8--py38h6eac312_0": "sha256:77f2952faf107bd2412e2373d37e50d7ecbf1da81d75d008233f24cf42fc1d5e", "2.2.14--py310hd6be1da_0": "sha256:482df47e1c70df9735a0e857786074e303982ddce0af01a7613b7070a3fe011f", "2.3.0--py39hec7c8de_1": "sha256:d642346a92d9a10ecd86d2bdfbe57de1aa73e4af0b30c0c6300e128abe3876fd", "2.3.1--py39hec7c8de_0": "sha256:ae0ea8c662a920109d0a6d65c0603212ac089a8c303c5e7b5571c98fd845863e", "2.3.1--py39h24fbfe6_1": "sha256:85acc69a326cf8c1c5c6840b91b17ada3078014846f0f7a725ac99053077d0b3", "2.3.1--py310h581d4b6_3": "sha256:a28cd42882e891873c09ac13635234fe38b6dfbd59b580ac8c695630154b9624"}, "docker": "quay.io/biocontainers/crispresso2", "aliases": {"CRISPResso": "/usr/local/bin/CRISPResso", "CRISPRessoAggregate": "/usr/local/bin/CRISPRessoAggregate", "CRISPRessoBatch": "/usr/local/bin/CRISPRessoBatch", "CRISPRessoCompare": "/usr/local/bin/CRISPRessoCompare", "CRISPRessoPooled": "/usr/local/bin/CRISPRessoPooled", "CRISPRessoPooledWGSCompare": "/usr/local/bin/CRISPRessoPooledWGSCompare", "CRISPRessoWGS": "/usr/local/bin/CRISPRessoWGS", "flash": "/usr/local/bin/flash", "trimmomatic": "/usr/local/bin/trimmomatic", "cups-config": "/usr/local/bin/cups-config", "ippeveprinter": "/usr/local/bin/ippeveprinter", "ipptool": "/usr/local/bin/ipptool", "bowtie2": "/usr/local/bin/bowtie2", "bowtie2-align-l": "/usr/local/bin/bowtie2-align-l", "bowtie2-align-s": "/usr/local/bin/bowtie2-align-s", "bowtie2-build": "/usr/local/bin/bowtie2-build", "bowtie2-build-l": "/usr/local/bin/bowtie2-build-l"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/crispresso2.
shpc-registry automated BioContainers addition for crispresso2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/crispresso2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/crispresso2:2.3.1--py310h581d4b6_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/crispresso2/2.3.1--py310h581d4b6_3
$ module help quay.io/biocontainers/crispresso2/2.3.1--py310h581d4b6_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### crispresso2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### crispresso2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### crispresso2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### crispresso2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### crispresso2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### crispresso2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CRISPResso

```bash
$ singularity exec <container> /usr/local/bin/CRISPResso
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPResso   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPResso   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CRISPRessoAggregate

```bash
$ singularity exec <container> /usr/local/bin/CRISPRessoAggregate
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPRessoAggregate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPRessoAggregate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CRISPRessoBatch

```bash
$ singularity exec <container> /usr/local/bin/CRISPRessoBatch
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPRessoBatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPRessoBatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CRISPRessoCompare

```bash
$ singularity exec <container> /usr/local/bin/CRISPRessoCompare
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPRessoCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPRessoCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CRISPRessoPooled

```bash
$ singularity exec <container> /usr/local/bin/CRISPRessoPooled
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPRessoPooled   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPRessoPooled   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CRISPRessoPooledWGSCompare

```bash
$ singularity exec <container> /usr/local/bin/CRISPRessoPooledWGSCompare
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPRessoPooledWGSCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPRessoPooledWGSCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CRISPRessoWGS

```bash
$ singularity exec <container> /usr/local/bin/CRISPRessoWGS
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPRessoWGS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPRessoWGS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flash

```bash
$ singularity exec <container> /usr/local/bin/flash
$ podman run --it --rm --entrypoint /usr/local/bin/flash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimmomatic

```bash
$ singularity exec <container> /usr/local/bin/trimmomatic
$ podman run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cups-config

```bash
$ singularity exec <container> /usr/local/bin/cups-config
$ podman run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ippeveprinter

```bash
$ singularity exec <container> /usr/local/bin/ippeveprinter
$ podman run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipptool

```bash
$ singularity exec <container> /usr/local/bin/ipptool
$ podman run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2

```bash
$ singularity exec <container> /usr/local/bin/bowtie2
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
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