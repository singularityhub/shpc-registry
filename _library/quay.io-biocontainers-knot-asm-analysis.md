---
layout: container
name:  "quay.io/biocontainers/knot-asm-analysis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/knot-asm-analysis/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/knot-asm-analysis/container.yaml"
updated_at: "2022-10-27 00:44:37.223598"
latest: "1.3.0--py_0"
container_url: "https://biocontainers.pro/tools/knot-asm-analysis"
aliases:
 - "fpa"
 - "gfapy-convert"
 - "gfapy-mergelinear"
 - "gfapy-renumber"
 - "gfapy-validate"
 - "knot"
 - "knot.analysis"
 - "knot.analysis.classifications"
 - "knot.analysis.hamilton_path"
 - "knot.extremity_search"
 - "knot.filter_tig"
 - "knot.path_search"
 - "knot.sg_generation"
 - "yacrd"
versions:
 - "1.3.0--py_0"
description: "shpc-registry automated BioContainers addition for knot-asm-analysis"
config: {"url": "https://biocontainers.pro/tools/knot-asm-analysis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for knot-asm-analysis", "latest": {"1.3.0--py_0": "sha256:0e678d4beba9b4a0bab3c2f17f4806e8af26520b38213c0b657311acae5b23cf"}, "tags": {"1.3.0--py_0": "sha256:0e678d4beba9b4a0bab3c2f17f4806e8af26520b38213c0b657311acae5b23cf"}, "docker": "quay.io/biocontainers/knot-asm-analysis", "aliases": {"fpa": "/usr/local/bin/fpa", "gfapy-convert": "/usr/local/bin/gfapy-convert", "gfapy-mergelinear": "/usr/local/bin/gfapy-mergelinear", "gfapy-renumber": "/usr/local/bin/gfapy-renumber", "gfapy-validate": "/usr/local/bin/gfapy-validate", "knot": "/usr/local/bin/knot", "knot.analysis": "/usr/local/bin/knot.analysis", "knot.analysis.classifications": "/usr/local/bin/knot.analysis.classifications", "knot.analysis.hamilton_path": "/usr/local/bin/knot.analysis.hamilton_path", "knot.extremity_search": "/usr/local/bin/knot.extremity_search", "knot.filter_tig": "/usr/local/bin/knot.filter_tig", "knot.path_search": "/usr/local/bin/knot.path_search", "knot.sg_generation": "/usr/local/bin/knot.sg_generation", "yacrd": "/usr/local/bin/yacrd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/knot-asm-analysis.
shpc-registry automated BioContainers addition for knot-asm-analysis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/knot-asm-analysis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/knot-asm-analysis:1.3.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/knot-asm-analysis/1.3.0--py_0
$ module help quay.io/biocontainers/knot-asm-analysis/1.3.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### knot-asm-analysis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### knot-asm-analysis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### knot-asm-analysis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### knot-asm-analysis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### knot-asm-analysis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### knot-asm-analysis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fpa

```bash
$ singularity exec <container> /usr/local/bin/fpa
$ podman run --it --rm --entrypoint /usr/local/bin/fpa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fpa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfapy-convert

```bash
$ singularity exec <container> /usr/local/bin/gfapy-convert
$ podman run --it --rm --entrypoint /usr/local/bin/gfapy-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfapy-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfapy-mergelinear

```bash
$ singularity exec <container> /usr/local/bin/gfapy-mergelinear
$ podman run --it --rm --entrypoint /usr/local/bin/gfapy-mergelinear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfapy-mergelinear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfapy-renumber

```bash
$ singularity exec <container> /usr/local/bin/gfapy-renumber
$ podman run --it --rm --entrypoint /usr/local/bin/gfapy-renumber   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfapy-renumber   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfapy-validate

```bash
$ singularity exec <container> /usr/local/bin/gfapy-validate
$ podman run --it --rm --entrypoint /usr/local/bin/gfapy-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfapy-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### knot

```bash
$ singularity exec <container> /usr/local/bin/knot
$ podman run --it --rm --entrypoint /usr/local/bin/knot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/knot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### knot.analysis

```bash
$ singularity exec <container> /usr/local/bin/knot.analysis
$ podman run --it --rm --entrypoint /usr/local/bin/knot.analysis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/knot.analysis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### knot.analysis.classifications

```bash
$ singularity exec <container> /usr/local/bin/knot.analysis.classifications
$ podman run --it --rm --entrypoint /usr/local/bin/knot.analysis.classifications   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/knot.analysis.classifications   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### knot.analysis.hamilton_path

```bash
$ singularity exec <container> /usr/local/bin/knot.analysis.hamilton_path
$ podman run --it --rm --entrypoint /usr/local/bin/knot.analysis.hamilton_path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/knot.analysis.hamilton_path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### knot.extremity_search

```bash
$ singularity exec <container> /usr/local/bin/knot.extremity_search
$ podman run --it --rm --entrypoint /usr/local/bin/knot.extremity_search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/knot.extremity_search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### knot.filter_tig

```bash
$ singularity exec <container> /usr/local/bin/knot.filter_tig
$ podman run --it --rm --entrypoint /usr/local/bin/knot.filter_tig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/knot.filter_tig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### knot.path_search

```bash
$ singularity exec <container> /usr/local/bin/knot.path_search
$ podman run --it --rm --entrypoint /usr/local/bin/knot.path_search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/knot.path_search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### knot.sg_generation

```bash
$ singularity exec <container> /usr/local/bin/knot.sg_generation
$ podman run --it --rm --entrypoint /usr/local/bin/knot.sg_generation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/knot.sg_generation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yacrd

```bash
$ singularity exec <container> /usr/local/bin/yacrd
$ podman run --it --rm --entrypoint /usr/local/bin/yacrd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yacrd   -v ${PWD} -w ${PWD} <container> -c " $@"
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