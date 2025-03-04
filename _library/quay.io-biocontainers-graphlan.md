---
layout: container
name:  "quay.io/biocontainers/graphlan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/graphlan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/graphlan/container.yaml"
updated_at: "2025-03-04 03:28:55.171485"
latest: "1.1.3--2"
container_url: "https://biocontainers.pro/tools/graphlan"
aliases:
 - "__init__.py"
 - "graphlan.py"
 - "graphlan_annotate.py"
 - "graphlan_lib.py"
 - "pyphlan.py"
 - "f2py2"
 - "f2py2.7"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "1.1.3--2"
description: "shpc-registry automated BioContainers addition for graphlan"
config: {"url": "https://biocontainers.pro/tools/graphlan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for graphlan", "latest": {"1.1.3--2": "sha256:f12c86a00d0a956e46f55064bf108135c1467977a2621f4eba897d8abd9263c6"}, "tags": {"1.1.3--2": "sha256:f12c86a00d0a956e46f55064bf108135c1467977a2621f4eba897d8abd9263c6"}, "docker": "quay.io/biocontainers/graphlan", "aliases": {"__init__.py": "/usr/local/bin/__init__.py", "graphlan.py": "/usr/local/bin/graphlan.py", "graphlan_annotate.py": "/usr/local/bin/graphlan_annotate.py", "graphlan_lib.py": "/usr/local/bin/graphlan_lib.py", "pyphlan.py": "/usr/local/bin/pyphlan.py", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/graphlan.
shpc-registry automated BioContainers addition for graphlan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/graphlan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/graphlan:1.1.3--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/graphlan/1.1.3--2
$ module help quay.io/biocontainers/graphlan/1.1.3--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### graphlan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### graphlan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### graphlan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### graphlan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### graphlan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### graphlan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### __init__.py

```bash
$ singularity exec <container> /usr/local/bin/__init__.py
$ podman run --it --rm --entrypoint /usr/local/bin/__init__.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/__init__.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graphlan.py

```bash
$ singularity exec <container> /usr/local/bin/graphlan.py
$ podman run --it --rm --entrypoint /usr/local/bin/graphlan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphlan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graphlan_annotate.py

```bash
$ singularity exec <container> /usr/local/bin/graphlan_annotate.py
$ podman run --it --rm --entrypoint /usr/local/bin/graphlan_annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphlan_annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graphlan_lib.py

```bash
$ singularity exec <container> /usr/local/bin/graphlan_lib.py
$ podman run --it --rm --entrypoint /usr/local/bin/graphlan_lib.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphlan_lib.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyphlan.py

```bash
$ singularity exec <container> /usr/local/bin/pyphlan.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyphlan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyphlan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2.7

```bash
$ singularity exec <container> /usr/local/bin/f2py2.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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