---
layout: container
name:  "quay.io/biocontainers/stringtie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/stringtie/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/stringtie/container.yaml"
updated_at: "2022-10-27 00:37:52.163012"
latest: "2.2.1--hecb563c_2"
container_url: "https://biocontainers.pro/tools/stringtie"
aliases:
 - "prepDE.py"
 - "stringtie"
versions:
 - "2.2.1--hecb563c_2"
description: "shpc-registry automated BioContainers addition for stringtie"
config: {"url": "https://biocontainers.pro/tools/stringtie", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for stringtie", "latest": {"2.2.1--hecb563c_2": "sha256:8f557d827442a99b264caf623e075f4e3bd4421b2ffc8de69bc45156a076dadf"}, "tags": {"2.2.1--hecb563c_2": "sha256:8f557d827442a99b264caf623e075f4e3bd4421b2ffc8de69bc45156a076dadf"}, "docker": "quay.io/biocontainers/stringtie", "aliases": {"prepDE.py": "/usr/local/bin/prepDE.py", "stringtie": "/usr/local/bin/stringtie"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/stringtie.
shpc-registry automated BioContainers addition for stringtie
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/stringtie
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/stringtie:2.2.1--hecb563c_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/stringtie/2.2.1--hecb563c_2
$ module help quay.io/biocontainers/stringtie/2.2.1--hecb563c_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stringtie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stringtie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stringtie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stringtie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stringtie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stringtie-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### prepDE.py

```bash
$ singularity exec <container> /usr/local/bin/prepDE.py
$ podman run --it --rm --entrypoint /usr/local/bin/prepDE.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepDE.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stringtie

```bash
$ singularity exec <container> /usr/local/bin/stringtie
$ podman run --it --rm --entrypoint /usr/local/bin/stringtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stringtie   -v ${PWD} -w ${PWD} <container> -c " $@"
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