---
layout: container
name:  "quay.io/biocontainers/r-facets"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-facets/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-facets/container.yaml"
updated_at: "2025-04-24 03:40:23.826104"
latest: "0.6.2--r44h2761816_7"
container_url: "https://biocontainers.pro/tools/r-facets"

versions:
 - "0.6.2--r41h1107714_1"
 - "0.6.2--r42h1107714_2"
 - "0.6.2--r42h1c9e865_3"
 - "0.6.2--r43haf399aa_4"
 - "0.6.2--r43haf399aa_5"
 - "0.6.2--r43haf399aa_6"
 - "0.6.2--r44h2761816_7"
description: "shpc-registry automated BioContainers addition for r-facets"
config: {"url": "https://biocontainers.pro/tools/r-facets", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-facets", "latest": {"0.6.2--r44h2761816_7": "sha256:d7e2916d1759b7490893b8c712dd691d3fbe2d90998aa476963fd2a3b439dccd"}, "tags": {"0.6.2--r41h1107714_1": "sha256:0e2f95e9cc91ba9e34a9e75ad9164042404ace12c738f7dad145079bb2e53e0a", "0.6.2--r42h1107714_2": "sha256:7e991005daa9b8960682cc80ff9231056bbccdf281ae573870dc2ca773413071", "0.6.2--r42h1c9e865_3": "sha256:74a4a02e9d525f6da118515c893d9fee3f2aa942a0748ed878f009cc415e5ae7", "0.6.2--r43haf399aa_4": "sha256:78e0a1fa7e4aa1922d61669d8b5d9b6427a3a220f4a9856d5e385b2282254c64", "0.6.2--r43haf399aa_5": "sha256:cb588b2787ef85abf5e1cf69b57da23e3743412196edb42dfcf4fbbc61def30d", "0.6.2--r43haf399aa_6": "sha256:86ab6652bf07a913d5a1b77831521b1fb88e7eb9f163d023a43877ff0d9639d1", "0.6.2--r44h2761816_7": "sha256:d7e2916d1759b7490893b8c712dd691d3fbe2d90998aa476963fd2a3b439dccd"}, "docker": "quay.io/biocontainers/r-facets"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-facets.
shpc-registry automated BioContainers addition for r-facets
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-facets
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-facets:0.6.2--r44h2761816_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-facets/0.6.2--r44h2761816_7
$ module help quay.io/biocontainers/r-facets/0.6.2--r44h2761816_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-facets-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-facets-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-facets-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-facets-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-facets-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-facets-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-facets

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