---
layout: container
name:  "quay.io/biocontainers/bioconductor-peacoqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-peacoqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-peacoqc/container.yaml"
updated_at: "2023-10-13 02:42:15.295968"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-peacoqc"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-peacoqc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-peacoqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-peacoqc", "latest": {"1.10.0--r43hdfd78af_0": "sha256:40bf380b8a185dfa05dc41af35f8e8434264fc92b0fdb2ede1806d61db4378a7"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:19fd6b5c66e9ba663c5c22d4b619d484dca29a24b9c050ad6b74e4587710657a", "1.8.0--r42hdfd78af_0": "sha256:dabe0aef3f67ba0fc98d15a1f815e559df1b81d678a78d49e702b9d401d085a0", "1.10.0--r43hdfd78af_0": "sha256:40bf380b8a185dfa05dc41af35f8e8434264fc92b0fdb2ede1806d61db4378a7"}, "docker": "quay.io/biocontainers/bioconductor-peacoqc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-peacoqc.
shpc-registry automated BioContainers addition for bioconductor-peacoqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-peacoqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-peacoqc:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-peacoqc/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-peacoqc/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-peacoqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-peacoqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-peacoqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-peacoqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-peacoqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-peacoqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-peacoqc

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