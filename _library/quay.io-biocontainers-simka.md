---
layout: container
name:  "quay.io/biocontainers/simka"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/simka/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/simka/container.yaml"
updated_at: "2025-04-11 03:20:51.843001"
latest: "1.5.3--h077b44d_5"
container_url: "https://biocontainers.pro/tools/simka"
aliases:
 - "simka"
 - "simkaCount"
 - "simkaCountProcess"
 - "simkaMerge"
 - "simkaMin.py"
 - "simkaMinCore"
 - "simkaMin_update.py"
 - "simkaMin_utils.py"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.5.3--hd03093a_2"
 - "1.5.3--hd03093a_3"
 - "1.5.3--hdcf5f25_4"
 - "1.5.3--h077b44d_5"
description: "shpc-registry automated BioContainers addition for simka"
config: {"url": "https://biocontainers.pro/tools/simka", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for simka", "latest": {"1.5.3--h077b44d_5": "sha256:6674c05dc50fb6b67d002c4d02ef7cf65fbef0ee27f93025bc572a86cf98533b"}, "tags": {"1.5.3--hd03093a_2": "sha256:7e6acc9951a8350da07d006a2b238e81bf5af3db3338a678c2bc55d9b1619c8c", "1.5.3--hd03093a_3": "sha256:4d62cba540ed4cf7b27e6a3abb9c09a5d9b2291a44e2641e3c3d37ee82cf17c7", "1.5.3--hdcf5f25_4": "sha256:65d6b17763573fa05f1dd4d60f5b6b97fc8fc0d67264c86ed630cb385636a0e8", "1.5.3--h077b44d_5": "sha256:6674c05dc50fb6b67d002c4d02ef7cf65fbef0ee27f93025bc572a86cf98533b"}, "docker": "quay.io/biocontainers/simka", "aliases": {"simka": "/usr/local/bin/simka", "simkaCount": "/usr/local/bin/simkaCount", "simkaCountProcess": "/usr/local/bin/simkaCountProcess", "simkaMerge": "/usr/local/bin/simkaMerge", "simkaMin.py": "/usr/local/bin/simkaMin.py", "simkaMinCore": "/usr/local/bin/simkaMinCore", "simkaMin_update.py": "/usr/local/bin/simkaMin_update.py", "simkaMin_utils.py": "/usr/local/bin/simkaMin_utils.py", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/simka.
shpc-registry automated BioContainers addition for simka
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/simka
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/simka:1.5.3--h077b44d_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/simka/1.5.3--h077b44d_5
$ module help quay.io/biocontainers/simka/1.5.3--h077b44d_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### simka-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### simka-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### simka-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### simka-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### simka-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### simka-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### simka

```bash
$ singularity exec <container> /usr/local/bin/simka
$ podman run --it --rm --entrypoint /usr/local/bin/simka   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simka   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simkaCount

```bash
$ singularity exec <container> /usr/local/bin/simkaCount
$ podman run --it --rm --entrypoint /usr/local/bin/simkaCount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simkaCount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simkaCountProcess

```bash
$ singularity exec <container> /usr/local/bin/simkaCountProcess
$ podman run --it --rm --entrypoint /usr/local/bin/simkaCountProcess   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simkaCountProcess   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simkaMerge

```bash
$ singularity exec <container> /usr/local/bin/simkaMerge
$ podman run --it --rm --entrypoint /usr/local/bin/simkaMerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simkaMerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simkaMin.py

```bash
$ singularity exec <container> /usr/local/bin/simkaMin.py
$ podman run --it --rm --entrypoint /usr/local/bin/simkaMin.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simkaMin.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simkaMinCore

```bash
$ singularity exec <container> /usr/local/bin/simkaMinCore
$ podman run --it --rm --entrypoint /usr/local/bin/simkaMinCore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simkaMinCore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simkaMin_update.py

```bash
$ singularity exec <container> /usr/local/bin/simkaMin_update.py
$ podman run --it --rm --entrypoint /usr/local/bin/simkaMin_update.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simkaMin_update.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simkaMin_utils.py

```bash
$ singularity exec <container> /usr/local/bin/simkaMin_utils.py
$ podman run --it --rm --entrypoint /usr/local/bin/simkaMin_utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simkaMin_utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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