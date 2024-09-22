---
layout: container
name:  "quay.io/biocontainers/rdfextras"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rdfextras/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rdfextras/container.yaml"
updated_at: "2024-09-22 03:25:14.426058"
latest: "0.4--py27_3"
container_url: "https://biocontainers.pro/tools/rdfextras"
aliases:
 - "csv2rdf"
 - "rdf2dot"
 - "rdfgraphisomorphism"
 - "rdfpipe"
 - "rdfs2dot"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
versions:
 - "0.4--py27_3"
description: "shpc-registry automated BioContainers addition for rdfextras"
config: {"url": "https://biocontainers.pro/tools/rdfextras", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rdfextras", "latest": {"0.4--py27_3": "sha256:96338ec5128085a9b55059b6911228a3a9abc274f2ebbe41e87752c1d4c3f754"}, "tags": {"0.4--py27_3": "sha256:96338ec5128085a9b55059b6911228a3a9abc274f2ebbe41e87752c1d4c3f754"}, "docker": "quay.io/biocontainers/rdfextras", "aliases": {"csv2rdf": "/usr/local/bin/csv2rdf", "rdf2dot": "/usr/local/bin/rdf2dot", "rdfgraphisomorphism": "/usr/local/bin/rdfgraphisomorphism", "rdfpipe": "/usr/local/bin/rdfpipe", "rdfs2dot": "/usr/local/bin/rdfs2dot", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rdfextras.
shpc-registry automated BioContainers addition for rdfextras
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rdfextras
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rdfextras:0.4--py27_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rdfextras/0.4--py27_3
$ module help quay.io/biocontainers/rdfextras/0.4--py27_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rdfextras-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rdfextras-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rdfextras-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rdfextras-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rdfextras-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rdfextras-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### csv2rdf

```bash
$ singularity exec <container> /usr/local/bin/csv2rdf
$ podman run --it --rm --entrypoint /usr/local/bin/csv2rdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv2rdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdf2dot

```bash
$ singularity exec <container> /usr/local/bin/rdf2dot
$ podman run --it --rm --entrypoint /usr/local/bin/rdf2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdf2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdfgraphisomorphism

```bash
$ singularity exec <container> /usr/local/bin/rdfgraphisomorphism
$ podman run --it --rm --entrypoint /usr/local/bin/rdfgraphisomorphism   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdfgraphisomorphism   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdfpipe

```bash
$ singularity exec <container> /usr/local/bin/rdfpipe
$ podman run --it --rm --entrypoint /usr/local/bin/rdfpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdfpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdfs2dot

```bash
$ singularity exec <container> /usr/local/bin/rdfs2dot
$ podman run --it --rm --entrypoint /usr/local/bin/rdfs2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdfs2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
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