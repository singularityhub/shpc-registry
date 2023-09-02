---
layout: container
name:  "quay.io/biocontainers/bioconductor-ichip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ichip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ichip/container.yaml"
updated_at: "2023-09-02 03:09:15.632765"
latest: "1.54.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ichip"

versions:
 - "1.48.0--r41hc0cfd56_2"
 - "1.52.0--r42hc0cfd56_0"
 - "1.52.0--r42ha9d7317_1"
 - "1.54.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ichip"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ichip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ichip", "latest": {"1.54.0--r43ha9d7317_0": "sha256:ab972f570d1e2a877afe6a789098ccce62dafb767de41ac6826086d7bfa4fdd4"}, "tags": {"1.48.0--r41hc0cfd56_2": "sha256:5e6174ae3f6499d5e353a9b0290b8194626a586ba9437d840333cd08724de9b1", "1.52.0--r42hc0cfd56_0": "sha256:c972484eba06a756ae1e6dd26a0485c43a3fc1615e0e2d01029592c52a48868e", "1.52.0--r42ha9d7317_1": "sha256:710214e266c5542167e70793c69f2df1919cba3b1923aac278784c5b52d5e3ca", "1.54.0--r43ha9d7317_0": "sha256:ab972f570d1e2a877afe6a789098ccce62dafb767de41ac6826086d7bfa4fdd4"}, "docker": "quay.io/biocontainers/bioconductor-ichip"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ichip.
shpc-registry automated BioContainers addition for bioconductor-ichip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ichip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ichip:1.54.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ichip/1.54.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-ichip/1.54.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ichip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ichip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ichip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ichip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ichip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ichip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ichip

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