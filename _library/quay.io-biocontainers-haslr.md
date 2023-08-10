---
layout: container
name:  "quay.io/biocontainers/haslr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/haslr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/haslr/container.yaml"
updated_at: "2023-08-10 03:25:43.133063"
latest: "0.8a1--py39hd65a603_4"
container_url: "https://biocontainers.pro/tools/haslr"
aliases:
 - "fastutils"
 - "gatb-h5dump"
 - "haslr.py"
 - "haslr_assemble"
 - "merci"
 - "minia"
 - "minia_nooverlap"
 - "sdust"
 - "paftools.js"
 - "minimap2"
 - "k8"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
versions:
 - "0.8a1--py37h595c7a6_3"
 - "0.8a1--py39hd65a603_4"
description: "shpc-registry automated BioContainers addition for haslr"
config: {"url": "https://biocontainers.pro/tools/haslr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for haslr", "latest": {"0.8a1--py39hd65a603_4": "sha256:3302dcd3728b48dae013c9750ce0e735b16daf10a23118b346b2d2f60dd0e7e0"}, "tags": {"0.8a1--py37h595c7a6_3": "sha256:ac6f248384731e4a987f9115632a820f3d9ce78f412fc68df7382dc0cb1ab5b3", "0.8a1--py39hd65a603_4": "sha256:3302dcd3728b48dae013c9750ce0e735b16daf10a23118b346b2d2f60dd0e7e0"}, "docker": "quay.io/biocontainers/haslr", "aliases": {"fastutils": "/usr/local/bin/fastutils", "gatb-h5dump": "/usr/local/bin/gatb-h5dump", "haslr.py": "/usr/local/bin/haslr.py", "haslr_assemble": "/usr/local/bin/haslr_assemble", "merci": "/usr/local/bin/merci", "minia": "/usr/local/bin/minia", "minia_nooverlap": "/usr/local/bin/minia_nooverlap", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "k8": "/usr/local/bin/k8", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/haslr.
shpc-registry automated BioContainers addition for haslr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/haslr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/haslr:0.8a1--py39hd65a603_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/haslr/0.8a1--py39hd65a603_4
$ module help quay.io/biocontainers/haslr/0.8a1--py39hd65a603_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### haslr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### haslr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### haslr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### haslr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### haslr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### haslr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastutils

```bash
$ singularity exec <container> /usr/local/bin/fastutils
$ podman run --it --rm --entrypoint /usr/local/bin/fastutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatb-h5dump

```bash
$ singularity exec <container> /usr/local/bin/gatb-h5dump
$ podman run --it --rm --entrypoint /usr/local/bin/gatb-h5dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatb-h5dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### haslr.py

```bash
$ singularity exec <container> /usr/local/bin/haslr.py
$ podman run --it --rm --entrypoint /usr/local/bin/haslr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haslr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### haslr_assemble

```bash
$ singularity exec <container> /usr/local/bin/haslr_assemble
$ podman run --it --rm --entrypoint /usr/local/bin/haslr_assemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haslr_assemble   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merci

```bash
$ singularity exec <container> /usr/local/bin/merci
$ podman run --it --rm --entrypoint /usr/local/bin/merci   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merci   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minia

```bash
$ singularity exec <container> /usr/local/bin/minia
$ podman run --it --rm --entrypoint /usr/local/bin/minia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minia   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minia_nooverlap

```bash
$ singularity exec <container> /usr/local/bin/minia_nooverlap
$ podman run --it --rm --entrypoint /usr/local/bin/minia_nooverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minia_nooverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m

```bash
$ singularity exec <container> /usr/local/bin/python3.7m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
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