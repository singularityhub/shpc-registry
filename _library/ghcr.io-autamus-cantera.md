---
layout: container
name:  "ghcr.io/autamus/cantera"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/cantera/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/cantera/container.yaml"
updated_at: "2024-11-13 03:57:06.464278"
latest: "2.5.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/cantera"

versions:
 - "2.4.0"
 - "2.5.1"
 - "latest"
description: "Cantera is an open-source collection of object-oriented software tools for problems involving chemical kinetics, thermodynamics, and transport processes."
config: {"docker": "ghcr.io/autamus/cantera", "url": "https://github.com/orgs/autamus/packages/container/package/cantera", "maintainer": "@vsoch", "description": "Cantera is an open-source collection of object-oriented software tools for problems involving chemical kinetics, thermodynamics, and transport processes.", "latest": {"2.5.1": "sha256:779594e546190fb2f309413a39cf58bf0ed4bd1b25219a22507e5986bf77675e"}, "tags": {"2.4.0": "sha256:ad490652d6f83f71cb56b6195f92ec4837671ceafcdb897d66393e564cde9699", "2.5.1": "sha256:779594e546190fb2f309413a39cf58bf0ed4bd1b25219a22507e5986bf77675e", "latest": "sha256:779594e546190fb2f309413a39cf58bf0ed4bd1b25219a22507e5986bf77675e"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/cantera.
Cantera is an open-source collection of object-oriented software tools for problems involving chemical kinetics, thermodynamics, and transport processes.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/cantera
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/cantera:2.5.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/cantera/2.5.1
$ module help ghcr.io/autamus/cantera/2.5.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cantera-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cantera-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cantera-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cantera-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cantera-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cantera-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### cantera

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