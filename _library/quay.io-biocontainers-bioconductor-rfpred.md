---
layout: container
name:  "quay.io/biocontainers/bioconductor-rfpred"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rfpred/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rfpred/container.yaml"
updated_at: "2023-10-31 02:37:47.782753"
latest: "1.38.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rfpred"

versions:
 - "1.32.0--r41hc0cfd56_2"
 - "1.36.0--r42hc0cfd56_0"
 - "1.36.0--r42ha9d7317_1"
 - "1.38.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rfpred"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rfpred", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rfpred", "latest": {"1.38.0--r43ha9d7317_0": "sha256:0aceae5bc82fa7ecebf382a0fd5b229220e0306c5be8cf8db5eef09610845051"}, "tags": {"1.32.0--r41hc0cfd56_2": "sha256:28ce1fc75743b112883973adbd2b247369bd70f826d343e1d05158eec501181b", "1.36.0--r42hc0cfd56_0": "sha256:594b365d3344f0a1fd0b4fc621883eafde5f696e5b45140d6d55469430765227", "1.36.0--r42ha9d7317_1": "sha256:8b827d1b0a664bf6460177746b87cc5adbdc41e657695c2415ef68b84e867453", "1.38.0--r43ha9d7317_0": "sha256:0aceae5bc82fa7ecebf382a0fd5b229220e0306c5be8cf8db5eef09610845051"}, "docker": "quay.io/biocontainers/bioconductor-rfpred"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rfpred.
shpc-registry automated BioContainers addition for bioconductor-rfpred
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rfpred
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rfpred:1.38.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rfpred/1.38.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-rfpred/1.38.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rfpred-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rfpred-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rfpred-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rfpred-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rfpred-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rfpred-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rfpred

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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