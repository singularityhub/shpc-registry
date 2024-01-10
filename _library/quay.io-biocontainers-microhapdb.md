---
layout: container
name:  "quay.io/biocontainers/microhapdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/microhapdb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/microhapdb/container.yaml"
updated_at: "2024-01-10 09:01:52.242628"
latest: "0.11--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/microhapdb"
aliases:
 - "microhapdb"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.7--pyhdfd78af_0"
 - "0.8.2--pyhdfd78af_0"
 - "0.9--pyhdfd78af_0"
 - "0.10--pyhdfd78af_0"
 - "0.11--pyhdfd78af_0"
 - "0.10.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for microhapdb"
config: {"url": "https://biocontainers.pro/tools/microhapdb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for microhapdb", "latest": {"0.11--pyhdfd78af_0": "sha256:b74c7f1d6f18770066d486f7d74961470fcce301d1ab033e8dd65f5f06e0fd32"}, "tags": {"0.7--pyhdfd78af_0": "sha256:b537af27e4611aaa3332259a166cf71859f8bac727148de9ce8a0a7e71207096", "0.8.2--pyhdfd78af_0": "sha256:606621b49405b923998868c992d7c4aff9c17915fe686aac706149300a49318f", "0.9--pyhdfd78af_0": "sha256:208646e48b05f9f021b11ca46fa79375c38d1ee0be463710be8fe9403cc9f0c6", "0.10--pyhdfd78af_0": "sha256:0fb40b539a86536f9542d2e95c3db98be19fb5d1dba0060686476477882c5044", "0.11--pyhdfd78af_0": "sha256:b74c7f1d6f18770066d486f7d74961470fcce301d1ab033e8dd65f5f06e0fd32", "0.10.1--pyhdfd78af_0": "sha256:ad197df96a472ee53118406e367e628a8b4afec9e7feb0740b41398a8b59aa76"}, "docker": "quay.io/biocontainers/microhapdb", "aliases": {"microhapdb": "/usr/local/bin/microhapdb", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/microhapdb.
shpc-registry automated BioContainers addition for microhapdb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/microhapdb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/microhapdb:0.11--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/microhapdb/0.11--pyhdfd78af_0
$ module help quay.io/biocontainers/microhapdb/0.11--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### microhapdb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### microhapdb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### microhapdb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### microhapdb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### microhapdb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### microhapdb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### microhapdb

```bash
$ singularity exec <container> /usr/local/bin/microhapdb
$ podman run --it --rm --entrypoint /usr/local/bin/microhapdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/microhapdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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