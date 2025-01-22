---
layout: container
name:  "quay.io/biocontainers/xmatchview"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/xmatchview/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/xmatchview/container.yaml"
updated_at: "2025-01-22 03:04:42.735327"
latest: "1.2.5--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/xmatchview"
aliases:
 - "icc2ps"
 - "icclink"
 - "icctrans"
 - "wtpt"
 - "xmatchview-conifer.py"
 - "xmatchview.py"
 - "pilconvert.py"
 - "pildriver.py"
 - "pilfile.py"
 - "pilfont.py"
 - "pilprint.py"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
versions:
 - "v1.1.1--py_0"
 - "1.2.5--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for xmatchview"
config: {"url": "https://biocontainers.pro/tools/xmatchview", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for xmatchview", "latest": {"1.2.5--hdfd78af_1": "sha256:b2b5d13863d1e7636a0d02d19cd351e6bb9de99c96448d9d67bc633df1f3e598"}, "tags": {"v1.1.1--py_0": "sha256:6c2fe5076170b59de866a4dbafe9358919ade94308e4a08bd002e16590360be9", "1.2.5--hdfd78af_1": "sha256:b2b5d13863d1e7636a0d02d19cd351e6bb9de99c96448d9d67bc633df1f3e598"}, "docker": "quay.io/biocontainers/xmatchview", "aliases": {"icc2ps": "/usr/local/bin/icc2ps", "icclink": "/usr/local/bin/icclink", "icctrans": "/usr/local/bin/icctrans", "wtpt": "/usr/local/bin/wtpt", "xmatchview-conifer.py": "/usr/local/bin/xmatchview-conifer.py", "xmatchview.py": "/usr/local/bin/xmatchview.py", "pilconvert.py": "/usr/local/bin/pilconvert.py", "pildriver.py": "/usr/local/bin/pildriver.py", "pilfile.py": "/usr/local/bin/pilfile.py", "pilfont.py": "/usr/local/bin/pilfont.py", "pilprint.py": "/usr/local/bin/pilprint.py", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/xmatchview.
shpc-registry automated BioContainers addition for xmatchview
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/xmatchview
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/xmatchview:1.2.5--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/xmatchview/1.2.5--hdfd78af_1
$ module help quay.io/biocontainers/xmatchview/1.2.5--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xmatchview-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xmatchview-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xmatchview-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xmatchview-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xmatchview-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xmatchview-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### icc2ps

```bash
$ singularity exec <container> /usr/local/bin/icc2ps
$ podman run --it --rm --entrypoint /usr/local/bin/icc2ps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/icc2ps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### icclink

```bash
$ singularity exec <container> /usr/local/bin/icclink
$ podman run --it --rm --entrypoint /usr/local/bin/icclink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/icclink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### icctrans

```bash
$ singularity exec <container> /usr/local/bin/icctrans
$ podman run --it --rm --entrypoint /usr/local/bin/icctrans   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/icctrans   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtpt

```bash
$ singularity exec <container> /usr/local/bin/wtpt
$ podman run --it --rm --entrypoint /usr/local/bin/wtpt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtpt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xmatchview-conifer.py

```bash
$ singularity exec <container> /usr/local/bin/xmatchview-conifer.py
$ podman run --it --rm --entrypoint /usr/local/bin/xmatchview-conifer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmatchview-conifer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xmatchview.py

```bash
$ singularity exec <container> /usr/local/bin/xmatchview.py
$ podman run --it --rm --entrypoint /usr/local/bin/xmatchview.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmatchview.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilconvert.py

```bash
$ singularity exec <container> /usr/local/bin/pilconvert.py
$ podman run --it --rm --entrypoint /usr/local/bin/pilconvert.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilconvert.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pildriver.py

```bash
$ singularity exec <container> /usr/local/bin/pildriver.py
$ podman run --it --rm --entrypoint /usr/local/bin/pildriver.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pildriver.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilfile.py

```bash
$ singularity exec <container> /usr/local/bin/pilfile.py
$ podman run --it --rm --entrypoint /usr/local/bin/pilfile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilfile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilfont.py

```bash
$ singularity exec <container> /usr/local/bin/pilfont.py
$ podman run --it --rm --entrypoint /usr/local/bin/pilfont.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilfont.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilprint.py

```bash
$ singularity exec <container> /usr/local/bin/pilprint.py
$ podman run --it --rm --entrypoint /usr/local/bin/pilprint.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilprint.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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