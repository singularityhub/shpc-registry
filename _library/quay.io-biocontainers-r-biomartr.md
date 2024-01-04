---
layout: container
name:  "quay.io/biocontainers/r-biomartr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-biomartr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-biomartr/container.yaml"
updated_at: "2024-01-04 02:47:35.498427"
latest: "1.0.7--r43h3342da4_0"
container_url: "https://biocontainers.pro/tools/r-biomartr"

versions:
 - "1.0.2--r41h3342da4_0"
 - "1.0.2--r42h3342da4_1"
 - "1.0.3--r42h3342da4_0"
 - "1.0.4--r43h3342da4_1"
 - "1.0.6--r43h3342da4_0"
 - "1.0.7--r43h3342da4_0"
description: "shpc-registry automated BioContainers addition for r-biomartr"
config: {"url": "https://biocontainers.pro/tools/r-biomartr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-biomartr", "latest": {"1.0.7--r43h3342da4_0": "sha256:6a0dfb04094f2ae1f89403915ca3d3eb4bca342b959b6079b219a15774228d07"}, "tags": {"1.0.2--r41h3342da4_0": "sha256:c4135b83551875e0260531672bb71d2edcaad5ae544a6a3424c80540d30d687f", "1.0.2--r42h3342da4_1": "sha256:27a2405009dfdd6e929c47aca82eca7b3ccb7eb7bdbaae7f9e99f69fb7a80593", "1.0.3--r42h3342da4_0": "sha256:68d9ab8aa5ab77077c2fc3f1630510db1f2e00618de93bd6cb611ab15bab4a84", "1.0.4--r43h3342da4_1": "sha256:fdbd722cca7b4c5dbca4b1ccc7c8a3d4da1f9c0668985f5b0f7348336abae8ed", "1.0.6--r43h3342da4_0": "sha256:0fb5081452557f36307d9033110a46ca7559243cb96482a6a61e6f152010102a", "1.0.7--r43h3342da4_0": "sha256:6a0dfb04094f2ae1f89403915ca3d3eb4bca342b959b6079b219a15774228d07"}, "docker": "quay.io/biocontainers/r-biomartr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-biomartr.
shpc-registry automated BioContainers addition for r-biomartr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-biomartr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-biomartr:1.0.7--r43h3342da4_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-biomartr/1.0.7--r43h3342da4_0
$ module help quay.io/biocontainers/r-biomartr/1.0.7--r43h3342da4_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-biomartr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-biomartr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-biomartr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-biomartr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-biomartr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-biomartr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-biomartr

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