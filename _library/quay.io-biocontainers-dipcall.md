---
layout: container
name:  "quay.io/biocontainers/dipcall"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dipcall/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dipcall/container.yaml"
updated_at: "2024-11-22 04:13:11.665671"
latest: "0.3--0"
container_url: "https://biocontainers.pro/tools/dipcall"
aliases:
 - "bedtk"
 - "dipcall-aux.js"
 - "htsbox"
 - "meryl-analyze"
 - "meryl-check"
 - "meryl-import"
 - "meryl-lookup"
 - "meryl-simple"
 - "run-dipcall"
 - "unimap"
 - "winnowmap"
 - "meryl"
 - "perl5.32.0"
 - "sdust"
 - "paftools.js"
 - "minimap2"
 - "k8"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "ace2sam"
 - "blast2sam.pl"
versions:
 - "0.3--0"
 - "0.3--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for dipcall"
config: {"url": "https://biocontainers.pro/tools/dipcall", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dipcall", "latest": {"0.3--0": "sha256:3bde49fdb0ff0bb2ad6b64483acd5be92ab520253e359e0ee7009819d6762fa0"}, "tags": {"0.3--0": "sha256:3bde49fdb0ff0bb2ad6b64483acd5be92ab520253e359e0ee7009819d6762fa0", "0.3--hdfd78af_0": "sha256:500ec2ec8ea9c9c73538c49ae53e50a4fbb4ad7988b32fbc6f9c77e44dcb034c"}, "docker": "quay.io/biocontainers/dipcall", "aliases": {"bedtk": "/usr/local/bin/bedtk", "dipcall-aux.js": "/usr/local/bin/dipcall-aux.js", "htsbox": "/usr/local/bin/htsbox", "meryl-analyze": "/usr/local/bin/meryl-analyze", "meryl-check": "/usr/local/bin/meryl-check", "meryl-import": "/usr/local/bin/meryl-import", "meryl-lookup": "/usr/local/bin/meryl-lookup", "meryl-simple": "/usr/local/bin/meryl-simple", "run-dipcall": "/usr/local/bin/run-dipcall", "unimap": "/usr/local/bin/unimap", "winnowmap": "/usr/local/bin/winnowmap", "meryl": "/usr/local/bin/meryl", "perl5.32.0": "/usr/local/bin/perl5.32.0", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "k8": "/usr/local/bin/k8", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dipcall.
shpc-registry automated BioContainers addition for dipcall
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dipcall
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dipcall:0.3--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dipcall/0.3--0
$ module help quay.io/biocontainers/dipcall/0.3--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dipcall-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dipcall-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dipcall-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dipcall-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dipcall-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dipcall-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bedtk

```bash
$ singularity exec <container> /usr/local/bin/bedtk
$ podman run --it --rm --entrypoint /usr/local/bin/bedtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedtk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dipcall-aux.js

```bash
$ singularity exec <container> /usr/local/bin/dipcall-aux.js
$ podman run --it --rm --entrypoint /usr/local/bin/dipcall-aux.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dipcall-aux.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsbox

```bash
$ singularity exec <container> /usr/local/bin/htsbox
$ podman run --it --rm --entrypoint /usr/local/bin/htsbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl-analyze

```bash
$ singularity exec <container> /usr/local/bin/meryl-analyze
$ podman run --it --rm --entrypoint /usr/local/bin/meryl-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl-check

```bash
$ singularity exec <container> /usr/local/bin/meryl-check
$ podman run --it --rm --entrypoint /usr/local/bin/meryl-check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl-check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl-import

```bash
$ singularity exec <container> /usr/local/bin/meryl-import
$ podman run --it --rm --entrypoint /usr/local/bin/meryl-import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl-import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl-lookup

```bash
$ singularity exec <container> /usr/local/bin/meryl-lookup
$ podman run --it --rm --entrypoint /usr/local/bin/meryl-lookup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl-lookup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl-simple

```bash
$ singularity exec <container> /usr/local/bin/meryl-simple
$ podman run --it --rm --entrypoint /usr/local/bin/meryl-simple   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl-simple   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-dipcall

```bash
$ singularity exec <container> /usr/local/bin/run-dipcall
$ podman run --it --rm --entrypoint /usr/local/bin/run-dipcall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-dipcall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unimap

```bash
$ singularity exec <container> /usr/local/bin/unimap
$ podman run --it --rm --entrypoint /usr/local/bin/unimap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unimap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### winnowmap

```bash
$ singularity exec <container> /usr/local/bin/winnowmap
$ podman run --it --rm --entrypoint /usr/local/bin/winnowmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/winnowmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl

```bash
$ singularity exec <container> /usr/local/bin/meryl
$ podman run --it --rm --entrypoint /usr/local/bin/meryl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
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