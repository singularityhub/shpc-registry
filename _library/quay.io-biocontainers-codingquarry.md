---
layout: container
name:  "quay.io/biocontainers/codingquarry"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/codingquarry/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/codingquarry/container.yaml"
updated_at: "2023-10-02 02:46:51.662298"
latest: "2.0--py39h1f90b4d_8"
container_url: "https://biocontainers.pro/tools/codingquarry"
aliases:
 - "CodingQuarry"
 - "CufflinksGTF_to_CodingQuarryGFF3.py"
 - "run_CQ-PM_mine.sh"
 - "run_CQ-PM_stranded.sh"
 - "run_CQ-PM_unstranded.sh"
 - "f2py3.8"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "2.0--py38h4a32c8e_6"
 - "2.0--py39h1f90b4d_8"
description: "shpc-registry automated BioContainers addition for codingquarry"
config: {"url": "https://biocontainers.pro/tools/codingquarry", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for codingquarry", "latest": {"2.0--py39h1f90b4d_8": "sha256:6bce13ef87fb22ace96b8653696836ff8fcb124d0419c245a3b7ba7c51c5b24c"}, "tags": {"2.0--py38h4a32c8e_6": "sha256:4efe1b30b34d49ab74fe0791b3f3fd8b596928ace09bd517e82fb59a541ff8fa", "2.0--py39h1f90b4d_8": "sha256:6bce13ef87fb22ace96b8653696836ff8fcb124d0419c245a3b7ba7c51c5b24c"}, "docker": "quay.io/biocontainers/codingquarry", "aliases": {"CodingQuarry": "/usr/local/bin/CodingQuarry", "CufflinksGTF_to_CodingQuarryGFF3.py": "/usr/local/bin/CufflinksGTF_to_CodingQuarryGFF3.py", "run_CQ-PM_mine.sh": "/usr/local/bin/run_CQ-PM_mine.sh", "run_CQ-PM_stranded.sh": "/usr/local/bin/run_CQ-PM_stranded.sh", "run_CQ-PM_unstranded.sh": "/usr/local/bin/run_CQ-PM_unstranded.sh", "f2py3.8": "/usr/local/bin/f2py3.8", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/codingquarry.
shpc-registry automated BioContainers addition for codingquarry
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/codingquarry
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/codingquarry:2.0--py39h1f90b4d_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/codingquarry/2.0--py39h1f90b4d_8
$ module help quay.io/biocontainers/codingquarry/2.0--py39h1f90b4d_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### codingquarry-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### codingquarry-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### codingquarry-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### codingquarry-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### codingquarry-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### codingquarry-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CodingQuarry

```bash
$ singularity exec <container> /usr/local/bin/CodingQuarry
$ podman run --it --rm --entrypoint /usr/local/bin/CodingQuarry   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CodingQuarry   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CufflinksGTF_to_CodingQuarryGFF3.py

```bash
$ singularity exec <container> /usr/local/bin/CufflinksGTF_to_CodingQuarryGFF3.py
$ podman run --it --rm --entrypoint /usr/local/bin/CufflinksGTF_to_CodingQuarryGFF3.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CufflinksGTF_to_CodingQuarryGFF3.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_CQ-PM_mine.sh

```bash
$ singularity exec <container> /usr/local/bin/run_CQ-PM_mine.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_CQ-PM_mine.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_CQ-PM_mine.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_CQ-PM_stranded.sh

```bash
$ singularity exec <container> /usr/local/bin/run_CQ-PM_stranded.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_CQ-PM_stranded.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_CQ-PM_stranded.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_CQ-PM_unstranded.sh

```bash
$ singularity exec <container> /usr/local/bin/run_CQ-PM_unstranded.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_CQ-PM_unstranded.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_CQ-PM_unstranded.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
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