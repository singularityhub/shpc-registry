---
layout: container
name:  "quay.io/biocontainers/rgi_conda_dev"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rgi_conda_dev/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rgi_conda_dev/container.yaml"
updated_at: "2025-05-22 04:02:24.055268"
latest: "3.1.2--py27_1"
container_url: "https://biocontainers.pro/tools/rgi_conda_dev"
aliases:
 - "rgi"
 - "rgi_clean"
 - "rgi_jsonformat"
 - "rgi_jsontab"
 - "rgi_load"
 - "createfontdatachunk.py"
 - "enhancer.py"
 - "explode.py"
 - "gifmaker.py"
 - "painter.py"
 - "player.py"
 - "thresholder.py"
 - "viewer.py"
 - "pilconvert.py"
 - "pildriver.py"
versions:
 - "3.1.2--py27_1"
description: "shpc-registry automated BioContainers addition for rgi_conda_dev"
config: {"url": "https://biocontainers.pro/tools/rgi_conda_dev", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rgi_conda_dev", "latest": {"3.1.2--py27_1": "sha256:1c5fc246773867c14c7e73e0b7b89389841126956e87fe609f5a99cc7a9ce9f0"}, "tags": {"3.1.2--py27_1": "sha256:1c5fc246773867c14c7e73e0b7b89389841126956e87fe609f5a99cc7a9ce9f0"}, "docker": "quay.io/biocontainers/rgi_conda_dev", "aliases": {"rgi": "/usr/local/bin/rgi", "rgi_clean": "/usr/local/bin/rgi_clean", "rgi_jsonformat": "/usr/local/bin/rgi_jsonformat", "rgi_jsontab": "/usr/local/bin/rgi_jsontab", "rgi_load": "/usr/local/bin/rgi_load", "createfontdatachunk.py": "/usr/local/bin/createfontdatachunk.py", "enhancer.py": "/usr/local/bin/enhancer.py", "explode.py": "/usr/local/bin/explode.py", "gifmaker.py": "/usr/local/bin/gifmaker.py", "painter.py": "/usr/local/bin/painter.py", "player.py": "/usr/local/bin/player.py", "thresholder.py": "/usr/local/bin/thresholder.py", "viewer.py": "/usr/local/bin/viewer.py", "pilconvert.py": "/usr/local/bin/pilconvert.py", "pildriver.py": "/usr/local/bin/pildriver.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rgi_conda_dev.
shpc-registry automated BioContainers addition for rgi_conda_dev
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rgi_conda_dev
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rgi_conda_dev:3.1.2--py27_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rgi_conda_dev/3.1.2--py27_1
$ module help quay.io/biocontainers/rgi_conda_dev/3.1.2--py27_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rgi_conda_dev-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rgi_conda_dev-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rgi_conda_dev-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rgi_conda_dev-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rgi_conda_dev-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rgi_conda_dev-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rgi

```bash
$ singularity exec <container> /usr/local/bin/rgi
$ podman run --it --rm --entrypoint /usr/local/bin/rgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgi_clean

```bash
$ singularity exec <container> /usr/local/bin/rgi_clean
$ podman run --it --rm --entrypoint /usr/local/bin/rgi_clean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgi_clean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgi_jsonformat

```bash
$ singularity exec <container> /usr/local/bin/rgi_jsonformat
$ podman run --it --rm --entrypoint /usr/local/bin/rgi_jsonformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgi_jsonformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgi_jsontab

```bash
$ singularity exec <container> /usr/local/bin/rgi_jsontab
$ podman run --it --rm --entrypoint /usr/local/bin/rgi_jsontab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgi_jsontab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgi_load

```bash
$ singularity exec <container> /usr/local/bin/rgi_load
$ podman run --it --rm --entrypoint /usr/local/bin/rgi_load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgi_load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createfontdatachunk.py

```bash
$ singularity exec <container> /usr/local/bin/createfontdatachunk.py
$ podman run --it --rm --entrypoint /usr/local/bin/createfontdatachunk.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createfontdatachunk.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enhancer.py

```bash
$ singularity exec <container> /usr/local/bin/enhancer.py
$ podman run --it --rm --entrypoint /usr/local/bin/enhancer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enhancer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### explode.py

```bash
$ singularity exec <container> /usr/local/bin/explode.py
$ podman run --it --rm --entrypoint /usr/local/bin/explode.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/explode.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifmaker.py

```bash
$ singularity exec <container> /usr/local/bin/gifmaker.py
$ podman run --it --rm --entrypoint /usr/local/bin/gifmaker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifmaker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### painter.py

```bash
$ singularity exec <container> /usr/local/bin/painter.py
$ podman run --it --rm --entrypoint /usr/local/bin/painter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/painter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### player.py

```bash
$ singularity exec <container> /usr/local/bin/player.py
$ podman run --it --rm --entrypoint /usr/local/bin/player.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/player.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### thresholder.py

```bash
$ singularity exec <container> /usr/local/bin/thresholder.py
$ podman run --it --rm --entrypoint /usr/local/bin/thresholder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/thresholder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### viewer.py

```bash
$ singularity exec <container> /usr/local/bin/viewer.py
$ podman run --it --rm --entrypoint /usr/local/bin/viewer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/viewer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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