---
layout: container
name:  "quay.io/biocontainers/irma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/irma/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/irma/container.yaml"
updated_at: "2022-10-29 05:42:01.303977"
latest: "1.0.2--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/irma"
aliases:
 - "IRMA"
 - "LABEL"
 - "QUICK_INSTALL.txt"
 - "FastTree"
 - "FastTreeMP"
 - "ace2sam"
 - "bgzip"
 - "blast2sam.pl"
 - "blat"
 - "bowtie2sam.pl"
 - "build_env_setup.sh"
 - "conda_build.sh"
 - "env_parallel"
versions:
 - "1.0.2--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for irma"
config: {"url": "https://biocontainers.pro/tools/irma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for irma", "latest": {"1.0.2--pl5321hdfd78af_2": "sha256:1ae0ba56c93255dd42011f02887d78decae4b0231940ba47d08c378de1e4ccc9"}, "tags": {"1.0.2--pl5321hdfd78af_2": "sha256:1ae0ba56c93255dd42011f02887d78decae4b0231940ba47d08c378de1e4ccc9"}, "docker": "quay.io/biocontainers/irma", "aliases": {"IRMA": "/usr/local/bin/IRMA", "LABEL": "/usr/local/bin/LABEL", "QUICK_INSTALL.txt": "/usr/local/bin/QUICK_INSTALL.txt", "FastTree": "/usr/local/bin/FastTree", "FastTreeMP": "/usr/local/bin/FastTreeMP", "ace2sam": "/usr/local/bin/ace2sam", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "blat": "/usr/local/bin/blat", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "build_env_setup.sh": "/usr/local/bin/build_env_setup.sh", "conda_build.sh": "/usr/local/bin/conda_build.sh", "env_parallel": "/usr/local/bin/env_parallel"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/irma.
shpc-registry automated BioContainers addition for irma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/irma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/irma:1.0.2--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/irma/1.0.2--pl5321hdfd78af_2
$ module help quay.io/biocontainers/irma/1.0.2--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### irma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### irma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### irma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### irma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### irma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### irma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### IRMA

```bash
$ singularity exec <container> /usr/local/bin/IRMA
$ podman run --it --rm --entrypoint /usr/local/bin/IRMA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IRMA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LABEL

```bash
$ singularity exec <container> /usr/local/bin/LABEL
$ podman run --it --rm --entrypoint /usr/local/bin/LABEL   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LABEL   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### QUICK_INSTALL.txt

```bash
$ singularity exec <container> /usr/local/bin/QUICK_INSTALL.txt
$ podman run --it --rm --entrypoint /usr/local/bin/QUICK_INSTALL.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/QUICK_INSTALL.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree

```bash
$ singularity exec <container> /usr/local/bin/FastTree
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTreeMP

```bash
$ singularity exec <container> /usr/local/bin/FastTreeMP
$ podman run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blat

```bash
$ singularity exec <container> /usr/local/bin/blat
$ podman run --it --rm --entrypoint /usr/local/bin/blat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/bowtie2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_env_setup.sh

```bash
$ singularity exec <container> /usr/local/bin/build_env_setup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda_build.sh

```bash
$ singularity exec <container> /usr/local/bin/conda_build.sh
$ podman run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel

```bash
$ singularity exec <container> /usr/local/bin/env_parallel
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
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