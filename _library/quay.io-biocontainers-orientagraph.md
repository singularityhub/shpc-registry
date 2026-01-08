---
layout: container
name:  "quay.io/biocontainers/orientagraph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/orientagraph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/orientagraph/container.yaml"
updated_at: "2026-01-08 03:43:35.139484"
latest: "1.1--hb66fcc3_6"
container_url: "https://biocontainers.pro/tools/orientagraph"
aliases:
 - "f4ratio"
 - "fourpop"
 - "orientagraph"
 - "threepop"
versions:
 - "1.1--h52d0f6c_2"
 - "1.1--hcfb5669_4"
 - "1.1--h4dfc31f_5"
 - "1.1--hb66fcc3_6"
description: "shpc-registry automated BioContainers addition for orientagraph"
config: {"url": "https://biocontainers.pro/tools/orientagraph", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for orientagraph", "latest": {"1.1--hb66fcc3_6": "sha256:d70f6eba56ff2efc735896906b0369cf877700e1b14723aed9728ce66c471ba4"}, "tags": {"1.1--h52d0f6c_2": "sha256:9ca4f01a89ed40ecaf9560cc77b80cfbe204b590141a1c07730f3d6eaa1e3e92", "1.1--hcfb5669_4": "sha256:35af31c4fd287935c64e59546fc4d37e70f21176a0fc93cb9ea6ef5811419447", "1.1--h4dfc31f_5": "sha256:ac54bdc7ce1ba1e3b4d8c21d3a82d5946a735516d88686007fe719f68defe1a9", "1.1--hb66fcc3_6": "sha256:d70f6eba56ff2efc735896906b0369cf877700e1b14723aed9728ce66c471ba4"}, "docker": "quay.io/biocontainers/orientagraph", "aliases": {"f4ratio": "/usr/local/bin/f4ratio", "fourpop": "/usr/local/bin/fourpop", "orientagraph": "/usr/local/bin/orientagraph", "threepop": "/usr/local/bin/threepop"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/orientagraph.
shpc-registry automated BioContainers addition for orientagraph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/orientagraph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/orientagraph:1.1--hb66fcc3_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/orientagraph/1.1--hb66fcc3_6
$ module help quay.io/biocontainers/orientagraph/1.1--hb66fcc3_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### orientagraph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### orientagraph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### orientagraph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### orientagraph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### orientagraph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### orientagraph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### f4ratio

```bash
$ singularity exec <container> /usr/local/bin/f4ratio
$ podman run --it --rm --entrypoint /usr/local/bin/f4ratio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f4ratio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fourpop

```bash
$ singularity exec <container> /usr/local/bin/fourpop
$ podman run --it --rm --entrypoint /usr/local/bin/fourpop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fourpop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orientagraph

```bash
$ singularity exec <container> /usr/local/bin/orientagraph
$ podman run --it --rm --entrypoint /usr/local/bin/orientagraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orientagraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### threepop

```bash
$ singularity exec <container> /usr/local/bin/threepop
$ podman run --it --rm --entrypoint /usr/local/bin/threepop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/threepop   -v ${PWD} -w ${PWD} <container> -c " $@"
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