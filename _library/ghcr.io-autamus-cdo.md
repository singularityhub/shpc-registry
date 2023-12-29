---
layout: container
name:  "ghcr.io/autamus/cdo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/cdo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/cdo/container.yaml"
updated_at: "2023-12-29 03:06:27.079841"
latest: "2.1.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/cdo"
aliases:
 - "cdo"
versions:
 - "1.9.10"
 - "2.0.0"
 - "2.0.2"
 - "latest"
 - "2.1.0"
description: "CDO is a collection of command line Operators to manipulate and analyse Climate and NWP model Data."
config: {"docker": "ghcr.io/autamus/cdo", "url": "https://github.com/orgs/autamus/packages/container/package/cdo", "maintainer": "@vsoch", "description": "CDO is a collection of command line Operators to manipulate and analyse Climate and NWP model Data.", "latest": {"2.1.0": "sha256:b2b5bfb1191338a9e1b0f49bfe24c9b37b66e50b79f2e759131bf91613c0997d"}, "tags": {"1.9.10": "sha256:eaca37691d65bff0c742ec985a21402fc580ac40b272f5fb4a7c540ee432055f", "2.0.0": "sha256:8c0c87162310ef914c0c48c3fac00c73f4572c1b5e1e10d6c35e54219103e0f7", "2.0.2": "sha256:bf9371003d5c5b82d9461100d2abeda78d6720dd6a003ec6a50a9acae2c5c272", "latest": "sha256:b2b5bfb1191338a9e1b0f49bfe24c9b37b66e50b79f2e759131bf91613c0997d", "2.1.0": "sha256:b2b5bfb1191338a9e1b0f49bfe24c9b37b66e50b79f2e759131bf91613c0997d"}, "aliases": {"cdo": "/opt/view/bin/cdo"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/cdo.
CDO is a collection of command line Operators to manipulate and analyse Climate and NWP model Data.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/cdo
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/cdo:2.1.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/cdo/2.1.0
$ module help ghcr.io/autamus/cdo/2.1.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cdo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cdo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cdo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cdo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cdo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cdo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cdo

```bash
$ singularity exec <container> /opt/view/bin/cdo
$ podman run --it --rm --entrypoint /opt/view/bin/cdo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cdo   -v ${PWD} -w ${PWD} <container> -c " $@"
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