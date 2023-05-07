---
layout: container
name:  "quay.io/biocontainers/manta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/manta/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/manta/container.yaml"
updated_at: "2023-05-07 03:18:27.499823"
latest: "1.6.0--h9ee0642_2"
container_url: "https://biocontainers.pro/tools/manta"
aliases:
 - "configManta.py"
 - "convertInversion.py"
 - "denovo_scoring.py"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "1.6.0--h9ee0642_2"
description: "shpc-registry automated BioContainers addition for manta"
config: {"url": "https://biocontainers.pro/tools/manta", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for manta", "latest": {"1.6.0--h9ee0642_2": "sha256:021aabe5f7314e02e60722c559f6f3c4bb6b1118c2e2ec0eb3095a8c7e431f26"}, "tags": {"1.6.0--h9ee0642_2": "sha256:021aabe5f7314e02e60722c559f6f3c4bb6b1118c2e2ec0eb3095a8c7e431f26"}, "docker": "quay.io/biocontainers/manta", "aliases": {"configManta.py": "/usr/local/bin/configManta.py", "convertInversion.py": "/usr/local/bin/convertInversion.py", "denovo_scoring.py": "/usr/local/bin/denovo_scoring.py", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/manta.
shpc-registry automated BioContainers addition for manta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/manta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/manta:1.6.0--h9ee0642_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/manta/1.6.0--h9ee0642_2
$ module help quay.io/biocontainers/manta/1.6.0--h9ee0642_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### manta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### manta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### manta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### manta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### manta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### manta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### configManta.py

```bash
$ singularity exec <container> /usr/local/bin/configManta.py
$ podman run --it --rm --entrypoint /usr/local/bin/configManta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/configManta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertInversion.py

```bash
$ singularity exec <container> /usr/local/bin/convertInversion.py
$ podman run --it --rm --entrypoint /usr/local/bin/convertInversion.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertInversion.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### denovo_scoring.py

```bash
$ singularity exec <container> /usr/local/bin/denovo_scoring.py
$ podman run --it --rm --entrypoint /usr/local/bin/denovo_scoring.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/denovo_scoring.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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