---
layout: container
name:  "quay.io/biocontainers/altamisa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/altamisa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/altamisa/container.yaml"
updated_at: "2025-12-07 04:07:40.142792"
latest: "0.3.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/altamisa"
aliases:
 - "isatab2dot"
 - "isatab2isatab"
 - "isatab_validate"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.2.9--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_0"
 - "0.3.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for altamisa"
config: {"url": "https://biocontainers.pro/tools/altamisa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for altamisa", "latest": {"0.3.1--pyhdfd78af_0": "sha256:9e0c446fe1ab5f91a1226ac6b50c351c4e54a6860e1f16d77f81d4d8e6708945"}, "tags": {"0.2.9--pyhdfd78af_0": "sha256:e857a7752e2bd13d1a3e9e1636791075114e00be07f19766b23fcff575d45d08", "0.3.0--pyhdfd78af_0": "sha256:d69b91f49aff346dd43c4fd279be8749570a1e3d86f4daea21fbc7cedc6642d4", "0.3.1--pyhdfd78af_0": "sha256:9e0c446fe1ab5f91a1226ac6b50c351c4e54a6860e1f16d77f81d4d8e6708945"}, "docker": "quay.io/biocontainers/altamisa", "aliases": {"isatab2dot": "/usr/local/bin/isatab2dot", "isatab2isatab": "/usr/local/bin/isatab2isatab", "isatab_validate": "/usr/local/bin/isatab_validate", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/altamisa.
shpc-registry automated BioContainers addition for altamisa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/altamisa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/altamisa:0.3.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/altamisa/0.3.1--pyhdfd78af_0
$ module help quay.io/biocontainers/altamisa/0.3.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### altamisa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### altamisa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### altamisa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### altamisa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### altamisa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### altamisa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### isatab2dot

```bash
$ singularity exec <container> /usr/local/bin/isatab2dot
$ podman run --it --rm --entrypoint /usr/local/bin/isatab2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isatab2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isatab2isatab

```bash
$ singularity exec <container> /usr/local/bin/isatab2isatab
$ podman run --it --rm --entrypoint /usr/local/bin/isatab2isatab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isatab2isatab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isatab_validate

```bash
$ singularity exec <container> /usr/local/bin/isatab_validate
$ podman run --it --rm --entrypoint /usr/local/bin/isatab_validate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isatab_validate   -v ${PWD} -w ${PWD} <container> -c " $@"
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