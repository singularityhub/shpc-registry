---
layout: container
name:  "quay.io/biocontainers/dnapi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dnapi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dnapi/container.yaml"
updated_at: "2024-12-01 04:04:37.186332"
latest: "1.1--pyh864c0ab_4"
container_url: "https://biocontainers.pro/tools/dnapi"
aliases:
 - "dnapi.py"
 - "qual_offset.py"
 - "qual_trim.py"
 - "to_fasta.py"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "1.1--pyh864c0ab_4"
description: "shpc-registry automated BioContainers addition for dnapi"
config: {"url": "https://biocontainers.pro/tools/dnapi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dnapi", "latest": {"1.1--pyh864c0ab_4": "sha256:8d5ba6fc7128a0938d5242ff8f0a43b43aeba30be3687689310e3ecc56699c95"}, "tags": {"1.1--pyh864c0ab_4": "sha256:8d5ba6fc7128a0938d5242ff8f0a43b43aeba30be3687689310e3ecc56699c95"}, "docker": "quay.io/biocontainers/dnapi", "aliases": {"dnapi.py": "/usr/local/bin/dnapi.py", "qual_offset.py": "/usr/local/bin/qual_offset.py", "qual_trim.py": "/usr/local/bin/qual_trim.py", "to_fasta.py": "/usr/local/bin/to_fasta.py", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dnapi.
shpc-registry automated BioContainers addition for dnapi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dnapi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dnapi:1.1--pyh864c0ab_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dnapi/1.1--pyh864c0ab_4
$ module help quay.io/biocontainers/dnapi/1.1--pyh864c0ab_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dnapi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dnapi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dnapi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dnapi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dnapi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dnapi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dnapi.py

```bash
$ singularity exec <container> /usr/local/bin/dnapi.py
$ podman run --it --rm --entrypoint /usr/local/bin/dnapi.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnapi.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qual_offset.py

```bash
$ singularity exec <container> /usr/local/bin/qual_offset.py
$ podman run --it --rm --entrypoint /usr/local/bin/qual_offset.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qual_offset.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qual_trim.py

```bash
$ singularity exec <container> /usr/local/bin/qual_trim.py
$ podman run --it --rm --entrypoint /usr/local/bin/qual_trim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qual_trim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### to_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/to_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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