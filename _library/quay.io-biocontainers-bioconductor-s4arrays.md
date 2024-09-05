---
layout: container
name:  "quay.io/biocontainers/bioconductor-s4arrays"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-s4arrays/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-s4arrays/container.yaml"
updated_at: "2024-09-05 03:25:18.752297"
latest: "1.2.0--r43ha9d7317_2"
container_url: "https://biocontainers.pro/tools/bioconductor-s4arrays"
aliases:
 - "hb-info"
 - "tjbench"
versions:
 - "1.0.4--r43ha9d7317_0"
 - "1.2.0--r43ha9d7317_1"
 - "1.2.0--r43ha9d7317_2"
description: "singularity registry hpc automated addition for bioconductor-s4arrays"
config: {"url": "https://biocontainers.pro/tools/bioconductor-s4arrays", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-s4arrays", "latest": {"1.2.0--r43ha9d7317_2": "sha256:6c912d254720823c28c66603485aed1ca25c5a096322c39d13306e649f56264f"}, "tags": {"1.0.4--r43ha9d7317_0": "sha256:8096e69c943cbc155a07a81147c594ead505e519acfe178913f35b0ba82a03ac", "1.2.0--r43ha9d7317_1": "sha256:387959d5c22569054022cb7366871f59624d23c42c0f11e80d4eb6b14b9a587d", "1.2.0--r43ha9d7317_2": "sha256:6c912d254720823c28c66603485aed1ca25c5a096322c39d13306e649f56264f"}, "docker": "quay.io/biocontainers/bioconductor-s4arrays", "aliases": {"hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-s4arrays.
singularity registry hpc automated addition for bioconductor-s4arrays
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-s4arrays
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-s4arrays:1.2.0--r43ha9d7317_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-s4arrays/1.2.0--r43ha9d7317_2
$ module help quay.io/biocontainers/bioconductor-s4arrays/1.2.0--r43ha9d7317_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-s4arrays-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-s4arrays-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-s4arrays-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-s4arrays-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-s4arrays-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-s4arrays-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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