---
layout: container
name:  "quay.io/biocontainers/gfastats"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gfastats/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gfastats/container.yaml"
updated_at: "2025-07-26 04:14:34.609390"
latest: "1.3.11--h077b44d_0"
container_url: "https://biocontainers.pro/tools/gfastats"
aliases:
 - "gfastats"
versions:
 - "1.3.5--hd03093a_0"
 - "1.3.6--hd03093a_0"
 - "1.3.6--hd03093a_1"
 - "1.3.6--hdcf5f25_3"
 - "1.3.7--hdcf5f25_1"
 - "1.3.8--hdcf5f25_1"
 - "1.3.9--hdcf5f25_0"
 - "1.3.9--h077b44d_1"
 - "1.3.10--h077b44d_0"
 - "1.3.11--h077b44d_0"
description: "shpc-registry automated BioContainers addition for gfastats"
config: {"url": "https://biocontainers.pro/tools/gfastats", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gfastats", "latest": {"1.3.11--h077b44d_0": "sha256:f4903ca4ed682bca6c192cac13f9b0355f149947a7cf3e53bbd2580f3a50bdd7"}, "tags": {"1.3.5--hd03093a_0": "sha256:0588b0114f6e092cd9492b2f0b5f160cc6b59b001d9ee8929c4b48b13fec0e77", "1.3.6--hd03093a_0": "sha256:a36354ca9f8fe248c5c950ba6cfdcdf4003841b4fa8a3d7b066fb60a81713ad6", "1.3.6--hd03093a_1": "sha256:7624199684f85df94d91b55a8b7561a11bc0aac33ef6c20309c087d0fd532cae", "1.3.6--hdcf5f25_3": "sha256:5ed545e0ac3c114ba262ba736a4c865f9d44b14cea131e4a11224a5e2b06f6eb", "1.3.7--hdcf5f25_1": "sha256:1611759abd36d92bb083b9b5539ccbbddb0de6d90443c695947ba20a115cb611", "1.3.8--hdcf5f25_1": "sha256:4133ec485bbddc10e90a067ec1eee115b8b92a191edb8e2651b62498971fcccc", "1.3.9--hdcf5f25_0": "sha256:bd5cd9e372372a87d3e2d4c42d1e83eb9abe76a6c801321add1c809c64a0e4da", "1.3.9--h077b44d_1": "sha256:f202d8ad6aa9b854a5104a4bf3ae56386daad9b5a8e912f2d681e63b830ffef6", "1.3.10--h077b44d_0": "sha256:c9845f1572600515e3a3ebfcc88411ac0377808938913bfd977e8bd9d8ea7cac", "1.3.11--h077b44d_0": "sha256:f4903ca4ed682bca6c192cac13f9b0355f149947a7cf3e53bbd2580f3a50bdd7"}, "docker": "quay.io/biocontainers/gfastats", "aliases": {"gfastats": "/usr/local/bin/gfastats"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gfastats.
shpc-registry automated BioContainers addition for gfastats
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gfastats
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gfastats:1.3.11--h077b44d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gfastats/1.3.11--h077b44d_0
$ module help quay.io/biocontainers/gfastats/1.3.11--h077b44d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gfastats-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gfastats-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gfastats-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gfastats-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gfastats-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gfastats-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gfastats

```bash
$ singularity exec <container> /usr/local/bin/gfastats
$ podman run --it --rm --entrypoint /usr/local/bin/gfastats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfastats   -v ${PWD} -w ${PWD} <container> -c " $@"
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