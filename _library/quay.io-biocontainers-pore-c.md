---
layout: container
name:  "quay.io/biocontainers/pore-c"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pore-c/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pore-c/container.yaml"
updated_at: "2022-10-29 05:40:17.988254"
latest: "0.4.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pore-c"
aliases:
 - "intake"
 - "intake-server"
 - "pairtools"
 - "pbgzip"
 - "pore_c"
 - "2to3-3.8"
 - "ace2sam"
 - "b2sum"
 - "bam2pairs"
 - "base32"
 - "base64"
 - "basename"
 - "basenc"
 - "bgzip"
 - "blast2sam.pl"
versions:
 - "0.4.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for pore-c"
config: {"url": "https://biocontainers.pro/tools/pore-c", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pore-c", "latest": {"0.4.0--pyhdfd78af_0": "sha256:9bc2957aef6e59d68f9e4a8b17ae6e1274ea5676b651f3ca11ab63c2e633e894"}, "tags": {"0.4.0--pyhdfd78af_0": "sha256:9bc2957aef6e59d68f9e4a8b17ae6e1274ea5676b651f3ca11ab63c2e633e894"}, "docker": "quay.io/biocontainers/pore-c", "aliases": {"intake": "/usr/local/bin/intake", "intake-server": "/usr/local/bin/intake-server", "pairtools": "/usr/local/bin/pairtools", "pbgzip": "/usr/local/bin/pbgzip", "pore_c": "/usr/local/bin/pore_c", "2to3-3.8": "/usr/local/bin/2to3-3.8", "ace2sam": "/usr/local/bin/ace2sam", "b2sum": "/usr/local/bin/b2sum", "bam2pairs": "/usr/local/bin/bam2pairs", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "basenc": "/usr/local/bin/basenc", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pore-c.
shpc-registry automated BioContainers addition for pore-c
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pore-c
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pore-c:0.4.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pore-c/0.4.0--pyhdfd78af_0
$ module help quay.io/biocontainers/pore-c/0.4.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pore-c-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pore-c-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pore-c-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pore-c-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pore-c-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pore-c-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### intake

```bash
$ singularity exec <container> /usr/local/bin/intake
$ podman run --it --rm --entrypoint /usr/local/bin/intake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intake-server

```bash
$ singularity exec <container> /usr/local/bin/intake-server
$ podman run --it --rm --entrypoint /usr/local/bin/intake-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intake-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pairtools

```bash
$ singularity exec <container> /usr/local/bin/pairtools
$ podman run --it --rm --entrypoint /usr/local/bin/pairtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbgzip

```bash
$ singularity exec <container> /usr/local/bin/pbgzip
$ podman run --it --rm --entrypoint /usr/local/bin/pbgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pore_c

```bash
$ singularity exec <container> /usr/local/bin/pore_c
$ podman run --it --rm --entrypoint /usr/local/bin/pore_c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pore_c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bam2pairs

```bash
$ singularity exec <container> /usr/local/bin/bam2pairs
$ podman run --it --rm --entrypoint /usr/local/bin/bam2pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
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