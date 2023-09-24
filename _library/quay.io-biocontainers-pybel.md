---
layout: container
name:  "quay.io/biocontainers/pybel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pybel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pybel/container.yaml"
updated_at: "2023-09-24 02:41:22.962651"
latest: "0.13.2--py_0"
container_url: "https://biocontainers.pro/tools/pybel"
aliases:
 - "geoff"
 - "neokit"
 - "p2n"
 - "py2neo"
 - "pybel"
 - "pyfiglet"
 - "csv2rdf"
 - "rdf2dot"
 - "rdfgraphisomorphism"
 - "rdfpipe"
 - "rdfs2dot"
 - "pygmentize"
 - "chardetect"
 - "python2-config"
 - "python2.7-config"
 - "python2"
versions:
 - "0.9.3--py27_1"
 - "0.13.2--py_0"
description: "shpc-registry automated BioContainers addition for pybel"
config: {"url": "https://biocontainers.pro/tools/pybel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pybel", "latest": {"0.13.2--py_0": "sha256:cc91a480851ed04d1a20d7f2d5ae04fa5ee8e00d9255a018c6cb7f68cf5d74d0"}, "tags": {"0.9.3--py27_1": "sha256:1e47a7882b3f9e6b4163a8ec2da0fc8d785068158c4df24f7b44dfe905d52aa1", "0.13.2--py_0": "sha256:cc91a480851ed04d1a20d7f2d5ae04fa5ee8e00d9255a018c6cb7f68cf5d74d0"}, "docker": "quay.io/biocontainers/pybel", "aliases": {"geoff": "/usr/local/bin/geoff", "neokit": "/usr/local/bin/neokit", "p2n": "/usr/local/bin/p2n", "py2neo": "/usr/local/bin/py2neo", "pybel": "/usr/local/bin/pybel", "pyfiglet": "/usr/local/bin/pyfiglet", "csv2rdf": "/usr/local/bin/csv2rdf", "rdf2dot": "/usr/local/bin/rdf2dot", "rdfgraphisomorphism": "/usr/local/bin/rdfgraphisomorphism", "rdfpipe": "/usr/local/bin/rdfpipe", "rdfs2dot": "/usr/local/bin/rdfs2dot", "pygmentize": "/usr/local/bin/pygmentize", "chardetect": "/usr/local/bin/chardetect", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pybel.
shpc-registry automated BioContainers addition for pybel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pybel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pybel:0.13.2--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pybel/0.13.2--py_0
$ module help quay.io/biocontainers/pybel/0.13.2--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pybel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pybel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pybel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pybel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pybel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pybel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### geoff

```bash
$ singularity exec <container> /usr/local/bin/geoff
$ podman run --it --rm --entrypoint /usr/local/bin/geoff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geoff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### neokit

```bash
$ singularity exec <container> /usr/local/bin/neokit
$ podman run --it --rm --entrypoint /usr/local/bin/neokit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/neokit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### p2n

```bash
$ singularity exec <container> /usr/local/bin/p2n
$ podman run --it --rm --entrypoint /usr/local/bin/p2n   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/p2n   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py2neo

```bash
$ singularity exec <container> /usr/local/bin/py2neo
$ podman run --it --rm --entrypoint /usr/local/bin/py2neo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py2neo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybel

```bash
$ singularity exec <container> /usr/local/bin/pybel
$ podman run --it --rm --entrypoint /usr/local/bin/pybel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyfiglet

```bash
$ singularity exec <container> /usr/local/bin/pyfiglet
$ podman run --it --rm --entrypoint /usr/local/bin/pyfiglet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyfiglet   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
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