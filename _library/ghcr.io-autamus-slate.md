---
layout: container
name:  "ghcr.io/autamus/slate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/slate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/slate/container.yaml"
updated_at: "2023-10-09 03:30:06.622966"
latest: "2022.07.00"
container_url: "https://github.com/orgs/autamus/packages/container/package/slate"

versions:
 - "2021.05.02"
 - "latest"
 - "2022.07.00"
description: "The Software for Linear Algebra Targeting Exascale (SLATE) project is to provide fundamental dense linear algebra capabilities to the US Department of Energy and to the high-performance computing (HPC) community at large."
config: {"docker": "ghcr.io/autamus/slate", "url": "https://github.com/orgs/autamus/packages/container/package/slate", "maintainer": "@vsoch", "description": "The Software for Linear Algebra Targeting Exascale (SLATE) project is to provide fundamental dense linear algebra capabilities to the US Department of Energy and to the high-performance computing (HPC) community at large.", "latest": {"2022.07.00": "sha256:ce16fb0ab895f7b5308895c4cbbc12906013bb981ab1779460a1f3000e20dbce"}, "tags": {"2021.05.02": "sha256:056b567b3909a6cc85ba0e3725812596fdf00543aa4989f7bfbad1324448afaf", "latest": "sha256:ce16fb0ab895f7b5308895c4cbbc12906013bb981ab1779460a1f3000e20dbce", "2022.07.00": "sha256:ce16fb0ab895f7b5308895c4cbbc12906013bb981ab1779460a1f3000e20dbce"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/slate.
The Software for Linear Algebra Targeting Exascale (SLATE) project is to provide fundamental dense linear algebra capabilities to the US Department of Energy and to the high-performance computing (HPC) community at large.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/slate
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/slate:2022.07.00
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/slate/2022.07.00
$ module help ghcr.io/autamus/slate/2022.07.00
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### slate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### slate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### slate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### slate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### slate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### slate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### slate

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