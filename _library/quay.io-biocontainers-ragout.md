---
layout: container
name:  "quay.io/biocontainers/ragout"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ragout/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ragout/container.yaml"
updated_at: "2024-04-20 02:56:22.359872"
latest: "2.3--py38h2494328_6"
container_url: "https://biocontainers.pro/tools/ragout"
aliases:
 - "C-Sibelia.py"
 - "Sibelia"
 - "ragout"
 - "ragout-maf2synteny"
 - "ragout-overlap"
 - "snpEffAnnotate.py"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
 - "pyvenv"
versions:
 - "2.3--py36h2ad2d48_4"
 - "2.3--py38h2494328_6"
description: "shpc-registry automated BioContainers addition for ragout"
config: {"url": "https://biocontainers.pro/tools/ragout", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ragout", "latest": {"2.3--py38h2494328_6": "sha256:434a49f523b60736a7ead3ba4d1b359b58e03fee10354ebda815434d9388b7f3"}, "tags": {"2.3--py36h2ad2d48_4": "sha256:f38f9ed228012953b6d21e180b47c6031cc9d727a4cf818ee13d24e1bf77799f", "2.3--py38h2494328_6": "sha256:434a49f523b60736a7ead3ba4d1b359b58e03fee10354ebda815434d9388b7f3"}, "docker": "quay.io/biocontainers/ragout", "aliases": {"C-Sibelia.py": "/usr/local/bin/C-Sibelia.py", "Sibelia": "/usr/local/bin/Sibelia", "ragout": "/usr/local/bin/ragout", "ragout-maf2synteny": "/usr/local/bin/ragout-maf2synteny", "ragout-overlap": "/usr/local/bin/ragout-overlap", "snpEffAnnotate.py": "/usr/local/bin/snpEffAnnotate.py", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ragout.
shpc-registry automated BioContainers addition for ragout
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ragout
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ragout:2.3--py38h2494328_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ragout/2.3--py38h2494328_6
$ module help quay.io/biocontainers/ragout/2.3--py38h2494328_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ragout-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ragout-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ragout-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ragout-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ragout-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ragout-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### C-Sibelia.py

```bash
$ singularity exec <container> /usr/local/bin/C-Sibelia.py
$ podman run --it --rm --entrypoint /usr/local/bin/C-Sibelia.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/C-Sibelia.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Sibelia

```bash
$ singularity exec <container> /usr/local/bin/Sibelia
$ podman run --it --rm --entrypoint /usr/local/bin/Sibelia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Sibelia   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ragout

```bash
$ singularity exec <container> /usr/local/bin/ragout
$ podman run --it --rm --entrypoint /usr/local/bin/ragout   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragout   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ragout-maf2synteny

```bash
$ singularity exec <container> /usr/local/bin/ragout-maf2synteny
$ podman run --it --rm --entrypoint /usr/local/bin/ragout-maf2synteny   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragout-maf2synteny   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ragout-overlap

```bash
$ singularity exec <container> /usr/local/bin/ragout-overlap
$ podman run --it --rm --entrypoint /usr/local/bin/ragout-overlap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragout-overlap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snpEffAnnotate.py

```bash
$ singularity exec <container> /usr/local/bin/snpEffAnnotate.py
$ podman run --it --rm --entrypoint /usr/local/bin/snpEffAnnotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpEffAnnotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.6

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv

```bash
$ singularity exec <container> /usr/local/bin/pyvenv
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
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