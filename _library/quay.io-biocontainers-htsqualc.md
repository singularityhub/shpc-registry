---
layout: container
name:  "quay.io/biocontainers/htsqualc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/htsqualc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/htsqualc/container.yaml"
updated_at: "2024-10-17 18:55:46.833493"
latest: "1.1--pyhfa5458b_0"
container_url: "https://biocontainers.pro/tools/htsqualc"
aliases:
 - "Filter_Pair.py"
 - "Filter_Single.py"
 - "StatisticPair.py"
 - "StatisticSingle.py"
 - "common_functions.py"
 - "filter.py"
 - "f2py3.9"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
 - "jpgicc"
versions:
 - "1.1--pyhfa5458b_0"
description: "shpc-registry automated BioContainers addition for htsqualc"
config: {"url": "https://biocontainers.pro/tools/htsqualc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for htsqualc", "latest": {"1.1--pyhfa5458b_0": "sha256:8fb234f05447b7e47730165462b3ad0a6d76771fae2d8868297d1cb4f5f31579"}, "tags": {"1.1--pyhfa5458b_0": "sha256:8fb234f05447b7e47730165462b3ad0a6d76771fae2d8868297d1cb4f5f31579"}, "docker": "quay.io/biocontainers/htsqualc", "aliases": {"Filter_Pair.py": "/usr/local/bin/Filter_Pair.py", "Filter_Single.py": "/usr/local/bin/Filter_Single.py", "StatisticPair.py": "/usr/local/bin/StatisticPair.py", "StatisticSingle.py": "/usr/local/bin/StatisticSingle.py", "common_functions.py": "/usr/local/bin/common_functions.py", "filter.py": "/usr/local/bin/filter.py", "f2py3.9": "/usr/local/bin/f2py3.9", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config", "jpgicc": "/usr/local/bin/jpgicc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/htsqualc.
shpc-registry automated BioContainers addition for htsqualc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/htsqualc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/htsqualc:1.1--pyhfa5458b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/htsqualc/1.1--pyhfa5458b_0
$ module help quay.io/biocontainers/htsqualc/1.1--pyhfa5458b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### htsqualc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### htsqualc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### htsqualc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### htsqualc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### htsqualc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### htsqualc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Filter_Pair.py

```bash
$ singularity exec <container> /usr/local/bin/Filter_Pair.py
$ podman run --it --rm --entrypoint /usr/local/bin/Filter_Pair.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Filter_Pair.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Filter_Single.py

```bash
$ singularity exec <container> /usr/local/bin/Filter_Single.py
$ podman run --it --rm --entrypoint /usr/local/bin/Filter_Single.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Filter_Single.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### StatisticPair.py

```bash
$ singularity exec <container> /usr/local/bin/StatisticPair.py
$ podman run --it --rm --entrypoint /usr/local/bin/StatisticPair.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/StatisticPair.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### StatisticSingle.py

```bash
$ singularity exec <container> /usr/local/bin/StatisticSingle.py
$ podman run --it --rm --entrypoint /usr/local/bin/StatisticSingle.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/StatisticSingle.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### common_functions.py

```bash
$ singularity exec <container> /usr/local/bin/common_functions.py
$ podman run --it --rm --entrypoint /usr/local/bin/common_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/common_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter.py

```bash
$ singularity exec <container> /usr/local/bin/filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_compress

```bash
$ singularity exec <container> /usr/local/bin/opj_compress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_decompress

```bash
$ singularity exec <container> /usr/local/bin/opj_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_dump

```bash
$ singularity exec <container> /usr/local/bin/opj_dump
$ podman run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpgicc

```bash
$ singularity exec <container> /usr/local/bin/jpgicc
$ podman run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
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