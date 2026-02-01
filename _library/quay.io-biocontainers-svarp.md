---
layout: container
name:  "quay.io/biocontainers/svarp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/svarp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/svarp/container.yaml"
updated_at: "2026-02-01 04:39:52.609172"
latest: "1.1.1--h077b44d_0"
container_url: "https://biocontainers.pro/tools/svarp"
aliases:
 - "GraphAligner"
 - "svarp"
 - "svarp-wtdbg2"
 - "jemalloc-config"
 - "jeprof"
 - "jemalloc.sh"
 - "protoc-25.3.0"
 - "ref-cache"
 - "bamtools"
 - "annot-tsv"
 - "x86_64-conda-linux-gnu.cfg"
 - "sdust"
 - "paftools.js"
 - "k8"
 - "minimap2"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "protoc"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "ace2sam"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "export2sam.pl"
 - "interpolate_sam.pl"
 - "maq2sam-long"
versions:
 - "1.0.1--h077b44d_0"
 - "1.1.1--h077b44d_0"
description: "singularity registry hpc automated addition for svarp"
config: {"url": "https://biocontainers.pro/tools/svarp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for svarp", "latest": {"1.1.1--h077b44d_0": "sha256:17f621b4631dd86a955cbd931ff9673bf14fd1417e8476998107269b2c4181e2"}, "tags": {"1.0.1--h077b44d_0": "sha256:81f4a3100d54f9cf8af1743decdb766ecc2a870d647039f435ecb2cd60176532", "1.1.1--h077b44d_0": "sha256:17f621b4631dd86a955cbd931ff9673bf14fd1417e8476998107269b2c4181e2"}, "docker": "quay.io/biocontainers/svarp", "aliases": {"GraphAligner": "/usr/local/bin/GraphAligner", "svarp": "/usr/local/bin/svarp", "svarp-wtdbg2": "/usr/local/bin/svarp-wtdbg2", "jemalloc-config": "/usr/local/bin/jemalloc-config", "jeprof": "/usr/local/bin/jeprof", "jemalloc.sh": "/usr/local/bin/jemalloc.sh", "protoc-25.3.0": "/usr/local/bin/protoc-25.3.0", "ref-cache": "/usr/local/bin/ref-cache", "bamtools": "/usr/local/bin/bamtools", "annot-tsv": "/usr/local/bin/annot-tsv", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "k8": "/usr/local/bin/k8", "minimap2": "/usr/local/bin/minimap2", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "protoc": "/usr/local/bin/protoc", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl", "maq2sam-long": "/usr/local/bin/maq2sam-long"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/svarp.
singularity registry hpc automated addition for svarp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/svarp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/svarp:1.1.1--h077b44d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/svarp/1.1.1--h077b44d_0
$ module help quay.io/biocontainers/svarp/1.1.1--h077b44d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### svarp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### svarp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### svarp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### svarp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### svarp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### svarp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GraphAligner

```bash
$ singularity exec <container> /usr/local/bin/GraphAligner
$ podman run --it --rm --entrypoint /usr/local/bin/GraphAligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GraphAligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svarp

```bash
$ singularity exec <container> /usr/local/bin/svarp
$ podman run --it --rm --entrypoint /usr/local/bin/svarp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svarp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svarp-wtdbg2

```bash
$ singularity exec <container> /usr/local/bin/svarp-wtdbg2
$ podman run --it --rm --entrypoint /usr/local/bin/svarp-wtdbg2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svarp-wtdbg2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jemalloc-config

```bash
$ singularity exec <container> /usr/local/bin/jemalloc-config
$ podman run --it --rm --entrypoint /usr/local/bin/jemalloc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jemalloc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jeprof

```bash
$ singularity exec <container> /usr/local/bin/jeprof
$ podman run --it --rm --entrypoint /usr/local/bin/jeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jemalloc.sh

```bash
$ singularity exec <container> /usr/local/bin/jemalloc.sh
$ podman run --it --rm --entrypoint /usr/local/bin/jemalloc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jemalloc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-25.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-25.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-25.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-25.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools

```bash
$ singularity exec <container> /usr/local/bin/bamtools
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### protoc

```bash
$ singularity exec <container> /usr/local/bin/protoc
$ podman run --it --rm --entrypoint /usr/local/bin/protoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/bowtie2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/export2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interpolate_sam.pl

```bash
$ singularity exec <container> /usr/local/bin/interpolate_sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maq2sam-long

```bash
$ singularity exec <container> /usr/local/bin/maq2sam-long
$ podman run --it --rm --entrypoint /usr/local/bin/maq2sam-long   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maq2sam-long   -v ${PWD} -w ${PWD} <container> -c " $@"
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