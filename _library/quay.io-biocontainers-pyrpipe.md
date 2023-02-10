---
layout: container
name:  "quay.io/biocontainers/pyrpipe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyrpipe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyrpipe/container.yaml"
updated_at: "2023-02-10 03:01:47.265010"
latest: "0.0.5--py_0"
container_url: "https://biocontainers.pro/tools/pyrpipe"
aliases:
 - "cairosvg"
 - "pyrpipe"
 - "pyrpipe_diagnostic"
 - "weasyprint"
 - "multiqc"
 - "get_objgraph"
 - "undill"
 - "coloredlogs"
 - "humanfriendly"
 - "markdown_py"
 - "futurize"
 - "pasteurize"
 - "chardetect"
 - "f2py3.9"
versions:
 - "0.0.5--py_0"
description: "shpc-registry automated BioContainers addition for pyrpipe"
config: {"url": "https://biocontainers.pro/tools/pyrpipe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyrpipe", "latest": {"0.0.5--py_0": "sha256:453268243ab589f495bb6240175b98e6445264b68483716a80904c683538f842"}, "tags": {"0.0.5--py_0": "sha256:453268243ab589f495bb6240175b98e6445264b68483716a80904c683538f842"}, "docker": "quay.io/biocontainers/pyrpipe", "aliases": {"cairosvg": "/usr/local/bin/cairosvg", "pyrpipe": "/usr/local/bin/pyrpipe", "pyrpipe_diagnostic": "/usr/local/bin/pyrpipe_diagnostic", "weasyprint": "/usr/local/bin/weasyprint", "multiqc": "/usr/local/bin/multiqc", "get_objgraph": "/usr/local/bin/get_objgraph", "undill": "/usr/local/bin/undill", "coloredlogs": "/usr/local/bin/coloredlogs", "humanfriendly": "/usr/local/bin/humanfriendly", "markdown_py": "/usr/local/bin/markdown_py", "futurize": "/usr/local/bin/futurize", "pasteurize": "/usr/local/bin/pasteurize", "chardetect": "/usr/local/bin/chardetect", "f2py3.9": "/usr/local/bin/f2py3.9"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyrpipe.
shpc-registry automated BioContainers addition for pyrpipe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyrpipe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyrpipe:0.0.5--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyrpipe/0.0.5--py_0
$ module help quay.io/biocontainers/pyrpipe/0.0.5--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyrpipe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyrpipe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyrpipe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyrpipe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyrpipe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyrpipe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cairosvg

```bash
$ singularity exec <container> /usr/local/bin/cairosvg
$ podman run --it --rm --entrypoint /usr/local/bin/cairosvg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cairosvg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrpipe

```bash
$ singularity exec <container> /usr/local/bin/pyrpipe
$ podman run --it --rm --entrypoint /usr/local/bin/pyrpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrpipe_diagnostic

```bash
$ singularity exec <container> /usr/local/bin/pyrpipe_diagnostic
$ podman run --it --rm --entrypoint /usr/local/bin/pyrpipe_diagnostic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrpipe_diagnostic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### weasyprint

```bash
$ singularity exec <container> /usr/local/bin/weasyprint
$ podman run --it --rm --entrypoint /usr/local/bin/weasyprint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/weasyprint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multiqc

```bash
$ singularity exec <container> /usr/local/bin/multiqc
$ podman run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_objgraph

```bash
$ singularity exec <container> /usr/local/bin/get_objgraph
$ podman run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### undill

```bash
$ singularity exec <container> /usr/local/bin/undill
$ podman run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown_py

```bash
$ singularity exec <container> /usr/local/bin/markdown_py
$ podman run --it --rm --entrypoint /usr/local/bin/markdown_py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown_py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasteurize

```bash
$ singularity exec <container> /usr/local/bin/pasteurize
$ podman run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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