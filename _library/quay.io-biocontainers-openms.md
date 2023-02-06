---
layout: container
name:  "quay.io/biocontainers/openms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/openms/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/openms/container.yaml"
updated_at: "2023-02-06 03:49:31.142221"
latest: "2.8.0--h604f271_4"
container_url: "https://biocontainers.pro/tools/openms"

versions:
 - "2.8.0--h7ca0330_3"
 - "2.8.0--h604f271_4"
description: "shpc-registry automated BioContainers addition for openms"
config: {"url": "https://biocontainers.pro/tools/openms", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for openms", "latest": {"2.8.0--h604f271_4": "sha256:ee39863df3e468d10e1a79e2388a9be848f5c8c3dc1ff1687c97c649309525cd"}, "tags": {"2.8.0--h7ca0330_3": "sha256:37623d295f4fa1808a1e92e31f2ebe402bcb733208a2d05218e31748f0d543d5", "2.8.0--h604f271_4": "sha256:ee39863df3e468d10e1a79e2388a9be848f5c8c3dc1ff1687c97c649309525cd"}, "docker": "quay.io/biocontainers/openms"}
---

This module is a singularity container wrapper for quay.io/biocontainers/openms.
shpc-registry automated BioContainers addition for openms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/openms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/openms:2.8.0--h604f271_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/openms/2.8.0--h604f271_4
$ module help quay.io/biocontainers/openms/2.8.0--h604f271_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### openms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### openms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### openms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### openms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### openms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### openms-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### openms

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