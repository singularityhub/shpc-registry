---
layout: container
name:  "quay.io/biocontainers/hsdecipher"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hsdecipher/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hsdecipher/container.yaml"
updated_at: "2025-03-13 05:15:28.600207"
latest: "1.1.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/hsdecipher"
aliases:
 - "HSD_add_on.py"
 - "HSD_batch_run.py"
 - "HSD_categories.py"
 - "hsd_heatmap"
 - "ko.tsv"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
 - "numpy-config"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "tjbench"
 - "brotli"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
versions:
 - "1.0.0--hdfd78af_0"
 - "1.0.0--hdfd78af_1"
 - "1.1.2--hdfd78af_0"
description: "singularity registry hpc automated addition for hsdecipher"
config: {"url": "https://biocontainers.pro/tools/hsdecipher", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hsdecipher", "latest": {"1.1.2--hdfd78af_0": "sha256:66bdacc6a6537b5c9af787b25b0c0772d827ed2015b5fef67bd17bbf7678a34e"}, "tags": {"1.0.0--hdfd78af_0": "sha256:dfcf0e713ba862e07e66df0aaa6ab05fd527303c3ef66ba9b69dfa4f5b92f61a", "1.0.0--hdfd78af_1": "sha256:1295383471c07aec6df66a6274bfaf541688e24ad88441b11911dedf6432d651", "1.1.2--hdfd78af_0": "sha256:66bdacc6a6537b5c9af787b25b0c0772d827ed2015b5fef67bd17bbf7678a34e"}, "docker": "quay.io/biocontainers/hsdecipher", "aliases": {"HSD_add_on.py": "/usr/local/bin/HSD_add_on.py", "HSD_batch_run.py": "/usr/local/bin/HSD_batch_run.py", "HSD_categories.py": "/usr/local/bin/HSD_categories.py", "hsd_heatmap": "/usr/local/bin/hsd_heatmap", "ko.tsv": "/usr/local/bin/ko.tsv", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox", "numpy-config": "/usr/local/bin/numpy-config", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "tjbench": "/usr/local/bin/tjbench", "brotli": "/usr/local/bin/brotli", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hsdecipher.
singularity registry hpc automated addition for hsdecipher
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hsdecipher
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hsdecipher:1.1.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hsdecipher/1.1.2--hdfd78af_0
$ module help quay.io/biocontainers/hsdecipher/1.1.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hsdecipher-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hsdecipher-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hsdecipher-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hsdecipher-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hsdecipher-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hsdecipher-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### HSD_add_on.py

```bash
$ singularity exec <container> /usr/local/bin/HSD_add_on.py
$ podman run --it --rm --entrypoint /usr/local/bin/HSD_add_on.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HSD_add_on.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### HSD_batch_run.py

```bash
$ singularity exec <container> /usr/local/bin/HSD_batch_run.py
$ podman run --it --rm --entrypoint /usr/local/bin/HSD_batch_run.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HSD_batch_run.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### HSD_categories.py

```bash
$ singularity exec <container> /usr/local/bin/HSD_categories.py
$ podman run --it --rm --entrypoint /usr/local/bin/HSD_categories.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HSD_categories.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hsd_heatmap

```bash
$ singularity exec <container> /usr/local/bin/hsd_heatmap
$ podman run --it --rm --entrypoint /usr/local/bin/hsd_heatmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hsd_heatmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ko.tsv

```bash
$ singularity exec <container> /usr/local/bin/ko.tsv
$ podman run --it --rm --entrypoint /usr/local/bin/ko.tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ko.tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
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