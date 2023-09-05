---
layout: container
name:  "quay.io/biocontainers/r-rphast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-rphast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-rphast/container.yaml"
updated_at: "2023-09-05 02:39:44.988722"
latest: "1.6.9--r42hd0ea4ef_9"
container_url: "https://biocontainers.pro/tools/r-rphast"

versions:
 - "1.6.9--r41h73dbb54_7"
 - "1.6.9--r42hbf250df_8"
 - "1.6.9--r42hd0ea4ef_9"
description: "shpc-registry automated BioContainers addition for r-rphast"
config: {"url": "https://biocontainers.pro/tools/r-rphast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-rphast", "latest": {"1.6.9--r42hd0ea4ef_9": "sha256:0e541eae8d8982e69284bb67ca95735e97c328b3fa21e8460be0701c51d27678"}, "tags": {"1.6.9--r41h73dbb54_7": "sha256:a987114ef42127b565a94bb535ec4d6765d92013d474d60a2cbc7302ddd2bc81", "1.6.9--r42hbf250df_8": "sha256:83350e6b6af3f1c6eb961105140925d8d016aa135a2952c45febf09b0fa88c89", "1.6.9--r42hd0ea4ef_9": "sha256:0e541eae8d8982e69284bb67ca95735e97c328b3fa21e8460be0701c51d27678"}, "docker": "quay.io/biocontainers/r-rphast"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-rphast.
shpc-registry automated BioContainers addition for r-rphast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-rphast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-rphast:1.6.9--r42hd0ea4ef_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-rphast/1.6.9--r42hd0ea4ef_9
$ module help quay.io/biocontainers/r-rphast/1.6.9--r42hd0ea4ef_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-rphast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-rphast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-rphast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-rphast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-rphast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-rphast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-rphast

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