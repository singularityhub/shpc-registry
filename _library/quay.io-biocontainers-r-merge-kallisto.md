---
layout: container
name:  "quay.io/biocontainers/r-merge-kallisto"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-merge-kallisto/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-merge-kallisto/container.yaml"
updated_at: "2024-12-15 03:31:33.666933"
latest: "0.6--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/r-merge-kallisto"
aliases:
 - "merge_kallisto.R"
 - "rsync-ssl"
 - "rsync"
 - "xxh128sum"
 - "xxh32sum"
 - "xxh64sum"
 - "xxhsum"
 - "basenc"
 - "b2sum"
 - "base32"
 - "base64"
versions:
 - "0.6--hdfd78af_1"
 - "0.6--hdfd78af_2"
 - "0.6--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for r-merge-kallisto"
config: {"url": "https://biocontainers.pro/tools/r-merge-kallisto", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-merge-kallisto", "latest": {"0.6--hdfd78af_3": "sha256:b444998c3540743d8d5bc45d824a6eeab2b84d7504701baa5e3152bf7b8f3082"}, "tags": {"0.6--hdfd78af_1": "sha256:3b4522235d25f421df8b5174f2f7ac3666b3a850aff808a54c2f90de521b8532", "0.6--hdfd78af_2": "sha256:c906dc6421f31614d317fbce605ddcb68fbe5cd08b27d19f4f1edb26a62db9d5", "0.6--hdfd78af_3": "sha256:b444998c3540743d8d5bc45d824a6eeab2b84d7504701baa5e3152bf7b8f3082"}, "docker": "quay.io/biocontainers/r-merge-kallisto", "aliases": {"merge_kallisto.R": "/usr/local/bin/merge_kallisto.R", "rsync-ssl": "/usr/local/bin/rsync-ssl", "rsync": "/usr/local/bin/rsync", "xxh128sum": "/usr/local/bin/xxh128sum", "xxh32sum": "/usr/local/bin/xxh32sum", "xxh64sum": "/usr/local/bin/xxh64sum", "xxhsum": "/usr/local/bin/xxhsum", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-merge-kallisto.
shpc-registry automated BioContainers addition for r-merge-kallisto
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-merge-kallisto
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-merge-kallisto:0.6--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-merge-kallisto/0.6--hdfd78af_3
$ module help quay.io/biocontainers/r-merge-kallisto/0.6--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-merge-kallisto-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-merge-kallisto-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-merge-kallisto-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-merge-kallisto-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-merge-kallisto-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-merge-kallisto-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### merge_kallisto.R

```bash
$ singularity exec <container> /usr/local/bin/merge_kallisto.R
$ podman run --it --rm --entrypoint /usr/local/bin/merge_kallisto.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_kallisto.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsync-ssl

```bash
$ singularity exec <container> /usr/local/bin/rsync-ssl
$ podman run --it --rm --entrypoint /usr/local/bin/rsync-ssl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsync-ssl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsync

```bash
$ singularity exec <container> /usr/local/bin/rsync
$ podman run --it --rm --entrypoint /usr/local/bin/rsync   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsync   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh128sum

```bash
$ singularity exec <container> /usr/local/bin/xxh128sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh128sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh128sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh32sum

```bash
$ singularity exec <container> /usr/local/bin/xxh32sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh32sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh32sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh64sum

```bash
$ singularity exec <container> /usr/local/bin/xxh64sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh64sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh64sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxhsum

```bash
$ singularity exec <container> /usr/local/bin/xxhsum
$ podman run --it --rm --entrypoint /usr/local/bin/xxhsum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxhsum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basenc

```bash
$ singularity exec <container> /usr/local/bin/basenc
$ podman run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
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