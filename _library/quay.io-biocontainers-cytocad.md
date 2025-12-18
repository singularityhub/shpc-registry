---
layout: container
name:  "quay.io/biocontainers/cytocad"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cytocad/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cytocad/container.yaml"
updated_at: "2025-12-18 04:04:06.294611"
latest: "1.0.3--py38he5da3d1_2"
container_url: "https://biocontainers.pro/tools/cytocad"
aliases:
 - "cytocad"
 - "rfmix2tagore.py"
 - "tagore"
 - "f2py3.6"
 - "rsvg-convert"
 - "gdk-pixbuf-thumbnailer"
 - "gdk-pixbuf-csource"
 - "gdk-pixbuf-pixdata"
 - "gdk-pixbuf-query-loaders"
 - "fasta-sanitize.pl"
 - "shiftBed"
 - "plot-ampliconstats"
 - "annotateBed"
versions:
 - "1.0.3--py36h91eb985_1"
 - "1.0.3--py38he5da3d1_2"
 - "1.0.3--py310h4b81fae_2"
description: "shpc-registry automated BioContainers addition for cytocad"
config: {"url": "https://biocontainers.pro/tools/cytocad", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cytocad", "latest": {"1.0.3--py38he5da3d1_2": "sha256:44611d0035be75024c525140c6087018644aa0dfedd2096606b764dab0b2dddf"}, "tags": {"1.0.3--py36h91eb985_1": "sha256:0ae1ca6f9d2f7f6a684b8e209db217de93e9632b8f11ec340c929971fc3e9715", "1.0.3--py38he5da3d1_2": "sha256:44611d0035be75024c525140c6087018644aa0dfedd2096606b764dab0b2dddf", "1.0.3--py310h4b81fae_2": "sha256:0340759eaefd7db9b421502e4f75a22ef730becde64e3871b2769aaf1c19e1b7"}, "docker": "quay.io/biocontainers/cytocad", "aliases": {"cytocad": "/usr/local/bin/cytocad", "rfmix2tagore.py": "/usr/local/bin/rfmix2tagore.py", "tagore": "/usr/local/bin/tagore", "f2py3.6": "/usr/local/bin/f2py3.6", "rsvg-convert": "/usr/local/bin/rsvg-convert", "gdk-pixbuf-thumbnailer": "/usr/local/bin/gdk-pixbuf-thumbnailer", "gdk-pixbuf-csource": "/usr/local/bin/gdk-pixbuf-csource", "gdk-pixbuf-pixdata": "/usr/local/bin/gdk-pixbuf-pixdata", "gdk-pixbuf-query-loaders": "/usr/local/bin/gdk-pixbuf-query-loaders", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "shiftBed": "/usr/local/bin/shiftBed", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "annotateBed": "/usr/local/bin/annotateBed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cytocad.
shpc-registry automated BioContainers addition for cytocad
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cytocad
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cytocad:1.0.3--py38he5da3d1_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cytocad/1.0.3--py38he5da3d1_2
$ module help quay.io/biocontainers/cytocad/1.0.3--py38he5da3d1_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cytocad-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cytocad-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cytocad-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cytocad-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cytocad-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cytocad-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cytocad

```bash
$ singularity exec <container> /usr/local/bin/cytocad
$ podman run --it --rm --entrypoint /usr/local/bin/cytocad   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cytocad   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rfmix2tagore.py

```bash
$ singularity exec <container> /usr/local/bin/rfmix2tagore.py
$ podman run --it --rm --entrypoint /usr/local/bin/rfmix2tagore.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rfmix2tagore.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tagore

```bash
$ singularity exec <container> /usr/local/bin/tagore
$ podman run --it --rm --entrypoint /usr/local/bin/tagore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tagore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsvg-convert

```bash
$ singularity exec <container> /usr/local/bin/rsvg-convert
$ podman run --it --rm --entrypoint /usr/local/bin/rsvg-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsvg-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdk-pixbuf-thumbnailer

```bash
$ singularity exec <container> /usr/local/bin/gdk-pixbuf-thumbnailer
$ podman run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-thumbnailer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-thumbnailer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdk-pixbuf-csource

```bash
$ singularity exec <container> /usr/local/bin/gdk-pixbuf-csource
$ podman run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-csource   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-csource   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdk-pixbuf-pixdata

```bash
$ singularity exec <container> /usr/local/bin/gdk-pixbuf-pixdata
$ podman run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-pixdata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-pixdata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdk-pixbuf-query-loaders

```bash
$ singularity exec <container> /usr/local/bin/gdk-pixbuf-query-loaders
$ podman run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-query-loaders   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-query-loaders   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
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