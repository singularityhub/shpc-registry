---
layout: container
name:  "quay.io/biocontainers/bioconductor-cellmapperdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cellmapperdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cellmapperdata/container.yaml"
updated_at: "2024-03-25 03:30:34.481940"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cellmapperdata"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cellmapperdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cellmapperdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cellmapperdata", "latest": {"1.28.0--r43hdfd78af_0": "sha256:13e927bb9254bf583676db76c290407f25fbb3082ad5d7f5d5d286e997460c91"}, "tags": {"1.8.0--r351_0": "sha256:d4b477e1338975df01c607d8e2689011173094a13c146cb6b1741549c67d3036", "1.24.0--r42hdfd78af_0": "sha256:ff2f52b867520079d33f7181083dcb3fad69fa8fd04bdcdeb02003bfe226a67f", "1.20.0--r41hdfd78af_1": "sha256:d7557fd06ebbbf87d34a6e54eaecb9ffb03de68b18fcad01a0e8e369762c04c0", "1.18.0--r41hdfd78af_0": "sha256:f25a66944c29eb912659b92fef182a7e92a7e3a771b56ff0ab21a42d0f119292", "1.16.0--r40hdfd78af_1": "sha256:60db6c6714bdef9a9808230ceae44d7b91405a520220ba4243d49f1086c2e5cd", "1.14.0--r40_0": "sha256:bfc29996b52830a1921ab2e79b11fab56b384c4dd64b1bde45d4ad169d1b154d", "1.26.0--r43hdfd78af_0": "sha256:6fb26fe0c0da2b4f745e1a76b6b9af05df9a820672cecb8f79e3e8280fde835d", "1.28.0--r43hdfd78af_0": "sha256:13e927bb9254bf583676db76c290407f25fbb3082ad5d7f5d5d286e997460c91"}, "docker": "quay.io/biocontainers/bioconductor-cellmapperdata", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cellmapperdata.
shpc-registry automated BioContainers addition for bioconductor-cellmapperdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cellmapperdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cellmapperdata:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cellmapperdata/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cellmapperdata/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cellmapperdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellmapperdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellmapperdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cellmapperdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cellmapperdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cellmapperdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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