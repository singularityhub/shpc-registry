---
layout: container
name:  "quay.io/biocontainers/r-basejump"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-basejump/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-basejump/container.yaml"
updated_at: "2023-11-16 03:27:21.033975"
latest: "0.14.17--r41hdfd78af_2"
container_url: "https://biocontainers.pro/tools/r-basejump"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "0.9.9--r351_0"
 - "0.14.17--r41hdfd78af_2"
 - "0.13.4--r40_0"
 - "0.12.16--r40_0"
 - "0.11.23--r36_0"
 - "0.10.9--r351_1"
description: "shpc-registry automated BioContainers addition for r-basejump"
config: {"url": "https://biocontainers.pro/tools/r-basejump", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-basejump", "latest": {"0.14.17--r41hdfd78af_2": "sha256:1f245e059fb6c0f1eb7620c33eca863ddcab9e7b996174a48206b34d4d20323e"}, "tags": {"0.9.9--r351_0": "sha256:01eaf445ae38a81bac6793680bfc751cdae1827beac4b05756e107c75e4e4bf4", "0.14.17--r41hdfd78af_2": "sha256:1f245e059fb6c0f1eb7620c33eca863ddcab9e7b996174a48206b34d4d20323e", "0.13.4--r40_0": "sha256:21058bd5f181f0fc131a93e3a13251060c3580085edd2918c88098e7906f38ce", "0.12.16--r40_0": "sha256:7c3fcd7e02d85c733b7ef78928bc93bd085279ea89fd460ebbc5fdd60b5a1dbb", "0.11.23--r36_0": "sha256:3d8672de50c4fa3d027f990578c2c2f43bd4c4c5543b1dd387b87f36035431b1", "0.10.9--r351_1": "sha256:b65c3d891f0a2253aa57d18ed985d51347d81090511b15c42e4711d7e9da2d43"}, "docker": "quay.io/biocontainers/r-basejump", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-basejump.
shpc-registry automated BioContainers addition for r-basejump
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-basejump
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-basejump:0.14.17--r41hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-basejump/0.14.17--r41hdfd78af_2
$ module help quay.io/biocontainers/r-basejump/0.14.17--r41hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-basejump-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-basejump-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-basejump-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-basejump-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-basejump-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-basejump-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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