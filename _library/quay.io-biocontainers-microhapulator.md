---
layout: container
name:  "quay.io/biocontainers/microhapulator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/microhapulator/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/microhapulator/container.yaml"
updated_at: "2022-10-29 05:44:18.477425"
latest: "0.7.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/microhapulator"
aliases:
 - "happer"
 - "iss"
 - "mhpl8r"
 - "termgraph"
 - "2to3-3.9"
 - "ace2sam"
 - "aserver"
 - "bgzip"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "brotli"
 - "bwa"
 - "cbc"
 - "clp"
versions:
 - "0.7.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for microhapulator"
config: {"url": "https://biocontainers.pro/tools/microhapulator", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for microhapulator", "latest": {"0.7.2--pyhdfd78af_0": "sha256:c542f99626c3034d8042a28174a40f661b8318e039ebc46dbe51818f481f9973"}, "tags": {"0.7.2--pyhdfd78af_0": "sha256:c542f99626c3034d8042a28174a40f661b8318e039ebc46dbe51818f481f9973"}, "docker": "quay.io/biocontainers/microhapulator", "aliases": {"happer": "/usr/local/bin/happer", "iss": "/usr/local/bin/iss", "mhpl8r": "/usr/local/bin/mhpl8r", "termgraph": "/usr/local/bin/termgraph", "2to3-3.9": "/usr/local/bin/2to3-3.9", "ace2sam": "/usr/local/bin/ace2sam", "aserver": "/usr/local/bin/aserver", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "brotli": "/usr/local/bin/brotli", "bwa": "/usr/local/bin/bwa", "cbc": "/usr/local/bin/cbc", "clp": "/usr/local/bin/clp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/microhapulator.
shpc-registry automated BioContainers addition for microhapulator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/microhapulator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/microhapulator:0.7.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/microhapulator/0.7.2--pyhdfd78af_0
$ module help quay.io/biocontainers/microhapulator/0.7.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### microhapulator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### microhapulator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### microhapulator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### microhapulator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### microhapulator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### microhapulator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### happer

```bash
$ singularity exec <container> /usr/local/bin/happer
$ podman run --it --rm --entrypoint /usr/local/bin/happer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/happer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iss

```bash
$ singularity exec <container> /usr/local/bin/iss
$ podman run --it --rm --entrypoint /usr/local/bin/iss   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iss   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhpl8r

```bash
$ singularity exec <container> /usr/local/bin/mhpl8r
$ podman run --it --rm --entrypoint /usr/local/bin/mhpl8r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhpl8r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### termgraph

```bash
$ singularity exec <container> /usr/local/bin/termgraph
$ podman run --it --rm --entrypoint /usr/local/bin/termgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/termgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bowtie2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/bowtie2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbc

```bash
$ singularity exec <container> /usr/local/bin/cbc
$ podman run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clp

```bash
$ singularity exec <container> /usr/local/bin/clp
$ podman run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
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