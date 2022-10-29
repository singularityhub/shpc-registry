---
layout: container
name:  "quay.io/biocontainers/nudup"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nudup/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/nudup/container.yaml"
updated_at: "2022-10-29 05:34:23.768330"
latest: "2.3.3--py_2"
container_url: "https://biocontainers.pro/tools/nudup"
aliases:
 - "nudup.py"
 - "ace2sam"
 - "b2sum"
 - "base32"
 - "base64"
 - "basename"
 - "basenc"
 - "bgzip"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "cat"
versions:
 - "2.3.3--py_2"
description: "shpc-registry automated BioContainers addition for nudup"
config: {"url": "https://biocontainers.pro/tools/nudup", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nudup", "latest": {"2.3.3--py_2": "sha256:33d15014310fe929682c7b24ee9c938b32e1965ee2e32d92613ed08f80afefe7"}, "tags": {"2.3.3--py_2": "sha256:33d15014310fe929682c7b24ee9c938b32e1965ee2e32d92613ed08f80afefe7"}, "docker": "quay.io/biocontainers/nudup", "aliases": {"nudup.py": "/usr/local/bin/nudup.py", "ace2sam": "/usr/local/bin/ace2sam", "b2sum": "/usr/local/bin/b2sum", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "basenc": "/usr/local/bin/basenc", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "cat": "/usr/local/bin/cat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nudup.
shpc-registry automated BioContainers addition for nudup
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nudup
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nudup:2.3.3--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nudup/2.3.3--py_2
$ module help quay.io/biocontainers/nudup/2.3.3--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nudup-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nudup-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nudup-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nudup-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nudup-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nudup-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nudup.py

```bash
$ singularity exec <container> /usr/local/bin/nudup.py
$ podman run --it --rm --entrypoint /usr/local/bin/nudup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nudup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2sum

```bash
$ singularity exec <container> /usr/local/bin/b2sum
$ podman run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base32

```bash
$ singularity exec <container> /usr/local/bin/base32
$ podman run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base64

```bash
$ singularity exec <container> /usr/local/bin/base64
$ podman run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basename

```bash
$ singularity exec <container> /usr/local/bin/basename
$ podman run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basenc

```bash
$ singularity exec <container> /usr/local/bin/basenc
$ podman run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### cat

```bash
$ singularity exec <container> /usr/local/bin/cat
$ podman run --it --rm --entrypoint /usr/local/bin/cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cat   -v ${PWD} -w ${PWD} <container> -c " $@"
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