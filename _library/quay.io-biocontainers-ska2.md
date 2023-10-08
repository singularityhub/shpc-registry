---
layout: container
name:  "quay.io/biocontainers/ska2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ska2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ska2/container.yaml"
updated_at: "2023-10-08 02:52:35.376176"
latest: "0.3.2--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/ska2"
aliases:
 - "ska"
versions:
 - "0.2.0--h4349ce8_0"
 - "0.2.3--h4349ce8_0"
 - "0.2.4--h4349ce8_0"
 - "0.3.0--h4349ce8_0"
 - "0.3.2--h4349ce8_0"
description: "singularity registry hpc automated addition for ska2"
config: {"url": "https://biocontainers.pro/tools/ska2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ska2", "latest": {"0.3.2--h4349ce8_0": "sha256:491076aa549182ee018f9c5936b61a6c531ebd66ea557fb3ba9af27aacc5a6a7"}, "tags": {"0.2.0--h4349ce8_0": "sha256:ac907e8f690bb947459c83e6a793a8b4baf053207e9f5de06d0dd43f3ae05ca1", "0.2.3--h4349ce8_0": "sha256:60f227a8f5c22ae96742b973e7efd221df68c1e0d9a88f103dcc1f4d6af57fe3", "0.2.4--h4349ce8_0": "sha256:993a23db4bc0face24c434a117d6d2600131eea07e949a56387b61ec20b327eb", "0.3.0--h4349ce8_0": "sha256:f11078e0975809140b132ff729e70c9fc06b53ed06b3b7c7893d5a0c9002a489", "0.3.2--h4349ce8_0": "sha256:491076aa549182ee018f9c5936b61a6c531ebd66ea557fb3ba9af27aacc5a6a7"}, "docker": "quay.io/biocontainers/ska2", "aliases": {"ska": "/usr/local/bin/ska"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ska2.
singularity registry hpc automated addition for ska2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ska2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ska2:0.3.2--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ska2/0.3.2--h4349ce8_0
$ module help quay.io/biocontainers/ska2/0.3.2--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ska2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ska2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ska2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ska2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ska2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ska2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ska

```bash
$ singularity exec <container> /usr/local/bin/ska
$ podman run --it --rm --entrypoint /usr/local/bin/ska   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ska   -v ${PWD} -w ${PWD} <container> -c " $@"
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