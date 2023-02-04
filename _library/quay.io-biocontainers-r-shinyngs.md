---
layout: container
name:  "quay.io/biocontainers/r-shinyngs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-shinyngs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-shinyngs/container.yaml"
updated_at: "2023-02-04 03:25:59.456414"
latest: "1.5.1--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-shinyngs"
aliases:
 - "make_app_from_files.R"
versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.4.2--r42hdfd78af_1"
 - "1.3.2--r41hdfd78af_0"
 - "1.4.2--r42hdfd78af_3"
 - "1.5.1--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-shinyngs"
config: {"url": "https://biocontainers.pro/tools/r-shinyngs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-shinyngs", "latest": {"1.5.1--r42hdfd78af_0": "sha256:264d95da54d2efc272715b255acf3d03a0ce77c608f2acc8c12c63193ca533b0"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:0b2271a598ca51e7099addc4126c557292666b864121fb1a9011c35e919ff79b", "1.4.2--r42hdfd78af_1": "sha256:3330de58c91d3f130fb40ab7bcc3f163b9e33f63af72f511ca90383659b1cdd2", "1.3.2--r41hdfd78af_0": "sha256:f47057276e3e039cde275fab6ab3d5e1e67e7f05f7f3d61810afb613d6521a3b", "1.4.2--r42hdfd78af_3": "sha256:c983dcf329f4ddee9b8cae70b5fc979322f806051cd6b6dfea37390664f0f826", "1.5.1--r42hdfd78af_0": "sha256:264d95da54d2efc272715b255acf3d03a0ce77c608f2acc8c12c63193ca533b0"}, "docker": "quay.io/biocontainers/r-shinyngs", "aliases": {"make_app_from_files.R": "/usr/local/bin/make_app_from_files.R"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-shinyngs.
shpc-registry automated BioContainers addition for r-shinyngs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-shinyngs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-shinyngs:1.5.1--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-shinyngs/1.5.1--r42hdfd78af_0
$ module help quay.io/biocontainers/r-shinyngs/1.5.1--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-shinyngs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-shinyngs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-shinyngs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-shinyngs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-shinyngs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-shinyngs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### make_app_from_files.R

```bash
$ singularity exec <container> /usr/local/bin/make_app_from_files.R
$ podman run --it --rm --entrypoint /usr/local/bin/make_app_from_files.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_app_from_files.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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