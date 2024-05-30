---
layout: container
name:  "quay.io/biocontainers/wise2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/wise2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/wise2/container.yaml"
updated_at: "2024-05-30 02:43:17.253098"
latest: "2.4.1--h5c1b0a6_5"
container_url: "https://biocontainers.pro/tools/wise2"
aliases:
 - "dba"
 - "dnal"
 - "estwise"
 - "estwisedb"
 - "genewise"
 - "genewisedb"
 - "promoterwise"
 - "psw"
 - "pswdb"
 - "scanwise"
 - "scanwise_server"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "2.4.1--h40d77a6_1"
 - "2.4.1--h671cb6e_2"
 - "2.4.1--h5c1b0a6_4"
 - "2.4.1--h5c1b0a6_5"
description: "shpc-registry automated BioContainers addition for wise2"
config: {"url": "https://biocontainers.pro/tools/wise2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for wise2", "latest": {"2.4.1--h5c1b0a6_5": "sha256:3635bd61e101cc0897d077d5da7a111c3e5cdcd78eb3541d36f17a1742dda2cf"}, "tags": {"2.4.1--h40d77a6_1": "sha256:9541d66cc07102b1cbb0b8252f3cd8fe2d575788d55248b1a9d5b899d7223059", "2.4.1--h671cb6e_2": "sha256:907a57932131980e099f625c821284af8511caa603bba04b8c0f3a5399f43432", "2.4.1--h5c1b0a6_4": "sha256:cab57c48ef42f76bc933afad56af4a14ab9664c8ffe1d968e3c4cad739ebc906", "2.4.1--h5c1b0a6_5": "sha256:3635bd61e101cc0897d077d5da7a111c3e5cdcd78eb3541d36f17a1742dda2cf"}, "docker": "quay.io/biocontainers/wise2", "aliases": {"dba": "/usr/local/bin/dba", "dnal": "/usr/local/bin/dnal", "estwise": "/usr/local/bin/estwise", "estwisedb": "/usr/local/bin/estwisedb", "genewise": "/usr/local/bin/genewise", "genewisedb": "/usr/local/bin/genewisedb", "promoterwise": "/usr/local/bin/promoterwise", "psw": "/usr/local/bin/psw", "pswdb": "/usr/local/bin/pswdb", "scanwise": "/usr/local/bin/scanwise", "scanwise_server": "/usr/local/bin/scanwise_server", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/wise2.
shpc-registry automated BioContainers addition for wise2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/wise2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/wise2:2.4.1--h5c1b0a6_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/wise2/2.4.1--h5c1b0a6_5
$ module help quay.io/biocontainers/wise2/2.4.1--h5c1b0a6_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### wise2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### wise2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### wise2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### wise2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### wise2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### wise2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dba

```bash
$ singularity exec <container> /usr/local/bin/dba
$ podman run --it --rm --entrypoint /usr/local/bin/dba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnal

```bash
$ singularity exec <container> /usr/local/bin/dnal
$ podman run --it --rm --entrypoint /usr/local/bin/dnal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estwise

```bash
$ singularity exec <container> /usr/local/bin/estwise
$ podman run --it --rm --entrypoint /usr/local/bin/estwise   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estwise   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estwisedb

```bash
$ singularity exec <container> /usr/local/bin/estwisedb
$ podman run --it --rm --entrypoint /usr/local/bin/estwisedb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estwisedb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genewise

```bash
$ singularity exec <container> /usr/local/bin/genewise
$ podman run --it --rm --entrypoint /usr/local/bin/genewise   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genewise   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genewisedb

```bash
$ singularity exec <container> /usr/local/bin/genewisedb
$ podman run --it --rm --entrypoint /usr/local/bin/genewisedb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genewisedb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### promoterwise

```bash
$ singularity exec <container> /usr/local/bin/promoterwise
$ podman run --it --rm --entrypoint /usr/local/bin/promoterwise   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/promoterwise   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psw

```bash
$ singularity exec <container> /usr/local/bin/psw
$ podman run --it --rm --entrypoint /usr/local/bin/psw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pswdb

```bash
$ singularity exec <container> /usr/local/bin/pswdb
$ podman run --it --rm --entrypoint /usr/local/bin/pswdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pswdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanwise

```bash
$ singularity exec <container> /usr/local/bin/scanwise
$ podman run --it --rm --entrypoint /usr/local/bin/scanwise   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanwise   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanwise_server

```bash
$ singularity exec <container> /usr/local/bin/scanwise_server
$ podman run --it --rm --entrypoint /usr/local/bin/scanwise_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanwise_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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