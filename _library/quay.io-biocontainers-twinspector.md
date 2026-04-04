---
layout: container
name:  "quay.io/biocontainers/twinspector"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/twinspector/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/twinspector/container.yaml"
updated_at: "2026-04-04 04:58:29.062631"
latest: "0.1.1--pyh106432d_0"
container_url: "https://biocontainers.pro/tools/twinspector"
aliases:
 - "CRISPResso"
 - "CRISPRessoAggregate"
 - "CRISPRessoBatch"
 - "CRISPRessoCompare"
 - "CRISPRessoPooled"
 - "CRISPRessoPooledWGSCompare"
 - "CRISPRessoWGS"
 - "TwInsPEctor"
 - "plotly_get_chrome"
 - "fastp"
 - "ref-cache"
 - "igzip"
 - "bowtie2"
 - "bowtie2-align-l"
 - "bowtie2-align-s"
 - "bowtie2-build"
 - "bowtie2-build-l"
 - "bowtie2-build-s"
 - "bowtie2-inspect"
 - "bowtie2-inspect-l"
 - "bowtie2-inspect-s"
 - "annot-tsv"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
versions:
 - "0.1.1--pyh106432d_0"
description: "singularity registry hpc automated addition for twinspector"
config: {"url": "https://biocontainers.pro/tools/twinspector", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for twinspector", "latest": {"0.1.1--pyh106432d_0": "sha256:3cfdffecbe53fc7e762f1b211b3a9027c8c627d9bd1ca6cac9f828d5247668be"}, "tags": {"0.1.1--pyh106432d_0": "sha256:3cfdffecbe53fc7e762f1b211b3a9027c8c627d9bd1ca6cac9f828d5247668be"}, "docker": "quay.io/biocontainers/twinspector", "aliases": {"CRISPResso": "/usr/local/bin/CRISPResso", "CRISPRessoAggregate": "/usr/local/bin/CRISPRessoAggregate", "CRISPRessoBatch": "/usr/local/bin/CRISPRessoBatch", "CRISPRessoCompare": "/usr/local/bin/CRISPRessoCompare", "CRISPRessoPooled": "/usr/local/bin/CRISPRessoPooled", "CRISPRessoPooledWGSCompare": "/usr/local/bin/CRISPRessoPooledWGSCompare", "CRISPRessoWGS": "/usr/local/bin/CRISPRessoWGS", "TwInsPEctor": "/usr/local/bin/TwInsPEctor", "plotly_get_chrome": "/usr/local/bin/plotly_get_chrome", "fastp": "/usr/local/bin/fastp", "ref-cache": "/usr/local/bin/ref-cache", "igzip": "/usr/local/bin/igzip", "bowtie2": "/usr/local/bin/bowtie2", "bowtie2-align-l": "/usr/local/bin/bowtie2-align-l", "bowtie2-align-s": "/usr/local/bin/bowtie2-align-s", "bowtie2-build": "/usr/local/bin/bowtie2-build", "bowtie2-build-l": "/usr/local/bin/bowtie2-build-l", "bowtie2-build-s": "/usr/local/bin/bowtie2-build-s", "bowtie2-inspect": "/usr/local/bin/bowtie2-inspect", "bowtie2-inspect-l": "/usr/local/bin/bowtie2-inspect-l", "bowtie2-inspect-s": "/usr/local/bin/bowtie2-inspect-s", "annot-tsv": "/usr/local/bin/annot-tsv", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/twinspector.
singularity registry hpc automated addition for twinspector
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/twinspector
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/twinspector:0.1.1--pyh106432d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/twinspector/0.1.1--pyh106432d_0
$ module help quay.io/biocontainers/twinspector/0.1.1--pyh106432d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### twinspector-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### twinspector-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### twinspector-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### twinspector-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### twinspector-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### twinspector-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CRISPResso

```bash
$ singularity exec <container> /usr/local/bin/CRISPResso
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPResso   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPResso   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CRISPRessoAggregate

```bash
$ singularity exec <container> /usr/local/bin/CRISPRessoAggregate
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPRessoAggregate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPRessoAggregate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CRISPRessoBatch

```bash
$ singularity exec <container> /usr/local/bin/CRISPRessoBatch
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPRessoBatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPRessoBatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CRISPRessoCompare

```bash
$ singularity exec <container> /usr/local/bin/CRISPRessoCompare
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPRessoCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPRessoCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CRISPRessoPooled

```bash
$ singularity exec <container> /usr/local/bin/CRISPRessoPooled
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPRessoPooled   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPRessoPooled   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CRISPRessoPooledWGSCompare

```bash
$ singularity exec <container> /usr/local/bin/CRISPRessoPooledWGSCompare
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPRessoPooledWGSCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPRessoPooledWGSCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CRISPRessoWGS

```bash
$ singularity exec <container> /usr/local/bin/CRISPRessoWGS
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPRessoWGS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPRessoWGS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TwInsPEctor

```bash
$ singularity exec <container> /usr/local/bin/TwInsPEctor
$ podman run --it --rm --entrypoint /usr/local/bin/TwInsPEctor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TwInsPEctor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotly_get_chrome

```bash
$ singularity exec <container> /usr/local/bin/plotly_get_chrome
$ podman run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastp

```bash
$ singularity exec <container> /usr/local/bin/fastp
$ podman run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2

```bash
$ singularity exec <container> /usr/local/bin/bowtie2
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
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