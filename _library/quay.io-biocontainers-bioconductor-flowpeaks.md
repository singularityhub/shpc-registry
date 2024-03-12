---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowpeaks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowpeaks/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowpeaks/container.yaml"
updated_at: "2024-03-12 02:54:24.566037"
latest: "1.48.0--r43h7c4fd5e_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowpeaks"

versions:
 - "1.40.0--r41hd4b0f26_3"
 - "1.44.0--r42hd4b0f26_0"
 - "1.44.0--r42h7c4fd5e_2"
 - "1.46.0--r43h7c4fd5e_0"
 - "1.48.0--r43h7c4fd5e_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowpeaks"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowpeaks", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowpeaks", "latest": {"1.48.0--r43h7c4fd5e_0": "sha256:1964fa38d22a9e48c0a48c3a2a0313c960a022a1755244e11cb80a77616c395e"}, "tags": {"1.40.0--r41hd4b0f26_3": "sha256:c70678760e26f13209281686175015c3dd2f8aa6bc155840984ddd88915bf57c", "1.44.0--r42hd4b0f26_0": "sha256:daeeeb47c13c7a8893efb42822c0a120bde01109b789b6e4e7a235a4e5ba1406", "1.44.0--r42h7c4fd5e_2": "sha256:b4710f6f27ff5f8fb20790a98aa838d07c812e671dd596e4ea85260fd2fc9d88", "1.46.0--r43h7c4fd5e_0": "sha256:57f1798bac0400c09f3e09123877e93046c3d311b63bf30d2a17a6f698df33bf", "1.48.0--r43h7c4fd5e_0": "sha256:1964fa38d22a9e48c0a48c3a2a0313c960a022a1755244e11cb80a77616c395e"}, "docker": "quay.io/biocontainers/bioconductor-flowpeaks"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowpeaks.
shpc-registry automated BioContainers addition for bioconductor-flowpeaks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowpeaks
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowpeaks:1.48.0--r43h7c4fd5e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowpeaks/1.48.0--r43h7c4fd5e_0
$ module help quay.io/biocontainers/bioconductor-flowpeaks/1.48.0--r43h7c4fd5e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowpeaks-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowpeaks-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowpeaks-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowpeaks-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowpeaks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowpeaks-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowpeaks

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