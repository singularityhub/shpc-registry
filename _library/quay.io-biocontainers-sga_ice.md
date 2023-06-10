---
layout: container
name:  "quay.io/biocontainers/sga_ice"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sga_ice/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sga_ice/container.yaml"
updated_at: "2023-06-10 02:57:32.027077"
latest: "1.01--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/sga_ice"
aliases:
 - "SGA-ICE.py"
 - "sga"
 - "sga-astat.py"
 - "sga-bam2de.pl"
 - "sga-mergeDriver.pl"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "bamtools"
 - "python3.1"
versions:
 - "1.01--hdfd78af_0"
description: "singularity registry hpc automated addition for sga_ice"
config: {"url": "https://biocontainers.pro/tools/sga_ice", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sga_ice", "latest": {"1.01--hdfd78af_0": "sha256:e4d6af4ff2a6499d0960eccc4d99f396345d4b2e74cb4ad261f34ca1f006d623"}, "tags": {"1.01--hdfd78af_0": "sha256:e4d6af4ff2a6499d0960eccc4d99f396345d4b2e74cb4ad261f34ca1f006d623"}, "docker": "quay.io/biocontainers/sga_ice", "aliases": {"SGA-ICE.py": "/usr/local/bin/SGA-ICE.py", "sga": "/usr/local/bin/sga", "sga-astat.py": "/usr/local/bin/sga-astat.py", "sga-bam2de.pl": "/usr/local/bin/sga-bam2de.pl", "sga-mergeDriver.pl": "/usr/local/bin/sga-mergeDriver.pl", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "bamtools": "/usr/local/bin/bamtools", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sga_ice.
singularity registry hpc automated addition for sga_ice
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sga_ice
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sga_ice:1.01--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sga_ice/1.01--hdfd78af_0
$ module help quay.io/biocontainers/sga_ice/1.01--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sga_ice-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sga_ice-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sga_ice-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sga_ice-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sga_ice-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sga_ice-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SGA-ICE.py

```bash
$ singularity exec <container> /usr/local/bin/SGA-ICE.py
$ podman run --it --rm --entrypoint /usr/local/bin/SGA-ICE.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SGA-ICE.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sga

```bash
$ singularity exec <container> /usr/local/bin/sga
$ podman run --it --rm --entrypoint /usr/local/bin/sga   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sga   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sga-astat.py

```bash
$ singularity exec <container> /usr/local/bin/sga-astat.py
$ podman run --it --rm --entrypoint /usr/local/bin/sga-astat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sga-astat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sga-bam2de.pl

```bash
$ singularity exec <container> /usr/local/bin/sga-bam2de.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sga-bam2de.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sga-bam2de.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sga-mergeDriver.pl

```bash
$ singularity exec <container> /usr/local/bin/sga-mergeDriver.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sga-mergeDriver.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sga-mergeDriver.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools

```bash
$ singularity exec <container> /usr/local/bin/bamtools
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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