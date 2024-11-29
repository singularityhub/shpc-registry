---
layout: container
name:  "ghcr.io/autamus/cabana"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/cabana/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/cabana/container.yaml"
updated_at: "2024-11-29 03:01:32.453519"
latest: "0.5.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/cabana"

versions:
 - "0.3.0"
 - "0.4.0"
 - "latest"
 - "0.5.0"
description: "The Exascale Co-Design Center for Particle Applications Toolkit"
config: {"docker": "ghcr.io/autamus/cabana", "url": "https://github.com/orgs/autamus/packages/container/package/cabana", "maintainer": "@vsoch", "description": "The Exascale Co-Design Center for Particle Applications Toolkit", "latest": {"0.5.0": "sha256:c2e65bc4822e32cfa4d3c8242f2b87a5ff1f7afcaf40eccfba2fb281cccc9bc8"}, "tags": {"0.3.0": "sha256:0869596ab9201f4c5ef1cf91ab99083243a989f21d90547e4b2bfee0df45fab6", "0.4.0": "sha256:dbcdce5fbc0985356fa44028b58609ead795222e2cc5f5887f4e11d57ea4e019", "latest": "sha256:c2e65bc4822e32cfa4d3c8242f2b87a5ff1f7afcaf40eccfba2fb281cccc9bc8", "0.5.0": "sha256:c2e65bc4822e32cfa4d3c8242f2b87a5ff1f7afcaf40eccfba2fb281cccc9bc8"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/cabana.
The Exascale Co-Design Center for Particle Applications Toolkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/cabana
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/cabana:0.5.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/cabana/0.5.0
$ module help ghcr.io/autamus/cabana/0.5.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cabana-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cabana-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cabana-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cabana-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cabana-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cabana-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### cabana

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