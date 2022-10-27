---
layout: container
name:  "quay.io/biocontainers/mimseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mimseq/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mimseq/container.yaml"
updated_at: "2022-10-27 00:49:03.609551"
latest: "1.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mimseq"
aliases:
 - "git2_cli"
 - "gmap_compress"
 - "gmap_reassemble"
 - "gmap_uncompress"
 - "mimseq"
versions:
 - "1.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for mimseq"
config: {"url": "https://biocontainers.pro/tools/mimseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mimseq", "latest": {"1.2--pyhdfd78af_0": "sha256:7f03bf31b08f2b425b4effab2d248b429953b9e4660494265e0a0dcaf8e65262"}, "tags": {"1.2--pyhdfd78af_0": "sha256:7f03bf31b08f2b425b4effab2d248b429953b9e4660494265e0a0dcaf8e65262"}, "docker": "quay.io/biocontainers/mimseq", "aliases": {"git2_cli": "/usr/local/bin/git2_cli", "gmap_compress": "/usr/local/bin/gmap_compress", "gmap_reassemble": "/usr/local/bin/gmap_reassemble", "gmap_uncompress": "/usr/local/bin/gmap_uncompress", "mimseq": "/usr/local/bin/mimseq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mimseq.
shpc-registry automated BioContainers addition for mimseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mimseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mimseq:1.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mimseq/1.2--pyhdfd78af_0
$ module help quay.io/biocontainers/mimseq/1.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mimseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mimseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mimseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mimseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mimseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mimseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### git2_cli

```bash
$ singularity exec <container> /usr/local/bin/git2_cli
$ podman run --it --rm --entrypoint /usr/local/bin/git2_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git2_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_compress

```bash
$ singularity exec <container> /usr/local/bin/gmap_compress
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_reassemble

```bash
$ singularity exec <container> /usr/local/bin/gmap_reassemble
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_reassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_reassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_uncompress

```bash
$ singularity exec <container> /usr/local/bin/gmap_uncompress
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mimseq

```bash
$ singularity exec <container> /usr/local/bin/mimseq
$ podman run --it --rm --entrypoint /usr/local/bin/mimseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mimseq   -v ${PWD} -w ${PWD} <container> -c " $@"
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