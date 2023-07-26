---
layout: container
name:  "quay.io/biocontainers/carnac-lr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/carnac-lr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/carnac-lr/container.yaml"
updated_at: "2023-07-26 02:50:16.201493"
latest: "1.0.0--hdbdd923_4"
container_url: "https://biocontainers.pro/tools/carnac-lr"
aliases:
 - "CARNAC-LR"
 - "CARNAC_to_fasta"
 - "CARNAC_to_fasta.py"
 - "paf_to_CARNAC.py"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.0.0--h87f3376_2"
 - "1.0.0--hdbdd923_4"
description: "shpc-registry automated BioContainers addition for carnac-lr"
config: {"url": "https://biocontainers.pro/tools/carnac-lr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for carnac-lr", "latest": {"1.0.0--hdbdd923_4": "sha256:51c2aa1fda4badc37f0fd5440c6a5f8ff19feb6932c4d9b20c068ae18e4c9f68"}, "tags": {"1.0.0--h87f3376_2": "sha256:6956f76c647d8a8cecd5ab95d15717c4781bb93a2e6332d2eacfefaa31101ffb", "1.0.0--hdbdd923_4": "sha256:51c2aa1fda4badc37f0fd5440c6a5f8ff19feb6932c4d9b20c068ae18e4c9f68"}, "docker": "quay.io/biocontainers/carnac-lr", "aliases": {"CARNAC-LR": "/usr/local/bin/CARNAC-LR", "CARNAC_to_fasta": "/usr/local/bin/CARNAC_to_fasta", "CARNAC_to_fasta.py": "/usr/local/bin/CARNAC_to_fasta.py", "paf_to_CARNAC.py": "/usr/local/bin/paf_to_CARNAC.py", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/carnac-lr.
shpc-registry automated BioContainers addition for carnac-lr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/carnac-lr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/carnac-lr:1.0.0--hdbdd923_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/carnac-lr/1.0.0--hdbdd923_4
$ module help quay.io/biocontainers/carnac-lr/1.0.0--hdbdd923_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### carnac-lr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### carnac-lr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### carnac-lr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### carnac-lr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### carnac-lr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### carnac-lr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CARNAC-LR

```bash
$ singularity exec <container> /usr/local/bin/CARNAC-LR
$ podman run --it --rm --entrypoint /usr/local/bin/CARNAC-LR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CARNAC-LR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CARNAC_to_fasta

```bash
$ singularity exec <container> /usr/local/bin/CARNAC_to_fasta
$ podman run --it --rm --entrypoint /usr/local/bin/CARNAC_to_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CARNAC_to_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CARNAC_to_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/CARNAC_to_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/CARNAC_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CARNAC_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paf_to_CARNAC.py

```bash
$ singularity exec <container> /usr/local/bin/paf_to_CARNAC.py
$ podman run --it --rm --entrypoint /usr/local/bin/paf_to_CARNAC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paf_to_CARNAC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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