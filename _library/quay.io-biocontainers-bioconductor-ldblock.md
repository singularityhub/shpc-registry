---
layout: container
name:  "quay.io/biocontainers/bioconductor-ldblock"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ldblock/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ldblock/container.yaml"
updated_at: "2025-07-29 04:36:20.318568"
latest: "1.36.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ldblock"

versions:
 - "1.24.0--r41hdfd78af_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.36.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ldblock"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ldblock", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ldblock", "latest": {"1.36.0--r44hdfd78af_0": "sha256:620be3f3361abf1a14c965d99f5e5815c2e2eec9e16ee3cdf21bcdef1fefa1e1"}, "tags": {"1.24.0--r41hdfd78af_0": "sha256:90723b79084217a6a4342ecee417fff81c260850efe1e5c31f622d16e6d63045", "1.28.0--r42hdfd78af_0": "sha256:a20a42b7f1d8c23698df0bf4158db5dfd276c185ebe008531048a8aadbaa7010", "1.30.0--r43hdfd78af_0": "sha256:4070172ea6550ba7e3fbc09491ec5a08f081f4fd8eebca96afe0bb1fffc62492", "1.32.0--r43hdfd78af_0": "sha256:d36db8015cc705ad505ed203c98414a8afa31ff10d317254748fe64412036848", "1.36.0--r44hdfd78af_0": "sha256:620be3f3361abf1a14c965d99f5e5815c2e2eec9e16ee3cdf21bcdef1fefa1e1"}, "docker": "quay.io/biocontainers/bioconductor-ldblock"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ldblock.
shpc-registry automated BioContainers addition for bioconductor-ldblock
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ldblock
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ldblock:1.36.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ldblock/1.36.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ldblock/1.36.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ldblock-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ldblock-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ldblock-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ldblock-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ldblock-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ldblock-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ldblock

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