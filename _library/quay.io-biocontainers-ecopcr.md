---
layout: container
name:  "quay.io/biocontainers/ecopcr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ecopcr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ecopcr/container.yaml"
updated_at: "2024-11-21 02:59:41.708702"
latest: "0.5.0--py27_1"
container_url: "https://biocontainers.pro/tools/ecopcr"
aliases:
 - "ecoPCR"
 - "ecoPCRFilter.py"
 - "ecoPCRFormat.py"
 - "ecoSort.py"
 - "ecofind"
 - "ecogrep"
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
 - "0.5.0--py27_1"
description: "shpc-registry automated BioContainers addition for ecopcr"
config: {"url": "https://biocontainers.pro/tools/ecopcr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ecopcr", "latest": {"0.5.0--py27_1": "sha256:a07aa996b16457916b856ab68525ba5011d69b891d546d0cca462a1061fa0930"}, "tags": {"0.5.0--py27_1": "sha256:a07aa996b16457916b856ab68525ba5011d69b891d546d0cca462a1061fa0930"}, "docker": "quay.io/biocontainers/ecopcr", "aliases": {"ecoPCR": "/usr/local/bin/ecoPCR", "ecoPCRFilter.py": "/usr/local/bin/ecoPCRFilter.py", "ecoPCRFormat.py": "/usr/local/bin/ecoPCRFormat.py", "ecoSort.py": "/usr/local/bin/ecoSort.py", "ecofind": "/usr/local/bin/ecofind", "ecogrep": "/usr/local/bin/ecogrep", "createfontdatachunk.py": "/usr/local/bin/createfontdatachunk.py", "enhancer.py": "/usr/local/bin/enhancer.py", "explode.py": "/usr/local/bin/explode.py", "gifmaker.py": "/usr/local/bin/gifmaker.py", "painter.py": "/usr/local/bin/painter.py", "player.py": "/usr/local/bin/player.py", "thresholder.py": "/usr/local/bin/thresholder.py", "viewer.py": "/usr/local/bin/viewer.py", "pilconvert.py": "/usr/local/bin/pilconvert.py", "pildriver.py": "/usr/local/bin/pildriver.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ecopcr.
shpc-registry automated BioContainers addition for ecopcr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ecopcr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ecopcr:0.5.0--py27_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ecopcr/0.5.0--py27_1
$ module help quay.io/biocontainers/ecopcr/0.5.0--py27_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ecopcr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ecopcr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ecopcr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ecopcr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ecopcr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ecopcr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ecoPCR

```bash
$ singularity exec <container> /usr/local/bin/ecoPCR
$ podman run --it --rm --entrypoint /usr/local/bin/ecoPCR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecoPCR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecoPCRFilter.py

```bash
$ singularity exec <container> /usr/local/bin/ecoPCRFilter.py
$ podman run --it --rm --entrypoint /usr/local/bin/ecoPCRFilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecoPCRFilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecoPCRFormat.py

```bash
$ singularity exec <container> /usr/local/bin/ecoPCRFormat.py
$ podman run --it --rm --entrypoint /usr/local/bin/ecoPCRFormat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecoPCRFormat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecoSort.py

```bash
$ singularity exec <container> /usr/local/bin/ecoSort.py
$ podman run --it --rm --entrypoint /usr/local/bin/ecoSort.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecoSort.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecofind

```bash
$ singularity exec <container> /usr/local/bin/ecofind
$ podman run --it --rm --entrypoint /usr/local/bin/ecofind   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecofind   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecogrep

```bash
$ singularity exec <container> /usr/local/bin/ecogrep
$ podman run --it --rm --entrypoint /usr/local/bin/ecogrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecogrep   -v ${PWD} -w ${PWD} <container> -c " $@"
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