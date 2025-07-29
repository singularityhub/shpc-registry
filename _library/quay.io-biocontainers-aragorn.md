---
layout: container
name:  "quay.io/biocontainers/aragorn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/aragorn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/aragorn/container.yaml"
updated_at: "2025-07-29 04:21:46.133086"
latest: "1.2.41--h7b50bb2_5"
container_url: "https://biocontainers.pro/tools/aragorn"
aliases:
 - "aragorn"
versions:
 - "1.2.41--hec16e2b_0"
 - "1.2.41--h031d066_1"
 - "1.2.41--h031d066_2"
 - "1.2.41--h031d066_3"
 - "1.2.41--h7b50bb2_4"
 - "1.2.41--h7b50bb2_5"
description: "shpc-registry automated BioContainers addition for aragorn"
config: {"url": "https://biocontainers.pro/tools/aragorn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for aragorn", "latest": {"1.2.41--h7b50bb2_5": "sha256:af8f5d2655ce4ab6dc8e7da72595aa8525fffc692f8f01b95cd9f7f71b328123"}, "tags": {"1.2.41--hec16e2b_0": "sha256:f2861de42c8da62ebf1114c533d681f57e1f93bc8278efc27306b19a192d6bd4", "1.2.41--h031d066_1": "sha256:497f6ebf0e15535856704eb4486b81b4fa6d243a8cb35c22db8ef54cee1c8f98", "1.2.41--h031d066_2": "sha256:52d29a85c9456be32c04f39e704a035fa3270d3b7055bcdd5672ab8802eddfd8", "1.2.41--h031d066_3": "sha256:9da6c131b6023b91a82098d60339f2365b03209b1a60997f0ac709e777283b5b", "1.2.41--h7b50bb2_4": "sha256:c1571fc954cf86a3b19c31fcf0af90cfef3185c79a71a9717f444b91cd50deee", "1.2.41--h7b50bb2_5": "sha256:af8f5d2655ce4ab6dc8e7da72595aa8525fffc692f8f01b95cd9f7f71b328123"}, "docker": "quay.io/biocontainers/aragorn", "aliases": {"aragorn": "/usr/local/bin/aragorn"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/aragorn.
shpc-registry automated BioContainers addition for aragorn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/aragorn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/aragorn:1.2.41--h7b50bb2_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/aragorn/1.2.41--h7b50bb2_5
$ module help quay.io/biocontainers/aragorn/1.2.41--h7b50bb2_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aragorn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aragorn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aragorn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aragorn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aragorn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aragorn-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aragorn

```bash
$ singularity exec <container> /usr/local/bin/aragorn
$ podman run --it --rm --entrypoint /usr/local/bin/aragorn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aragorn   -v ${PWD} -w ${PWD} <container> -c " $@"
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