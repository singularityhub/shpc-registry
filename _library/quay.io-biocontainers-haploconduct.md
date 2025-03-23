---
layout: container
name:  "quay.io/biocontainers/haploconduct"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/haploconduct/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/haploconduct/container.yaml"
updated_at: "2025-03-23 03:37:18.633285"
latest: "0.2.1--py27h16ec135_3"
container_url: "https://biocontainers.pro/tools/haploconduct"
aliases:
 - "haploconduct"
 - "kallisto"
 - "rust-overlaps"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
 - "f2py2"
 - "f2py2.7"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "python2-config"
 - "python2.7-config"
 - "python2"
versions:
 - "0.2.1--py27h16ec135_3"
description: "shpc-registry automated BioContainers addition for haploconduct"
config: {"url": "https://biocontainers.pro/tools/haploconduct", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for haploconduct", "latest": {"0.2.1--py27h16ec135_3": "sha256:35438cf11320433689af1860613f4a97c4ab84f13651abfa4b088c74b57a13dc"}, "tags": {"0.2.1--py27h16ec135_3": "sha256:35438cf11320433689af1860613f4a97c4ab84f13651abfa4b088c74b57a13dc"}, "docker": "quay.io/biocontainers/haploconduct", "aliases": {"haploconduct": "/usr/local/bin/haploconduct", "kallisto": "/usr/local/bin/kallisto", "rust-overlaps": "/usr/local/bin/rust-overlaps", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/haploconduct.
shpc-registry automated BioContainers addition for haploconduct
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/haploconduct
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/haploconduct:0.2.1--py27h16ec135_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/haploconduct/0.2.1--py27h16ec135_3
$ module help quay.io/biocontainers/haploconduct/0.2.1--py27h16ec135_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### haploconduct-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### haploconduct-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### haploconduct-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### haploconduct-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### haploconduct-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### haploconduct-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### haploconduct

```bash
$ singularity exec <container> /usr/local/bin/haploconduct
$ podman run --it --rm --entrypoint /usr/local/bin/haploconduct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haploconduct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kallisto

```bash
$ singularity exec <container> /usr/local/bin/kallisto
$ podman run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust-overlaps

```bash
$ singularity exec <container> /usr/local/bin/rust-overlaps
$ podman run --it --rm --entrypoint /usr/local/bin/rust-overlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust-overlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualfa2fq.pl

```bash
$ singularity exec <container> /usr/local/bin/qualfa2fq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xa2multi.pl

```bash
$ singularity exec <container> /usr/local/bin/xa2multi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2.7

```bash
$ singularity exec <container> /usr/local/bin/f2py2.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
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