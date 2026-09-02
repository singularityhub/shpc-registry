---
layout: container
name:  "quay.io/biocontainers/shredtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/shredtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/shredtools/container.yaml"
updated_at: "2026-09-02 07:07:26.166064"
latest: "0.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/shredtools"
aliases:
 - "anchor_merge"
 - "compute_lengths"
 - "extract_mums"
 - "mumemto"
 - "mumemto_exec"
 - "shredtools"
 - "fc-genconf"
 - "numba"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
 - "tqdm"
 - "numpy-config"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
versions:
 - "0.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for shredtools"
config: {"url": "https://biocontainers.pro/tools/shredtools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for shredtools", "latest": {"0.1.0--pyhdfd78af_0": "sha256:2b5a8fce028db44b1f27eb8a63812bf9408645e787459072c50bccb98031d1da"}, "tags": {"0.1.0--pyhdfd78af_0": "sha256:2b5a8fce028db44b1f27eb8a63812bf9408645e787459072c50bccb98031d1da"}, "docker": "quay.io/biocontainers/shredtools", "aliases": {"anchor_merge": "/usr/local/bin/anchor_merge", "compute_lengths": "/usr/local/bin/compute_lengths", "extract_mums": "/usr/local/bin/extract_mums", "mumemto": "/usr/local/bin/mumemto", "mumemto_exec": "/usr/local/bin/mumemto_exec", "shredtools": "/usr/local/bin/shredtools", "fc-genconf": "/usr/local/bin/fc-genconf", "numba": "/usr/local/bin/numba", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox", "tqdm": "/usr/local/bin/tqdm", "numpy-config": "/usr/local/bin/numpy-config", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/shredtools.
singularity registry hpc automated addition for shredtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/shredtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/shredtools:0.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/shredtools/0.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/shredtools/0.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### shredtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### shredtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### shredtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### shredtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### shredtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### shredtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### anchor_merge

```bash
$ singularity exec <container> /usr/local/bin/anchor_merge
$ podman run --it --rm --entrypoint /usr/local/bin/anchor_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anchor_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compute_lengths

```bash
$ singularity exec <container> /usr/local/bin/compute_lengths
$ podman run --it --rm --entrypoint /usr/local/bin/compute_lengths   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compute_lengths   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_mums

```bash
$ singularity exec <container> /usr/local/bin/extract_mums
$ podman run --it --rm --entrypoint /usr/local/bin/extract_mums   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_mums   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mumemto

```bash
$ singularity exec <container> /usr/local/bin/mumemto
$ podman run --it --rm --entrypoint /usr/local/bin/mumemto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mumemto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mumemto_exec

```bash
$ singularity exec <container> /usr/local/bin/mumemto_exec
$ podman run --it --rm --entrypoint /usr/local/bin/mumemto_exec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mumemto_exec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shredtools

```bash
$ singularity exec <container> /usr/local/bin/shredtools
$ podman run --it --rm --entrypoint /usr/local/bin/shredtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shredtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numba

```bash
$ singularity exec <container> /usr/local/bin/numba
$ podman run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftsubset

```bash
$ singularity exec <container> /usr/local/bin/pyftsubset
$ podman run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttx

```bash
$ singularity exec <container> /usr/local/bin/ttx
$ podman run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
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