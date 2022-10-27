---
layout: container
name:  "quay.io/biocontainers/perl-moosex-role-withoverloading"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-moosex-role-withoverloading/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/perl-moosex-role-withoverloading/container.yaml"
updated_at: "2022-10-27 00:54:09.897379"
latest: "0.17--pl5321h9f5acd7_4"
container_url: "https://biocontainers.pro/tools/perl-moosex-role-withoverloading"

versions:
 - "0.17--pl5321h9f5acd7_4"
description: "shpc-registry automated BioContainers addition for perl-moosex-role-withoverloading"
config: {"url": "https://biocontainers.pro/tools/perl-moosex-role-withoverloading", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-moosex-role-withoverloading", "latest": {"0.17--pl5321h9f5acd7_4": "sha256:e33c1aef2328d2f212b969ac25ae65a1d35a4bf88b3eac1d5091b28332642dff"}, "tags": {"0.17--pl5321h9f5acd7_4": "sha256:e33c1aef2328d2f212b969ac25ae65a1d35a4bf88b3eac1d5091b28332642dff"}, "docker": "quay.io/biocontainers/perl-moosex-role-withoverloading"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-moosex-role-withoverloading.
shpc-registry automated BioContainers addition for perl-moosex-role-withoverloading
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-moosex-role-withoverloading
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-moosex-role-withoverloading:0.17--pl5321h9f5acd7_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-moosex-role-withoverloading/0.17--pl5321h9f5acd7_4
$ module help quay.io/biocontainers/perl-moosex-role-withoverloading/0.17--pl5321h9f5acd7_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-moosex-role-withoverloading-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-moosex-role-withoverloading-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-moosex-role-withoverloading-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-moosex-role-withoverloading-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-moosex-role-withoverloading-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-moosex-role-withoverloading-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-moosex-role-withoverloading

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