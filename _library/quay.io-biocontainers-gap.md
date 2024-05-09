---
layout: container
name:  "quay.io/biocontainers/gap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gap/container.yaml"
updated_at: "2024-05-09 02:46:20.532343"
latest: "4.8.10--0"
container_url: "https://biocontainers.pro/tools/gap"

versions:
 - "4.8.10--0"
description: "shpc-registry automated BioContainers addition for gap"
config: {"url": "https://biocontainers.pro/tools/gap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gap", "latest": {"4.8.10--0": "sha256:1d991acc7f47d073a1caba9ed30a9e64117dc7dacf9e139b48d63f947f8e2eaa"}, "tags": {"4.8.10--0": "sha256:1d991acc7f47d073a1caba9ed30a9e64117dc7dacf9e139b48d63f947f8e2eaa"}, "docker": "quay.io/biocontainers/gap"}
---

This module is a singularity container wrapper for quay.io/biocontainers/gap.
shpc-registry automated BioContainers addition for gap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gap:4.8.10--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gap/4.8.10--0
$ module help quay.io/biocontainers/gap/4.8.10--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### gap

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