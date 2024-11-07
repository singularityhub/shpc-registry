---
layout: container
name:  "quay.io/biocontainers/pymlst"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pymlst/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pymlst/container.yaml"
updated_at: "2024-11-07 03:09:42.471630"
latest: "2.1.6--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pymlst"
aliases:
 - "alembic"
 - "claMLST"
 - "clamlst"
 - "kma"
 - "kma_index"
 - "kma_shm"
 - "kma_update"
 - "pyMLST"
 - "pymlst"
 - "wgMLST"
 - "wgmlst"
 - "blat"
 - "mako-render"
 - "mafft-sparsecore.rb"
 - "einsi"
 - "fftns"
 - "fftnsi"
 - "ginsi"
 - "linsi"
 - "mafft-distance"
 - "mafft-einsi"
 - "mafft-fftns"
 - "mafft-fftnsi"
 - "mafft-ginsi"
 - "mafft-homologs.rb"
 - "mafft-linsi"
 - "mafft-nwns"
 - "mafft-nwnsi"
 - "mafft-profile"
 - "mafft-qinsi"
 - "mafft-xinsi"
 - "nwns"
 - "nwnsi"
 - "mafft"
 - "py.test"
 - "pytest"
versions:
 - "2.1.3--pyh5e36f6f_0"
 - "2.1.3--pyhdfd78af_1"
 - "2.1.4--pyhdfd78af_0"
 - "2.1.5--pyhdfd78af_0"
 - "2.1.6--pyhdfd78af_0"
description: "singularity registry hpc automated addition for pymlst"
config: {"url": "https://biocontainers.pro/tools/pymlst", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pymlst", "latest": {"2.1.6--pyhdfd78af_0": "sha256:39bbc6dd980ccffdd04f72f84a84fc14d010cbc7fdea28ff5e1bebc97ed4b554"}, "tags": {"2.1.3--pyh5e36f6f_0": "sha256:bf078e3873b39f33f7303a011b5ad3cc1b5186ef303a40da75e9c55dbd943d67", "2.1.3--pyhdfd78af_1": "sha256:c3c48d2aaa2173bcd53dcad882e3dd4e4f62600c9118975d5b361c53a7725f2d", "2.1.4--pyhdfd78af_0": "sha256:664581a06ccc362f160eb7334f939f6f4994784597a40119ad9f2501bb60fe8c", "2.1.5--pyhdfd78af_0": "sha256:98c06285bbe1eaa45ec2649933b9d921d7a036996f19e019a3f4284a11c4d3cd", "2.1.6--pyhdfd78af_0": "sha256:39bbc6dd980ccffdd04f72f84a84fc14d010cbc7fdea28ff5e1bebc97ed4b554"}, "docker": "quay.io/biocontainers/pymlst", "aliases": {"alembic": "/usr/local/bin/alembic", "claMLST": "/usr/local/bin/claMLST", "clamlst": "/usr/local/bin/clamlst", "kma": "/usr/local/bin/kma", "kma_index": "/usr/local/bin/kma_index", "kma_shm": "/usr/local/bin/kma_shm", "kma_update": "/usr/local/bin/kma_update", "pyMLST": "/usr/local/bin/pyMLST", "pymlst": "/usr/local/bin/pymlst", "wgMLST": "/usr/local/bin/wgMLST", "wgmlst": "/usr/local/bin/wgmlst", "blat": "/usr/local/bin/blat", "mako-render": "/usr/local/bin/mako-render", "mafft-sparsecore.rb": "/usr/local/bin/mafft-sparsecore.rb", "einsi": "/usr/local/bin/einsi", "fftns": "/usr/local/bin/fftns", "fftnsi": "/usr/local/bin/fftnsi", "ginsi": "/usr/local/bin/ginsi", "linsi": "/usr/local/bin/linsi", "mafft-distance": "/usr/local/bin/mafft-distance", "mafft-einsi": "/usr/local/bin/mafft-einsi", "mafft-fftns": "/usr/local/bin/mafft-fftns", "mafft-fftnsi": "/usr/local/bin/mafft-fftnsi", "mafft-ginsi": "/usr/local/bin/mafft-ginsi", "mafft-homologs.rb": "/usr/local/bin/mafft-homologs.rb", "mafft-linsi": "/usr/local/bin/mafft-linsi", "mafft-nwns": "/usr/local/bin/mafft-nwns", "mafft-nwnsi": "/usr/local/bin/mafft-nwnsi", "mafft-profile": "/usr/local/bin/mafft-profile", "mafft-qinsi": "/usr/local/bin/mafft-qinsi", "mafft-xinsi": "/usr/local/bin/mafft-xinsi", "nwns": "/usr/local/bin/nwns", "nwnsi": "/usr/local/bin/nwnsi", "mafft": "/usr/local/bin/mafft", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pymlst.
singularity registry hpc automated addition for pymlst
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pymlst
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pymlst:2.1.6--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pymlst/2.1.6--pyhdfd78af_0
$ module help quay.io/biocontainers/pymlst/2.1.6--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pymlst-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pymlst-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pymlst-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pymlst-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pymlst-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pymlst-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alembic

```bash
$ singularity exec <container> /usr/local/bin/alembic
$ podman run --it --rm --entrypoint /usr/local/bin/alembic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alembic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### claMLST

```bash
$ singularity exec <container> /usr/local/bin/claMLST
$ podman run --it --rm --entrypoint /usr/local/bin/claMLST   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/claMLST   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clamlst

```bash
$ singularity exec <container> /usr/local/bin/clamlst
$ podman run --it --rm --entrypoint /usr/local/bin/clamlst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clamlst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma

```bash
$ singularity exec <container> /usr/local/bin/kma
$ podman run --it --rm --entrypoint /usr/local/bin/kma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_index

```bash
$ singularity exec <container> /usr/local/bin/kma_index
$ podman run --it --rm --entrypoint /usr/local/bin/kma_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_shm

```bash
$ singularity exec <container> /usr/local/bin/kma_shm
$ podman run --it --rm --entrypoint /usr/local/bin/kma_shm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_shm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_update

```bash
$ singularity exec <container> /usr/local/bin/kma_update
$ podman run --it --rm --entrypoint /usr/local/bin/kma_update   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_update   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyMLST

```bash
$ singularity exec <container> /usr/local/bin/pyMLST
$ podman run --it --rm --entrypoint /usr/local/bin/pyMLST   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyMLST   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pymlst

```bash
$ singularity exec <container> /usr/local/bin/pymlst
$ podman run --it --rm --entrypoint /usr/local/bin/pymlst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pymlst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wgMLST

```bash
$ singularity exec <container> /usr/local/bin/wgMLST
$ podman run --it --rm --entrypoint /usr/local/bin/wgMLST   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wgMLST   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wgmlst

```bash
$ singularity exec <container> /usr/local/bin/wgmlst
$ podman run --it --rm --entrypoint /usr/local/bin/wgmlst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wgmlst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blat

```bash
$ singularity exec <container> /usr/local/bin/blat
$ podman run --it --rm --entrypoint /usr/local/bin/blat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mako-render

```bash
$ singularity exec <container> /usr/local/bin/mako-render
$ podman run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-sparsecore.rb

```bash
$ singularity exec <container> /usr/local/bin/mafft-sparsecore.rb
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-sparsecore.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-sparsecore.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### einsi

```bash
$ singularity exec <container> /usr/local/bin/einsi
$ podman run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftns

```bash
$ singularity exec <container> /usr/local/bin/fftns
$ podman run --it --rm --entrypoint /usr/local/bin/fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftnsi

```bash
$ singularity exec <container> /usr/local/bin/fftnsi
$ podman run --it --rm --entrypoint /usr/local/bin/fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ginsi

```bash
$ singularity exec <container> /usr/local/bin/ginsi
$ podman run --it --rm --entrypoint /usr/local/bin/ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linsi

```bash
$ singularity exec <container> /usr/local/bin/linsi
$ podman run --it --rm --entrypoint /usr/local/bin/linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-distance

```bash
$ singularity exec <container> /usr/local/bin/mafft-distance
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-distance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-distance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-einsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-einsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-fftns

```bash
$ singularity exec <container> /usr/local/bin/mafft-fftns
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-fftnsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-fftnsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-ginsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-ginsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-homologs.rb

```bash
$ singularity exec <container> /usr/local/bin/mafft-homologs.rb
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-homologs.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-homologs.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-linsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-linsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-nwns

```bash
$ singularity exec <container> /usr/local/bin/mafft-nwns
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-nwns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-nwns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-nwnsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-nwnsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-nwnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-nwnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-profile

```bash
$ singularity exec <container> /usr/local/bin/mafft-profile
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-qinsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-qinsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-qinsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-qinsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-xinsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-xinsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-xinsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-xinsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nwns

```bash
$ singularity exec <container> /usr/local/bin/nwns
$ podman run --it --rm --entrypoint /usr/local/bin/nwns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nwns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nwnsi

```bash
$ singularity exec <container> /usr/local/bin/nwnsi
$ podman run --it --rm --entrypoint /usr/local/bin/nwnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nwnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft

```bash
$ singularity exec <container> /usr/local/bin/mafft
$ podman run --it --rm --entrypoint /usr/local/bin/mafft   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test

```bash
$ singularity exec <container> /usr/local/bin/py.test
$ podman run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pytest

```bash
$ singularity exec <container> /usr/local/bin/pytest
$ podman run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
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