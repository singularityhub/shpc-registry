---
layout: container
name:  "quay.io/biocontainers/pyprophet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyprophet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyprophet/container.yaml"
updated_at: "2023-04-15 02:46:24.956670"
latest: "2.2.5--py39hbf8eff0_0"
container_url: "https://biocontainers.pro/tools/pyprophet"

versions:
 - "2.1.6--py36h4c5857e_0"
 - "2.1.11--py39hbf8eff0_0"
 - "2.1.12--py39hbf8eff0_0"
 - "2.2.3--py39hbf8eff0_0"
 - "2.2.5--py39hbf8eff0_0"
description: "shpc-registry automated BioContainers addition for pyprophet"
config: {"url": "https://biocontainers.pro/tools/pyprophet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyprophet", "latest": {"2.2.5--py39hbf8eff0_0": "sha256:a04827d322938c6b9ac73c6d72602fc9ef329d4d51b492627a354053be61479c"}, "tags": {"2.1.6--py36h4c5857e_0": "sha256:6e962addd89ee9edbf00f45bfe0b9c3b4042fdc36bc315f253faee88989a0802", "2.1.11--py39hbf8eff0_0": "sha256:d173e6224e2b7678b9b7449bfc68c20c626774daff0255cdcf1e7a5acad269d2", "2.1.12--py39hbf8eff0_0": "sha256:c23dcbf9e72c2a79ccf14819d73f766d7a1a247ad3018e0b43fa669f3b1f0fae", "2.2.3--py39hbf8eff0_0": "sha256:148ca8cd7fd29fb8b76aa4a5b6b357c5d65be23aef2c0ed4e7bf1e483fd01c1d", "2.2.5--py39hbf8eff0_0": "sha256:a04827d322938c6b9ac73c6d72602fc9ef329d4d51b492627a354053be61479c"}, "docker": "quay.io/biocontainers/pyprophet"}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyprophet.
shpc-registry automated BioContainers addition for pyprophet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyprophet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyprophet:2.2.5--py39hbf8eff0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyprophet/2.2.5--py39hbf8eff0_0
$ module help quay.io/biocontainers/pyprophet/2.2.5--py39hbf8eff0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyprophet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyprophet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyprophet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyprophet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyprophet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyprophet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### pyprophet

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