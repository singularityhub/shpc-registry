---
layout: container
name:  "quay.io/biocontainers/bioconductor-director"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-director/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-director/container.yaml"
updated_at: "2023-08-28 08:50:52.632775"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-director"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-director"
config: {"url": "https://biocontainers.pro/tools/bioconductor-director", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-director", "latest": {"1.26.0--r43hdfd78af_0": "sha256:c89a9091ea5ed0636eedee31f47742ee8516fe62e1eb9d129de5ef73c76b2d0c"}, "tags": {"1.8.0--r351_0": "sha256:f0b06b839bf1e8c21935078af372f8eafccf46ac3799e4fe086f09610521742d", "1.24.0--r42hdfd78af_0": "sha256:6df99390bc47dbe0f3aa2dce4f91d83dd560b69a2515c2a5b800eb8797671f59", "1.20.0--r41hdfd78af_0": "sha256:a77d431bb15ad5f555682ce3b58f521f8a270bf886e2c4d8a2019fce96aef7fd", "1.18.0--r41hdfd78af_0": "sha256:d6b5e9fa4ad3808a497491cd02883d9165cc6b7ee205807e1dd7565ff54065de", "1.16.0--r40hdfd78af_1": "sha256:a48dbfc887b475daa3ac7176d66d29dae50b5ebe431a4fa479ad8e16f8eca9dd", "1.14.0--r40_0": "sha256:f27cc33c07641e19b0f8415773baf23bc37d566308129efcda96440e863ef8a3", "1.26.0--r43hdfd78af_0": "sha256:c89a9091ea5ed0636eedee31f47742ee8516fe62e1eb9d129de5ef73c76b2d0c"}, "docker": "quay.io/biocontainers/bioconductor-director", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-director.
shpc-registry automated BioContainers addition for bioconductor-director
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-director
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-director:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-director/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-director/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-director-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-director-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-director-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-director-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-director-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-director-inspect-deffile:

```bash
$ singularity inspect -d <container>
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