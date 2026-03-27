---
layout: container
name:  "quay.io/biocontainers/siren-rnai"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/siren-rnai/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/siren-rnai/container.yaml"
updated_at: "2026-03-27 05:00:24.307721"
latest: "0.1.9--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/siren-rnai"
aliases:
 - "RNAcalibrate"
 - "RNAeffective"
 - "RNAhybrid"
 - "SIREN"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "bdftogd"
 - "gd2copypal"
 - "gd2togif"
 - "gd2topng"
 - "gdcmpgif"
 - "gdparttopng"
 - "gdtopng"
 - "giftogd2"
 - "pngtogd"
 - "pngtogd2"
 - "webpng"
 - "annotate"
 - "numpy-config"
 - "tqdm"
 - "fonttools"
versions:
 - "0.1.9--pyhdfd78af_0"
description: "singularity registry hpc automated addition for siren-rnai"
config: {"url": "https://biocontainers.pro/tools/siren-rnai", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for siren-rnai", "latest": {"0.1.9--pyhdfd78af_0": "sha256:0c7bc7f7fc38297cc027353d677e8048699138ce476bf16b1e1471aa1ebea18a"}, "tags": {"0.1.9--pyhdfd78af_0": "sha256:0c7bc7f7fc38297cc027353d677e8048699138ce476bf16b1e1471aa1ebea18a"}, "docker": "quay.io/biocontainers/siren-rnai", "aliases": {"RNAcalibrate": "/usr/local/bin/RNAcalibrate", "RNAeffective": "/usr/local/bin/RNAeffective", "RNAhybrid": "/usr/local/bin/RNAhybrid", "SIREN": "/usr/local/bin/SIREN", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "bdftogd": "/usr/local/bin/bdftogd", "gd2copypal": "/usr/local/bin/gd2copypal", "gd2togif": "/usr/local/bin/gd2togif", "gd2topng": "/usr/local/bin/gd2topng", "gdcmpgif": "/usr/local/bin/gdcmpgif", "gdparttopng": "/usr/local/bin/gdparttopng", "gdtopng": "/usr/local/bin/gdtopng", "giftogd2": "/usr/local/bin/giftogd2", "pngtogd": "/usr/local/bin/pngtogd", "pngtogd2": "/usr/local/bin/pngtogd2", "webpng": "/usr/local/bin/webpng", "annotate": "/usr/local/bin/annotate", "numpy-config": "/usr/local/bin/numpy-config", "tqdm": "/usr/local/bin/tqdm", "fonttools": "/usr/local/bin/fonttools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/siren-rnai.
singularity registry hpc automated addition for siren-rnai
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/siren-rnai
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/siren-rnai:0.1.9--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/siren-rnai/0.1.9--pyhdfd78af_0
$ module help quay.io/biocontainers/siren-rnai/0.1.9--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### siren-rnai-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### siren-rnai-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### siren-rnai-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### siren-rnai-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### siren-rnai-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### siren-rnai-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RNAcalibrate

```bash
$ singularity exec <container> /usr/local/bin/RNAcalibrate
$ podman run --it --rm --entrypoint /usr/local/bin/RNAcalibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAcalibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAeffective

```bash
$ singularity exec <container> /usr/local/bin/RNAeffective
$ podman run --it --rm --entrypoint /usr/local/bin/RNAeffective   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAeffective   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAhybrid

```bash
$ singularity exec <container> /usr/local/bin/RNAhybrid
$ podman run --it --rm --entrypoint /usr/local/bin/RNAhybrid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAhybrid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SIREN

```bash
$ singularity exec <container> /usr/local/bin/SIREN
$ podman run --it --rm --entrypoint /usr/local/bin/SIREN   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SIREN   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qconvex

```bash
$ singularity exec <container> /usr/local/bin/qconvex
$ podman run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdelaunay

```bash
$ singularity exec <container> /usr/local/bin/qdelaunay
$ podman run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhalf

```bash
$ singularity exec <container> /usr/local/bin/qhalf
$ podman run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhull

```bash
$ singularity exec <container> /usr/local/bin/qhull
$ podman run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvoronoi

```bash
$ singularity exec <container> /usr/local/bin/qvoronoi
$ podman run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbox

```bash
$ singularity exec <container> /usr/local/bin/rbox
$ podman run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bdftogd

```bash
$ singularity exec <container> /usr/local/bin/bdftogd
$ podman run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gd2copypal

```bash
$ singularity exec <container> /usr/local/bin/gd2copypal
$ podman run --it --rm --entrypoint /usr/local/bin/gd2copypal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gd2copypal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gd2togif

```bash
$ singularity exec <container> /usr/local/bin/gd2togif
$ podman run --it --rm --entrypoint /usr/local/bin/gd2togif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gd2togif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gd2topng

```bash
$ singularity exec <container> /usr/local/bin/gd2topng
$ podman run --it --rm --entrypoint /usr/local/bin/gd2topng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gd2topng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdcmpgif

```bash
$ singularity exec <container> /usr/local/bin/gdcmpgif
$ podman run --it --rm --entrypoint /usr/local/bin/gdcmpgif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdcmpgif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdparttopng

```bash
$ singularity exec <container> /usr/local/bin/gdparttopng
$ podman run --it --rm --entrypoint /usr/local/bin/gdparttopng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdparttopng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdtopng

```bash
$ singularity exec <container> /usr/local/bin/gdtopng
$ podman run --it --rm --entrypoint /usr/local/bin/gdtopng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdtopng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giftogd2

```bash
$ singularity exec <container> /usr/local/bin/giftogd2
$ podman run --it --rm --entrypoint /usr/local/bin/giftogd2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giftogd2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pngtogd

```bash
$ singularity exec <container> /usr/local/bin/pngtogd
$ podman run --it --rm --entrypoint /usr/local/bin/pngtogd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pngtogd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pngtogd2

```bash
$ singularity exec <container> /usr/local/bin/pngtogd2
$ podman run --it --rm --entrypoint /usr/local/bin/pngtogd2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pngtogd2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### webpng

```bash
$ singularity exec <container> /usr/local/bin/webpng
$ podman run --it --rm --entrypoint /usr/local/bin/webpng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/webpng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate

```bash
$ singularity exec <container> /usr/local/bin/annotate
$ podman run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
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