---
layout: container
name:  "quay.io/biocontainers/mammal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mammal/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mammal/container.yaml"
updated_at: "2023-03-05 03:35:13.978922"
latest: "1.1.1--h87f3376_0"
container_url: "https://biocontainers.pro/tools/mammal"
aliases:
 - "charfreq"
 - "dgpe"
 - "mammal"
 - "mammal-sigma"
 - "mult-data"
 - "mult-mix-lwt"
versions:
 - "1.1.1--h87f3376_0"
description: "singularity registry hpc automated addition for mammal"
config: {"url": "https://biocontainers.pro/tools/mammal", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mammal", "latest": {"1.1.1--h87f3376_0": "sha256:233eb078fad2e6eb913e2e69ccda7d1cd6cabfa25259022ae44596d94712a6f6"}, "tags": {"1.1.1--h87f3376_0": "sha256:233eb078fad2e6eb913e2e69ccda7d1cd6cabfa25259022ae44596d94712a6f6"}, "docker": "quay.io/biocontainers/mammal", "aliases": {"charfreq": "/usr/local/bin/charfreq", "dgpe": "/usr/local/bin/dgpe", "mammal": "/usr/local/bin/mammal", "mammal-sigma": "/usr/local/bin/mammal-sigma", "mult-data": "/usr/local/bin/mult-data", "mult-mix-lwt": "/usr/local/bin/mult-mix-lwt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mammal.
singularity registry hpc automated addition for mammal
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mammal
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mammal:1.1.1--h87f3376_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mammal/1.1.1--h87f3376_0
$ module help quay.io/biocontainers/mammal/1.1.1--h87f3376_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mammal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mammal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mammal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mammal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mammal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mammal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### charfreq

```bash
$ singularity exec <container> /usr/local/bin/charfreq
$ podman run --it --rm --entrypoint /usr/local/bin/charfreq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/charfreq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dgpe

```bash
$ singularity exec <container> /usr/local/bin/dgpe
$ podman run --it --rm --entrypoint /usr/local/bin/dgpe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dgpe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mammal

```bash
$ singularity exec <container> /usr/local/bin/mammal
$ podman run --it --rm --entrypoint /usr/local/bin/mammal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mammal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mammal-sigma

```bash
$ singularity exec <container> /usr/local/bin/mammal-sigma
$ podman run --it --rm --entrypoint /usr/local/bin/mammal-sigma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mammal-sigma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mult-data

```bash
$ singularity exec <container> /usr/local/bin/mult-data
$ podman run --it --rm --entrypoint /usr/local/bin/mult-data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mult-data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mult-mix-lwt

```bash
$ singularity exec <container> /usr/local/bin/mult-mix-lwt
$ podman run --it --rm --entrypoint /usr/local/bin/mult-mix-lwt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mult-mix-lwt   -v ${PWD} -w ${PWD} <container> -c " $@"
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