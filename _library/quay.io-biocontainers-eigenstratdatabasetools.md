---
layout: container
name:  "quay.io/biocontainers/eigenstratdatabasetools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/eigenstratdatabasetools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/eigenstratdatabasetools/container.yaml"
updated_at: "2024-01-11 03:00:07.954490"
latest: "1.1.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/eigenstratdatabasetools"
aliases:
 - "eigenstrat_database_tools"
 - "eigenstrat_rename_snps"
 - "eigenstrat_snp_coverage"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.1.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for eigenstratdatabasetools"
config: {"url": "https://biocontainers.pro/tools/eigenstratdatabasetools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for eigenstratdatabasetools", "latest": {"1.1.0--hdfd78af_0": "sha256:4368f3a69bf34122c3c21d5911d488e7273dd66bc7b16b09a06ab8572e69d9cb"}, "tags": {"1.1.0--hdfd78af_0": "sha256:4368f3a69bf34122c3c21d5911d488e7273dd66bc7b16b09a06ab8572e69d9cb"}, "docker": "quay.io/biocontainers/eigenstratdatabasetools", "aliases": {"eigenstrat_database_tools": "/usr/local/bin/eigenstrat_database_tools", "eigenstrat_rename_snps": "/usr/local/bin/eigenstrat_rename_snps", "eigenstrat_snp_coverage": "/usr/local/bin/eigenstrat_snp_coverage", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/eigenstratdatabasetools.
shpc-registry automated BioContainers addition for eigenstratdatabasetools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/eigenstratdatabasetools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/eigenstratdatabasetools:1.1.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/eigenstratdatabasetools/1.1.0--hdfd78af_0
$ module help quay.io/biocontainers/eigenstratdatabasetools/1.1.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### eigenstratdatabasetools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### eigenstratdatabasetools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### eigenstratdatabasetools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### eigenstratdatabasetools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### eigenstratdatabasetools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### eigenstratdatabasetools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### eigenstrat_database_tools

```bash
$ singularity exec <container> /usr/local/bin/eigenstrat_database_tools
$ podman run --it --rm --entrypoint /usr/local/bin/eigenstrat_database_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eigenstrat_database_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eigenstrat_rename_snps

```bash
$ singularity exec <container> /usr/local/bin/eigenstrat_rename_snps
$ podman run --it --rm --entrypoint /usr/local/bin/eigenstrat_rename_snps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eigenstrat_rename_snps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eigenstrat_snp_coverage

```bash
$ singularity exec <container> /usr/local/bin/eigenstrat_snp_coverage
$ podman run --it --rm --entrypoint /usr/local/bin/eigenstrat_snp_coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eigenstrat_snp_coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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