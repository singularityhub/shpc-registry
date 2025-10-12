---
layout: container
name:  "quay.io/biocontainers/gretl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gretl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gretl/container.yaml"
updated_at: "2025-10-12 03:56:00.848698"
latest: "0.1.1--hc1c3326_2"
container_url: "https://biocontainers.pro/tools/gretl"
aliases:
 - "block.py"
 - "core.py"
 - "gretl"
 - "multi.auto.py"
 - "multi.correlate.py"
 - "multi.heatmap.py"
 - "multi.histogram.py"
 - "multi.scatter.py"
 - "nwindow.py"
 - "path.py"
 - "ps.py"
 - "saturation_plotter.py"
 - "stats_path.py"
 - "window.py"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
 - "numpy-config"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
 - "tjbench"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.1.0--h715e4b3_0"
 - "0.1.1--h715e4b3_1"
 - "0.1.1--hc1c3326_2"
description: "singularity registry hpc automated addition for gretl"
config: {"url": "https://biocontainers.pro/tools/gretl", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gretl", "latest": {"0.1.1--hc1c3326_2": "sha256:52974a3a1598244121d28813b86f99aa5feb6a9910d1250ad4c4598fa53ca274"}, "tags": {"0.1.0--h715e4b3_0": "sha256:94dbc85bb994f011a7786e87034596120d3ae56efaaeb3cfe8d78ea62609b421", "0.1.1--h715e4b3_1": "sha256:2f154ec74981972de835e57b466df67b7cec4ee9e07cfd507b491bdca265f1fc", "0.1.1--hc1c3326_2": "sha256:52974a3a1598244121d28813b86f99aa5feb6a9910d1250ad4c4598fa53ca274"}, "docker": "quay.io/biocontainers/gretl", "aliases": {"block.py": "/usr/local/bin/block.py", "core.py": "/usr/local/bin/core.py", "gretl": "/usr/local/bin/gretl", "multi.auto.py": "/usr/local/bin/multi.auto.py", "multi.correlate.py": "/usr/local/bin/multi.correlate.py", "multi.heatmap.py": "/usr/local/bin/multi.heatmap.py", "multi.histogram.py": "/usr/local/bin/multi.histogram.py", "multi.scatter.py": "/usr/local/bin/multi.scatter.py", "nwindow.py": "/usr/local/bin/nwindow.py", "path.py": "/usr/local/bin/path.py", "ps.py": "/usr/local/bin/ps.py", "saturation_plotter.py": "/usr/local/bin/saturation_plotter.py", "stats_path.py": "/usr/local/bin/stats_path.py", "window.py": "/usr/local/bin/window.py", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox", "numpy-config": "/usr/local/bin/numpy-config", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli", "tjbench": "/usr/local/bin/tjbench", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gretl.
singularity registry hpc automated addition for gretl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gretl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gretl:0.1.1--hc1c3326_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gretl/0.1.1--hc1c3326_2
$ module help quay.io/biocontainers/gretl/0.1.1--hc1c3326_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gretl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gretl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gretl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gretl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gretl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gretl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### block.py

```bash
$ singularity exec <container> /usr/local/bin/block.py
$ podman run --it --rm --entrypoint /usr/local/bin/block.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/block.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### core.py

```bash
$ singularity exec <container> /usr/local/bin/core.py
$ podman run --it --rm --entrypoint /usr/local/bin/core.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/core.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gretl

```bash
$ singularity exec <container> /usr/local/bin/gretl
$ podman run --it --rm --entrypoint /usr/local/bin/gretl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gretl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multi.auto.py

```bash
$ singularity exec <container> /usr/local/bin/multi.auto.py
$ podman run --it --rm --entrypoint /usr/local/bin/multi.auto.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multi.auto.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multi.correlate.py

```bash
$ singularity exec <container> /usr/local/bin/multi.correlate.py
$ podman run --it --rm --entrypoint /usr/local/bin/multi.correlate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multi.correlate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multi.heatmap.py

```bash
$ singularity exec <container> /usr/local/bin/multi.heatmap.py
$ podman run --it --rm --entrypoint /usr/local/bin/multi.heatmap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multi.heatmap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multi.histogram.py

```bash
$ singularity exec <container> /usr/local/bin/multi.histogram.py
$ podman run --it --rm --entrypoint /usr/local/bin/multi.histogram.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multi.histogram.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multi.scatter.py

```bash
$ singularity exec <container> /usr/local/bin/multi.scatter.py
$ podman run --it --rm --entrypoint /usr/local/bin/multi.scatter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multi.scatter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nwindow.py

```bash
$ singularity exec <container> /usr/local/bin/nwindow.py
$ podman run --it --rm --entrypoint /usr/local/bin/nwindow.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nwindow.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### path.py

```bash
$ singularity exec <container> /usr/local/bin/path.py
$ podman run --it --rm --entrypoint /usr/local/bin/path.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/path.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ps.py

```bash
$ singularity exec <container> /usr/local/bin/ps.py
$ podman run --it --rm --entrypoint /usr/local/bin/ps.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ps.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saturation_plotter.py

```bash
$ singularity exec <container> /usr/local/bin/saturation_plotter.py
$ podman run --it --rm --entrypoint /usr/local/bin/saturation_plotter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saturation_plotter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stats_path.py

```bash
$ singularity exec <container> /usr/local/bin/stats_path.py
$ podman run --it --rm --entrypoint /usr/local/bin/stats_path.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stats_path.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### window.py

```bash
$ singularity exec <container> /usr/local/bin/window.py
$ podman run --it --rm --entrypoint /usr/local/bin/window.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/window.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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