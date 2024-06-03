---
layout: container
name:  "quay.io/biocontainers/arem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/arem/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/arem/container.yaml"
updated_at: "2024-06-03 03:10:38.435853"
latest: "1.0.1--py_2"
container_url: "https://biocontainers.pro/tools/arem"
aliases:
 - "arem"
 - "elandexport2bed"
 - "elandmulti2bed"
 - "elandresult2bed"
 - "wignorm"
 - "sam2bed"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "1.0.1--py_2"
description: "shpc-registry automated BioContainers addition for arem"
config: {"url": "https://biocontainers.pro/tools/arem", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for arem", "latest": {"1.0.1--py_2": "sha256:5ece1f39bf600242edaa5245363e30e09649e41126bbc48a1082112eb14e3686"}, "tags": {"1.0.1--py_2": "sha256:5ece1f39bf600242edaa5245363e30e09649e41126bbc48a1082112eb14e3686"}, "docker": "quay.io/biocontainers/arem", "aliases": {"arem": "/usr/local/bin/arem", "elandexport2bed": "/usr/local/bin/elandexport2bed", "elandmulti2bed": "/usr/local/bin/elandmulti2bed", "elandresult2bed": "/usr/local/bin/elandresult2bed", "wignorm": "/usr/local/bin/wignorm", "sam2bed": "/usr/local/bin/sam2bed", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/arem.
shpc-registry automated BioContainers addition for arem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/arem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/arem:1.0.1--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/arem/1.0.1--py_2
$ module help quay.io/biocontainers/arem/1.0.1--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### arem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### arem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### arem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### arem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### arem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### arem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### arem

```bash
$ singularity exec <container> /usr/local/bin/arem
$ podman run --it --rm --entrypoint /usr/local/bin/arem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elandexport2bed

```bash
$ singularity exec <container> /usr/local/bin/elandexport2bed
$ podman run --it --rm --entrypoint /usr/local/bin/elandexport2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elandexport2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elandmulti2bed

```bash
$ singularity exec <container> /usr/local/bin/elandmulti2bed
$ podman run --it --rm --entrypoint /usr/local/bin/elandmulti2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elandmulti2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elandresult2bed

```bash
$ singularity exec <container> /usr/local/bin/elandresult2bed
$ podman run --it --rm --entrypoint /usr/local/bin/elandresult2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elandresult2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wignorm

```bash
$ singularity exec <container> /usr/local/bin/wignorm
$ podman run --it --rm --entrypoint /usr/local/bin/wignorm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wignorm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam2bed

```bash
$ singularity exec <container> /usr/local/bin/sam2bed
$ podman run --it --rm --entrypoint /usr/local/bin/sam2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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