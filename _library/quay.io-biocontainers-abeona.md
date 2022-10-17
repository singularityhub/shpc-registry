---
layout: container
name:  "quay.io/biocontainers/abeona"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/abeona/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/abeona/container.yaml"
updated_at: "2022-10-17 02:49:00.230326"
latest: "0.45.0--py36_0"
container_url: "https://biocontainers.pro/tools/abeona"
aliases:
 - "abeona"
 - "b2sum"
 - "bwa"
 - "cortexpy"
 - "factor"
 - "kallisto"
 - "nextflow"
 - "python"
 - "python3"
versions:
 - "0.45.0--py36_0"
description: "A simple transcriptome assembler based on kallisto and cortex graphs."
config: {"url": "https://biocontainers.pro/tools/abeona", "maintainer": "@vsoch", "description": "A simple transcriptome assembler based on kallisto and cortex graphs.", "latest": {"0.45.0--py36_0": "sha256:5be8da7bf9360eacc9cdaff7caf6a6081d7380584ef7946c046fa23450803a13"}, "tags": {"0.45.0--py36_0": "sha256:5be8da7bf9360eacc9cdaff7caf6a6081d7380584ef7946c046fa23450803a13"}, "docker": "quay.io/biocontainers/abeona", "aliases": {"abeona": "/usr/local/bin/abeona", "b2sum": "/usr/local/bin/b2sum", "bwa": "/usr/local/bin/bwa", "cortexpy": "/usr/local/bin/cortexpy", "factor": "/usr/local/bin/factor", "kallisto": "/usr/local/bin/kallisto", "nextflow": "/usr/local/bin/nextflow", "python": "/usr/local/bin/python", "python3": "/usr/local/bin/python3"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/abeona.
A simple transcriptome assembler based on kallisto and cortex graphs.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/abeona
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/abeona:0.45.0--py36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/abeona/0.45.0--py36_0
$ module help quay.io/biocontainers/abeona/0.45.0--py36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### abeona-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### abeona-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### abeona-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### abeona-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### abeona-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### abeona-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abeona
       
```bash
$ singularity exec <container> /usr/local/bin/abeona
$ podman run --it --rm --entrypoint /usr/local/bin/abeona   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abeona   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2sum
       
```bash
$ singularity exec <container> /usr/local/bin/b2sum
$ podman run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa
       
```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cortexpy
       
```bash
$ singularity exec <container> /usr/local/bin/cortexpy
$ podman run --it --rm --entrypoint /usr/local/bin/cortexpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cortexpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### factor
       
```bash
$ singularity exec <container> /usr/local/bin/factor
$ podman run --it --rm --entrypoint /usr/local/bin/factor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/factor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kallisto
       
```bash
$ singularity exec <container> /usr/local/bin/kallisto
$ podman run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nextflow
       
```bash
$ singularity exec <container> /usr/local/bin/nextflow
$ podman run --it --rm --entrypoint /usr/local/bin/nextflow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nextflow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python
       
```bash
$ singularity exec <container> /usr/local/bin/python
$ podman run --it --rm --entrypoint /usr/local/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3
       
```bash
$ singularity exec <container> /usr/local/bin/python3
$ podman run --it --rm --entrypoint /usr/local/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
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