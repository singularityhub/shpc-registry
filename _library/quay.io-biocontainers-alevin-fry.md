---
layout: container
name:  "quay.io/biocontainers/alevin-fry"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/alevin-fry/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/alevin-fry/container.yaml"
updated_at: "2024-04-27 03:01:30.810256"
latest: "0.9.0--h919a2d8_0"
container_url: "https://biocontainers.pro/tools/alevin-fry"
aliases:
 - "alevin-fry"
versions:
 - "0.8.0--h9f5acd7_0"
 - "0.8.1--h9f5acd7_0"
 - "0.8.1--h4ac6f70_2"
 - "0.8.2--h4ac6f70_0"
 - "0.9.0--h919a2d8_0"
description: "shpc-registry automated BioContainers addition for alevin-fry"
config: {"url": "https://biocontainers.pro/tools/alevin-fry", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for alevin-fry", "latest": {"0.9.0--h919a2d8_0": "sha256:b99a3420beba60825d0659d585ece2ad82d1e4ce63cbae656dc67dfed79f9f4c"}, "tags": {"0.8.0--h9f5acd7_0": "sha256:9b09ad00fde35fc0a19768c5ba82bc6bf5cbe83afa719eb57654927bc67283cb", "0.8.1--h9f5acd7_0": "sha256:a354dca356ee686930c886ebaf768325870b8133cd6d68b8039631ee4f145ff8", "0.8.1--h4ac6f70_2": "sha256:72c10bfb3688ae80f5ce6827b66090d80af302eaac7c6304749c91073a21f52c", "0.8.2--h4ac6f70_0": "sha256:9a42a6e8fc644f990781c4f5e286f37c73eaeb37aae689f0a2940fbc4242fd34", "0.9.0--h919a2d8_0": "sha256:b99a3420beba60825d0659d585ece2ad82d1e4ce63cbae656dc67dfed79f9f4c"}, "docker": "quay.io/biocontainers/alevin-fry", "aliases": {"alevin-fry": "/usr/local/bin/alevin-fry"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/alevin-fry.
shpc-registry automated BioContainers addition for alevin-fry
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/alevin-fry
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/alevin-fry:0.9.0--h919a2d8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/alevin-fry/0.9.0--h919a2d8_0
$ module help quay.io/biocontainers/alevin-fry/0.9.0--h919a2d8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### alevin-fry-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### alevin-fry-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### alevin-fry-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### alevin-fry-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### alevin-fry-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### alevin-fry-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alevin-fry

```bash
$ singularity exec <container> /usr/local/bin/alevin-fry
$ podman run --it --rm --entrypoint /usr/local/bin/alevin-fry   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alevin-fry   -v ${PWD} -w ${PWD} <container> -c " $@"
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