---
layout: container
name:  "quay.io/biocontainers/cnvetti"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cnvetti/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cnvetti/container.yaml"
updated_at: "2025-02-18 03:01:31.752519"
latest: "0.2.0--he4cf2ce_0"
container_url: "https://biocontainers.pro/tools/cnvetti"
aliases:
 - "cnvetti"
versions:
 - "0.2.0--he4cf2ce_0"
description: "shpc-registry automated BioContainers addition for cnvetti"
config: {"url": "https://biocontainers.pro/tools/cnvetti", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cnvetti", "latest": {"0.2.0--he4cf2ce_0": "sha256:442a26e94809d83b12027d95c24668dfe2c9daa6b95bc3052f0c6f116cfe953d"}, "tags": {"0.2.0--he4cf2ce_0": "sha256:442a26e94809d83b12027d95c24668dfe2c9daa6b95bc3052f0c6f116cfe953d"}, "docker": "quay.io/biocontainers/cnvetti", "aliases": {"cnvetti": "/usr/local/bin/cnvetti"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cnvetti.
shpc-registry automated BioContainers addition for cnvetti
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cnvetti
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cnvetti:0.2.0--he4cf2ce_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cnvetti/0.2.0--he4cf2ce_0
$ module help quay.io/biocontainers/cnvetti/0.2.0--he4cf2ce_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cnvetti-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cnvetti-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cnvetti-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cnvetti-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cnvetti-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cnvetti-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cnvetti

```bash
$ singularity exec <container> /usr/local/bin/cnvetti
$ podman run --it --rm --entrypoint /usr/local/bin/cnvetti   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cnvetti   -v ${PWD} -w ${PWD} <container> -c " $@"
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