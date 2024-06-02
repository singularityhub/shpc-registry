---
layout: container
name:  "quay.io/biocontainers/rustynuc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rustynuc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rustynuc/container.yaml"
updated_at: "2024-06-02 03:13:08.448050"
latest: "0.3.1--he4a0461_2"
container_url: "https://biocontainers.pro/tools/rustynuc"
aliases:
 - "rustynuc"
versions:
 - "0.3.1--h7132678_0"
 - "0.3.1--he4a0461_2"
description: "shpc-registry automated BioContainers addition for rustynuc"
config: {"url": "https://biocontainers.pro/tools/rustynuc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rustynuc", "latest": {"0.3.1--he4a0461_2": "sha256:ba22698847146cfef931ecaad44ef1a447b91532220a9fe38a9cd8df072a13b6"}, "tags": {"0.3.1--h7132678_0": "sha256:d3f73cb0fc0d06af1d1629af56019bd83770a7483d879e66457dcbf253b2a8fe", "0.3.1--he4a0461_2": "sha256:ba22698847146cfef931ecaad44ef1a447b91532220a9fe38a9cd8df072a13b6"}, "docker": "quay.io/biocontainers/rustynuc", "aliases": {"rustynuc": "/usr/local/bin/rustynuc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rustynuc.
shpc-registry automated BioContainers addition for rustynuc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rustynuc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rustynuc:0.3.1--he4a0461_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rustynuc/0.3.1--he4a0461_2
$ module help quay.io/biocontainers/rustynuc/0.3.1--he4a0461_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rustynuc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rustynuc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rustynuc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rustynuc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rustynuc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rustynuc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rustynuc

```bash
$ singularity exec <container> /usr/local/bin/rustynuc
$ podman run --it --rm --entrypoint /usr/local/bin/rustynuc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rustynuc   -v ${PWD} -w ${PWD} <container> -c " $@"
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