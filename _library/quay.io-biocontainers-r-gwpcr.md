---
layout: container
name:  "quay.io/biocontainers/r-gwpcr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-gwpcr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-gwpcr/container.yaml"
updated_at: "2023-08-26 02:44:15.146441"
latest: "1.0.4--r43h031d066_5"
container_url: "https://biocontainers.pro/tools/r-gwpcr"

versions:
 - "1.0.4--r41hec16e2b_1"
 - "1.0.4--r42hec16e2b_2"
 - "1.0.4--r42h031d066_4"
 - "1.0.4--r43h031d066_5"
description: "shpc-registry automated BioContainers addition for r-gwpcr"
config: {"url": "https://biocontainers.pro/tools/r-gwpcr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-gwpcr", "latest": {"1.0.4--r43h031d066_5": "sha256:ca3c67d8009236446c4a266e1bb29b1affda58f3b84c24719eed89faac976f3f"}, "tags": {"1.0.4--r41hec16e2b_1": "sha256:7fbbf45b37dbb420197fa24ce0e357e5b451a9ffbd07fe891b3c3a02431de45e", "1.0.4--r42hec16e2b_2": "sha256:b0966e176075725c824f72fe88a275fbf48ea1fca2c68315dfa1f8f0555293e0", "1.0.4--r42h031d066_4": "sha256:ea0c4e6ebb482b1ed203fea1e5a64bbd0e59491b772ab2a259ca478cc2466b3a", "1.0.4--r43h031d066_5": "sha256:ca3c67d8009236446c4a266e1bb29b1affda58f3b84c24719eed89faac976f3f"}, "docker": "quay.io/biocontainers/r-gwpcr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-gwpcr.
shpc-registry automated BioContainers addition for r-gwpcr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-gwpcr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-gwpcr:1.0.4--r43h031d066_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-gwpcr/1.0.4--r43h031d066_5
$ module help quay.io/biocontainers/r-gwpcr/1.0.4--r43h031d066_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-gwpcr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-gwpcr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-gwpcr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-gwpcr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-gwpcr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-gwpcr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-gwpcr

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