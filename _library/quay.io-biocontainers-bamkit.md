---
layout: container
name:  "quay.io/biocontainers/bamkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bamkit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bamkit/container.yaml"
updated_at: "2023-08-29 03:03:43.171801"
latest: "16.07.26--py_0"
container_url: "https://biocontainers.pro/tools/bamkit"
aliases:
 - "bamcleanheader.py"
 - "bamfilterrg.py"
 - "bamgroupreads.py"
 - "bamheadrg.py"
 - "bamlibs.py"
 - "bamtofastq.py"
 - "sectosupp"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "16.07.26--py_0"
description: "shpc-registry automated BioContainers addition for bamkit"
config: {"url": "https://biocontainers.pro/tools/bamkit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bamkit", "latest": {"16.07.26--py_0": "sha256:88fec69401a1fb439f5cffccde7aaca50bc5b9032570b4c5d50710b8deffa723"}, "tags": {"16.07.26--py_0": "sha256:88fec69401a1fb439f5cffccde7aaca50bc5b9032570b4c5d50710b8deffa723"}, "docker": "quay.io/biocontainers/bamkit", "aliases": {"bamcleanheader.py": "/usr/local/bin/bamcleanheader.py", "bamfilterrg.py": "/usr/local/bin/bamfilterrg.py", "bamgroupreads.py": "/usr/local/bin/bamgroupreads.py", "bamheadrg.py": "/usr/local/bin/bamheadrg.py", "bamlibs.py": "/usr/local/bin/bamlibs.py", "bamtofastq.py": "/usr/local/bin/bamtofastq.py", "sectosupp": "/usr/local/bin/sectosupp", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bamkit.
shpc-registry automated BioContainers addition for bamkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bamkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bamkit:16.07.26--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bamkit/16.07.26--py_0
$ module help quay.io/biocontainers/bamkit/16.07.26--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bamkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bamkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bamkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bamkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bamkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bamkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bamcleanheader.py

```bash
$ singularity exec <container> /usr/local/bin/bamcleanheader.py
$ podman run --it --rm --entrypoint /usr/local/bin/bamcleanheader.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamcleanheader.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamfilterrg.py

```bash
$ singularity exec <container> /usr/local/bin/bamfilterrg.py
$ podman run --it --rm --entrypoint /usr/local/bin/bamfilterrg.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamfilterrg.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamgroupreads.py

```bash
$ singularity exec <container> /usr/local/bin/bamgroupreads.py
$ podman run --it --rm --entrypoint /usr/local/bin/bamgroupreads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamgroupreads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamheadrg.py

```bash
$ singularity exec <container> /usr/local/bin/bamheadrg.py
$ podman run --it --rm --entrypoint /usr/local/bin/bamheadrg.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamheadrg.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamlibs.py

```bash
$ singularity exec <container> /usr/local/bin/bamlibs.py
$ podman run --it --rm --entrypoint /usr/local/bin/bamlibs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamlibs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtofastq.py

```bash
$ singularity exec <container> /usr/local/bin/bamtofastq.py
$ podman run --it --rm --entrypoint /usr/local/bin/bamtofastq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtofastq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sectosupp

```bash
$ singularity exec <container> /usr/local/bin/sectosupp
$ podman run --it --rm --entrypoint /usr/local/bin/sectosupp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sectosupp   -v ${PWD} -w ${PWD} <container> -c " $@"
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