---
layout: container
name:  "quay.io/biocontainers/r-tidyheatmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-tidyheatmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-tidyheatmap/container.yaml"
updated_at: "2025-04-06 03:14:48.080789"
latest: "1.11.6--r44h3121a25_0"
container_url: "https://biocontainers.pro/tools/r-tidyheatmap"

versions:
 - "1.8.1--r42h3121a25_1"
 - "1.8.1--r43h3121a25_2"
 - "1.8.1--r44h3121a25_3"
 - "1.11.4--r44h3121a25_0"
 - "1.11.6--r44h3121a25_0"
description: "singularity registry hpc automated addition for r-tidyheatmap"
config: {"url": "https://biocontainers.pro/tools/r-tidyheatmap", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-tidyheatmap", "latest": {"1.11.6--r44h3121a25_0": "sha256:ce4b25648357c10574ca446e3f525114f245a97a114a7080dfac6f903c3870ee"}, "tags": {"1.8.1--r42h3121a25_1": "sha256:d1ad44848753d459dfca2871b05a69a4988585f6f10faac4a0c06d09af1f526e", "1.8.1--r43h3121a25_2": "sha256:94a741e6a2220c0ca2ee7698b5f479ed96cb5c19d6acbdc9ecff282c6eaff4bb", "1.8.1--r44h3121a25_3": "sha256:bf4bb692d5b6cc8a04769e6a786c7123504a771890aad83bbc0d99a1ab5eb30d", "1.11.4--r44h3121a25_0": "sha256:2d83d45581018e87deecb4b17e0159847b70815832b08786619c4627c7fdc83b", "1.11.6--r44h3121a25_0": "sha256:ce4b25648357c10574ca446e3f525114f245a97a114a7080dfac6f903c3870ee"}, "docker": "quay.io/biocontainers/r-tidyheatmap"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-tidyheatmap.
singularity registry hpc automated addition for r-tidyheatmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-tidyheatmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-tidyheatmap:1.11.6--r44h3121a25_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-tidyheatmap/1.11.6--r44h3121a25_0
$ module help quay.io/biocontainers/r-tidyheatmap/1.11.6--r44h3121a25_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-tidyheatmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-tidyheatmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-tidyheatmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-tidyheatmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-tidyheatmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-tidyheatmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-tidyheatmap

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