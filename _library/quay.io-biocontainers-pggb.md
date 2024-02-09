---
layout: container
name:  "quay.io/biocontainers/pggb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pggb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pggb/container.yaml"
updated_at: "2024-02-09 02:36:21.511345"
latest: "0.5.4--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/pggb"
aliases:
 - "gfaffix"
 - "odgi"
 - "pggb"
 - "rich-click"
 - "seqwish"
 - "smoothxg"
 - "time"
 - "vg"
 - "wfmash"
 - "multiqc"
 - "bc"
 - "dc"
 - "cmark"
 - "gff2gff.py"
 - "coloredlogs"
 - "humanfriendly"
 - "pigz"
 - "unpigz"
 - "markdown_py"
versions:
 - "0.4.1--hdfd78af_0"
 - "0.5.0--hdfd78af_0"
 - "0.5.1--hdfd78af_1"
 - "0.5.2--hdfd78af_0"
 - "0.5.3--hdfd78af_2"
 - "0.5.4--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for pggb"
config: {"url": "https://biocontainers.pro/tools/pggb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pggb", "latest": {"0.5.4--hdfd78af_0": "sha256:d24a3152c130d25bb0d9c453ed41ad807c8aca733e4cdf759276a8d7c0940f5e"}, "tags": {"0.4.1--hdfd78af_0": "sha256:18875ce064179e4e4f2a1459b87a7de2af233f4d5f50d365f813d8d9ac50fc69", "0.5.0--hdfd78af_0": "sha256:a0fabae4c656e72e8cb4467401529617061e7d68db335fcabc61cc2a4abcfc64", "0.5.1--hdfd78af_1": "sha256:41c370aed5893a4ed669ccbdcaf7c2ed814e2d5dd71cd0006e8aada500437475", "0.5.2--hdfd78af_0": "sha256:c73a122857427f98f960b8e0c24e9c9c2cc0ed50a61d7bc8c6c0e195fb18288e", "0.5.3--hdfd78af_2": "sha256:20f409e7a15a2ff5283822e318bbe3ee67166852df72e31b7197dc66b89b66bf", "0.5.4--hdfd78af_0": "sha256:d24a3152c130d25bb0d9c453ed41ad807c8aca733e4cdf759276a8d7c0940f5e"}, "docker": "quay.io/biocontainers/pggb", "aliases": {"gfaffix": "/usr/local/bin/gfaffix", "odgi": "/usr/local/bin/odgi", "pggb": "/usr/local/bin/pggb", "rich-click": "/usr/local/bin/rich-click", "seqwish": "/usr/local/bin/seqwish", "smoothxg": "/usr/local/bin/smoothxg", "time": "/usr/local/bin/time", "vg": "/usr/local/bin/vg", "wfmash": "/usr/local/bin/wfmash", "multiqc": "/usr/local/bin/multiqc", "bc": "/usr/local/bin/bc", "dc": "/usr/local/bin/dc", "cmark": "/usr/local/bin/cmark", "gff2gff.py": "/usr/local/bin/gff2gff.py", "coloredlogs": "/usr/local/bin/coloredlogs", "humanfriendly": "/usr/local/bin/humanfriendly", "pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz", "markdown_py": "/usr/local/bin/markdown_py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pggb.
shpc-registry automated BioContainers addition for pggb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pggb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pggb:0.5.4--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pggb/0.5.4--hdfd78af_0
$ module help quay.io/biocontainers/pggb/0.5.4--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pggb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pggb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pggb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pggb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pggb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pggb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gfaffix

```bash
$ singularity exec <container> /usr/local/bin/gfaffix
$ podman run --it --rm --entrypoint /usr/local/bin/gfaffix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfaffix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### odgi

```bash
$ singularity exec <container> /usr/local/bin/odgi
$ podman run --it --rm --entrypoint /usr/local/bin/odgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/odgi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pggb

```bash
$ singularity exec <container> /usr/local/bin/pggb
$ podman run --it --rm --entrypoint /usr/local/bin/pggb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pggb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rich-click

```bash
$ singularity exec <container> /usr/local/bin/rich-click
$ podman run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqwish

```bash
$ singularity exec <container> /usr/local/bin/seqwish
$ podman run --it --rm --entrypoint /usr/local/bin/seqwish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqwish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smoothxg

```bash
$ singularity exec <container> /usr/local/bin/smoothxg
$ podman run --it --rm --entrypoint /usr/local/bin/smoothxg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smoothxg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### time

```bash
$ singularity exec <container> /usr/local/bin/time
$ podman run --it --rm --entrypoint /usr/local/bin/time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vg

```bash
$ singularity exec <container> /usr/local/bin/vg
$ podman run --it --rm --entrypoint /usr/local/bin/vg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wfmash

```bash
$ singularity exec <container> /usr/local/bin/wfmash
$ podman run --it --rm --entrypoint /usr/local/bin/wfmash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wfmash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multiqc

```bash
$ singularity exec <container> /usr/local/bin/multiqc
$ podman run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bc

```bash
$ singularity exec <container> /usr/local/bin/bc
$ podman run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dc

```bash
$ singularity exec <container> /usr/local/bin/dc
$ podman run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmark

```bash
$ singularity exec <container> /usr/local/bin/cmark
$ podman run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pigz

```bash
$ singularity exec <container> /usr/local/bin/pigz
$ podman run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpigz

```bash
$ singularity exec <container> /usr/local/bin/unpigz
$ podman run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown_py

```bash
$ singularity exec <container> /usr/local/bin/markdown_py
$ podman run --it --rm --entrypoint /usr/local/bin/markdown_py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown_py   -v ${PWD} -w ${PWD} <container> -c " $@"
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