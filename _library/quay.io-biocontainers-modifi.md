---
layout: container
name:  "quay.io/biocontainers/modifi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/modifi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/modifi/container.yaml"
updated_at: "2026-04-04 05:08:36.978221"
latest: "0.0.1--hd63eeec_0"
container_url: "https://biocontainers.pro/tools/modifi"
aliases:
 - "bam2fasta"
 - "bam2fastq"
 - "ccs-kinetics-bystrandify"
 - "extracthifi"
 - "modifi"
 - "pbindex"
 - "pbindexdump"
 - "pbmerge"
 - "pbmm2"
 - "zmwfilter"
 - "jnativescan"
 - "bash"
 - "bashbug"
 - "hb-raster"
 - "hb-vector"
 - "h2benchmark"
 - "checksum-profile"
 - "ref-cache"
 - "jwebserver"
 - "elasticurl"
 - "annot-tsv"
 - "jpackage"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
 - "h5delete"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "cups-config"
 - "ippeveprinter"
versions:
 - "0.0.1--hd63eeec_0"
description: "singularity registry hpc automated addition for modifi"
config: {"url": "https://biocontainers.pro/tools/modifi", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for modifi", "latest": {"0.0.1--hd63eeec_0": "sha256:11dea3b9da15484df49953f6960fcb382a1ac903494e96df5b892c7959890d0c"}, "tags": {"0.0.1--hd63eeec_0": "sha256:11dea3b9da15484df49953f6960fcb382a1ac903494e96df5b892c7959890d0c"}, "docker": "quay.io/biocontainers/modifi", "aliases": {"bam2fasta": "/usr/local/bin/bam2fasta", "bam2fastq": "/usr/local/bin/bam2fastq", "ccs-kinetics-bystrandify": "/usr/local/bin/ccs-kinetics-bystrandify", "extracthifi": "/usr/local/bin/extracthifi", "modifi": "/usr/local/bin/modifi", "pbindex": "/usr/local/bin/pbindex", "pbindexdump": "/usr/local/bin/pbindexdump", "pbmerge": "/usr/local/bin/pbmerge", "pbmm2": "/usr/local/bin/pbmm2", "zmwfilter": "/usr/local/bin/zmwfilter", "jnativescan": "/usr/local/bin/jnativescan", "bash": "/usr/local/bin/bash", "bashbug": "/usr/local/bin/bashbug", "hb-raster": "/usr/local/bin/hb-raster", "hb-vector": "/usr/local/bin/hb-vector", "h2benchmark": "/usr/local/bin/h2benchmark", "checksum-profile": "/usr/local/bin/checksum-profile", "ref-cache": "/usr/local/bin/ref-cache", "jwebserver": "/usr/local/bin/jwebserver", "elasticurl": "/usr/local/bin/elasticurl", "annot-tsv": "/usr/local/bin/annot-tsv", "jpackage": "/usr/local/bin/jpackage", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox", "h5delete": "/usr/local/bin/h5delete", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "cups-config": "/usr/local/bin/cups-config", "ippeveprinter": "/usr/local/bin/ippeveprinter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/modifi.
singularity registry hpc automated addition for modifi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/modifi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/modifi:0.0.1--hd63eeec_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/modifi/0.0.1--hd63eeec_0
$ module help quay.io/biocontainers/modifi/0.0.1--hd63eeec_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### modifi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### modifi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### modifi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### modifi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### modifi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### modifi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam2fasta

```bash
$ singularity exec <container> /usr/local/bin/bam2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/bam2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2fastq

```bash
$ singularity exec <container> /usr/local/bin/bam2fastq
$ podman run --it --rm --entrypoint /usr/local/bin/bam2fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccs-kinetics-bystrandify

```bash
$ singularity exec <container> /usr/local/bin/ccs-kinetics-bystrandify
$ podman run --it --rm --entrypoint /usr/local/bin/ccs-kinetics-bystrandify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccs-kinetics-bystrandify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extracthifi

```bash
$ singularity exec <container> /usr/local/bin/extracthifi
$ podman run --it --rm --entrypoint /usr/local/bin/extracthifi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extracthifi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### modifi

```bash
$ singularity exec <container> /usr/local/bin/modifi
$ podman run --it --rm --entrypoint /usr/local/bin/modifi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/modifi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbindex

```bash
$ singularity exec <container> /usr/local/bin/pbindex
$ podman run --it --rm --entrypoint /usr/local/bin/pbindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbindexdump

```bash
$ singularity exec <container> /usr/local/bin/pbindexdump
$ podman run --it --rm --entrypoint /usr/local/bin/pbindexdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbindexdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbmerge

```bash
$ singularity exec <container> /usr/local/bin/pbmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pbmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbmm2

```bash
$ singularity exec <container> /usr/local/bin/pbmm2
$ podman run --it --rm --entrypoint /usr/local/bin/pbmm2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbmm2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zmwfilter

```bash
$ singularity exec <container> /usr/local/bin/zmwfilter
$ podman run --it --rm --entrypoint /usr/local/bin/zmwfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zmwfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jnativescan

```bash
$ singularity exec <container> /usr/local/bin/jnativescan
$ podman run --it --rm --entrypoint /usr/local/bin/jnativescan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jnativescan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bash

```bash
$ singularity exec <container> /usr/local/bin/bash
$ podman run --it --rm --entrypoint /usr/local/bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bashbug

```bash
$ singularity exec <container> /usr/local/bin/bashbug
$ podman run --it --rm --entrypoint /usr/local/bin/bashbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bashbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-raster

```bash
$ singularity exec <container> /usr/local/bin/hb-raster
$ podman run --it --rm --entrypoint /usr/local/bin/hb-raster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-raster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-vector

```bash
$ singularity exec <container> /usr/local/bin/hb-vector
$ podman run --it --rm --entrypoint /usr/local/bin/hb-vector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-vector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h2benchmark

```bash
$ singularity exec <container> /usr/local/bin/h2benchmark
$ podman run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checksum-profile

```bash
$ singularity exec <container> /usr/local/bin/checksum-profile
$ podman run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jwebserver

```bash
$ singularity exec <container> /usr/local/bin/jwebserver
$ podman run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl

```bash
$ singularity exec <container> /usr/local/bin/elasticurl
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpackage

```bash
$ singularity exec <container> /usr/local/bin/jpackage
$ podman run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### h5delete

```bash
$ singularity exec <container> /usr/local/bin/h5delete
$ podman run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### cups-config

```bash
$ singularity exec <container> /usr/local/bin/cups-config
$ podman run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ippeveprinter

```bash
$ singularity exec <container> /usr/local/bin/ippeveprinter
$ podman run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
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